---
title: 实验复现：重复的囚徒困境博弈 - Experiment Replication：Repeated Prisoner's Dilemma Game
permalink: post/22/
excerpt: ...这说明爱与和平不能拯救世界，法治和正义才能<br>...This highlights that love and peace cannot save the world, but law and justice can.
date: 2023-09-10 21:30:08
tags: 编程 - Programming
---

## 背景 - Background

囚徒困境是博弈论的非零和博弈中具代表性的例子，个人最佳选择并非群体的最佳选择。以下为囚徒困境的经典表述：

The prisoner's dilemma is a representative example in non-zero-sum game theory, where the best choice for the individual is not necessarily the best choice for the group. Here is a classic presentation of the Prisoner's Dilemma:

<br>

警方逮捕甲、乙两名嫌疑犯，但没有足够证据指控二人有罪。于是警方分开囚禁嫌疑犯，分别和二人见面，并向双方提供以下相同的选择：

若一人认罪并作证检控对方（背叛对方），而对方保持沉默，此人将即时获释，沉默者将判监3年。

若二人都保持沉默（互相合作），则二人同样判监1年。

若二人都互相检举（互相背叛），则二人同样判监2年。

The police arrested two suspects, A and B, but there was not enough evidence to charge them. Therefore, the police detained the suspects separately, met with them individually, and offered the same options to both:

If one confesses and testifies against the other (defects), while the other remains silent, the one who confessed will be released immediately, and the silent one will be sentenced to 3 years in prison. 

If both remain silent (cooperate), they will both be sentenced to 1 year in prison. 

If both testify against each other (defect), they will both be sentenced to 2 years in prison.

https://zh.wikipedia.org/wiki/%E5%9B%9A%E5%BE%92%E5%9B%B0%E5%A2%83

https://en.wikipedia.org/wiki/Prisoner%27s_dilemma

<br>

因为不知道另一位囚徒是否会选择合作还是背叛，而无论对方选择什么，自己选择背叛的收益总比选择合作要高。所以，对于理性的囚徒来说，最佳的选择是选择背叛。因此两位囚徒都选择了背叛，他们被判监2年。

As the prisoner is uncertain if the other prisoner will choose to cooperate or defect, the gains from defecting tend to be higher no matter what the other decides. Hence, it's rational for the prisoner to choose defecting. As a result, both prisoners defected, resulting in a two-year sentence.

<br>

但这种选择又明显不是整体利益最大化的解决方案（帕累托最优）。如果双方都选择合作，两人只会被判监1年。

However, this decision obviously isn't the optimal solution for maximizing collective interests (Pareto optimal). If both parties chose to cooperate, they would only have to serve a one-year sentence.

重复的囚徒困境博弈 - Repeated Prisoner's Dilemma Game
如果允许两个囚犯重复博弈，那么结果就完全不一样了，因为一个囚犯被背叛后，可以在下一轮中惩罚他的对手，这会在某种程度上鼓励对方与自己合作。

The outcome is completely different if the two prisoners are allowed to play the game repeatedly. In such a case, a prisoner would have the chance to retaliate in the next round if he is defected against. This could, to a certain extent, encourage his opponent to cooperate with him. 

<br>

阿克塞尔罗德组织了一场重复囚徒困境博弈，参与者提交代码两两对决，每人都有自己独特的策略。最终，根据总得分判断输赢。这其中，最出彩的却是一种简单的方法：“以牙还牙”策略。该策略在第一次博弈中选择合作，之后会在下一次博弈中重复对手上一次的选择。本文打算复现他的博弈结果。

Axelrod organized a Repeated Prisoner's Dilemma game where participants submitted codes for head-to-head battles, each with their unique strategies. The winners were determined based on total scores. Among all, the most impressive strategy was a simple one: "Tit for Tat." This strategy cooperates in the first round, then copies the opponent's decision in the next round thereafter. This article intends to replicate his game results.

<br>

## 模拟实验 - Simulating

首先，定义一系列策略。我把我能想到的策略都罗列了出来，包括总是合作（always_cooperation），总是背叛（always_defect），随机（random），以牙还牙（tit_for_tat）及其一些变种，报复（retaliatory_strike），和测试者（tester）等等。读者也可以添加自己的策略。

Firstly, a range of strategies are defined. I've listed all the strategies I could think of, including always_cooperation, always_defect, random, tit_for_tat and its variants, retaliatory_strike, tester, and so on. Readers can add their own strategies.

```python
def always_cooperation(we=None, them=None):
    return True


def always_defect(we=None, them=None):
    return False


def random_react_50(we=None, them=None):
    return bool(random.randint(0, 1))


def tit_for_tat(we=None, them=None):
    if len(them) < 1:
        return True
    else:
        return them[-1]


def generous_tit_for_tat(we=None, them=None):
    if len(them) < 1:
        return True
    else:
        if not them[-1]:
            return not bool(random.randint(0, 9))
        else:
            return True


def tit_for_two_tat(we=None, them=None):
    if len(them) < 2:
        return True
    elif (not them[-1]) and (not them[-2]):
        return False
    else:
        return True


def retaliatory_strike(we=None, them=None):
    if False in them:
        return False
    else:
        return True


def tester_5(we=None, them=None):
    if len(them) < 1:
        return False
    else:
        try:
            if False in them[-5:]:
                return True
            else:
                return False
        except IndexError:
            return True
```
这其中，“慷慨的以牙还牙”指即使对面选择了背叛，下一次的策略也有10%的可能是合作；“报复”指以合作开始，但一旦对面背叛了一次，就一直背叛直到结束。“测试者”是以背叛开始，如果对面选择背叛，就选择合作。但一旦对面持续合作5次，就再次开始背叛。

The term "Generous Tit-for-Tat" refers to the strategy where even if the opponent chooses to defect, there's a 10% chance of cooperation in the next round. "Retaliatory_strike" strategy starts with cooperation but switches to constant defection once betrayed. The "Tester" begins with defection, chooses cooperation if the opponent also defects, but returns to defection after five continuous rounds of opponent's cooperation.

<br>

为每个策略生成10个玩家，使其进行200次交易。（但是玩家们（明显）不知道交易的次数）。定义玩家的奖惩机制如下：

Create ten players for each strategy and let them engage in 200 transactions. However, the players (obviously) are not aware of the number of transactions. Let's define the reward and punishment mechanism for the players as follows:

```python
        if st1 and st2:
            score1 += 3
            score2 += 3
        if st1 and not st2:
            score1 += 0
            score2 += 5
        if not st1 and st2:
            score1 += 5
            score2 += 0
        if not st1 and not st2:
            score1 += 1
            score2 += 1
```
每个玩家的初始分数为100000分，每当它参与一局游戏（200次交易）后就扣掉一定的分数（在本局游戏中是480分），当分数小于0时，就迫使它将策略改变成另一个场上存在的策略。通过这种方法来增加选择压力，使得最终只有强大的策略才能存活下来。

Each player starts with a score of 100,000 points. After each game (200 transactions), points are deducted from their score (480 points in this case). When their score falls below zero, they are forced to adopt an alternative strategy currently in use in the field. This methodology increases selection pressure, ensuring only the most robust strategies survive.

<br>

模拟1500场对局，并渲染成视频。完整代码如下：

Simulate 1500 games and render them into a video. The full code is as follows:

```python
import random

from matplotlib import pyplot as plt
from matplotlib.animation import FFMpegWriter


# define strategies
def always_cooperation(we=None, them=None):
    return True


def always_defect(we=None, them=None):
    return False


def random_react_75(we=None, them=None):
    return bool(random.randint(0, 3))


def random_react_50(we=None, them=None):
    return bool(random.randint(0, 1))


def random_react_25(we=None, them=None):
    return not bool(random.randint(0, 3))


def tit_for_tat(we=None, them=None):
    if len(them) < 1:
        return True
    else:
        return them[-1]


def reverse_tit_for_tat(we=None, them=None):
    if len(them) < 1:
        return False
    else:
        return not them[-1]


def generous_tit_for_tat(we=None, them=None):
    if len(them) < 1:
        return True
    else:
        if not them[-1]:
            return not bool(random.randint(0, 9))
        else:
            return True


def tit_for_two_tat(we=None, them=None):
    if len(them) < 2:
        return True
    elif (not them[-1]) and (not them[-2]):
        return False
    else:
        return True


def retaliatory_strike(we=None, them=None):
    if False in them:
        return False
    else:
        return True


def tester_2(we=None, them=None):
    if len(them) < 1:
        return False
    else:
        try:
            if False in them[-2:]:
                return True
            else:
                return False
        except IndexError:
            return True


def tester_5(we=None, them=None):
    if len(them) < 1:
        return False
    else:
        try:
            if False in them[-5:]:
                return True
            else:
                return False
        except IndexError:
            return True


def win_stay_lose_switch(we=None, them=None):
    if len(them) == 0:
        return True
    if we[-1] == them[-1]:
        return True
    else:
        return False


class Player:
    st_name = ''
    st_func = None
    score = 100000


players = []

fig = plt.figure(figsize=(12, 5))
plt.subplots_adjust(left=0.15)

strategies = {'always_cooperation': always_cooperation,
              'random_react_75': random_react_75,
              'tester_5': tester_5,
              'tit_for_two_tat': tit_for_two_tat,
              'generous_tit_for_tat': generous_tit_for_tat,
              'tit_for_tat': tit_for_tat,
              'win_stay_lose_switch': win_stay_lose_switch,
              'random_react_50': random_react_50,
              'reverse_tit_for_tat': reverse_tit_for_tat,
              'retaliatory_strike': retaliatory_strike,
              'tester_2': tester_2,
              'random_react_25': random_react_25,
              'always_defect': always_defect, }

# Increase the number of players using a certain strategy from 10 to 50
strategy_increase = []

for strategy in strategies:
    for _ in range(10):
        player = Player()
        player.st_name = strategy
        player.st_func = strategies[player.st_name]
        players.append(player)

for strategy in strategy_increase:
    for _ in range(40):
        player = Player()
        player.st_name = strategy
        player.st_func = strategies[player.st_name]
        players.append(player)

treat_num = 200


def treat(player1: Player, player2: Player):
    history1 = []
    history2 = []
    score1 = 0
    score2 = 0

    for _ in range(treat_num):
        # There is a 1% chance that the decision will go wrong
        st1 = player1.st_func(history1, history2)
        st1 = st1 if random.randint(0, 99) > 1 else (not st1)
        st2 = player2.st_func(history2, history1)
        st2 = st2 if random.randint(0, 99) > 1 else (not st2)

        if st1 and st2:
            score1 += 3
            score2 += 3
        if st1 and not st2:
            score1 += 0
            score2 += 5
        if not st1 and st2:
            score1 += 5
            score2 += 0
        if not st1 and not st2:
            score1 += 1
            score2 += 1

        history1.append(st1)
        history2.append(st2)

    # Add some pressure to force each player to improve their score.
    player1.score += score1 - 2.4 * treat_num
    player2.score += score2 - 2.4 * treat_num


writer = FFMpegWriter(fps=30)

with writer.saving(fig, "rpdg.mp4", dpi=100):
    for i in range(1, 1501):
        for player1 in range(len(players)):
            while True:
                player2 = random.randint(0, len(players) - 1)
                if player1 != player2:
                    break
            treat(players[player1], players[player2])

            # Players unable to improve their scores will be forced to use new strategies
            if players[player1].score <= 0:
                p = random.randint(0, len(players) - 1)
                players[player1].score = 10000
                players[player1].st_name = players[p].st_name
                players[player1].st_func = players[p].st_func

            if players[player1].score <= 0:
                p = random.randint(0, len(players) - 1)
                players[player2].score = 10000
                players[player2].st_name = players[p].st_name
                players[player2].st_func = players[p].st_func

        x = list(strategies.keys())
        result = [0 for result in x]
        for player in players:
            result[x.index(player.st_name)] += player.score

        plt.clf()
        plt.barh(x, result)
        plt.title(f'increase={strategy_increase} round={i} ')
        plt.pause(0.001)
        if i % 10 == 0:
            writer.grab_frame()
```

<br>

生成的视频如下：

The videos are as follows:

![](1.mp4)

<br>

可以看出，“总是合作”策略不久就消失了，一些无脑合作的策略消失的也很快。虽然“总是背叛”和“报复”在中期主导着局面，并且导致所有的策略的分数都掉得飞快，但最终还是三种“以牙还牙”策略坚持到了最后。这似乎说明纯圣母和纯坏蛋都不会在社会上存在，主导社会的是有自卫能力的好人。

It becomes clear that the "always cooperate" strategy soon faded, as did strategies that involved mindless cooperation. Although "always defect" and "retaliatory strike" dominated the scene in the medium term and caused a rapid drop in all strategies' scores, three types of "tit-for-tat" strategies eventually prevailed. This suggests that Real good guys and real devils do not exist in society, and those who govern are good people with the ability to defend themselves.

<br>

另，“慷慨的以牙还牙”要比普通“以牙还牙”更成功，这似乎说明要适当原谅别人的错误。

Additionally, the "generous tit-for-tat" has proven to be more successful than the regular "tit-for-tat," implying the importance of forgiving others' mistakes.

<br>

## 修改初始分布 - Adjusting the Initial Distribution

考虑到如果只有一个“以牙还牙”，其余人都是“全部背叛”，那这一个“以牙还牙”一定坚持不了多久。这说明最终结果与策略的初始分布有关。在上文的程序中，在strategy_increase列表处添加策略的名字可以将此策略的初始数量从10加到50。比如：

It seems that if there is only one "tit-for-tat," and everyone else "always betrays", this single one is unlikely to last long. Does this signify that the final outcome is related to the initial distribution of strategies. In the above program, adding strategy names to the strategy_increase list increases its initial number from 10 to 50. For instance:

```python
strategy_increase = ['tit_for_tat', 'generous_tit_for_tat']
```

<br>

所有模拟的结果只有两种可能，“针锋相对”阵营获胜，或者“报复”获胜。“针锋相对”阵营其实相当脆弱。如果“全部背叛”和“报复”的比例超过一定值，那针锋相对就很难取得优势。值得注意的是，即使开局是由“全部合作”主导的，但由于它不会存活太久，它反而变成了培养“全部背叛”等非友善策略的土壤。

All the simulations' results only have two possibilities - either the "Tit for Tat" camp wins or the "retaliatory strike" prevails. The "Tit for Tat" camp is relatively fragile. If the proportion of "always betrays" and "retaliatory strike" exceeds a certain level, it makes it challenging for "Tit for Tat" to gain superiority. Notably, even though the game could start with a dominance of "Total Cooperation", it doesn’t last long and ironically, it becomes the breeding ground for non-friendly strategies like "always betrays". 

<br>

另外，如果开局就是由“针锋相对”系策略主导，那么所有的非友善策略会很快得全都消失，但很多友善策略都能有存活空间。

这说明爱与和平不能拯救世界，法治和正义才能（

On another note, if the game starts dominated by the "Tit for Tat" strategy, then all the non-friendly strategies will soon disappear, providing space for many friendly strategies. 

This highlights that love and peace cannot save the world, but law and justice can.