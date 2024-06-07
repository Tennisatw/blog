---
title: 为MDAnalysis包增加计算间断氢键自相关函数功能 - Add the functionality to calculate intermittent hydrogen bond autocorrelation functions to the MDAnalysis package
permalink: post/49/
excerpt: MDAnalysis包是一个用于分析MD的数据结果的python包，其内有丰富的分析工具，包括分析氢键的自相关函数（Hydrogen bond autocorelation function，hbacf）。但是其只支持分析连续的氢键自相关函数（continuous hbacf），不支持分析间断的（intermittent hbacf）。而其内部支持的intermittency参数也不完全符合间断的hbacf的定义。所以，我打算手动修改源代码。<br>The MDAnalysis package is a Python package for analyzing molecular dynamics (MD) data results, equipped with a rich set of analysis tools, including a function for analyzing Hydrogen bond autocorrelation function (hbacf). However, it only supports the analysis of continuous hbacf and not intermittent hbacf. The intermittency parameter included does not fully comply with the definition of intermittent hbacf either. Therefore, I plan to manually modify the source code.
date: 2024-05-05 02:38:34
tags:
 - 编程 - Programming
 - 技术 - Technology
---

MDAnalysis包是一个用于分析MD的数据结果的python包，其内有丰富的分析工具，包括分析氢键的自相关函数（Hydrogen bond autocorelation function，hbacf）。但是其只支持分析连续的氢键自相关函数（continuous hbacf），不支持分析间断的（intermittent hbacf）。而其内部支持的intermittency参数也不完全符合间断的hbacf的定义。所以，我打算手动修改源代码。

The MDAnalysis package is a Python package for analyzing molecular dynamics (MD) data results, equipped with a rich set of analysis tools, including a function for analyzing Hydrogen bond autocorrelation function (hbacf). However, it only supports the analysis of continuous hbacf and not intermittent hbacf. The intermittency parameter included does not fully comply with the definition of intermittent hbacf either. Therefore, I plan to manually modify the source code.

<p><br></p>

首先，其计算自相关函数的源代码是MDAnalysis/lib/correlation.py处的autocorrelation函数。在这里有一行代码：

Firstly, the source code for computing the autocorrelation function is found in MDAnalysis/lib/correlation.py, within the autocorrelation function. There is a line of code:

```python
Ntau = len(set.intersection(*list_of_sets[t:t + tau + 1]))
```

<p><br></p>

其中，`*list_of_sets[t:t + tau + 1]`是每一帧的氢键数据的集合。如果想要把它修改成既可以计算连续的，也可以计算间断的的hbacf的话，可以把它改成`list_of_sets[t], list_of_sets[t + tau]`。即，将这一行修改为：

where `*list_of_sets[t:t + tau + 1]` represents the collection of hydrogen bond data for each frame. To modify this to compute both continuous and intermittent hbacf, it can be changed to `list_of_sets[t], list_of_sets[t + tau]`. Thus, modifying this line to:

```python
if continuous:
    # continuous: IDs that survive from t to t + tau and at every frame in between
    Ntau = len(set.intersection(*list_of_sets[t:t + tau + 1]))
else:
    # intermittent: IDs that survive at t and t + tau
    Ntau = len(set.intersection(list_of_sets[t], list_of_sets[t + tau]))
```

<p><br></p>

这样，如果参数continuous为Ture，就会计算连续的hbacf，如果continuous为False，就会计算间断的。

This time, if the continuous parameter is set to True, it will compute the continuous hbacf; if set to False, it will compute the intermittent type.

<p><br></p>

autocorrelation函数的定义处也需要修改一下：

The definition of the autocorrelation function also needs some modification:

```python
def autocorrelation(list_of_sets, tau_max, window_step=1, continuous=True):
```

<p><br></p>

通常，我们用来计算氢键的自相关函数所用的是HydrogenBondAnalysis类的lifetime方法。这个方法的源代码在MDAnalysis/analysis/hydrogenbonds/hbond_analysis.py中。我们需要在lifetime调用autocorrelation函数时，传递一个continuous变量，即把它修改成：

Normally, we use the lifetime method of the HydrogenBondAnalysis class to calculate the autocorrelation function of hydrogen bonds. The source code for this method is located in MDAnalysis/analysis/hydrogenbonds/hbond_analysis.py. We need to modify it to pass a continuous variable when the lifetime method calls the autocorrelation function, changing it to:

```python
tau_timeseries, timeseries = autocorrelation(
    intermittent_hbonds,
    tau_max,
    window_step=window_step,
    continuous=continuous
)
```

<p><br></p>

同样，在lifetime的定义处，修改为

Similarly, in the definition of lifetime, modify to:

```python
def lifetime(self, tau_max=20, window_step=1, intermittency=0, continuous=True):
```

<p><br></p>

这样，在计算hbacf时，如果我们将continuous参数设为False，就会得到间断的自相关函数，如下所示。

With these changes, when calculating hbacf and setting the continuous parameter to False, the resulting function will produce intermittent autocorrelation, as shown below.

```python
tau_frame, hbond_lifetime = hbonds.lifetime(tau_max=2000, continuous=False)
```

<p><br></p>

附注： - Note:

[https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.85.768](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.85.768)

这篇文章里提到了连续的和间断的hbacf的定义。

This article also discusses the definitions of continuous and intermittent hbacf.