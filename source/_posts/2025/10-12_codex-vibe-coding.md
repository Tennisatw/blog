---
title: 使用codex进行Vibe-Coding的过程记录 - Process Log of Vibe-Coding with Codex
permalink: post/94/
excerpt: <!-- -->
date: 2025-10-12 21:48:33
tags: 
- 编程 - Programming
---

codex是一个非常好用的项目辅助工具，功能十分强大。

前一段时间，本人使用vscode的codex插件，将一个R语言的生信项目：*Iris*，用python进行了重构。

Codex is an exceptionally powerful and user-friendly tool for project assistance.

Some time ago, I used the Codex extension in VSCode to refactor a bioinformatics project originally written in R — *Iris* — into Python.

<br>

具体流程：

1. 通读R代码，理解其框架
2. 手动搭出一个python项目框架，包括创建必要的文件夹，文件。提供函数名。
3. 以函数（或20行代码）为单位手动拆分R代码
4. 逐块发送给codex插件，转录成python代码，并添加至合适位置
    - 注：每次使用codex之前先备份！
5. 逐块同步调试python和R代码，确保python代码能跑通，且关键变量的值与R代码一致

Detailed Workflow:

1. Read through the R code to understand its structure and logic.
2. Manually set up a basic Python project framework, including creating necessary folders and files, and defining function names.
3. Break down the R code manually into functional units (typically functions or blocks of about 20 lines).
4. Send each block to the Codex extension to transcribe it into Python, and insert the output into the appropriate place in the project.
   - *Note: Always back up the project before using Codex!*
5. Debug the Python and R code in parallel, block by block, ensuring the Python version runs correctly and that key variable values match those in the R version.

<br>

难点：

1. 理解IRIS算法的框架，即某个函数究竟在做什么。实不相瞒，直到完成项目时我都没完全搞清楚。
2. 使用稀疏矩阵储存数据，需要决定用什么格式/怎么处理行列名/怎么修改代码。python没有和R的sparseMatrix完全对应的类型，所以需要自己实现class。
3. 调试很难，因为IRIS包已经被编译好了。所以只能使用github上的源码进行调试。出现bug时，由于不懂源代码的逻辑，所以很难看清楚是什么问题（不过可以让codex分析代码）。
4. IRIS算法使用了很多生信的专业知识，比如RNA组学，基因表达矩阵等。还是用了一些机器学习的知识。本人知识储备实在是有限，只能靠codex帮忙理解。

Challenges Encountered:

1. Understanding the IRIS Algorithm Framework
   One major difficulty was grasping the overall structure of the IRIS algorithm — what each function was actually doing. To be honest, I still didn’t fully understand it even by the time the project was completed.
2. Handling Sparse Matrices
   The original code stored data using sparse matrices, which required decisions on the appropriate format, how to handle row and column names, and how to adapt the code. Since Python doesn’t have a direct equivalent of R’s sparseMatrix, I had to implement a custom class to replicate its functionality.
3. Debugging Compiled Code
   Debugging was tough because the IRIS R package is precompiled, making it hard to trace the code behavior directly. I had to rely on the source code from GitHub for debugging. When bugs appeared, I often couldn’t figure out the root cause due to limited understanding of the original logic — though I could sometimes ask Codex to help analyze the code.
4. Domain-Specific Knowledge
   The IRIS algorithm involves a lot of domain-specific knowledge in bioinformatics, such as RNA sequencing and gene expression matrices. It also incorporates machine learning concepts. With limited background in these areas, I often had to rely on Codex to interpret and explain the code to me.

<br>

一些体会：

1. vibe coding基本上靠谱，因为大语言模型的能力越来越强了。至少gpt-5-codex有能力理解需求并生成代码。
2. vibe coding过程中是不需要本人懂细节，懂流程的。人需要做的事只有拆分任务，使用提示词指挥codex工作，运行代码，并将结果反馈给codex进行下一轮优化即可。当然，如果本人懂细节，懂流程，做起来会心里更踏实。
3. vibe coding的提示词不需要多么精良。重要的是清晰，且提供必要的上下文。
4. codex会犯错。遇到错误时重复追问几次，可能会得到更好的结果。

Reflections and Takeaways:

1. Vibe Coding is generally reliable, thanks to the growing capabilities of large language models. At the very least, GPT-5-Codex is already capable of understanding requirements and generating code accordingly.
2. During vibe coding, it’s not necessary for the user to fully grasp the technical details or the overall process. Your role is mainly to break down tasks, guide Codex using prompts, run the code, and provide feedback for the next iteration. Of course, if you do understand the details, the whole process feels more reassuring and controllable.
3. The prompts used in vibe coding don’t have to be finely crafted. What matters most is clarity and the inclusion of relevant context.
4. Codex can and does make errors. When that happens, simply asking follow-up questions or trying a few different phrasings can often lead to better results.