---
title: TUB75/76 simulate process
permalink: post/70/
excerpt: 暂无预览 - No preview available
date: 2025-01-10 10:43:28
tags:
---

总结一下最近带领团队做的一个小项目：使用Lammps模拟两种MOF：TUB75与TUB76，在潮湿环境下，对CO2吸附作用的动力学。

本模拟将试图解释：为什么在潮湿环境下，TUB75也能表现出优异的CO2吸附性能；并预测TUB76是否也有此性能。

本项目是更大的项目的一部分，在合作组的实验做完后，整体的项目将会以文章的形式发表。

<br>

### Description of Simulated Systems

在本项研究中，我们共基于TUB75与TUB76这两种MOF构建了含有不同数量的H2O和CO2分子的数个系统。

本模拟使用实验测定的TUB75 unit cell的结构尺寸与重原子初始坐标，在适当的位置加入氢原子。之后，我们采用密度泛函理论（DFT）对几何结构进行优化。我们采用的泛函为PBE，结合GTH-PBE赝势和DZVP-MOLOPT-SR-GTH基组，并包括DFT-D3(BJ)范德华修正。我们使用优化后的结构构建了4*12*4的TUB75 supercell，其边长为71.63Å x 55.72Å x 40.34Å，共含有13824个原子。

对于TUB75体系，我们分别构建了含有30，100，300个水分子的系统，以模拟3种不同的潮湿度。对于每一种潮湿度，我们又分别向系统插入了0，10，30，100个CO2分子，以模拟不同浓度的CO2环境。所有的系统共计12个。

与TUB75类似，本模拟使用实验测定的TUB76 unit cell的结构尺寸与重原子初始坐标，在适当的位置加入氢原子，之后在相同的DFT计算条件下进行了几何优化。TUB76与TUB75的晶胞排列方式并不相同，我们构建了2*12*2的TUB76 supercell，以保证两个MOF的supercell的金属原子数量与配体数量相同。TUB76 supercell的边长为90.54Å x 55.56Å x 39.98Å，共含有15744个原子。

由CO2填充预实验可知，TUB76的空穴体积约为TUB75的1.5倍。所以对于含有TUB76的系统，我们选择的H2O浓度为：45，150，450个水分子，CO2浓度为：0，15，45，150个CO2分子。

<br>

### Force Fields

<br>

### Simulation Details

<br>

### Analysis method