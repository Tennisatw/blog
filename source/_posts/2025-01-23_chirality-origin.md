---
title: 模拟实验：自然界中手性偏好的起源 - Simulation Experiment：The Origin of Chiral Preference in Nature
permalink: post/73/
excerpt: 自然界中的手性偏好可能源于自催化分子手性与活性突变的不均衡。出于好奇，我们通过模拟自催化分子的演化过程，考察了手性在时间演变中的分布变化。<br>The chiral preference observed in nature may stem from an imbalance between the self-catalytic chirality of molecules and active mutations. Out of curiosity, we simulated the evolutionary process of self-catalytic molecules to explore how chirality evolves over time.
date: 2025-01-23 16:11:07
tags: 编程 - Programming
---

自然界中的手性偏好可能源于自催化分子手性与活性突变的不均衡。出于好奇，我们通过模拟自催化分子的演化过程，考察了手性在时间演变中的分布变化。

The chiral preference observed in nature may stem from an imbalance between the self-catalytic chirality of molecules and active mutations. Out of curiosity, we simulated the evolutionary process of self-catalytic molecules to explore how chirality evolves over time.

<br>

起初，系统中分子具有随机的手性和活性，并经历两种主要过程：自催化繁殖和与环境承载能力相关的死亡。繁殖时，分子的手性保持不变，活性则可能略有波动。

在模拟中，分子数量经历了“爆炸式”指数增长后逐渐趋于稳定。左旋和右旋分子在指数增长初期存在微小的活性差异，在增长过程中，这种差异被持续放大，导致一种手性分子的数量与平均活性高于另一种手性。

在指数增长后期，随着环境承载能力开始限制总数量并提升死亡率，手性数量差距会进一步加剧，最终可能使其中一种手性完全消失。

Initially, the system contained molecules with random chirality and activity, undergoing two main processes: self-catalytic reproduction and death related to the environment's carrying capacity. During reproduction, the chirality of molecules remained unchanged, while their activity could slightly fluctuate.

In the simulation, the number of molecules experienced an "explosive" exponential growth before stabilizing. Left-handed and right-handed molecules had minor differences in activity at the start of the exponential growth phase, but this difference was continuously amplified throughout the process, leading to one chiral type having a higher population and average activity than the other.

In the later stages of exponential growth, as the environment's carrying capacity began to limit the total number and increase the death rate, the disparity in chiral populations intensified, ultimately causing one chiral type to potentially disappear completely.

<br>

若在繁殖过程中允许发生极低概率的手性反转，则会出现优势群体（一种手性的分子）与小群体（另一种手性的分子）竞争的情形。通常，小群体因为数量少、在选择压力下难以维持而迅速灭绝；但在极端情况下，小群体也可能取代优势群体并实现整体系统的手性反转。

If a very low probability of chirality inversion is allowed during reproduction, a competitive scenario emerges between a dominant population (one chiral type) and a small population (the other chiral type). Typically, the small population, due to its low numbers and inability to sustain under selective pressure, would quickly go extinct. However, in extreme cases, the small population might replace the dominant one, resulting in a complete chiral reversal of the system.

<br>

本实验具有化学和生物学研究意义。我们的模拟结果表明，手性偏好有可能在自催化体系中自发出现，并不需要外部因素。

This experiment holds significance for both chemical and biological research. Our simulation results suggest that chiral preference may spontaneously emerge in self-catalytic systems without the need for external factors.

![](image.png)

---

代码 - Code

```python
import random
import matplotlib.pyplot as plt


class molecule:
    def __init__(self, chirality: bool, activity: int):
        self.chirality = chirality  # True = right, False = left
        self.activity = activity

     
# 初始化一些随机手性，随机活性的分子
# 初始时，分子的活性都不太高。
# 初始活性上限越低，越容易出现手性选择性
# 初始分子数量越少，越容易出现手性选择性
# Initialize molecules with random chirality and random activity
# Initially, the activity of the molecules is not very high.
# The lower the initial activity limit, the more likely chirality selection occurs
# The fewer the initial molecules, the more likely chirality selection occurs
moles = []
for i in range(20):
    moles.append(molecule(random.choice([True, False]), random.randint(0, 5)))
    

total_count = 0
right_count = 0
left_count = 0
total = []

right = []
left = []
right_ave_act = []
left_ave_act = []

# 开始模拟
# Start simulation
for i in range(1000):
    for mol in moles:
            
        # 具有繁殖能力的分子会随机死亡，死亡率与种群数量成正比
        # The molecules with reproduction ability randomly die, with the death rate proportional to the population size
        death_rate = total_count / 5000
        if random.random() < death_rate:
            moles.remove(mol)
            continue
            
        # 繁殖
        # Reproduction
        if (random.randint(0, 100) < mol.activity):
            chirality = mol.chirality
            
            # 繁殖时，手性几乎不突变
            # 即右手手性的分子繁殖时，几乎不会出现左手手性的分子
            # 如果手性突变概率过高，则不会出现手性选择性
            # During reproduction, chirality hardly mutates
            # That is, when a right-handed molecule reproduces, it almost never produces a left-handed molecule
            # If the probability of chirality mutation is too high, chirality selection will not occur
            if random.random() < 0.0001:
                chirality = not chirality
                
            # 繁殖时，活度可能由于突变稍有改变，且有害突变更多
            # 如果有益突变远多于有害突变，则不会出现手性选择性
            # During reproduction, the activity may change slightly due to mutation, and harmful mutations are more common
            # If beneficial mutations are much more than harmful mutations, chirality selection will not occur
            activity = mol.activity + random.randint(-10, 3)
            
            # 活度低于1时，不能生成有繁殖能力的分子
            # If the activity is less than 1, the molecule cannot generate a molecule with reproduction ability
            if activity < 1:
                continue
            
            # 活度有上限
            # The activity has an upper limit
            if activity > 100:
                activity = 100
                
            moles.append(molecule(chirality=chirality, activity=activity))
            
            # 由于老化，分子自身的活度也会稍有降低
            # 活度低于1时，分子死亡
            # 此值不影响手性选择性的出现
            # Due to aging, the activity of the molecule itself also slightly decreases
            # If the activity is less than 1, the molecule dies
            # This value does not affect the appearance of chirality selection
            
            # mol.activity -= 1
            # if mol.activity < 1:
            #     moles.remove(mol)
                
    total_count = len(moles)
    right_count = 0
    left_count = 0
    right_total_act = 0
    left_total_act = 0

    for mol in moles:
        if mol.chirality:
            right_count += 1
            right_total_act += mol.activity
        else:
            left_count += 1
            left_total_act += mol.activity
                
    total.append(total_count)
    left.append(left_count)
    right.append(right_count)
    if left_count > 0:
        left_ave_act_amount = left_total_act / left_count
        left_ave_act.append(left_ave_act_amount)
    else:
        left_ave_act_amount = 0
        left_ave_act.append(left_ave_act_amount)
        
    if right_count > 0:
        right_ave_act_amount = right_total_act / right_count
        right_ave_act.append(right_ave_act_amount)
    else:
        right_ave_act_amount = 0
        right_ave_act.append(right_ave_act_amount)
        
    print(f"Step: {i}, Total: {total_count}, Right: {right_count}, Left: {left_count}, Right_ave_act: {right_ave_act_amount}, Left_ave_act: {left_ave_act_amount}")

plt.rcParams['font.family'] = ['Arial', 'SimHei', 'sans-serif']
fig, axs = plt.subplots(2, 1)

axs[0].plot(right, label='Right', alpha=0.5)
axs[0].plot(left, label='Left', alpha=0.5)
axs[0].plot(total, label='Total', alpha=0.5)
axs[0].legend()
axs[0].set_title('分子数量 - Molecule count')
axs[1].plot(right_ave_act, label='Right_ave_activity', alpha=0.5)
axs[1].plot(left_ave_act, label='Left_ave_activity', alpha=0.5)
axs[1].legend()
axs[1].set_title('平均活性 - Average activity')
plt.show()
```
