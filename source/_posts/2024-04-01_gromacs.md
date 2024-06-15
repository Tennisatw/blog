---
title: 魔改Gromacs，并运行 - Modify the Gromacs, and run it
permalink: post/47/
excerpt: Gromacs是一个开源的软件，用c++开发。如果对Gromacs的某个功能不满意，大可以直接去修改其源代码，然后编译，安装。<br>Gromacs is an open-source software developed in C++. If you are dissatisfied with a particular feature of Gromacs, you can directly modify its source code, then compile and install it.
date: 2024-04-01 01:16:08
tags:
 - 编程 - Programming
 - 技术 - Technology
---

Gromacs是一个开源的软件，用c++开发。如果对Gromacs的某个功能不满意，大可以直接去修改其源代码，然后编译，安装。

Gromacs is an open-source software developed in C++. If you are dissatisfied with a particular feature of Gromacs, you can directly modify its source code, then compile and install it.

<br>

首先，从github上下载其源代码：在想要储存代码的地方打开terminal（或者对于windows用户就是powershell），输入：

First, download the source code from GitHub: Open the terminal (or PowerShell for Windows users) in the desired location to store the code, and type:

```
git clone https://github.com/gromacs/gromacs.git
```

<br>

源代码储存在gromacs/src/gromacs/里，比如分析氢键的gmx hbond就位于gromacs/src/gromacs/gmxana/gmx_hbond.cpp

想怎么改都可以，改好后保存。

The source code is stored in gromacs/src/gromacs/. For example, the code for analyzing hydrogen bonds, gmx hbond, is located at gromacs/src/gromacs/gmxana/gmx_hbond.cpp.

Modify as you like and then save.

<br>

然后，使用cmake编译gromacs：进入gromacs的主文件夹，创建一个名为build的文件夹，进入，在此打开terminal，输入：

Next, compile Gromacs using cmake: Enter the main Gromacs directory, create a folder named build, enter it, open the terminal there, and type:

```
cmake .. -DCMAKE_INSTALL_PREFIX=/path/to/new/gromacs
```
此地址为你想要将新gromacs安装的位置。

这中间可能会报错，通常是因为缺少一些包，sudo安装就好。

This path is where you want to install the new Gromacs.

Errors may occur during this process, usually due to missing packages. Installing them with sudo should resolve the issue.

<br>

编译好了之后，输入：

After compilation, enter:

```
make install
```
安装魔改版的gromacs。

To install the modified version of Gromacs.

<br>

（可选）使用以下命令将此gromacs所在的位置暂时添加到环境变量中。这样使用时就可以不用指定其完整路径了。

(Optional) Use the following command to temporarily add the location of this Gromacs to the environment variables. This way, you won't need to specify the full path when using.

```
export PATH=/path/to/new/gromacs/bin:$PATH
```

<br>

Since today is April Fool's Day, a small April Fool's effect has been added, as shown in the image below. Happy April Fool's Day to everyone.

由于今天是愚人节，这里做了一个小小的愚人节效果，如下图所示。大家愚人节快乐。

![](1.png)