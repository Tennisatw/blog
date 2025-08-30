---
title: LLM排行榜及测评：25/08/17 - LLMs Leaderboard and Evaluation：25/08/17
permalink: post/86/
excerpt: 本表格汇总了常用大语言模型在常用评测榜单上的表现。榜单涵盖人类偏好、知识与推理能力、数学能力、代码能力、多模态能力等多个方面。<br>This table summarizes the performance of popular large language models across well-known benchmark leaderboards. These rankings cover a range of capabilities, including human preference, knowledge and reasoning, mathematical skills, coding ability, and multimodal performance.
date: 2025-08-17 16:11:52
tags: 
- 随想 - Thoughts
- 技术 - Technology
categories: LLM排行榜 - LLM Leaderboard
---

![](chinese version.png)

本表格汇总了常用大语言模型在常用评测榜单上的表现。榜单涵盖人类偏好、知识与推理能力、数学能力、代码能力、多模态能力等多个方面。

![](english version.png)

This table summarizes the performance of popular large language models across well-known benchmark leaderboards. These rankings cover a range of capabilities, including human preference, knowledge and reasoning, mathematical skills, coding ability, and multimodal performance.

<br>

### 整体评价 - Overall Assessment

新发布的gpt5不出意外地拿到了第一名。都说gpt5的使用手感不如预期，文字生成能力不如gpt4.5，但是在各项能力上还是力压群雄。“既具有很高的原始性能（推理、数学），又具有很强的用户偏好分数（gpt5自评）” 只要有钱，无脑冲openai家的pro会员。

老马说grok是世界上最聪明的模型，他还真不是瞎说。此外，先不论grok的能力有多强，它有（美式）二次元虚拟角色这一点就已经把其他模型秒了。老马还是太会了啊。

刚才说有钱人无脑冲gpt5，其实排名第四的gemini-2.5-pro是可以在google ai studio中免费使用的。虽然有限额，但google账号是可以无限注册的，所以真的是纯白送。作为唯一一个能长期和openai抗衡的公司，google做事还是很让人舒服的。

颇让我意外的是阿里的qwen3竟然排名这么高，尤其是在数学和代码能力上，绝对的t1。其实中国厂商的模型在这张表上整体有点虚低。如果添加一个多语言能力的话，这些模型的排名还能再高一点。另，deepseek什么时候更新啊。

虽然claude opus的代码能力不强，但Claude Code还是太舒服了。

唯一真神gpt-4o排在了30整，廉颇老矣。幸亏我赶紧把这个表做出来了，下一次排名就不一定有了。

新出的claude-opus-4.1也很强，arena text的排名相当高，只是其他榜单还没有更新。

As expected, the newly released GPT-5 took the top spot. While some say GPT-5 doesn’t feel as impressive in use—its text generation reportedly trails GPT-4.5—in raw capability, it still dominates the competition. “It combines exceptional core performance (reasoning, math) with high user preference scores (self-assessed by GPT-5).” If you’ve got the money, it’s a no-brainer to subscribe to OpenAI’s Pro plan.

Elon claims Grok is the smartest model in the world—and he’s not entirely bluffing. Regardless of how strong Grok actually is, the fact that it comes with an anime-style (American take) virtual persona gives it a unique edge over other models. He really knows how to play the game.

While GPT-5 is the obvious choice for those willing to spend, Gemini 2.5 Pro—ranked fourth—is actually free to use on Google AI Studio. Though usage is limited, you can register unlimited Google accounts, effectively making it a free-for-all. As the only company consistently able to rival OpenAI, Google’s offerings are refreshingly user-friendly.

I was quite surprised to see Alibaba’s Qwen3 ranked so highly, especially in math and coding where it's solidly Tier 1. Overall, Chinese-developed models seem slightly underrated on this chart. If multilingual capability were factored in, their rankings would likely rise even further. Also—when will DeepSeek release an update?

Although Claude Opus isn't particularly strong in coding, Claude Code is just such a joy to use.

The GOAT, GPT-4o, sits precisely at rank 30—clearly showing its age. Good thing I managed to compile this table now; it might not make the cut next time.

The newly released Claude Opus 4.1 is also very capable, ranking highly on Arena Text, though other benchmark updates are still pending.

<br>

---

### 附1：[本项目的github仓库地址](https://github.com/Tennisatw/LLM-Leaderboard) - Appendix 1: [GitHub Repository for This Project](https://github.com/Tennisatw/LLM-Leaderboard)

<br>

---

### 附2：各榜单简介及数据来源 - Appendix 2: Introduction to Each Benchmark and Data Source

针对大语言模型的每一个能力，选择了1-3个榜单进行评测。在选择榜单时尽量挑选实时更新的，通用的，且有区分度的榜单。

For each core capability of large language models, 1-3 representative leaderboards were selected for evaluation. Preference was given to leaderboards that are updated in real time, have broad applicability, and offer strong differentiation among models.

<br>

#### 人类偏好 - Human Preference

[LMArena](https://huggingface.co/spaces/lmarena-ai/lmarena-leaderboard)

<!-- https://lmarena.ai/leaderboard -->

通过真实用户对话投票，评估大语言模型在**综合对话体验**上的表现，包括理解能力、回答质量、逻辑性和互动自然度。分数更新很快。

Evaluates **overall dialogue experience** through real user voting—assessing comprehension, response quality, logic, and conversational naturalness. Scores are updated frequently.

<br>

#### 知识与推理能力 - Knowledge & Reasoning

[MMLU-Pro](https://artificialanalysis.ai/evaluations/mmlu-pro)



一个专为更严谨评估大型语言模型语言理解与推理能力而设计的多任务难度提升版知识问答基准，共收录约 12,000 道更具挑战性的题目，选项数量从原始的 4 个增加至 10 个，同时强化了复杂推理需求与题目鲁棒性。

An advanced multi-task benchmark designed to more rigorously test language understanding and reasoning. It includes ~12,000 challenging questions, increasing options from 4 to 10 and strengthening requirements for complex reasoning and question robustness.

<br>

[GPQA](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro)

一个用于评估大语言模型在高质量、专业难度问答（尤其是跨学科推理和知识深度）上的基准数据集。其中 GPQA-Diamond 是指其中最困难、最严格的人类专家编写和验证的问题子集。

A benchmark for evaluating high-quality, expert-level Q&A—especially on interdisciplinary reasoning and deep knowledge. The GPQA-Diamond subset includes the most difficult, expert-curated questions.

<br>

[Humanity’s Last Exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam)

HLE是一个多模态语言模型基准测试，包含约 2,500 道专家设计的跨学科难题，旨在成为衡量 AI 在封闭学术问题上人类专家水平的“最后考试”式评测。

A multimodal benchmark with ~2,500 expert-designed, cross-disciplinary problems. It aims to assess whether AI can match human expert performance on closed academic tasks—like a “final exam” for AI.

<br>

### 长文本推理 - Long Context Reasoning

[AA-LCR](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning)

专注于在**超长文本**中进行分析和推理的人工智能基准与方法，用于评估模型在复杂、多层次语境下的理解与推理能力。

Designed to assess a model’s ability to analyze and reason across **very long texts**, this benchmark focuses on multi-layered, complex contextual understanding and inference.

<br>

<!-- ### 指令遵循? -->

<!-- ### 事实问答？ -->

<!-- [SimpleQA](https://www.kaggle.com/benchmarks/openai/simpleqa) -->

#### 数学能力 - Mathematical Ability

[AIME2025](https://artificialanalysis.ai/evaluations/aime-2025)

美国数学邀请赛 (AIME) 基准测试旨在评估大型语言模型在一项面向高中生、仅限受邀参加的著名数学竞赛中的表现。该基准测试极具挑战性，涵盖代数、几何和数论等广泛的数学主题。

Based on the American Invitational Mathematics Examination, this benchmark tests models on highly challenging problems in algebra, geometry, and number theory—designed for elite high school math competitors.

<br>

#### 代码能力 - Coding Ability

<!-- [SWE-Bench](https://www.swebench.com/)

SWE-Bench 是一个用于评估大型语言模型在真实软件工程场景中自动修复代码能力的基准数据集与测试平台，基于 GitHub 开源项目的历史问题与修复提交构建。

<br> -->

[LiveCodeBench](https://livecodebench.github.io/leaderboard.html)

针对大型语言模型（LLM）进行 **实时代码生成与执行能力** 测评的基准，侧重评估模型在动态环境下编写、运行并修正代码的表现。

Measures real-time code generation and execution. It evaluates how well a model can write, run, and debug code dynamically in an interactive environment.

<br>

#### 多模态能力 - Multimodal Ability

[MMMU](https://mmmu-benchmark.github.io/)

一个跨学科、多模态的大规模评测基准，旨在测试大型模型在涵盖文本、图像等多模态输入下的综合理解与推理能力。

A large-scale, interdisciplinary benchmark focused on assessing a model’s ability to reason across text and image modalities. It covers a wide variety of academic topics and real-world scenarios.

<br>

<!-- MMbench -->

<!-- #### 多语言能力：

[MMMLU](https://huggingface.co/spaces/StarscreamDeceptions/Multilingual-MMLU-Benchmark-Leaderboard)

MMMLU 是一个大规模多语言版本的 MMLU 测试集，用于评测语言模型在多种语言和多学科知识上的理解与推理能力。

<br> -->

---

### 附3：制作流程 - Appendix 3: Workflow Overview

首先，下载各个榜单的网页，然后用BeautifulSoup库解析出各个榜单的表格数据，存为csv文件。

First, each leaderboard webpage was downloaded and parsed using the BeautifulSoup library to extract the table data, which was then saved as CSV files.

<br>

然后，将各个表格的内容合并到一个总表格中，存为表格文件。

统一模型名称是一个难点。因为模型名称有很多变体，且不同榜单使用的名称不一致。

这里我们使用了关键词匹配法：首先列出所有模型家族的关键词（如gpt-4o、gemini-2.5等），然后对每个榜单的模型名称进行关键词匹配，然后再附加上模型修饰词（mini，high，pro等），和模型大小（70B）。匹配不到关键词的模型则使用difflab库模糊匹配。此处代码由chatgpt5帮助编写。

此外，由于很多榜单对模型名称的命名非常随意，所以我们也设置了大量的硬性替换词。这里暂时没有太优雅的方法。

Next, the tables were merged into a single master spreadsheet.

Unifying model names was a major challenge, as model names often have multiple variants and differ across leaderboards. To address this, a keyword matching method was used:

We first listed keywords for all major model families (e.g., GPT-4o, Gemini-2.5). Then, each model name on the leaderboards was matched against these keywords. Additional modifiers like "mini", "high", "pro", or model size tags like "70B" were appended when available. For models that couldn’t be matched via keywords, fuzzy matching was performed using the difflib library. This part of the code was assisted by ChatGPT-5.

Due to inconsistent naming conventions across leaderboards, many hard-coded name replacements were also used. At present, there’s no elegant solution for this step.

<br>

我们希望筛选出常用且功能较强的模型。

首先，我们剔除了只出现在一个榜单中的模型。

由于不同的榜单的难度不同，且收录模型的数量不同，所以我们使用z-score方法对榜单的分数进行标准化处理。然后，我们使用SVD Imputation方法对缺失值进行填充，以估计缺失的分数。最后，我们对补全后的矩阵的每一行求均值，得到每个模型的综合分数。此处思路由chatgpt5提供，代码由chatgpt5帮助编写。

We aimed to include models that are both widely used and functionally strong.

Models appearing on only one leaderboard were excluded.

Because each leaderboard varies in difficulty and coverage, scores were standardized using the z-score method. SVD imputation was applied to fill in missing values and estimate incomplete scores. Finally, the mean score across all benchmarks was calculated for each model to produce an overall composite score. This scoring strategy was proposed by ChatGPT-5, and the code was also developed with its assistance.

<br>

使用chatgpt5的agent模式，批量爬取各模型发布商的官网，获取模型的发布时间信息。

Using ChatGPT-5’s agent mode, we batch-scraped official websites of model providers to retrieve release dates for each model.

<br>

---

### 附4：一些榜单网站 - Appendix 4: Some Benchmark Websites

https://www.datalearner.com/ai-benchmarks

https://llm-stats.com/benchmarks

https://rank.opencompass.org.cn/home