---
title: 基于vscode的最简易的c/c++开发环境搭建
permalink: post/76/
excerpt: 对于非计算机专业的人来说，c/c++的配置和构建相当复杂。这里给习惯vscode的windows用户推荐一个简单的方案：使用vscode及插件 + msys2作为开发环境。
date: 2025-04-14 14:43:05
tags: 编程 - Programming
---

c++广泛用于系统开发、游戏开发和高性能应用。但对于非计算机专业的人来说，c/c++的配置和构建相当复杂。

最简单的方法是直接使用Visual Studio作为开发环境。但vs安装包超级大，而且使用起来很麻烦。所以这里给习惯vscode的windows用户推荐一个次优的开发环境方案：使用vscode及插件 + msys2作为开发环境。

C++ is widely used for system development, game development, and high-performance applications. However, for those without a computer science background, configuring and building C/C++ projects can be quite complex.

The simplest approach is to use Visual Studio as the development environment. But it's huge, and the IDE can be cumbersome to use. So here’s a solid alternative for Windows users who prefer VS Code: using VS Code with extensions + MSYS2 as your development environment.

<br>

### 安装及更新msys2 - Installing and Updating MSYS2

msys2是一个微型的Linux系统，可以使用msys2的包管理器（pacman）安装开发c/c++所需的所有工具，包括编译器（mingw64的gcc和g++），调试器（mingw64的gdb），项目构建配置工具（mingw64的cmake），项目构建工具（mingw64的make或ninja）。

首先去[msys2官网](https://www.msys2.org/)下载安装msys2，安装完成后，运行**MSYS2 MINGW64**，执行以下命令更新系统：

MSYS2 is a lightweight Linux-like environment for Windows. It comes with a package manager (pacman) that allows you to install all the necessary tools for C/C++ development, including a compiler (mingw64 versions of GCC and G++), debugger (mingw64-gdb), build configuration tools (mingw64-cmake), and build systems (mingw64-make or Ninja).

First, download and install MSYS2 from the [official website](https://www.msys2.org/). After installation, launch **MSYS2 MINGW64**, and run the following command to update the system:

```bash
pacman -Syu
```

如果提示需要重启msys2，则重启后继续执行此命令。

更新完成后，将 `C:\msys64\mingw64\bin` 添加到系统的环境变量中。建议添加到靠前的位置。

If prompted to restart MSYS2, do so and then rerun the same command.

Once the update is complete, add `C:\msys64\mingw64\bin` to your system's PATH environment variable—preferably near the top of the list.

<br>

### 安装开发工具 - Installing Development Tools

接下来，在msys2中安装c/c++的开发工具：

Next, install the necessary C/C++ development tools within MSYS2:

```bash
pacman -S mingw-w64-x86_64-toolchain
pacman -S mingw-w64-x86_64-cmake
```

toolchain包括了gcc、gdb等工具，而cmake包括了cmake和ninja等构建工具。

在c/c++开发过程中，如果需要使用其他库，也可以通过pacman安装。比如安装SFML库：

The toolchain package includes tools like gcc and gdb, while the cmake package contains build tools like CMake and Ninja.

If your C/C++ project requires additional libraries, you can install them via pacman as well. For example, to install the SFML library:

```bash
pacman -S mingw-w64-x86_64-sfml
```

<br>

### 安装vscode及插件 - Installing VS Code and Extensions

去官网下载并安装vscode。安装完成后，安装C/C++插件和CMake Tools插件。

注：其他插件可能会影响构建，比如python插件，需要提前disable。此外，构建时需要退出所有的conda环境。

注2：从2025年4月初开始，vscode的C/C++插件不支持其他vscode类型的ide了，比如cursor。要么使用vscode，要么在cursor中安装之前的插件版本。（微软，说好的开源精神呢？）

Download and install VS Code from its official website. Once installed, add the C/C++ extension and the CMake Tools extension.

Note: Some other extensions (like the Python extension) might interfere with the build process, so it's best to disable them beforehand. Also, be sure to exit any active Conda environments before building your project.

Note 2: As of early April 2025, the VS Code C/C++ extension no longer supports alternative VS Code distributions like Cursor. So you’ll need to either use official VS Code or install an earlier version of the extension in Cursor. (To Microsoft: where's your spirit of open source?)

<br>

### 创建项目 - Creating a Project

在vscode中打开一个新的文件夹，作为项目的根目录，之后就可以在这个文件夹中开发c/c++项目了。

在项目文件夹的根目录，创建一个CMakeLists.txt文件，用于配置项目构建。其内容因语言/使用的库而会有不同。对于我的项目（使用c++语言，且使用SFML库，见下一篇博客），CMakeLists的内容如下：

Open a new folder in VS Code to serve as the root directory of your project. You’ll develop your C/C++ project inside this folder.

In the root directory, create a CMakeLists.txt file to configure the build process. Its content will vary depending on the language and libraries used. For example, here’s a CMakeLists.txt for a C++ project using the SFML library (as discussed in my next blog post):

```cmake
cmake_minimum_required(VERSION 3.10)

# 工程名 - Project name
project(galaxy)

# C++ 标准 - C++ Standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 找到 SFML（2.5 或以上） - Find SFML (2.5 or later)
find_package(SFML 2.5 COMPONENTS graphics window system REQUIRED)

# 收集 src/ 目录下所有 .cpp 文件 - Collect all .cpp files in the src/ directory
file(GLOB SRC_FILES "${PROJECT_SOURCE_DIR}/src/*.cpp")

# 生成可执行文件 galaxy.exe - Create executable file galaxy.exe
add_executable(galaxy ${SRC_FILES})

# 链接SFML库 - Link SFML libraries
target_link_libraries(galaxy
    PRIVATE
    sfml-graphics
    sfml-window
    sfml-system
)
```

<br>

### 配置并构建项目 - Configuring and Building the Project

项目编写完成后，使用vscode的CMake Tools插件来配置并构建项目。

首先打开Cmake Tools插件页面。在configure中选择msys2 - mingw64的GCC编译器，如图所示。之后，插件会依据CMakeLists自动配置项目。

After writing your code, use the CMake Tools extension in VS Code to configure and build the project.

First, open the CMake Tools panel and select the MSYS2 - mingw64 GCC compiler under the Configure option, as shown in the image. Then, the extension will automatically configure your project based on CMakeLists.txt.

![](image.png)

点击build右侧的按钮，插件会构建项目。构建好的可执行文件将出现在项目的build目录中。之后，点击test/debug/run栏右侧的按钮，就可以测试/调试/运行项目了。

Click the build button to compile the project. The resulting executable will appear in the build directory within your project. From there, you can test, debug, or run your project using the buttons in the Test / Debug / Run section.