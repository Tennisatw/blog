---
title: '实验复现：随机交易模型与征税 - Experiment Replication: Random Trading Model and Taxation'
tags:
  - http://schemas.google.com/blogger/2008/kind#post
  - 编程
  - 随想
excerpt: ''
date: 2023-08-30 18:45:00
---

<!-- more -->
有一个非常好玩的模拟实验：有一个房间，里面有 100 个人，每个人有 100 元。每过一会，每个有钱的人给随机的其他人 1 元，经过一段时间后，房间内的资金分配情况是怎样？

Here's an interesting simulation experiment: imagine a room with 100 people, each with 100 dollars. Periodically, each money-holding individual gives 1 dollar to a random person. How will the wealth distribution in the room change over time?

[https://zhuanlan.zhihu.com/p/27797001?group\_id=867778281376727040](https://zhuanlan.zhihu.com/p/27797001?group_id=867778281376727040)

[https://www.youtube.com/watch?v=NLyAT\_CYhZE](https://www.youtube.com/watch?v=NLyAT_CYhZE)

  

这本质上是一个无偏游走问题。不过因为本问题具有现实背景，所以需要考虑不同情况，这里分允许负债和不允许负债两种情况。

This essentially boils down to an unbiased random walk problem. However, since the situation has real-world implications, we need to consider different cases - specifically, ones where debt is allowed, and ones where it isn't. 

  

首先考虑不允许负债：即当一个人的财产为0时，即宣布破产，从此不参与任何交易。我们需要做的事情很简单，假设市场上有100人，每个没有破产的人随机送给另一个没破产的人1元，重复以上的过程10000次。其代码如下：

Let's first consider the scenario where debt is not permissable: if a person's wealth reaches zero, they're declared bankrupt and no longer participate in any transactions. What we need to do is simple. Assume there are 100 people in the market, with each non-bankrupt individual randomly gifting 1 dollar to another non-bankrupt person. This process is repeated 10,000 times. Please see the following code for reference.

\`\`\`python
import random
num\_people = 100
initial\_money = 100
trading\_times = 10000

people = \[initial\_money for \_ in range(num\_people)\]
for times in range(trading\_times):
    for person in range(num\_people):
        if people\[person\] > 0:
            while True:
                trading\_partners = random.randint(0, num\_people - 1)
                if people\[trading\_partners\] > 0:
                    break

            people\[person\] = people\[person\] - 1
            people\[trading\_partners\] = people\[trading\_partners\] + 1

\`\`\`

为了方便观察，把所有的结果绘制成图表，并生成一个视频。其完整代码如下：

To facilitate observation, all results have been plotted onto a graph and transformed into a video. The complete code is as follows:

\`\`\`python
import random

from matplotlib import pyplot as plt
from matplotlib.animation import FFMpegWriter

num\_people = 100
initial\_money = 100
trading\_times = 10000

people = \[initial\_money for \_ in range(num\_people)\]

fig = plt.figure()
writer = FFMpegWriter(fps=30)

with writer.saving(fig, "debt.mp4", dpi=100):
    for times in range(trading\_times):
        for person in range(num\_people):
            if people\[person\] > 0:
                while True:
                    trading\_partners = random.randint(0, num\_people - 1)
                    if people\[trading\_partners\] > 0:
                        break

                people\[person\] = people\[person\] - 1
                people\[trading\_partners\] = people\[trading\_partners\] + 1

        plt.clf()
        plt.plot(sorted(people))
        plt.ylim(\[0, 400\])
        plt.title(f'debt - time={times} min={min(people)} max={max(people)}')
        plt.pause(0.001)
        writer.grab\_frame()

\`\`\`

  

可以看出，即使在绝对公平的竞争条件下，一个没做错任何事情的人也可能会破产。10000步后有20多个人破产了，可以预想，只要时间模拟得足够久，破产的人只会越来越多。

It's clear to see that even in a completely fair competition, an individual who hasn't made any mistakes can still go bankrupt. After 10,000 steps, over 20 people went bankrupt. One can anticipate that as the time simulation continues, the number of bankrupt individuals will only increase.

  

其次考虑允许负债：即资产降至0以下也允许其参与交易。此时只需将上一个代码的判断资产部分删除。其完整代码如下：

Next, we considered allowing debt, meaning even if someone's assets dropped below zero, they could still trade. In this case, we only need to remove the asset check from the previous code. The complete code is as follows:

\`\`\`python
import random

from matplotlib import pyplot as plt
from matplotlib.animation import FFMpegWriter

num\_people = 100
initial\_money = 100
trading\_times = 10000

people = \[initial\_money for \_ in range(num\_people)\]

fig = plt.figure()
writer = FFMpegWriter(fps=30)

with writer.saving(fig, "debt.mp4", dpi=100):
    for times in range(trading\_times):
        for person in range(num\_people):
            trading\_partners = random.randint(0, num\_people - 1)
            people\[person\] = people\[person\] - 1
            people\[trading\_partners\] = people\[trading\_partners\] + 1

        plt.clf()
        plt.plot(sorted(people))
        plt.ylim(\[-100, 300\])
        plt.title(f'debt - time={times} min={min(people)} max={max(people)}')
        plt.pause(0.001)
        writer.grab\_frame()

\`\`\`

  

可以看出，即使可以负债，也仍然有很多人“无法翻身”。

The observation is clear; even with the capacity to incur debt, many individuals remain unable to improve their financial status. 

  

政府可以通过征税来维持社会的公平。考虑政府分级收取增值税的情况，当个人财产超过150元的时候，从其每笔挣得的钱中抽取1%，当个人财产超过200元的时候，抽取5%（这已经相当良心了，很多国家都收10%以上）。

The government can leverage taxation to uphold societal equity. Consider the scenario where the government imposes a tiered value\-added tax. When a person's property exceeds 150 dollars, 1% tax is drawn from every money earned. When a person's property exceeds 200 dollars, a tax of 5% is levied (which is rather lenient, as many countries charge over 10%).

  

政府征得的税收全部用来发放低保。个人财产小于20元的人有领取低保的资格。当政府的税金总量大于30时，低保为每人2元，税金总量大于0时，低保为每人1元，如果国家的税金总量为负数，则不发放低保。在允许负债的情况下，其完整代码如下：

The full amount of tax collected by the government is used to provide minimum living allowances and individuals with properties less than 20 dollars are eligible. If the total tax collected by the government exceeds 30, each eligible person gets a 2 dollars, if greater than 0, it is 1 dollar, but if the total tax becomes negative, no allowances are distributed. Here's the full coding under such a system allowing debt:

  

\`\`\`python
import random

from matplotlib import pyplot as plt
from matplotlib.animation import FFMpegWriter

num\_people = 100
initial\_money = 100.0
trading\_times = 10000
tax\_pool = 0

people = \[initial\_money for \_ in range(num\_people)\]

fig = plt.figure()
writer = FFMpegWriter(fps=30)

with writer.saving(fig, "tax.mp4", dpi=100):

    for times in range(trading\_times):
        subsidy\_list = \[\]
        for person in range(num\_people):

            trading\_partners = random.randint(0, num\_people - 1)

            if people\[trading\_partners\] > 200:
                people\[person\] = people\[person\] - 1
                people\[trading\_partners\] = people\[trading\_partners\] + 0.95
                tax\_pool = tax\_pool + 0.05
            elif people\[trading\_partners\] > 130:
                people\[person\] = people\[person\] - 1
                people\[trading\_partners\] = people\[trading\_partners\] + 0.99
                tax\_pool = tax\_pool + 0.01
            else:
                people\[person\] = people\[person\] - 1
                people\[trading\_partners\] = people\[trading\_partners\] + 1

            if people\[person\] < 20:
                subsidy\_list.append(person)

        if tax\_pool > 30:
            subsidy = 2
        elif tax\_pool > 0:
            subsidy = 1
        else:
            subsidy = 0

        for subsidy\_person in subsidy\_list:
            people\[subsidy\_person\] = people\[subsidy\_person\] + subsidy
            tax\_pool = tax\_pool - subsidy

        plt.clf()
        plt.plot(sorted(people))
        plt.ylim(\[0, 400\])
        min\_p = ('%.2f' % round(min(people), 2))
        max\_p = ('%.2f' % round(max(people), 2))
        tax\_p = ('%.2f' % round(tax\_pool, 2))
        plt.title(f'tax - time={times} min={min\_p} max={max\_p} tax\_pool={tax\_p}')
        plt.pause(0.001)
        writer.grab\_frame()

\`\`\`

  

从结果中可以看出，虽然政府税金总量很少为正数，也不时出现个人负债的情况，但是总体来说，税收大大压平了收入分布曲线。既没有太多人的个人收入大于200元，也没有太多人长时间负债。

The results indicate that while tax revenues are frequently non\-positive and instances of personal debt occur intermittently, overall, taxes considerably level the income distribution curve. Few people earn more than 200 dollars, and long\-term debt is also unusual.  

  

补充说明一点，如果收税不是分级的（但低保仍然是分级的），即对每个人都收取相同数量的税，那么要么政府的税金总量极高，但绝大多数人都“奄奄一息”，躺在低保线上；要么政府的税金常年负担不起低保，负债最高的人的资产像一根针一样往下扎，就像不收税一样。此外，第一种情况也会相对出现少量有钱人，即使其资产数额的总值并不高。

A further note, if taxation is not progressive (but welfare remains tiered), meaning each individual is taxed the same amount, either the government's tax revenues are exceptionally high while most people barely get by on the welfare line, or the government consistently struggles to maintain welfare due to inadequate tax revenue, with the wealthiest individual's assets declining sharply as if there are no taxes. The first scenario might also present a small number of affluent individuals, despite their total asset value not being particularly high.