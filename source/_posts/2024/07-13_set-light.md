---
title: 利用python脚本分别调节多个屏幕的亮度 - Set the brightness of multiple screens separately using python scripts
permalink: post/56/
excerpt: 通过python的screen_brightness_control包来调节多个显示器的亮度，使用tkinter库创建一个简单的图形化界面，通过滑动条来调节各个显示器的亮度。<br>Using the screen_brightness_control package in Python to adjust the brightness of multiple monitors, creating a simple graphical interface using the tkinter library to adjust the brightness of each monitor with sliders.
date: 2024-07-13 23:25:41
tags: 编程 - Programming
---

如果Windows电脑同时连接超过一个显示器，通过键盘快捷键就不能调节多个显示屏的亮度了，想要调节的话只能去按外接显示器的物理按钮。

If a Windows computer is connected to more than one monitor, the brightness of multiple displays cannot be adjusted using keyboard shortcuts. To adjust the brightness, you have to use the physical buttons on the external monitors.

如果物理按钮不方便使用，也可以通过python的`screen_brightness_control`包来调节多个显示器的亮度。

If the physical buttons are inconvenient to use, you can adjust the brightness of multiple monitors using the Python `screen_brightness_control` package.

<br>

---

### 使用screen_brightness_control包 - Using screen_brightness_control

首先安装`screen_brightness_control`包：

First, install the `screen_brightness_control` package:

```bash
pip install screen_brightness_control
```

<br>

它支持基础的获取屏幕亮度和设置屏幕亮度功能，如下所示。

It supports basic functions for getting and setting screen brightness, as shown below.

```python
import screen_brightness_control as sbc

# 获取所有显示器 - Get all monitors
displays = sbc.list_monitors()

# 获取第一个显示器的亮度 - Get the brightness of the first monitor
print(sbc.get_brightness(display=displays[0]))

# 设置第二个显示器的亮度为30 - Set the brightness of the second monitor to 30
sbc.set_brightness(30, display=displays[1])
```

这样就可以通过python代码来调节多个显示器的亮度了。

With this, you can adjust the brightness of multiple monitors using Python code.

<br>

---

### 图形化界面 - Graphical Interface (GUI)

为了更易于非程序员用户使用，可以使用`tkinter`库来创建一个简单的图形化界面，通过滑动条来调节各个显示器的亮度，如下所示。

To make it easier for non-programmers to use, you can create a simple graphical interface using the `tkinter` library, allowing users to adjust the brightness of each monitor with sliders, as shown below.

```python
import tkinter as tk
import screen_brightness_control as sbc

# 获取所有显示器和亮度 - Get all displays and their brightness
displays = sbc.list_monitors()
brightness = sbc.get_brightness()

# 创建一个根窗口 - Create a root window
root = tk.Tk()

for index, display in enumerate(displays):

    # 为每个显示器添加控制亮度的滑块
    # Add a slider to control the brightness for each display
    brightness_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", length=300)
    brightness_slider.set(brightness[index])
    brightness_slider.pack()

    # 绑定滑块到设置亮度的函数
    # Bind the slider to the set_brightness function
    brightness_slider.bind(
        "<Motion>",
        lambda event, idx=index: sbc.set_brightness(event.widget.get(), displays[idx]),
    )

# 运行窗口 - Run the window
root.mainloop()
```

这样就可以通过图形化界面来调节多个显示器的亮度了。

This allows you to adjust the brightness of multiple monitors using a graphical interface.

![](3.png)

<br>

稍稍美化一下界面。考虑到有些显示器不支持通过程序来调节亮度，在设置亮度时需添加try-except来捕获异常。最终代码如下所示。

Make the interface slightly more polished. Considering that some monitors do not support brightness adjustment through software, add a try-except block when setting the brightness to catch exceptions. The final code is shown below.

```python
# Control the brightness of the screen using a GUI interface

import tkinter as tk
import screen_brightness_control as sbc

# 获取所有显示器和亮度 - Get all displays and their brightness
displays = sbc.list_monitors()
brightness = sbc.get_brightness()

# 创建一个根窗口 - Create a root window
root = tk.Tk()
root.title("屏幕亮度控制 - Screen Brightness Control")

# 设置窗口的位置 - Set the position of the window
window_width = 500
window_height = 150 * len(displays)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_right = int(screen_width / 2 - window_width / 2)
position_down = int(screen_height / 2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

for index, display in enumerate(displays):

    # 为每个显示器添加标签
    # Add a label for each display
    display_label = tk.Label(root, text=f"\n{index + 1}: {display}")
    display_label.pack(pady=5)

    # 为每个显示器添加控制亮度的滑块
    # Add a slider to control the brightness for each display
    brightness_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", length=300)
    try:
        brightness_slider.set(brightness[index])
    except IndexError:
        # 如果显示器不支持亮度控制，则禁用滑块
        # If the display does not support brightness control, disable the slider
        brightness_slider.set(0)
        brightness_slider.config(state="disabled")
        brightness_slider.config(troughcolor="#505050")
        display_label.config(text=f"\n{index + 1}: {display} (不可用 - Not supported)")
    brightness_slider.pack(pady=5)

    # 绑定滑块到设置亮度的函数
    # Bind the slider to the set_brightness function
    brightness_slider.bind(
        "<Motion>",
        lambda event, idx=index: sbc.set_brightness(event.widget.get(), displays[idx]),
    )

# 运行窗口 - Run the window
root.mainloop()
```

<br>

其最终效果如图所示：

The final effect:

![](1.png)

<br>

有多个显示器时的效果如图所示：

The effect with multiple monitors:

![](2.png)

<br>

---

### 编译为可执行文件 - Compile to Executable

为了方便使用，可以将python脚本编译为可执行文件（.exe文件），这样就不需要安装python环境了。使用pyinstaller库可以实现这一功能。

To make it easier to use, you can compile the Python script into an executable file (.exe file) so that a Python environment is not needed. This can be done using the pyinstaller library.

<br>

首先安装`pyinstaller`库：

First, install the `pyinstaller` library:

```bash
pip install pyinstaller
```

然后使用以下命令将脚本编译为可执行文件，需将`script.py`替换为实际的脚本文件名。

Then use the following command to compile the script into an executable file, replacing `script.py` with the actual script file name.

```bash
pyinstaller --onefile --noconsole script.py
```

编译完成后，会在`dist`目录下生成一个可执行文件，双击即可运行。

After compilation, an executable file will be generated in the `dist` directory, which can be run by double-clicking.