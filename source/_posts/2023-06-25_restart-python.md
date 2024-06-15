---
title: 在Python中模拟程序重启 - Simulating Program Restart in Python
permalink: post/10/
excerpt: 在编写Tennisbot的主程序时，总是需要使其重启。Python中，可以使用以下命令模拟重启效果。<br>When writing the main program for Tennisbot, it always needs to be restarted. The following command can be used in Python to simulate a restart effect.
date: 2023-06-25 21:14:13
tags: 编程 - Programming
---

在编写Tennisbot的主程序时，总是需要使其重启。Python中，可以使用以下命令模拟重启效果。

When writing the main program for Tennisbot, it always needs to be restarted. The following command can be used in Python to simulate a restart effect.

```python
os.spawnv(os.P_WAIT, sys.executable, [sys.executable] + sys.argv)
exit(0)
```

<br>

本命令的原理是，首先，使用spawnv生成一个子进程，然后挂起父进程。子进程是使用相同的python程序执行相同的脚本。子进程结束后，父进程也立即退出。

The principle of this command is that it first generates a child process using spawnv and then suspends the parent process. The child process executes the same script using the same Python program. Once the child process ends, the parent process also exits immediately.

<br>

但是，其与真正意义上的重启不同的是，父进程是在子进程结束后才结束，所以，在子进程中，执行列出所有进程的代码，可以查看到父进程。如下所示：

However, it's different from a true restart in that the parent process ends only after the child process has finished. Therefore, if you run code to list all processes in the child process, you can see the parent process. This is demonstrated as follows:

<br>

```python
import os
import sys
import time

import psutil


pids = [p for p in psutil.pids() if psutil.Process(p).name() == 'python.exe']
print(pids)
time.sleep(1)
os.spawnv(os.P_WAIT, sys.executable, [sys.executable] + sys.argv)
exit(0)
```
<br>

其输出结果为：

One possible output could be:

```
[24188, 31972]
[9440, 19540, 24188, 31972]
[9440, 16408, 19540, 24188, 31972, 33404]
[9440, 9564, 12696, 16408, 19540, 24188, 31972, 33404]
[1352, 9440, 9564, 12696, 16408, 19540, 24188, 24700, 31972, 33404]
[1352, 4052, 9440, 9564, 12696, 16408, 19540, 24188, 24700, 31972, 33404, 33956]
...
```