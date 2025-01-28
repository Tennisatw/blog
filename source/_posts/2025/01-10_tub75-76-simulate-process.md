---
title: 两种MOF的潮湿环境下CO2吸附动力学模拟 - Simulation of CO2 Adsorption Dynamics by Two MOFs in a Humid Environment
permalink: post/70/
excerpt: 本文总结了我们团队近期完成的一个小项目：使用Lammps模拟两种MOF（TUB75和TUB76）在潮湿环境下对CO2吸附作用的动力学。本模拟旨在解释为何TUB75在潮湿环境下仍能表现出优异的CO2吸附性能，并预测TUB76是否也具备类似性能。<br>This article summarizes a recent small project completed by our team：using Lammps to simulate the dynamics of CO2 adsorption by two MOFs (TUB75 and TUB76) in a humid environment. The simulation aims to explain why TUB75 exhibits excellent CO2 adsorption performance in a humid environment and to predict whether TUB76 has similar performance.
date: 2025-01-10 10:43:28
tags: 技术 - Technology
---

本文总结了我们团队近期完成的一个小项目：使用Lammps模拟两种MOF（TUB75和TUB76）在潮湿环境下对CO2吸附作用的动力学。

本模拟旨在解释为何TUB75在潮湿环境下仍能表现出优异的CO2吸附性能，并预测TUB76是否也具备类似性能。

该项目是一个更大合作项目的一部分，待合作组的实验完成后，整体项目将以文章形式发表。

This article summarizes a recent small project completed by our team: using Lammps to simulate the dynamics of CO2 adsorption by two MOFs (TUB75 and TUB76) in a humid environment.

The simulation aims to explain why TUB75 exhibits excellent CO2 adsorption performance in a humid environment and to predict whether TUB76 has similar performance.

This project is part of a larger collaborative project, and the overall project will be published as an article after the experimental work by the collaborating group is completed.

<br>

## 研究方法 - Methods

### 模拟系统描述 - Description of Simulated Systems

在本研究中，我们基于TUB75和TUB76这两种MOF构建了含有不同数量H2O和CO2分子的多个系统。

我们使用实验测定（什么实验？x射线晶体衍射吗？）的TUB75晶胞结构尺寸和重原子初始坐标，在适当位置加入氢原子。然后使用cp2k，采用密度泛函理论（DFT）对几何结构进行优化。我们使用的泛函为PBE，结合GTH-PBE赝势和DZVP-MOLOPT-SR-GTH基组，并包括DFT-D3(BJ)范德华修正。优化后的结构用于构建4 x 12 x 4的TUB75超晶胞，其边长为71.63Å x 55.72Å x 40.34Å，共含有13824个原子。

对于TUB75体系，我们分别构建了含有30、100、300个水分子的系统，以模拟三种不同的湿度。对于每种湿度，我们又分别向系统中插入0、10、30、100个CO2分子，以模拟不同浓度的CO2环境。所有系统共计12个。

In this study, we constructed multiple systems containing different numbers of H2O and CO2 molecules based on the two MOFs, TUB75 and TUB76.

We used the experimentally determined (which experiment? X-ray crystallography?) unit cell dimensions and initial coordinates of heavy atoms of TUB75, adding hydrogen atoms at appropriate positions. Then, using cp2k, we optimized the geometry using density functional theory (DFT). The functional used was PBE, combined with GTH-PBE pseudopotentials and DZVP-MOLOPT-SR-GTH basis sets, including DFT-D3(BJ) van der Waals corrections. The optimized structure was used to construct a 4 x 12 x 4 TUB75 supercell with dimensions of 71.63Å x 55.72Å x 40.34Å, containing a total of 13824 atoms.

For the TUB75 system, we constructed systems containing 30, 100, and 300 water molecules to simulate three different humidity levels. For each humidity level, we inserted 0, 10, 30, and 100 CO2 molecules into the system to simulate different CO2 concentrations. There were a total of 12 systems.

<br>

与TUB75类似，我们使用实验测定的TUB76晶胞结构尺寸和重原子初始坐标，在适当位置加入氢原子，之后在相同的DFT计算条件下进行几何优化。由于TUB76与TUB75的晶胞排列方式不同，我们构建了2 x 12 x 2的TUB76超晶胞，以保证两个MOF的超晶胞结构相似，且金属原子和配体数量相同。TUB76超晶胞的边长为90.54Å x 55.56Å x 39.98Å，共含有15744个原子。

根据CO2填充预实验结果，TUB76的孔隙体积约为TUB75的1.5倍。因此，对于TUB76系统，我们选择的H2O浓度为45、150、450个水分子，CO2浓度为0、15、45、150个CO2分子，以保证对应系统的压强基本一致。

Similar to TUB75, we used the experimentally determined unit cell dimensions and initial coordinates of heavy atoms of TUB76, adding hydrogen atoms at appropriate positions, and then performed geometry optimization under the same DFT calculation conditions. Due to the different unit cell arrangements of TUB76 and TUB75, we constructed a 2 x 12 x 2 TUB76 supercell to ensure similar supercell structures for both MOFs, with the same number of metal atoms and ligands. The TUB76 supercell had dimensions of 90.54Å x 55.56Å x 39.98Å, containing a total of 15744 atoms.

According to the preliminary CO2 filling experiment results, the pore volume of TUB76 is about 1.5 times that of TUB75. Therefore, for the TUB76 system, we selected H2O concentrations of 45, 150, and 450 water molecules, and CO2 concentrations of 0, 15, 45, and 150 CO2 molecules, to ensure that the pressure of the corresponding systems was approximately the same.

<br>

### 力场选择 - Force Fields

本研究为TUB75和TUB76选择了柔性的UFF4MOF力场。水分子使用刚性的TIP4P模型，CO2分子使用TraPPE模型。范德华力的截断半径设为12.5Å，长程库仑相互作用的截断半径设为12Å。

In this study, we selected the flexible UFF4MOF force field for TUB75 and TUB76. The water molecules were modeled using the rigid TIP4P model, and the CO2 molecules were modeled using the TraPPE model. The cutoff radius for van der Waals forces was set to 12.5Å, and the cutoff radius for long-range Coulomb interactions was set to 12Å.

<br>

### 模拟细节 - Simulation Details

所有系统均采用Lammps（lammps-omp/20230802）进行模拟。首先对系统进行能量最小化，然后进行100ps的NVT平衡模拟，在平衡模拟中，温度从10K缓慢升至300K。随后进行50ns的NVT生产模拟，每1ps记录一次数据。我们使用Nose-Hoover恒温器控制温度，时间步长设为0.5fs。

我们对系统使用长程尾部校正，以提高系统压强和能量计算的精度。此外，使用力精度为1e-5的Particle-Particle Particle-Mesh（pppm）算法计算长程库仑相互作用。

All systems were simulated using Lammps (lammps-omp/20230802). First, energy minimization was performed on the systems, followed by a 100ps NVT equilibration simulation, during which the temperature was gradually raised from 10K to 300K. Subsequently, a 50ns NVT production simulation was conducted, with data recorded every 1ps. We used the Nose-Hoover thermostat to control the temperature, with a time step of 0.5fs.

We applied long-range tail corrections to the systems to improve the accuracy of pressure and energy calculations. Additionally, we used the Particle-Particle Particle-Mesh (pppm) algorithm with a force accuracy of 1e-5 to calculate long-range Coulomb interactions.

<br>

### 分析方法 - Analysis Methods

我们使用MDAnalysis（MDAnalysis 2.8.0）包对体系进行分析，包括各原子之间的径向分布函数与气体分子的扩散系数。此外，我们还使用自编的Python脚本为体系绘制了原子轨迹叠加图。

We used the MDAnalysis (MDAnalysis 2.8.0) package to analyze the systems, including the radial distribution functions between atoms and the diffusion coefficients of gas molecules. Additionally, we used custom Python scripts to plot the atomic trajectory overlay maps for the systems.

<br>

## 结果与讨论 - Results and Discussion

### 气体分子的位置分布 - Distribution of Gas Molecules

为了进一步了解CO2和H2O在TUB75与TUB76空穴管道中的分布情况，我们绘制了所有系统的原子轨迹叠加图。我们统计了轨迹中每一帧原子的位置坐标，并计算此坐标处在unit cell中的相对位置。之后，将三维坐标投影到三个方向的平面上，最终得到了三个平面（x-y平面，y-z平面，x-z平面）方向的原子密度图。

图中不同的颜色代表不同的原子种类，颜色深浅表示原子密度，颜色越深表示原子密度越高。

To further understand the distribution of CO2 and H2O in the pore channels of TUB75 and TUB76, we plotted the atomic trajectory overlay maps for all systems. We recorded the position coordinates of atoms in each frame of the trajectory and calculated their relative positions within the unit cell. Then, we projected the three-dimensional coordinates onto three planes (x-y plane, y-z plane, x-z plane) to obtain atomic density maps in three directions.

In the figures, different colors represent different types of atoms, and the color intensity indicates atomic density, with darker colors representing higher atomic density.

<img src="/post/70/traj_overlay_TUB75/TUB75_100_0_xz.png" style="width:400px; display:inline-block; margin-right: 1px;" />
<img src="/post/70/traj_overlay_TUB75/TUB75_100_10_xz.png" style="width:400px; display:inline-block;" />
<img src="/post/70/traj_overlay_TUB75/TUB75_100_30_xz.png" style="width:400px; display:inline-block; margin-right: 1px;" />
<img src="/post/70/traj_overlay_TUB75/TUB75_100_100_xz.png" style="width:400px; display:inline-block;" />

<div style="text-align: center; font-size: smaller;">
图一：TUB75系统中，含有100个H2O分子的系统的一个晶胞的x-z平面原子轨迹叠加图，CO2浓度分别为0、10、30、100。这其中，水色，绿色代表H2O的氧原子和氢原子；红色，橙色代表CO2的碳原子和氧原子；金色，深蓝色，深橙色，深红色，深灰色，灰色分别代表MOF中的铜原子，氮原子，磷原子，氧原子，碳原子和氢原子。图片中的单位为Angstrom。下同。

Figure 1: The x-z plane atomic trajectory overlay maps of a unit cell of the TUB75 system containing 100 H2O molecules with CO2 concentrations of 0, 10, 30, and 100. In this figure, cyan and green represent the oxygen and hydrogen atoms of H2O, respectively; red and orange represent the carbon and oxygen atoms of CO2, respectively; gold, dark blue, dark orange, dark red, dark gray, and gray represent the copper, nitrogen, phosphorus, oxygen, carbon, and hydrogen atoms in the MOF, respectively. The unit in the figure is Angstrom. The same below.
</div>

<img src="/post/70/traj_overlay_TUB75/TUB75_30_30_xz.png" style="width:400px; display:inline-block; margin-right: 1px;" />
<img src="/post/70/traj_overlay_TUB75/TUB75_100_30_xz.png" style="width:400px; display:inline-block;" />
<img src="/post/70/traj_overlay_TUB75/TUB75_300_30_xz.png" style="width:400px;" />

<div style="text-align: center; font-size: smaller;">
图二：TUB75系统中，含有30、100、300个H2O分子的系统的一个晶胞的x-z平面原子轨迹叠加图，CO2浓度均为30。

Figure 2: The x-z plane atomic trajectory overlay maps of a unit cell of the TUB75 system containing 30, 100, and 300 H2O molecules with a CO2 concentration of 30.
</div>

<img src="/post/70/traj_overlay_TUB76/TUB76_150_0_xz.png" style="width:400px; display:inline-block; margin-right: 1px;" />
<img src="/post/70/traj_overlay_TUB76/TUB76_150_15_xz.png" style="width:400px; display:inline-block;" />
<img src="/post/70/traj_overlay_TUB76/TUB76_150_45_xz.png" style="width:400px; display:inline-block; margin-right: 1px;" />
<img src="/post/70/traj_overlay_TUB76/TUB76_150_150_xz.png" style="width:400px; display:inline-block;" />

<div style="text-align: center; font-size: smaller;">
图三：TUB76系统中，含有150个H2O分子的系统的一个晶胞的x-z平面原子轨迹叠加图，CO2浓度分别为0、15、45、150。

Figure 3: The x-z plane atomic trajectory overlay maps of a unit cell of the TUB76 system containing 150 H2O molecules with CO2 concentrations of 0, 15, 45, and 150.
</div>

<img src="/post/70/traj_overlay_TUB76/TUB76_45_45_xz.png" style="width:400px; display:inline-block; margin-right: 1px;" />
<img src="/post/70/traj_overlay_TUB76/TUB76_150_45_xz.png" style="width:400px; display:inline-block;" />
<img src="/post/70/traj_overlay_TUB76/TUB76_450_45_xz.png" style="width:400px;" />

<div style="text-align: center; font-size: smaller;">
图四：TUB76系统中，含有45、150、450个H2O分子的系统的一个晶胞的x-z平面原子轨迹叠加图，CO2浓度均为45。

Figure 4: The x-z plane atomic trajectory overlay maps of a unit cell of the TUB76 system containing 45, 150, and 450 H2O molecules with a CO2 concentration of 45.
</div>

<br>

通过对原子轨迹叠加图进行分析，我们得到了许多有趣的结论：

By analyzing the atomic trajectory overlay maps, we obtained several interesting conclusions:

<br>

在TUB75中，CO2和H2O分子的取向和位置都明显受到疏水有机配体的限制，而呈现出较为规则的排列方式。CO2分子与H2O分子均主要分布于疏水有机配体包裹着的空穴管道中，且均倾向于分布在空穴管道的中心处。这两种分子的取向和位置并不重叠，不存在竞争性关系。

In TUB75, the orientation and position of CO2 and H2O molecules are significantly constrained by the hydrophobic organic ligands, resulting in a relatively regular arrangement. Both CO2 and H2O molecules are mainly distributed in the pore channels surrounded by hydrophobic organic ligands and tend to be located at the center of the pore channels. The orientation and position of these two types of molecules do not overlap, indicating no competitive relationship.

<br>

调整H2O的浓度基本对CO2的分布位置没有影响，且调整CO2的浓度也对H2O的分布影响较小。在CO2与H2O浓度均较高时，极少数H2O分子会穿过疏水有机配体，从而与铜氧簇形成氢键。

Adjusting the concentration of H2O has little effect on the distribution of CO2, and adjusting the concentration of CO2 also has little effect on the distribution of H2O. When both CO2 and H2O concentrations are high, a very small number of H2O molecules may penetrate the hydrophobic organic ligands and form hydrogen bonds with the copper-oxygen clusters.

<br>

相比于TUB75，TUB76的空穴管道更为宽敞，CO2分子仍倾向于分布在空穴管道的中心处。在H2O浓度较低时，H2O分子倾向于与铜氧簇形成氢键，并不与CO2接触；而在H2O浓度较高时，一部分H2O分子会进入空穴管道的中心。

Compared to TUB75, the pore channels of TUB76 are more spacious, and CO2 molecules still tend to be located at the center of the pore channels. At low H2O concentrations, H2O molecules tend to form hydrogen bonds with the copper-oxygen clusters and do not contact CO2; at high H2O concentrations, some H2O molecules enter the center of the pore channels.

<br>

在TUB76中，CO2和H2O分子的位置和取向分布无明显规律。

In TUB76, the position and orientation distribution of CO2 and H2O molecules show no obvious pattern.

<br>

对原子轨迹叠加图分析得到的结论也与径向分布函数的结果相符。我们绘制了H2O的O原子，与CO2的O原子和TUB75和TUB76中的铜氧簇中的O原子的径向分布函数，结果如下所示：

The conclusions obtained from the analysis of the atomic trajectory overlay maps are also consistent with the results of the radial distribution functions. We plotted the radial distribution functions of the O atoms of H2O, the O atoms of CO2, and the O atoms in the copper-oxygen clusters in TUB75 and TUB76, as shown below:

<img src="/post/70/rdf_TUB75/RDF_Ow_Oc_varying_H2O.png" style="width:400px; display:inline-block; margin-right: 1px;" />
<img src="/post/70/rdf_TUB75/RDF_Omof_Ow_varying_H2O.png" style="width:400px; display:inline-block;" />
<img src="/post/70/rdf_TUB75/RDF_Ow_Oc_varying_CO2.png" style="width:400px; display:inline-block; margin-right: 1px;" />
<img src="/post/70/rdf_TUB75/RDF_Omof_Ow_varying_CO2.png" style="width:400px; display:inline-block;" />

<div style="text-align: center; font-size: smaller;">
图五：TUB75系统中，CO2的O原子和H2O的O原子的径向分布函数，随着H2O浓度的变化的变化结果，与随着CO2浓度的变化的变化结果。以及H2O的O原子和MOF中铜氧簇中的O原子的径向分布函数，随着H2O浓度的变化的变化结果，与随着CO2浓度的变化的变化结果。H2O浓度分别为30、100、300，CO2浓度分别为0、10、30、100。

Figure 5: The radial distribution functions of the O atoms of CO2 and H2O in the TUB75 system, with varying H2O concentrations and varying CO2 concentrations. Also shown are the radial distribution functions of the O atoms of H2O and the O atoms in the copper-oxygen clusters in the MOF, with varying H2O concentrations and varying CO2 concentrations. The H2O concentrations were 30, 100, and 300, and the CO2 concentrations were 0, 10, 30, and 100.
</div>

<img src="/post/70/rdf_TUB76/RDF_Ow_Oc_varying_H2O.png" style="width:400px; display:inline-block; margin-right: 1px;" />
<img src="/post/70/rdf_TUB76/RDF_Omof_Ow_varying_H2O.png" style="width:400px; display:inline-block;" />
<img src="/post/70/rdf_TUB76/RDF_Ow_Oc_varying_CO2.png" style="width:400px; display:inline-block; margin-right: 1px;" />
<img src="/post/70/rdf_TUB76/RDF_Omof_Ow_varying_CO2.png" style="width:400px; display:inline-block;" />

<div style="text-align: center; font-size: smaller;">
图六：TUB76系统中，CO2的O原子和H2O的O原子的径向分布函数，随着H2O浓度的变化的变化结果，与随着CO2浓度的变化的变化结果。以及H2O的O原子和MOF中铜氧簇中的O原子的径向分布函数，随着H2O浓度的变化的变化结果，与随着CO2浓度的变化的变化结果。H2O浓度分别为45，150，450，CO2浓度分别为0，15，45，150。

Figure 6: The radial distribution functions of the O atoms of CO2 and H2O in the TUB76 system, with varying H2O concentrations and varying CO2 concentrations. Also shown are the radial distribution functions of the O atoms of H2O and the O atoms in the copper-oxygen clusters in the MOF, with varying H2O concentrations and varying CO2 concentrations. The H2O concentrations were 45, 150, and 450, and the CO2 concentrations were 0, 15, 45, and 150.
</div>

<br>

在TUB75系统中，随着H2O浓度逐渐升高，H2O（的O原子，下同）与CO2的径向分布函数的第一个峰逐渐降低。而增加CO2的浓度会使得此径向分布函数的第一个峰逐渐升高。除此之外，调节CO2和H2O的浓度对其他原子对的径向分布函数影响不大。

在TUB76系统中，随着H2O浓度逐渐升高，H2O中的O原子与铜氧簇中的O原子的径向分布函数的第一个峰逐渐降低，而其与CO2的O原子的径向分布函数的第一个峰逐渐升高。

In the TUB75 system, as the H2O concentration gradually increases, the first peak of the radial distribution function between H2O (O atoms, the same below) and CO2 gradually decreases. Increasing the CO2 concentration causes the first peak of this radial distribution function to gradually increase. Besides this, adjusting the concentrations of CO2 and H2O has little effect on the radial distribution functions of other atom pairs.

In the TUB76 system, as the H2O concentration gradually increases, the first peak of the radial distribution function between the O atoms in H2O and the O atoms in the copper-oxygen clusters gradually decreases, while the first peak of the radial distribution function between the O atoms in H2O and the O atoms in CO2 gradually increases.

<br>

### 扩散系数 - Diffusion Coefficients

（补充MSD的结果）

(Add results for MSD)

<br>

### 结论 - Conclusion

综上所述，由于TUB75的空穴管道是氢键惰性的管道，H2O与CO2都不与管道壁产生氢键相互作用，而是以静电相互作用和范德华力吸附在空穴管道中。CO2和H2O偏好物理结合在不同的位点。因此，这两种气体分子的吸附并不存在竞争性吸附关系。由于空穴管道内壁为低极性的疏水有机配体，较为倾向于与非极性的CO2分子相互作用，这也导致了H2O分子难以影响CO2的吸附。

相比之下，TUB76的空穴管道更为宽敞，且低浓度的H2O易于与铜氧簇形成氢键，CO2分子与H2O分子的吸附位点仍然不重叠。因此，TUB76的CO2吸附性能应该也不会受到H2O的影响。

In summary, since the pore channels of TUB75 are hydrogen-bond-inert channels, both H2O and CO2 do not form hydrogen bonds with the channel walls but are adsorbed in the pore channels through electrostatic interactions and van der Waals forces. CO2 and H2O prefer to physically bind at different sites, so there is no competitive adsorption relationship between these two gas molecules. Due to the low-polarity hydrophobic organic ligands on the inner walls of the pore channels, they tend to interact with non-polar CO2 molecules, making it difficult for H2O molecules to affect CO2 adsorption.

In contrast, the pore channels of TUB76 are more spacious, and low concentrations of H2O easily form hydrogen bonds with the copper-oxygen clusters, while the adsorption sites of CO2 and H2O molecules still do not overlap. Therefore, the CO2 adsorption performance of TUB76 should also not be affected by H2O.

<br>

（补充MSD的论据）

(Add arguments for MSD)

<br>

因此，我们认为，TUB76在潮湿环境下应该仍能表现出优异的CO2吸附性能。

Therefore, we believe that TUB76 should still exhibit excellent CO2 adsorption performance in a humid environment.