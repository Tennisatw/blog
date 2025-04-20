---
title: MDAnalysis线性密度模块的bug修复 - Bug fix for the MDAnalysis linear density module
permalink: post/52/
excerpt: MDAnalysis的线性密度模块有bug：模拟一盒Lammps模拟的均匀的水分子，计算出来的线性密度有一些向上突起的尖峰。<br>There is a bug in the MDAnalysis linear density module：when calculating the linear density of a uniformly simulated box of water molecules using LAMMPS, the result includes some sharp upward spikes.
date: 2024-06-10 13:45:07
tags: 
 - 编程 - Programming
 - 技术 - Technology
---

MDAnalysis的线性密度模块有bug：模拟一盒Lammps模拟的均匀的水分子，计算出来的线性密度有一些向上突起的尖峰，如图所示：


There is a bug in the MDAnalysis linear density module: when calculating the linear density of a uniformly simulated box of water molecules using LAMMPS, the result includes some sharp upward spikes, as shown below.

![](1.png)

<br>

其bug位于`lineardensity.py`中，`LinearDensity`类的`__init__`function，第218行：

The bug is located in the `lineardensity.py` file, within the `__init__` function of the `LinearDensity` class, at line 218:

```python
bins = (self.dimensions // self.binsize).astype(int)
```

<br>

当`self.dimensions`为`numpy([20., 20., 20.])`且`self.binsize`为`0.1`时，由于浮点精度误差，`bins`不是`200, 200, 200`，而是`199, 199, 199`。这会导致后续`np.histogram`函数计算出现错误。

可将其替换为：

When `self.dimensions` is `numpy([20., 20., 20.])` and `self.binsize` is `0.1`, due to floating-point precision errors, `bins` becomes `199, 199, 199` instead of `200, 200, 200`. This causes incorrect calculations in the subsequent `np.histogram` function. 

This can be fixed by replacing the line with:

```python
bins = np.round(self.dimensions / self.binsize).astype(int)
```

![](2.png)

<br>

有关于这个问题的详细讨论在[这个github issue](https://github.com/MDAnalysis/mdanalysis/issues/4476)中

For more detailed discussion on this issue, please refer to [this GitHub issue](https://github.com/MDAnalysis/mdanalysis/issues/4476).