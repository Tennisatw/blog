---
title: 深挖Lammps的源代码
permalink: post/81/
excerpt: <!-- -->
date: 2025-05-03 23:25:20
tags:
---

Lammps是一个分子动力学模拟软件，擅长并行运算。我打算用一点时间（几周），深挖一下Lammps的源代码。

我的目标是：
- 掌握Lammps的MD模拟工作流程
- 掌握Lammps的源代码结构
- 掌握Lammps的势函数内容
- 大体理解：
    - 并行原理（cpu-cpu，及cpu-gpu）
    - md的实现
    - gcmc的实现
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

### Lammps的MD模拟工作流程

#### 初始化

当运行Lammps时，会首先运行`src/main.cpp`中的`main()`函数。该函数是Lammps的入口函数。这其中：
`auto lammps = new LAMMPS(argc, argv, lammps_comm);`会创建一个LAMMPS对象。该对象管理Lammps的所有功能。

（注：在VSCode右键点击LAMMPS，选择go to definition，可以自动打开src/lammps.h文件，然后寻找同名的src/lammps.cpp文件，即可找到对应的定义。具体而言，它从src/lammps.cpp文件的第132行开始。对于其他的类或函数，也可以用类似的方法找到其声明或定义。）

在`LAMMPS`类的定义中：

首先，其创建Memory，Error对象，用于内存管理和错误处理。

在第238行，其读取命令行参数（比如-h，-in）并设置flag。

然后，第492行定义了partition并行的逻辑。

在第701行初始化kokkos（gpu/并行加速模块，如果用到的话），引用模块，输入模块等。

在第715行，初始化input对象，用于读取、解析和执行用户提供的LAMMPS输入脚本命令。

在第740行，调用了`create()`和`post_create()`函数，用于初始化核心模拟组件类，包括：
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
等对象，及配置加速器包（kokkos，intel，gpu和openmp）。

<br>

#### 读取并逐行执行输入文件

`main()`函数在初始化lammps对象完成后，会执行`lammps->input->file();`来读取输入文件。具体而言，首先调用`lammps`对象的`input`类，然后调用其内部的`file()`函数读取并逐行执行命令（`src/input.cpp` 第195行）。

在`file()`函数中，其使用mpi rank 0的进程从`infile`逐行读取文件，然后广播至其他进程。之后，各进程使用parse解析命令，然后调用`execute_command`(第313行)函数来调用相关处理函数，执行每一行命令。

在`execute_command`中，一些命令被硬编码了专门的处理函数，比如`bond_coeff`，`dump`，`thermo`等，在其中再调用其他模块中相关的函数来执行。

另一些命令在`command_map`中被映射到相应的处理函数，比如`run`，则调用其对应的`command`函数（第868行）。

<br>