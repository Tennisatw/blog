---
title: 使用自定义类捕获 Python 控制台输出 - Capturing Console Output in Python Using Custom Class
tags:
  - http://schemas.google.com/blogger/2008/kind#post
  - 编程
excerpt: ''
date: 2023-06-26 20:23:00
---

<!-- more -->
在python中，当执行一段代码时，如果想要获取这段代码输出到控制台的信息的话，可以使用重定向stdout的方法。

In Python, if you want to capture the information output to the console when executing a piece of code, you can use the method of redirecting stdout.

  

首先，建立一个类，里面有两个函数，write和flush

First, establish a class with two functions, write and flush.

\`\`\`python
class StdoutRedirect:
    def \_\_init\_\_(self):
        self.content = ''

    def write(self, text):
        self.content += text

    def flush(self):
        self.content = ''

\`\`\`

实例化这个类，并且重定向sys.stdout

Instantiate this class and redirect sys.stdout to it.

\`\`\`python
my\_stdout = StdoutRedirect()
sys.stdout = my\_stdout
\`\`\`

之后的任何输出都会进入my\_stdout的content里。

Any subsequent output will go into the content of my\_stdout.

  

在所需重定向输出的代码结束后，只需将sys.stdout重定向回默认的输出流即可。

At the end of the code where you need to redirect the output, you just need to redirect sys.stdout back to the default output stream.

\`\`\`python
sys.stdout = sys.\_\_stdout\_\_
\`\`\`

完整代码如下

The complete code is as follows:

\`\`\`python
import sys


class StdoutRedirect:
    def \_\_init\_\_(self):
        self.content = ''

    def write(self, text):
        self.content += text

    def flush(self):
        self.content = ''


my\_stdout = StdoutRedirect()
sys.stdout = my\_stdout

print(114514)

sys.stdout = sys.\_\_stdout\_\_
result = my\_stdout.content
my\_stdout.flush()

print("result: " + result)
\`\`\`