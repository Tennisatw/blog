---
title: 使用crest探索氨基酸构象 - Exploring Amino Acid Conformations with Crest
permalink: post/65/
excerpt: 氨基酸的可能的构象对于研究蛋白质的结构和功能至关重要。可以使用crest来对氨基酸的可能的构象进行探索。<br>The possible conformations of amino acids are crucial for studying protein structure and function. Crest can be used to explore these conformations.
date: 2024-10-04 01:15:03
tags: 技术 - Technology
---

氨基酸的可能的构象对于研究蛋白质的结构和功能至关重要。可以使用crest来对氨基酸的可能的构象进行探索。

The possible conformations of amino acids are crucial for studying protein structure and function. Crest can be used to explore these conformations.

<br>

首先，下载20种L-氨基酸的xyz文件。我使用的是[IQmol的xyz文件](https://github.com/nutjunkie/IQmol/tree/master/share/fragments/Molecules/Amino_Acids)。将其打包在同一个文件夹下。

First, download the XYZ files for the 20 standard L-amino acids. Here, I used the [IQmol XYZ files](https://github.com/nutjunkie/IQmol/tree/master/share/fragments/Molecules/Amino_Acids). Place them all in a single folder.

[Amino_Acids.zip](Amino_Acids.zip)

<br>

使用crest探索氨基酸的构象非常简单。只需以下命令即可：

Using crest to explore amino acid conformations is straightforward. Just use the following command:

`crest L-Aspartic_acid.xyz --gfn2 -T 4 --ewin 3`

这其中，--gfn2表示使用GFN2-xTB方法（一种半经验方法），-T 4表示使用4个线程，--ewin 3表示设定能量窗口为3 kcal/mol。

Here, --gfn2 specifies the GFN2-xTB method (a semi-empirical approach), -T 4 sets the number of threads to 4, and --ewin 3 sets the energy window to 3 kcal/mol.

<br>

以上为在真空中的构象搜索。如果需要在水溶液中搜索，可以使用以下命令：

The above command performs conformational search in vacuum. If you want to search in aqueous solution, use the following command:

`crest L-Aspartic_acid.xyz --gfn2 --gbsa -T 4 --ewin 3`

其中，--gbsa表示使用GBSA溶剂模型。

Here, --gbsa specifies the GBSA solvent model.