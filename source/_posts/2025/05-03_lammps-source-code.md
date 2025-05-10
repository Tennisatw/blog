---
title: 深挖Lammps的源代码
permalink: post/81/
excerpt: <!-- -->
date: 2025-05-03 23:25:20
tags: 
- 编程 - Programming
- 随想 - Thoughts
---

Lammps是一个分子动力学模拟软件，擅长并行运算。我打算用一点时间（几周），深挖一下Lammps的源代码。

我的目标是：

- 掌握Lammps的项目结构
- 掌握Lammps的工作流程
- 掌握MD模拟的流程
    - 着重掌握有关pair的部分，因为未来的工作中可能需要自定义原子势能。
- 修改，并编译Lammps的源代码

此外，我打算总结一套深挖项目代码的通用流程。

<br>

一些有用的链接：
- [Lammps的官方网站](https://www.lammps.org/#gsc.tab=0)
- [Lammps的源代码](https://github.com/lammps/lammps)
- [Lammps的文档](https://docs.lammps.org/)
- [Lammps的文章](https://www.sciencedirect.com/science/article/pii/S0010465521002836?via%3Dihub)

<br>

### Lammps的项目结构

![](1746478049194.png)

Lammps项目遵守典型的C++科研类项目架构。本段为不熟悉c++项目架构的读者简单介绍一下各文件/文件夹的内容：

#### 顶层文件

- README：项目的简介，目录，相关文档的位置。
- LICENSE：项目的许可证，即说明其他人可以如何使用这个项目。
- CITATION.cff：如何引用这个项目。

#### 代码

- src/：Lammps的源代码，实现各种Lammps的核心功能。这也是深挖的主要目标。
- lib/：一些Lammps的插件/扩张（比如GPU加速，机器学习势能，python）的源代码或接口，需要单独编译。
- cmake/：CMake构建脚本与模块，用于编译Lammps（即从c++源代码生成可执行程序）
- python/和fortran/：Lammps的python和fortran接口，允许用户使用python或fortran调用Lammps。
- potentials/：Lammps的势函数，包含了Lammps支持的所有势函数文件。

#### 工具

- tools/：一些预处理/后处理，类型转换的小程序。
- unittest/：Lammps的单元测试代码，测试Lammps的功能是否正常。
- bench/：用于测试不同编译条件下Lammps的性能。

#### 文档

- doc/：Lammps的文档，包括用户手册、开发者手册、教程等。
- examples/：Lammps的示例脚本和输入文件。

#### 其他

- .github/: 一些和提交有关的文件，包括CI（持续集成）工作流、Issue/PR 模板、贡献指南。
- third_party/：指向第三方库的链接。

<br>

### Lammps的工作流程

当运行Lammps时，会首先运行`src/main.cpp`中的`main()`函数。该函数是Lammps的入口函数。这其中：
`auto lammps = new LAMMPS(argc, argv, lammps_comm);`会创建一个LAMMPS对象。该对象管理Lammps的所有功能。

（注：在VSCode右键点击LAMMPS，选择go to definition，可以自动打开src/lammps.h文件，然后寻找同名的src/lammps.cpp文件，即可找到对应的定义。具体而言，它从src/lammps.cpp文件的第132行开始。对于其他的类或函数，也可以用类似的方法找到其声明或定义。）

在`LAMMPS`类的定义中：

首先，其创建Memory，Error对象，用于内存管理和错误处理。

在第238行，其读取命令行参数（比如-h，-in）并设置flag。

然后，第492行定义了partition并行的逻辑。

在第701行初始化kokkos（gpu/并行加速模块，如果用到的话），引用模块，输入模块等。

在第715行，初始化input对象，用于读取、解析和执行用户提供的LAMMPS输入脚本命令。

在第740行，调用了`create()`函数，用于初始化核心模拟组件类，包括：  

- comm（并行计算中的通信）
- neighbor（邻居列表构建和管理）
- domain（管理模拟盒子和边界）
- atom（管理原子数据）
- group（管理原子组）
- force（管理力场力）
- modify（fix命令和compute命令）
- output（管理输出）
- update（管理模拟过程中的时间步进，积分，最小化算法）
- timer（性能计时）
- python（python接口）

等类。这些类之间的关系见下图（[来源](https://docs.lammps.org/Developer_org.html)）。

![LAMMPS class topology](1746911232551.png)

所有核心模拟组件类都继承了`Pointer`类，包含了指向其他核心组件的指针。所以这些类的对象都可以互相访问。

此外，740行还调用了`post_create()`函数，用于配置加速器包（kokkos，intel，gpu和openmp）。

<br>

`main()`函数在初始化lammps对象完成后，会执行`lammps->input->file();`来读取输入文件。具体而言，首先调用`lammps`对象的`input`类，然后调用其内部的`file()`函数读取并逐行执行命令（`src/input.cpp` 第195行）。

在`file()`函数中，其使用mpi rank 0的进程从`infile`逐行读取文件，然后广播至其他进程。之后，各进程使用parse解析命令，然后调用`execute_command`(第313行)函数来调用相关处理函数，执行每一行命令。

在`execute_command`中（第764行），一些命令被硬编码了专门的处理函数，比如`bond_coeff`，`dump`，`thermo`等，在其中再调用其他模块中相关的函数来执行。

另一些命令在`command_map`中被映射到相应的处理函数，比如`run`，则调用其对应的`command`函数（第868行）。

<br>

所有命令都执行完毕后，Lammps中止MPI，优雅退出。

<br>

### MD模拟的流程

一份极简的[官方MD模拟输入文件](https://docs.lammps.org/Howto_spc.html)如下所示：

```lammps
units real
atom_style full
region box block -5 5 -5 5 -5 5
create_box 2 box  bond/types 1 angle/types 1 &
                extra/bond/per/atom 2 extra/angle/per/atom 1 extra/special/per/atom 2

mass 1 15.9994
mass 2 1.008

pair_style lj/cut/coul/cut 10.0
pair_coeff 1 1 0.1553 3.166
pair_coeff 1 2 0.0    1.0
pair_coeff 2 2 0.0    1.0

bond_style zero
bond_coeff 1 1.0

angle_style zero
angle_coeff 1 109.47

molecule water spce.mol
create_atoms 0 random 33 34564 NULL mol water 25367 overlap 1.33

timestep 1.0
fix rigid     all shake 0.0001 10 10000 b 1 a 1
minimize 0.0 0.0 1000 10000
velocity all create 300.0 5463576
fix integrate all nvt temp 300.0 300.0 100.0

thermo_style custom step temp press etotal density pe ke
thermo 1000
run 20000 upto
write_data spce.data nocoeff
```

让我们一行一行地分析一下此模拟的流程。

#### 设置模拟环境

第一个命令是`units real`。即使用真实单位（real units）系统。`units`命令定义在`src/input.cpp`的第2003行。在做了一些参数检查后，调用了`update`对象的`set_units`函数，并把第一个参数传了进去。`set_units`函数具体在`src/update.cpp`的134行。当检测到`units`为`real`时，对`force`对象中的一些物理常数和单位进行设置，包括玻尔兹曼常数，单位转换常数，电子电荷量等等。

`atom_style full`命令定义了原子的类型和属性为`full`(即包含全部的原子参数，包括坐标，键，键角，二面角，电荷...)。它创造了一个AtomVecFull类的实例，用于管理原子数据，并设置其可能的拓扑类型（比如是否可以含有键角，二面角等等）。此类在`src/MOLECULE/atom_vec_full.cpp`中定义。该类继承了抽象的AtomVec类（在`src/atom_vec.cpp`中定义）。

`region box block -5 5 -5 5 -5 5`命令定义了一个正方体的区域，边长为10。`add_region`函数（`src/domain.cpp`第1967行）进行参数检查，id重复检查之后，调用region_creator函数。此函数是一个模板函数（`src/domain.cpp`第55行），其本质上通过`region_map`查找并调用了region block对象的构造函数（`src/region_block.cpp`第30行）创建region（包括计算各边顶点，各面法向量）。最后，回到`add_region`函数，将region对象添加到regions列表中。

`create_box`是一个映射到`command_map`中的函数。其定义在`src/create_box.cpp`中。在做了一些检查后，从196行开始，通过bond/types等关键词，定义`atom`对象的nbondtypes，nangletypes，bond_per_atom，angle_per_atom属性。

<br>

#### 设置力场参数

`mass 1 15.9994`命令设置了原子类型1的质量为15.9994。`mass`命令调用了`atom`对象的`set_mass`函数（`src/atom.cpp`第1933行）。

`pair_style lj/cut/coul/cut 10.0`命令设置了原子之间的相互作用力为lj/cut/coul/cut，截断距离为10.0A。具体而言，它规定了原子之间的相互作用力包括有截断半径的范德华力（lj/cut）和有截断半径的库仑力（coul/cut）。此命令会调用在`src/input.cpp`第1787行的pair_style函数，当检查过之前没有定义pair_style后，在1787行，其调用create_pair函数（在`src/force.cpp` 第227行）以创建pair相互作用。

在create_pair函数中，调用new_pair函数（247行），其内部在`pair_map`中查找，所设置的pair样式是否有对应的类（在本例中，pair样式为lj/cut/coul/cut，对应的类为`PairLJCutCoulCut`（在`src/pair_lj_cut_coul_cut.cpp`中的33行））。

`pair_map`本身的生成过程很精妙。其定义在`src/force.cpp`第89行：`pair_map = new PairCreatorMap();`。这一行动态分布了一个`PairCreatorMap`对象，并将其指针存储在`pair_map`中。`PairCreatorMap`是一个映射，键是形如“lj/cut/coul/cut”的字符串，而值是一个函数指针，此函数将返回一个指向`Pair`类型的指针。

第92行定义了一个宏`PairStyle`，其接受两个参数`key`和`Class`。其作用则是将`&style_creator<Pair, Class>`赋值给`(*pair_map)[#key]`。比如`PairStyle("lj/cut/coul/cut", PairLJCutCoulCut)`就等于`(*pair_map)["lj/cut/coul/cut"] = &style_creator<Pair, PairLJCutCoulCut>;`。

`style_creator`是一个通用的工厂函数，在`src/force.cpp`的第41行定义。其作用是动态创建一个`Class`对象（在本例中为`PairLJCutCoulCut`对象），并返回指向此对象的指针。

`style_pair.h`文件将在编译过程中生成，其包含所有以`pair_`开头的头文件，并调用`PairStyle`宏将这些文件对应的类注册进`pair_map`中。`doc/src/Developer_code_design.rst`和`doc/src/Developer_write_pair.rst`中有对此过程的详细介绍。

上述 创建不同类型的Pair实例的编程模式 叫做“Style Factory”。此编程模式被很多其他的功能所采用，包括创建Bond，Angle，Dihedral，Improper等等，以及上文提到的atom style。