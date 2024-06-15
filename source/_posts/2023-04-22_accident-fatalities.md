---
title: 实验：如何判断报道的事故死亡人数是否被大量修改？ - Experiment： How to judge whether the reported accident fatalities have been substantially modified?
permalink: post/5/
excerpt: 从图中可以看出，从2016年到2021年，橙色线与红色线左右的事故发生频数差不多，符合指数分布。这说明从2016年到2021年，死亡人数未被大量修改。<br>It can be seen from the figure that from 2016 to 2021, the frequency of accidents around the orange line and the red line is similar, which conforms to the exponential distribution. This illustrates that the death toll has not been substantially revised from 2016 to 2021.
date: 2023-04-22 01:12:38
tags: 
 - 编程 - Programming
 - 随想 - Thoughts
 - 敏感 - Sensitive
---

<p class="tennisbot" id="左上角有google翻译，如果需要的话<br>There is Google Translate button in the upper left corner, if needed">由于本文可能稍有敏感，这里仅展示英文版。</p>

<br>

Experiment idea: If the number of death of each accident obeys the exponential distribution, then it can be judged whether the announced death toll has been substantially modified by comparing the published number of accident death toll samples with the values predicted by the exponential distribution.

The following is the process of this experiment.

<br>

The data source I chose is the official Weibo of the People's Daily. I searched for "遇难"(means "got killed" in Chinese) in the Weibo account of People's Daily, and count the death toll of all relevant accidents mentioned in Weibo from 2016 to the present (2023.4.22). The reason for choosing People's Daily is that it is the largest and most authoritative newspaper in China, and almost every blog related to the accident will be reported with a clear death toll.

<br>

Note, since the data in this experiment was manually collected by myself, and not all the blogs of accidents reported by the People's Daily will contain the word "遇难". Therefore, the data used in this experiment may be different from the real data, and the conclusion is for reference only.

<br>

The experimental results are shown below.

![](1.png)

<br>

The left panel shows the statistics of accident deaths from 2021 to the present, and the right shows the statistics of accident deaths from 2016 to 2021. The x-coordinate represents the number of deaths, and the y-coordinate represents the frequency of occurrence. The position of the orange line and the red line are 10 and 30 people, respectively, which represent the boundaries of relatively large accidents, major accidents, and extremely serious accidents stipulated by Chinese law. Accidents with more than 50 fatalities are not included in these figures.

<br>

In addition, I supplemented these figures with exponential regression curves using those sets of data. The conclusion can be shown more clearly by comparing the distance between the data at the ends of the orange line and the red line and the exponential regression curve.

<br>

It can be seen from the figure that from 2016 to 2021, the frequency of accidents around the orange line and the red line is similar, which conforms to the exponential distribution. This illustrates that the death toll has not been substantially revised from 2016 to 2021.

<br>

2023.4.22

<br>

<a href="/post/5/script.py" download>Appendum 1: The python script used for plotting:</a>

<a href="/post/5/遇难.xlsx" download>Addendum 2: Source Data</a>