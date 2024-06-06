---
title: >-
  使用python的scipy包做非线性回归 - Performing Nonlinear Regression Using Python's Scipy
  Package
tags:
  - http://schemas.google.com/blogger/2008/kind#post
  - 编程
excerpt: ''
date: 2023-11-09 01:35:00
---

<!-- more -->
可以使用python的scipy.optimize包的curve\_fit来进行非线性回归。

Nonlinear regression can be conducted using the curve\_fit function from Python's scipy.optimize package.

  

这其中最重要的是，需要定义一个函数充当要回归的方程。这里以Langmuir吸附方程举例

Crucially, you need to define a function that represents the equation to be regressed. For example, consider the Langmuir adsorption equation:

y=max\*kc/(1+kc)

  

这个方程有2个参数：k和max。将其转化为python格式，如下所示：

This equation has two parameters: k and max. Transformed into Python format, it appears as follows:

\`\`\`
def func(x, k, max):
    return max \* k \* x / (1 + k \* x)
\`\`\`

  

输入需要用于拟合的xdata和ydata，然后使用curve\_fit函数拟合。xdata和ydata需为np.array格式。

Input the xdata and ydata to be used for fitting, then use the curve\_fit function for fitting. Both xdata and ydata should be in the np.array format.

\`\`\`popt, pcov = curve\_fit(f=func, xdata=xdata, ydata=ydata)
\`\`\`

  

如果需要指定参数的初始猜测值的话，需在curve\_fit指定p0参数，p0的长度需与参数个数相同。

If you want to specify initial guesses for the parameters, use the p0 parameter in curve\_fit. The length of p0 should match the number of parameters.

  

完整版代码如下：

Here's the complete code:

\`\`\`
import numpy as np
from scipy.optimize import curve\_fit
import matplotlib.pyplot as plt

# the value of x and y
xdata = np.array(\[0.001, 0.0025, 0.005, 0.01, 0.015, 0.02\])
ydata = np.array(\[1.77, 7.07, 11.90, 16.41, 19.02, 20.42\])


# y=max\*kc/(1+kc)
def func(x, k, max):
    return max \* k \* x / (1 + k \* x)


popt, pcov = curve\_fit(f=func, xdata=xdata, ydata=ydata, p0=(200, 30))

k\_fit = popt\[0\]
max\_fit = popt\[1\]

# adjust the range of x
x\_linspace = np.linspace(0, 0.05, 50)
y\_linspace = func(x\_linspace, \*popt)

plt.plot(x\_linspace, y\_linspace, label='Fit line\\nk=%5.3f' % k\_fit + '\\nmax=%5.3f' % max\_fit, color='red')
plt.title('Non-linear Curve Fitting')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

print(k\_fit)
print(max\_fit)
\`\`\`

  

拟合结果如下所示。

The results of the fitting are as follows

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYILJhEI1_dKBjaVLNvtGIT5HT2MASD49qQqaibStBfNF-z_BWF3FMkw-OtTDfN26bKdrslSB3h0tn78Og5_3d2j2t72wB76RRlrDWFlcqc9eyaEinaQoAkwdPgCoZiZZto2RWlHbUPX1JRt8p_S1Dtf4WO5aHyRqBKfJqb2_HyNPWMsyOc5qwptJtHMQ/w640-h480/Figure_1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYILJhEI1_dKBjaVLNvtGIT5HT2MASD49qQqaibStBfNF-z_BWF3FMkw-OtTDfN26bKdrslSB3h0tn78Og5_3d2j2t72wB76RRlrDWFlcqc9eyaEinaQoAkwdPgCoZiZZto2RWlHbUPX1JRt8p_S1Dtf4WO5aHyRqBKfJqb2_HyNPWMsyOc5qwptJtHMQ/s640/Figure_1.png)