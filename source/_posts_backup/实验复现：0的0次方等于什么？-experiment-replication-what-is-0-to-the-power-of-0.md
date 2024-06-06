---
title: '实验复现：0的0次方等于什么？ - Experiment Replication: What is 0 to the power of 0?'
tags:
  - http://schemas.google.com/blogger/2008/kind#post
  - 编程
excerpt: ''
date: 2023-09-03 06:29:00
---

<!-- more -->
这个实验相当简单，使用计算器计算0^0，其显示1。

This experiment is quite straightforward, using a calculator to compute 0^0, which yields 1.

  

但是这个问题又远比上述复杂，因为我们只需要简单计算一下0^0.01就会发现，其结果等于0，而不是1。无论0的指数多么趋近于0，其结果也并没有更趋近于1。而按照微积分和极限的思路去考察，0^0又是个不定式，因为以各种不同的路径趋近于0时的极限值不同，所以它没有定义。

However, the issue proves to be more complex than it initially appears. Simply computing 0^0.01 reveals that the outcome is 0, not 1. No matter how the exponent of 0 approaches 0, the result does not converge to 1. Viewing it through the lens of calculus and limits, 0^0 is an indeterminate form, as it lacks a defined value due to differing limit values when approaching 0 through various routes.

  

所以与其纠结0^0的值，不如考察函数f(x,y)=x^y在(0,0)附近的图像，从更高的维度解答此问题。考虑从\[-1,1\]内均匀选取201个值，每两个点之间相隔0.01，分别带入x和y，并利用热图的方式画出函数图像。代码呈上。

Therefore, rather than fixating on the value of 0^0, it may be more insightful to examine the graph of function f(x,y)=x^y near (0,0) for a higher-dimensional perspective. Consider uniformly selecting 201 values within the range \[-1,1\], spacing each pair of points by 0.01, and substitute x and y accordingly. Then, the function is depicted using a heatmap. Here's the code.

\`\`\`python
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

x\_list = \[(x - 100) / 100 for x in range(201)\]
y\_list = \[(y - 100) / 100 for y in range(201)\]

z\_real = np.zeros(\[201, 201\])
z\_imag = np.zeros(\[201, 201\])

for x in enumerate(x\_list):
    for y in enumerate(y\_list):
        try:
            power = pow(complex(x\[1\]), y\[1\])
            z\_real\[x\[0\], y\[0\]\] = power.real
            z\_imag\[x\[0\], y\[0\]\] = power.imag
        except ZeroDivisionError:
            z\_real\[x\[0\], y\[0\]\] = None
            z\_imag\[x\[0\], y\[0\]\] = None

fig = plt.figure(figsize=(10, 8))
labels = \['-1'\] + \[''\] \* 49 + \['-0.5'\] + \[''\] \* 49 + \['0'\] + \[''\] \* 49 + \['0.5'\] + \[''\] \* 49 + \['1'\]
sns.heatmap(z\_real.transpose(), cmap='viridis', xticklabels=labels, yticklabels=labels,
            vmax=2, vmin=-2).invert\_yaxis()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

\`\`\`

  

其作出的f(x,y)=x^y的函数图像如下。

And the graph of the function f(x,y) = x^y is here.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6Br5_qOPxbQzFnz6-iOmSPL690AJW0MBQFLqVOoU0xG8QGyzZWlFIr8ukw9tZJTPNxoVZEYwK2q0IRIYgzNCINAWtW-YrHMXlAB9snD8K2-aSb4psCJ8UZXjh9PutgtkscEFT_NOcuQbVuCubKpa0SPTFE_EJcWvKGW4T7KFVw0l7rgee98RSGCZyaeM/w640-h512/Figure_1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6Br5_qOPxbQzFnz6-iOmSPL690AJW0MBQFLqVOoU0xG8QGyzZWlFIr8ukw9tZJTPNxoVZEYwK2q0IRIYgzNCINAWtW-YrHMXlAB9snD8K2-aSb4psCJ8UZXjh9PutgtkscEFT_NOcuQbVuCubKpa0SPTFE_EJcWvKGW4T7KFVw0l7rgee98RSGCZyaeM/s1000/Figure_1.png)

  

使用seaborn包来画热力图，会比普通的plt包好看很多。注意，超过2的值在此图中也会显示为紫色，低于-2的值同理也会显示为黄色。另外，负数的分数指数幂（即图像的左半边）是复数，此图只体现了其实部。

Utilize the seaborn package to create heatmaps, which tends to appear more visually pleasing than the traditional plt package. Note that in this graph, any value exceeding 2 will be presented in purple, and any value below -2 will be demonstrated in yellow. Furthermore, negative fractional powers (on the left side of the image) are complex numbers; this graph merely illustrates their real parts.

  

我们使用的0^0的值是一个约定值。从图中可以看出，f(x,y)=x^y在(0,0)附近没有极限。如果从lim(x→0+) x^0或lim(x→0-) x^0（即左右两方）趋近的话，其极限为1。从这个角度看，约定0^0为1似乎是合理的。然而，考虑lim(y→0+) 0^y（从上方趋近），其极限为0，而从下方趋近无定义。从这个角度看，约定0^0为几都不太合理。

The value we use for 0^0 is a conventional one. As it can be observed from the graph, it is evident that the function f(x,y)=x^y lacks a limit near (0,0). If you approach from lim(x→0+) x^0 or lim(x→0-) x^0 (i.e., from left and right sides), the limit will be 1. Therefore, defining 0^0 to be 1 seems reasonable from this perspective. However, when doing lim(y→0+) 0^y (approaching from above), the limit will be 0, and there's no definition if we approaching from below. Thus, defining 0^0 to any number may not be reasonable from this perspective.

  

事实上，无论约定0^0等于多少，f(x,y)=x^y在(0,0)附近都不连续。但考虑到如果约定0^0=1，f(x)=x^0这个函数就会变成连续函数（即上图中直线y=0处）。此外，约定0^0=1可以方便很多级数的定义，如：

In fact, regardless of the defined value for 0^0, the function f(x,y)=x^y will not be continuous near (0,0). However, if we agree that 0^0=1, the function f(x)=x^0 becomes a continuous function (as shown by the line y=0 in the graph). In addition, defining 0^0 as 1 can be beneficial for defining many series, like:

11\-x\=∑n\=0∞xn

  

但无论如何，0^0的值是人为约定的，如果在处理一类问题时约定0^0=3会变得更方便，那完全可以这么做。

Regardless, the value of 0^0 is a matter of arbitrary convention. If it's more convenient to set 0^0 as 3 when dealing with a certain type of problem, then it's perfectly acceptable to do so.

  

刚才提到，f(x,y)=x^y的函数值可能为复数，这张图是其虚部。

Earlier, it was mentioned that function values of f(x,y)=x^y could be complex numbers. This graph represents the imaginary part of those values.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgfx6MvC9JXXmZk_0qqz3i2-jqPnAPB93wZGbHTAO5Q63DfbE1muuwK1TEGP_p9r6JITJ-NfPqLvNHTMoU_Oq3tjmK95rsTY7V1TOw1cdtac6h2oXLpf_UuK0nJGI-MnbM3XmxnbsVQ_GVZZ6ZB9phlJadCuemncPNON6idq5nEWtqOGsEtKmuaQ5KuTR8/w640-h512/Figure_2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgfx6MvC9JXXmZk_0qqz3i2-jqPnAPB93wZGbHTAO5Q63DfbE1muuwK1TEGP_p9r6JITJ-NfPqLvNHTMoU_Oq3tjmK95rsTY7V1TOw1cdtac6h2oXLpf_UuK0nJGI-MnbM3XmxnbsVQ_GVZZ6ZB9phlJadCuemncPNON6idq5nEWtqOGsEtKmuaQ5KuTR8/s1000/Figure_2.png)