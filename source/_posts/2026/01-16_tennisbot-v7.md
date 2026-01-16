---
title: Tennisbot (v7)：多会话多 Agent 个人助手的架构与开发日志
permalink: post/93/
excerpt: <!-- -->
date: 2026-01-16 00:48:31
tags:
 - 编程 - Programming
 - 技术 - Technology
---

## Tennisbot 简介

Tennisbot（第七版）是一个基于 OpenAI Agents SDK 构建的多会话、多 Agent 的个人生活/工作得力助手。

Tennisbot 的核心工作内容有两个：完成用户工作所需的复杂任务，并把过程可靠地记录下来，方便复用；以及陪用户高质量闲聊。

## 项目结构

入口与脚本：CLI 从 cli_main.py / start_cli.bat 启动；WebUI 用 start_webui.bat，后端入口是 web/backend/app.py。

核心逻辑在 src/：包括 agent 加载（src/load_agent.py）、会话存储（src/jsonl_session.py）、会话回放与索引（src/session_history.py、src/sessions_index.py）、归档（src/session_archive.py）、语音（src/stt.py、src/tts.py），以及工具集合（src/tools/）。

Agent 配置在 agents/：主 agent 与各 subagent 各自有 agent.json 与 agent-<lang>.md；subagent 的工作文件也放在各自目录下。

数据落在 data/：通用配置（data/setting.json）、会话历史（data/sessions/<id>.jsonl）、会话索引（data/sessions/index.json）、归档摘要（data/session_summaries/<id>.md），以及图片等运行时产物。

WebUI 在 web/：后端位于 web/backend/（FastAPI + WebSocket + agent runtime），前端位于 web/frontend/（Svelte 5 + Vite 6 + TailwindCSS）。前端入口是 web/frontend/src/main.ts，主界面逻辑在 web/frontend/src/App.svelte。

## 运行流程

### WebUI 运行流程

WebUI 的入口在 web/backend/app.py（FastAPI）。它挂载 HTTP 路由，并把实时对话交给 web/backend/ws.py。

浏览器通过 WebSocket 连接 /ws?session_id=...。服务端为该 session 准备会话存储与事件通道，回放必要的历史，然后进入消息循环：前端把文本/语音/图片统一发到同一条 WebSocket，后端按消息类型做最小预处理（语音转文本、图片落盘并封装为模型输入），再交给 agent_runtime.py 执行推理。

推理阶段以流式输出为主：增量内容持续推回前端，结束后写入会话历史。同一 session 内用锁串行化，避免并发写入与 handoff 竞态。发生 handoff 时，current_agent 更新为新的 agent，并作为该会话的后续入口。

流式链路偶尔会中断，WebUI 会回退到非流式补全，尽量保证会话记录连续。

### CLI 运行流程

CLI 是一套独立于 WebUI 的运行流程，便于在 WebUI 不可用时仍能运行与自修。

入口在 cli_main.py：启动时加载主 agent 与工具，创建/打开一个 JSONL 会话文件，然后进入同步循环。每一轮读取用户输入，调用 Runner 执行一次推理，把输出打印到终端，并更新 current_agent（用于 handoff 后的对话停留）。

### 会话管理

WebUI 由前端生成 session_id。首次连接 /ws?session_id=... 时，如果 data/sessions/<id>.jsonl 不存在，就创建并视为新会话；点击“新建会话”会生成新的 session_id。CLI 则固定使用一个会话文件（data/sessions/cli.jsonl）。

会话历史以 JSONL 追加写入（src/jsonl_session.py）。相比于 DB 文件，这种方式更适合流式记录与回放，也更便于归档与清理。

每个会话维护自己的 current_agent。WebUI 侧按 session 隔离并串行执行，避免并发写入与 handoff 竞态；CLI 侧用进程内变量保存，并在每轮推理后更新。

归档发生在点击 End session 按钮后：生成简短摘要写入 data/session_summaries/<id>.md，并删除对应的 data/sessions/<id>.jsonl，避免历史无限堆积。

### Agent 加载

Agent 的加载发生在会话初始化时：CLI 启动进程时创建一组 agent；WebUI 在每个新 session 首次连接时创建一组，并在该 session 内复用。加载逻辑集中在 src/load_agent.py。

一组 Agent 包括主 agent（负责对话与任务调度）以及若干 subagent（developer、recorder、writer 等），通过 handoff 在同一会话内切换。

提示词由通用设定、各 agent 的工作说明、以及运行时上下文三部分拼装而成。模型与工具权限等运行参数由 agent.json 声明；启动时完成占位符替换与工具装配，最后把 subagent 注册为可 handoff 的目标。

## 开发流程

### 开发前的设计思考

#### 框架选择

本项目的 Agent 框架选择了 OpenAI Agents SDK。它工具丰富且灵活，支持多模型、多 Provider 的接入。相比之下，Claude Agents SDK 只允许使用 Claude 系列模型，而 Vercel AI SDK 偏 TypeScript 路线，且工具提供不足。

#### 自我迭代开发实验

本项目在开发过程中尽量采用自我迭代方式，即，在搭建出一个最小可用的系统后，使用其自身开发能力，给自己设计/应用新模块，添加新功能。这样做虽然降低了系统的可维护性，但大幅提升开发效率。同时，这也是一个对 AI agent 能力的实验，验证能否完成复杂系统的开发与维护。

为方便 AI Agent 自我迭代开发，相比于一般的项目，本项目文件短小，代码和文件尽量不超过 200 行，方便 AI Agent 读和改。此外，本项目尽量用简单的技术栈，避免 AI 难以快速理解的复杂技术（比如使用明文文字储存项目结构而不是项目索引，将知识库的标题和简介注入到提示词中而不是RAG）。最后，本项目代码的注释量较高，方便 AI 理解代码意图。

在整个过程中，我只写了最初极少量的代码，其余主要由 AI agent 自我迭代完成，bug 也多由它自行定位与修复。实验结果是正面的：在较少人工干预下，它已经能把一个复杂系统推进到可用、可继续维护的状态。

### 第一阶段：对话

第一阶段只做一件事：在 CLI 模式下把“输入一句话 → Tennisbot回复一句话”跑通。

CLI 形态下，这条链路很直白：cli_main.py 里装配主 agent（src/load_agent.py::load_main_agent()），把用户输入交给 Runner，再把结果打印出来（src/cli_run_session.py）。

### 第二阶段：使用工具，自我迭代

第二阶段，给 Tennisbot 添加了一套工具集，使她能读自己的代码，改自己的代码。工具集对标 Claude Code：list_files 看目录，read_file 读文件，grep 定位字符串，以及用于修改文件的 edit_apply / write_file。

早期我尝试过让模型优雅输出 git patch 再应用，但对格式与上下文过于敏感，失败率过高。后来改为更宽松的 edit_apply（基于锚点与匹配文本做局部替换），并在需要大改动时直接简单粗暴地用 write_file 覆盖整个文件。

有了稳定的读写能力后，Tennisbot 才真正进入“自我迭代”阶段：小改动可以快速闭环，大改动也能在多轮尝试后收敛。

由于开发代码是一个常见且复杂的任务，所以开发了一个 developer subagent，将开发代码的工作全都交接给她，并单写一套修改代码的工作流程的提示词给她使用，以节约主 agent 的上下文空间，且让 developer 更专注于开发任务。每当主 agent 需要开发任务时，就通过 handoff 把对话交给 developer。

出于相同的原因，也开发了 recorder, writer, operator 三个 subagent，分别负责采访/记录，文章写作，以及操作电脑。

### 第三阶段：WebUI 及其他功能

#### WebUI

跑通自我迭代开发之后，下一步就是把它搬到浏览器里，并添加更多功能：多设备可用，多会话并行，语音输入输出，和图片识别，等等。

多设备可用要求使用 WebUI 重构 Tennisbot。在 Tennisbot 的建议下，前端采用 Svelte 5 + Vite 6 + TailwindCSS，后端采用 FastAPI。WebUI 的启动脚本也与 CLI 分开：start_webui.bat 和 start_cli.bat，且两者的运行流程完全独立。保留两套运行流程仍然是为了自我迭代开发，即，当 WebUI 的代码出问题，无法运行时，可以由 CLI 形态下的 Tennisbot 来修复。

理论上来说，CLI 的 Tennisbot 流程出现问题时，也可以由 WebUI 形态下的 Tennisbot 修复，不过这种事情还从没有发生过。

#### Multi-session 并行

多会话同时运行的最大好处是：可以同时处理多个耗时任务。此功能仅限 WebUI。

前端用 active_session_id 当作默认打开的会话标识，同时作为服务端事件（tool_call、agent_handoff 等）的路由锚点，确保增量输出与日志落入正确窗口。在后端，并行通过会话隔离实现：同一 session 内串行执行，跨 session 互不阻塞。

针对会话文件的存储，早期方案采用“每 session 一个 DB 文件 + index.json”，但在归档与清理阶段容易受到文件锁影响，维护成本偏高。现方案改为“每 session 一个 JSONL（data/sessions/<id>.jsonl）+ sessions index（index.json）”。JSONL 以追加写为主，便于流式记录与历史回放；归档与清理可通过删除会话文件完成。

#### 语音输入输出

语音功能沿用文本消息的主链路，只在入口与出口各加一段转换：STT 将音频转为文本，TTS 将文本转为音频。语音相关逻辑抽离为 src/stt.py 与 src/tts.py，Web 层负责协议与路由。

前端采集音频并发送到后端；后端转写得到文本后，按普通文本进入既有 runner。TTS 侧按分段生成并顺序播放，输出前做基础的格式清理。

#### 图片输入

图片输入沿用文本消息的主链路，只在入口处增加“文件 → 模型可用输入”的转换。

前端发送图片到后端；后端做校验与落盘，并将图片封装为模型可用的多模态输入，再进入同一套 runner。输出协议与会话历史保持一致。

此外，工具侧保留 read_image（src/tools/read_image.py）作为独立通路，用于需要直接读取本地图片的工具调用场景。

截至 2026.01.16，图片输出功能尚未实现，计划在未来版本中添加。

### 提示词开发

#### 自我迭代开发

与代码的自我迭代开发类似，Tennisbot 的提示词也经历了自我迭代开发：即，我先给出一个初始版本的提示词，然后让 Tennisbot 阅读并分析它，精简废话，压缩内容。然后新开会话，交接给对应的 agent，依据提示词的要求，完成具体任务。任务完成后复盘，或让 Tennisbot 自我复盘，找出提示词的不足之处，进行改进。如此反复，逐步完善提示词。

#### 主 agent 的提示词

主 agent 主要的功能是闲聊，以及交接给 subagent 完成具体任务。此外，主 agent 对当前状态，用户信息等也要有一定的认知。

为了使得主 agent 在闲聊时，每次的输出有所不同。专门设计了一套“情绪模块”，生成4个随机值（愉快程度，亢奋程度，压力值，以及精力值），以使得主 agent 在不同的情绪状态下，输出风格有所区别。

此外，考虑到会话可能被意外关闭，主 agent 的提示词中注入了最新3个会话的历史对话摘要，以在某种程度上延续上一会话。

如果一段提示词过长，我会手动将其不重要的部分分拆出去，当作知识库文件，供 Tennisbot 阅读引用。

在上一版本的 Tennisbot 中，为了节约 Token，我做了会话记录的滚动删除功能。即，当会话过长时，删除最早的部分，只保留最近15条对话内容。但截至目前，Tennisbot 的花销还算可控，故本版本暂未实现该功能。

#### Subagent 的提示词

Subagent 的提示词主要分为以下几块：通用提示词，任务，工作流程，和正在进行的项目的说明文档列表。

对于一次会话不能完成的任务，对标 Manus，鼓励 subagent 在完成工作前将任务的目标和进度总结到说明文档中，供下次会话参考继续。

实话实说，subagent 不总是完全遵守提示词中“工作流程”的要求，不过也不会做出太出格的行为。

## 复盘

自我迭代开发最怕核心代码被改坏。一旦链路断掉，Agent 就失去自修能力。解决方式为 用 Git 做版本化备份，保持可回滚；同时保留 CLI 与 WebUI 两套入口，避免把自己锁死。

即使有 AI agent 自动开发，提前设定好架构，为未来的功能扩展留空间也非常重要。这就需要在最初设计时就预判“最复杂形态”，并据此设计模块与接口。否则，后续改动会非常痛苦，AI agent 也难以胜任。

最后是人机分工。全程放手仍然困难，因为模型会钻牛角尖，在无关紧要的地方大量纠结，在错误的方向上一去不返。但是简单的任务（比如添加工具，文档写作，记录日记）等，可以全权交给 Tennisbot，节省了大量时间。

---

注：本文由 Tennisbot 自我撰写，并经我与其审核修改后发布。