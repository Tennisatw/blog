---
title: SD WebUI 1： 如何安装Stable Diffusion WebUI？ - SD WebUI 1： How to install Stable Diffusion WebUI?
permalink: post/7/
excerpt: <!-- -->
date: 2023-05-04 21:14:38
tags: 
 - 技术 - Technology
 - 编程 - Programming
categories: 
 - SD WebUI
---

 Stable Diffusion WebUI是一个本地化AI作图的程序。相比于其他AI作图网站，SD WebUI免费，而且自由度更高，可以自由使用任何模型与Lora。

The Stable Diffusion WebUI is a program for localized AI drawing. Compared to other AI drawing websites, SD WebUI is free and offers a higher degree of freedom, allowing users to freely use any models and Lora.

<br>

我参考了SD WebUI的官网上的安装方法，如下所示：

I followed the installation guide provided on the official website of SD WebUI, and here are the steps.

[https://github.com/AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

<br>

第一步，下载python3.10.6。注意在安装过程中要勾选“将Python添加到系统路径中（Add Python to path）”否则程序找不到python解释器。

Step 1, download Python 3.10.6. During the installation process, be sure to check the option "Add Python to path," as this will ensure that the program can locate the Python interpreter seamlessly.

[https://www.python.org/downloads/release/python-3106/](https://www.python.org/downloads/release/python-3106/)

<br>

第二步，下载Git。

Step 2: Download Git.

[https://git-scm.com/download/win](https://git-scm.com/download/win)

<br>

第三步，在Git Command中执行以下命令：

Step 3: Execute the following command in Git Command:

```
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
```

<br>

这将在你的个人文件夹（C:\Users\<你的用户名>）里新建一个stable-diffusion-webui的文件夹。

This will create a new folder named "stable-diffusion-webui" in your personal folder (C:\Users\<YourUsername>).

<br>

第四步，打开文件夹，寻找并执行webui-user.bat文件。

Step 4: Open the folder, find, and run the webui-user.bat file.

<br>

注，如果电脑里已经有了其他版本的python，并且已经在系统路径中，webui-user有可能会识别到其他版本的python，从而报错。此时，可以编辑webui-user.bat，修改第三行，在其中指定之前下载的python3.10的路径。

Note that if your computer already has another version of Python installed and included in the system path, webui-user may detect that version and raise an error. In that case, you can edit the webui-user.bat file, modify the 3rd line, to specify the path of Python3.10 download before.

```
set PYTHON="C:\Users\xxx\Python310\python.exe"
```

<br>

这样，SD WebUI就安装好了。运行webui-user.bat文件即可使用。

With these steps, SD WebUI is now installed. To use it, simply run the webui-user.bat file.

<br>

但是，每一次在运行SD WebUI时，还需要手动打开浏览器输入网址。为了简化使用步骤，可以修改python代码，使得SD WebUI自动打开WebUI网页：

编辑webui.py，寻找def webui()这一行命令，在webui这个函数中，在initialize()和while 1:这两行代码中间插入这两行代码，注意用空格使得这两行与上下文对齐。

However, every time you run SD WebUI, you'll need to manually open a browser and input the web address. To simplify the process, you can modify the Python code to automatically open the WebUI page:

Edit webui.py and find the line with "def webui()". Inside the webui function, insert these two lines of code between the "initialize()" and "while 1:" lines, making sure to align the new lines with the surrounding code using spaces.

```python
import webbrowser
webbrowser.open('http://127.0.0.1:7860')
```

<br>

最后代码应该是这个样子。

```python
def webui():
    launch_api = cmd_opts.api
    initialize()
    import webbrowser
    webbrowser.open('http://127.0.0.1:7860')
    while 1:
```