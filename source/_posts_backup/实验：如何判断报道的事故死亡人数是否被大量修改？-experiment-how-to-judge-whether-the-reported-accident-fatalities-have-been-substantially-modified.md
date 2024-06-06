---
title: >-
  实验：如何判断报道的事故死亡人数是否被大量修改？ - Experiment: How to judge whether the reported
  accident fatalities have been substantially modified?
tags:
  - http://schemas.google.com/blogger/2008/kind#post
  - 敏感
  - 编程
  - 随想
excerpt: ''
date: 2023-04-22 01:13:00
---

<!-- more -->
 实验思路：如果认为每一次事故的死亡人数服从指数分布的话，那么可以通过比较公布的大量的事故死亡人数样本与指数分布预测的数值，从而判断公布的死亡人数是否被大量修改。

Experiment idea: If the number of death of each accident obeys the exponential distribution, then it can be judged whether the announced death toll has been substantially modified by comparing the published number of accident death toll samples with the values predicted by the exponential distribution.

  

以下是本实验的实现过程。

The following is the process of this experiment.

  

我选择的数据来源是人民日报官方微博。我在人民日报的微博账号中搜索“遇难”，并统计2016年至今(2023.4.22)的所有相关的微博中提到的事故的死亡人数。选择人民日报的原因是其是国内最大且最权威的报纸，而且几乎每一条与事故相关的微博都会报道一个清晰的死亡人数。

The data source I chose is the official Weibo of the People's Daily. I searched for "遇难"(means "got killed" in Chinese) in the Weibo account of People's Daily, and count the death toll of all relevant accidents mentioned in Weibo from 2016 to the present (2023.4.22). The reason for choosing People's Daily is that it is the largest and most authoritative newspaper in China, and almost every blog related to the accident will be reported with a clear death toll.

  

注，由于本实验的数据由本人手动统计，再加上不是所有的人民日报报道的事故的微博都会包含“遇难”一词。所以本实验所用的数据可能与真实数据有所出入，本实验得出的结论也只具有参考价值。

Note, since the data in this experiment was manually collected by myself, and not all the blogs of accidents reported by the People's Daily will contain the word "遇难". Therefore, the data used in this experiment may be different from the real data, and the conclusion is for reference only.

  

实验结果如下所示。

The experimental results are shown below.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi1uXlkVgGB66uTJ158UmuUPypQICvrIb3g4PvyOFGZVHZr9OPq9FlEUT8uyxEM75wtPC7ymn9sUKc-fB0hPYIa77OdIpAMaYQubOxEvDmEptKTv8LiKDuEUv2b-hq05slwl9PUILidyg5fxvyJCUDCYQMdQsLQZ4u0fL9BVF4HdmY2MFwDsxmvt8iK=w640-h266)](https://blogger.googleusercontent.com/img/a/AVvXsEi1uXlkVgGB66uTJ158UmuUPypQICvrIb3g4PvyOFGZVHZr9OPq9FlEUT8uyxEM75wtPC7ymn9sUKc-fB0hPYIa77OdIpAMaYQubOxEvDmEptKTv8LiKDuEUv2b-hq05slwl9PUILidyg5fxvyJCUDCYQMdQsLQZ4u0fL9BVF4HdmY2MFwDsxmvt8iK)

左图为从2021年至今的事故死亡人数统计图，右图为从2016年至2021年的事故死亡人数统计图。x坐标代表着死亡人数，y坐标代表着发生频数。橙色线和红色线的横坐标为10和30人，代表着中国法律规定的较大事故，重大事故，和特大事故的分界。图中未包括事故死亡人数为50人以上的事故。

The left panel shows the statistics of accident deaths from 2021 to the present, and the right shows the statistics of accident deaths from 2016 to 2021. The x-coordinate represents the number of deaths, and the y-coordinate represents the frequency of occurrence. The position of the orange line and the red line are 10 and 30 people, respectively, which represent the boundaries of relatively large accidents, major accidents, and extremely serious accidents stipulated by Chinese law. Accidents with more than 50 fatalities are not included in these figures.

  

此外，我在图中补充了利用两组数据做的指数回归曲线。通过比较橙色线和红色线两端的数据与指数回归曲线的差距，可以更清晰地体现结论。

In addition, I supplemented these figures with exponential regression curves using those sets of data. The conclusion can be shown more clearly by comparing the distance between the data at the ends of the orange line and the red line and the exponential regression curve.

  

从图中可以看出，从2016年到2021年，橙色线与红色线左右的事故发生频数差不多，符合指数分布。这说明从2016年到2021年，死亡人数未被大量修改。

It can be seen from the figure that from 2016 to 2021, the frequency of accidents around the orange line and the red line is similar, which conforms to the exponential distribution. This illustrates that the death toll has not been substantially revised from 2016 to 2021.

  

2023.4.22

  

附录1：画图所用的python程序：

Appendix 1: The python program used for drawing:

\`\`\`python
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve\_fit


def target\_func(x, a, b):
    return a \* np.exp(-b \* x)


df = pd.read\_excel(r'C:\\遇难.xlsx', sheet\_name='Sheet1')

x = \[\]
x1 = np.zeros(500)
x2 = np.zeros(500)
for num in df\["遇难人数"\]:
    x.append(int(num))
for data in x\[:37\]:
    x1\[data\] += 1
for data in x\[37:\]:
    x2\[data\] += 1

popt1, pcov1 = curve\_fit(f=target\_func, xdata=range(500), ydata=x1)
popt2, pcov2 = curve\_fit(f=target\_func, xdata=range(500), ydata=x2)

plt.figure(figsize=(12, 5))

a = plt.subplot(121)
a.bar(range(500), x1)
y1 = \[target\_func(i, popt1\[0\], popt1\[1\]) for i in range(500)\]
plt.plot(range(500), y1)
plt.xlim(\[0, 50\])
# plt.ylim(\[0, 0.15\])
plt.xticks(\[5, 10, 15, 20, 25, 30, 35, 40, 45, 50\])
plt.plot(\[9.5, 9.5\], \[5, 0\], color='orange')
plt.plot(\[29.5, 29.5\], \[5, 0\], color='red')

b = plt.subplot(122)
b.bar(range(500), x2)
y2 = \[target\_func(i, popt2\[0\], popt2\[1\]) for i in range(500)\]
plt.plot(range(500), y2)
plt.xlim(\[0, 50\])
# plt.ylim(\[0, 0.15\])
plt.xticks(\[5, 10, 15, 20, 25, 30, 35, 40, 45, 50\])
plt.plot(\[9.5, 9.5\], \[17, 0\], color='orange')
plt.plot(\[29.5, 29.5\], \[17, 0\], color='red')
plt.show()
\`\`\`

  

附录2：收集的数据：

Addendum 2: Data I collected:

  

 年 月日 事件 遇难人数

2023 4.18 长峰医院 29

3.1 蓝天救援队 1

2022 11.21 河南 38

9.18 贵阳三荔 27

9.12 陕西落水蒋正全 1

9.11 泸定地震 93

8.21 青海大通山洪 26

8.13 彭州山洪 7

6.17 兰州爆炸 6

6.1 雅安地震 4

5.5 长沙自建房倒塌 54

4.18 蓝天救援队邹鑫 1

3.28 东航飞行事故 132

2021 12.12 烟台货船沉没 9

12.5 山西寿阳 8

11.21 云南失联地质人员 4

10.5 山西蒲县山洪 4

9.13 青海柴达尔煤矿 19

8.12 湖北随县降雨 21

8.2 河南洪涝 302

7.21 珠海隧道透水 14

7.21 保定龙卷风 2

7.13 苏州酒店坍塌 17

7.9 山西黄河失联学生 5

6.11 甘肃越野赛 21

6.4 重庆王红旭 1

6.3 兰新铁路相撞 9

5.22 大理森林火灾 2

5.15 武汉龙卷风 8

5.1 洱海坠机 4

4.22 上海厂房火灾 8

4.8 河北赤城爆炸 9

4.3 浙江舟山渔船沉没 8

3.2 厦门坠海直升机 4

2.17 山东招远金矿 6

1.26 山东烟台金矿 10

1.5 喀什拉齐尼巴依卡 1

2020 12.5 重庆永川煤矿 23

10.1 太原景点火灾 13

8.30 临汾饭店坍塌 29

8.20 山东嘉祥煤矿 7

8.6 浙江永康山洪干部 1

8.4 哈尔滨仓库坍塌 9

7.27 四川甘洛山体垮塌 2

7.21 海南三亚退役军人 1

7.17 重庆开州山体滑坡 6

7.10 江西山洪消防员 1

7.9 湖北黄梅山体滑坡 8

7.7 安顺公交坠湖 21

7.3 广东火灾消防通道被堵 5

7.2 四川冕宁暴雨 16

6.29 东莞退伍军人跳水救人 1

6.21 学生落水 8

6.13 浙江温岭槽罐车 19

5.22 广州暴雨泥石流 2

3.31 西昌山火 19

3.30 湖南火车侧翻 1

3.11 泉州酒店坍塌 29

1.20 湖南浏阳烟花厂爆炸 13

1.14 西宁路面塌陷 9

2019 12.17 宜宾煤矿 5

12.11 云南家访 2

12.7 云南货车侧翻 7

11.25 贵州织金煤矿 1

11.18 平遥煤矿 15

10.29 云南坠江扶贫干部 1

10.23 无锡桥梁侧翻 3

10.10 甘肃扶贫干部 3

10.10 宜昌教授跳水救人 1

8.22 汶川暴雨 10

8.11 浙江新昌李安 1

8.11 安徽绩溪李夏 1

8.10 安徽绩溪台风 22

8.6 湖北十堰强降雨 13

8.5 湖北恩施山洪 12

8.1 烟台教师伦学冬 1

7.29 贵州特大山体滑坡 42

7.1 广西黄文秀 1

6.18 陕西宁强山体坍塌 5

6.17 宜宾地震 12

6.9 吉林矿震 9

5.23 贵州贞丰船只侧翻 10

5.16 上海厂房墙体倒塌 5

4.13 深圳洪水 11

4.11 中铝公司火车脱轨 4

4.5 四川木里森林大火 31

4.1 上海落水救人 2

3.26 响水化工厂爆炸 78

3.21 山西乡宁山体滑坡 20

2.23 内蒙古西乌银漫矿业 20

2.16 四川射洪的哥救人 1

1.14 神木百吉矿事故 21

2018 12.26 北京交大实验室爆炸 3

12.18 江西九江扶贫走访 2

12.7 辽宁鞍山冰窟窿 2

12.3 张家口爆燃 23

11.28 辽宁驾车冲撞 6

11.1 重庆万州公交坠江 13

10.29 山东煤业公司 21

10.9 四川达州地陷 4

8.26 哈尔滨酒店火灾 20

8.9 甘肃白银山洪 8

6.16 昆明直升机 3

5.16 102国道相撞 7

4.29 吕梁山体滑坡 9

1.17 安徽涡阳福利院院长 1

2017 8.30 贵州纳雍山体滑坡 23

8.23 广西台风天鸽 12

8.17 山东日照游客拍照 2

8.13 四川阿坝地震 25

7.4 吉林松原燃气管道爆炸 5

6.25 茂县山体垮塌 15

2.13 娄底煤矿爆炸 9

2.2 浙江温州民房坍塌 7

2016 12.3 内蒙古煤矿爆炸 32

11.27 江西丰城发电厂 74

11.1 重庆瓦斯爆炸 33

9.27 宁夏石嘴山 18

9.15 石家庄航空展 4

8.26 甘肃张掖飞行员 1

7.24 邢台洪灾 34

7.8 辽宁本溪黑煤窑 11

7.7 新疆叶城泥石流 35

7.4 三门峡旅游团车祸 1

7.2 天津津蓟客车爆胎 26

6.27 湖南旅游大巴起火 35

6.24 阜宁龙卷风 98

6.7 海监飞机坠毁 4

6.4 四川广元白龙湖游船 2

5.22 浙江平湖救人 2

5.22 大连补习班着火 3

5.11 江西抚州决堤 3

5.9 福建三明山体滑坡 34

3.23 山西同煤集团井下 19

3.8 四川乐山官员边岩垮塌 7

3.6 吉林松树煤矿 12

1.29 山东平邑矿难 1

1.7 宁夏公交大火 17

1.5 深圳滑坡 58