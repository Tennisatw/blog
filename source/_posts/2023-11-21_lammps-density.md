---
title: 计算lammps模拟系统的密度 - Calculate the density of a lammps simulated system
permalink: post/33/
excerpt: 暂无预览 - No preview available
date: 2023-11-21 22:45:01
tags: 编程 - Programming
---

想要计算lammps模拟系统的密度，需要知道系统的尺寸，和系统内的原子数。

To calculate the density of a lammps simulated system, you need to know the system's dimensions and the number of atoms within it.

<p><br></p>

对于尺寸在模拟中不发生变化的系统，可以读取其输入文件的结构文件来获得系统的三维尺寸。以下为一个典型的结构文件的例子：

For systems whose dimensions do not change during simulation, you can obtain the three-dimensional size of the system by reading the structure file in its input file. Here's an example of a typical structure file:

```
LAMMPS data file

3072 atoms
2 atom types
2048 bonds
1 bond types
1024 angles
1 angle types

-1.2631399999999999e+01 1.2631399999999999e+01 xlo xhi
-1.2631399999999999e+01 1.2631399999999999e+01 ylo yhi
-2.5262750000000000e+01 2.5262750000000000e+01 zlo zhi

Masses

1 1.008
2 15.9994
```

<p><br></p>

最长的那三行是盒子的尺寸。x方向的尺寸为12.6314-(-12.6314)=25.2628A。y和z方向的尺寸计算方法类似。

The three longest lines represent the dimensions of the box. The size in the x-direction is 12.6314 - (-12.6314) = 25.2628 Å. The size in the y and z directions is calculated similarly.

<p><br></p>

对于尺寸在模拟中发生变化的系统，可以使其输出某一帧的三维尺寸。可以在lammps使用dump命令，比如：

For systems whose dimensions change during simulation, you can output the three-dimensional size of a specific frame. In lammps, you can use the dump command, for example:

```
dump 1 all custom 1000 lammps_out.data id mol type q x y z
```
可以使得lammps输出模拟过程中的原子个数，盒子尺寸，原子的坐标等信息。

This allows lammps to output information during the simulation process, such as the number of atoms, box dimensions, and coordinates of atoms.

```
ITEM: TIMESTEP
100000
ITEM: NUMBER OF ATOMS
3072
ITEM: BOX BOUNDS pp pp pp
-1.2631399999999999e+01 1.2631399999999999e+01
-1.2631399999999999e+01 1.2631399999999999e+01
-2.5262750000000000e+01 2.5262750000000000e+01
```

<p><br></p>

系统内各分子或原子的种类与个数可以通过检查输入文件的结构文件来确定。

The types and numbers of molecules or atoms in the system can be determined by examining the structure file in the input file.

<p><br></p>

在清楚x，y，z，和系统的分子个数后，可以使用以下python脚本计算总系统的密度。

Once you know the dimensions in x, y, z, and the number of molecules in the system, you can use the following python script to calculate the overall density of the system.

```python
x = 25.2628  # A
y = 25.2628  # A
z = 50.5256  # A

molecule_amount = 1024

molecule_M = 18  # g/mol
# for water

#############################################

NA = 6.02 * 10**23  # mol^-1
volume = x * y * z * 10**-24  # cm^3
mass = molecule_amount * molecule_M / NA  # g
density = mass / volume  # g/cm^3

print("density = {:.4f} g/cm^3".format(density))

```