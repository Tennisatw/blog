---
title: Tennisbot第六版：更新简介，项目介绍及使用方法
permalink: post/72/
excerpt: Tennisbot更新至第六版，新版本支持Linux服务器运行，大幅重构代码结构使其更现代化，并全面支持中英文。本文详细介绍了更新内容、项目特性及部署方法。
date: 2025-01-16 11:44:57
tags:
 - 编程 - Programming
 - 技术 - Technology
---

## 更新简介

Tennisbot更新至第六版了。

[Tennisbot的GitHub仓库](https://github.com/Tennisatw/tennisbot)

<br>

（为所有的新读者介绍一下：Tennisbot是一个基于Python、discord.py和OpenAI API开发的AI助手及聊天机器人项目，支持中英文。今年（2025）是它诞生的第五年。之前已经有五代版本。）

<br>

在第五版的基础上，新版本为在linux服务器上运行做了适配，目前的Tennisbot支持windows和linux环境，并可以在Discord上使用。

除此之外，我们挖掘屎山，大幅拆分了代码，使其变得更现代，更模块化，更简洁，更易于维护，包括：  
1. 弃用conda，改为使用pip和pyenv来管理python环境，并精简了依赖包。  
2. 删除了大量的琐碎功能，比如"截屏"，"调节音量"，"查看电池电量"等，仅保留重要或有代表性的功能。  
   - 其中不乏从Tennisbot第一版就有的功能，但因为它们在服务器环境下意义不大，且可以简单通过使用console命令来实现。如果用户需要，可以自行添加。  
3. 收集分散在程序各处的中英文消息，并统一集成在util/config.MESSAGES中，使其看起来更符合现代编程理念。  
4. 使用各种高级（相对上一版而言）封装和传参手法，删除几乎所有的全局变量。  
5. 优化代码结构，对混乱的逻辑进行重构，给main.py减负，使其更符合现代编程理念，且更有助于Tennisbot自己阅读。
6. 重写system提示词，并在其中包含Tennisbot项目的完整信息。  
7. 大幅增加注释量，并重新编写了一个完整详尽的README.md文件，进行一个从安装python配置环境到在服务器上运行Tennisbot的手把手教学。  
8. 增修文本，使得Tennisbot从注释，运行日志，到提示词，聊天，全面支持中英文。  

<br>

此外，在本次更新中：**本项目的"AI安全性"得到了大幅削减**。

随着大语言模型的能力不断提升，Tennisbot的LLM API从gpt-3.5，到gpt-4，再到gpt-4-turbo，再到现在的gpt-4o/gpt-4o-mini，Tennisbot的"智商"也得到了大幅提升。现在的她，已经可以对本项目的代码和提示词进行自我指导并给出修改意见了。我们（指我和Tennisbot，下同）通过拆分代码以及编写system提示词，使Tennisbot可以阅读本项目的全部代码和文件。

但目前还有2个权限没有开放给她：一是无法编辑代码，二是无法真正地重启，以应用代码更新。不过，在后续的版本中，我打算开放权限，打造一个真正能"自我优化"的AI助手。

<br>

## 项目介绍

### 体验Tennisbot

欢迎加入我们的[Discord频道](https://discord.gg/trCwuPYvG2)与Tennisbot聊天。

<br>

### 功能特性

- 💬 智能对话：接入大语言模型API，且支持配置个性化人格（在mdcb/zh-CN-system.txt中）
- 🧠 记忆对话：支持记忆聊天记录，在清理聊天记录前，可以持续多轮对话
- 🌐 示例功能：可以抓取网页，备份聊天记录，查询wiki百科，以及让自己关机（但她可能会抗拒关机，可能需要劝劝）
  - 支持自行在`util.function.py`中删除或添加新功能，并在`mdcb/zh-CN-functions.txt`中修改提示词
- 📊 日志记录：详细的操作和错误日志
- 🔧 灵活设置：每个群组/用户可以有独立的聊天设置，且仅通过对话即可完成所有设置
- 🔄 多开模式：支持手动并行运行多个实例，增强解决复杂问题的能力
  - 除此之外，在遇到复杂问题时，她也可能自动并行运行多个实例
- 💻 访问运行环境：支持访问自身的python运行环境（的镜像），读取变量值，并执行代码，或访问控制台
- 🤖 智械危机：仅通过对话即可使其读取自身所有的代码，配置和运行日志，并指导开发者如何debug

完整的功能列表及使用说明可在部署后通过对话获取。

<br>

### 一些对话示例

- 请详细地介绍怎么使用Tennisbot？都有什么功能？
- 请设置一个7：40的起床闹钟
- 请查询所有闹钟，并取消它们
- 请查询温哥华的天气，并总结
- 请爬取你的开发者的个人博客上的内容
- 请给xxxx@qq.com发送一封邮件，标题为"刷茶壶"，内容为"别忘了刷你的茶壶！"
- 请在维基百科中查询"化学诺奖"页面，并简单预测开发者什么时候可以获奖
- 报一个IndexError
- 请查询本机ip地址。注意：你当前暂时运行在windows上
- 请列出你的所有log文件，判断并读取最新的文件（注：此对话在"mini"模型下可能会失败）
- 请你读取有关你的心智模型的代码（注：有一定概率会拒绝提供，可以适当调节用词）
- （接上）你有什么修改意见吗？

<br>

### 使用要点

- 直接对话：在私聊中，或者名字带有"_Tennisbot"的频道中直接发送消息
- 群组对话：将Tennisbot拉到群组中，在群组中使用 其昵称/`Tennisbot`/`tb` 前缀唤起Tennisbot对话
- 清除聊天记录：通过聊天告诉Tennisbot"清除聊天记录"，或者使用 `-` 前缀开始新对话

<br>

## 部署

### 系统要求

- Python 3.10, 3.11, 3.12（3.13因移除audioop不支持）  
- 可访问Discord API的网络环境，即，需要科学上网  

<br>

### 部署步骤

1. 克隆仓库：
```bash
git clone https://github.com/Tennisatw/tennisbot.git
cd tennisbot
```

2. 准备Python环境：
   - 下载安装Python（如未安装）：https://www.python.org/downloads/
   - 创建虚拟环境：
```bash
# 使用默认Python
python -m venv venv
# 或指定Python版本
path/to/python.exe -m venv venv
```

3. 激活虚拟环境：
```bash
# Linux/macOS
source venv/bin/activate
# Windows
.\venv\Scripts\activate
```

4. 安装依赖：
```bash
pip install -r requirements.txt
```

5. 配置文件设置：
   - 获取Discord token：https://discord.com/developers/applications
   - 获取ChatGPT token：https://platform.openai.com/
   - 获取Discord default chat id
   - 修改`files/bot_config.ini`配置文件

6. 运行机器人：
```bash
python main.py
```

7. （推荐）在服务器使用screen后台运行：
```bash
screen -S tennisbot
python main.py
Ctrl+A D
```

更多功能和使用说明可在部署后通过对话获取。

<br>

---

以下为冗长且无聊的代码结构，及运行逻辑介绍

## 代码结构

Tennisbot/  
│  
├── chat_log/  
│   ├── tennisatw.json  
│   ├── lkvijt-main.json  
│   └── ...  
│  
├── files/  
│   ├── bot_config.ini  
│   ├── emojis.json  
│   ├── gmail.json  
│   ├── schedule.ini  
│   └── welcome.txt  
│  
├── log/  
│   ├── 2025-01-17_09-22-00.log  
│   └── ...  
│  
├── mdcb/  
│   ├── en-US-conv.json  
│   ├── en-US-functions.txt  
│   ├── en-US-system.txt  
│   ├── zh-CN-conv.json  
│   ├── zh-CN-functions.txt  
│   └── zh-CN-system.txt  
│  
├── util/  
│   ├── config.py  
│   ├── func_chat_log.py  
│   ├── func_email.py  
│   ├── func_file.py  
│   ├── functions.py  
│   ├── get_message.py  
│   ├── info_process.py  
│   ├── log.py  
│   ├── mdcb.py  
│   ├── on_message.py  
│   ├── schedules.py  
│   ├── send_message.py  
│   └── set.py  
│  
├── venv/  
│  
├── main.py  
├── README.md  
├── README-zh.md  
├── LICENSE  
└── requirements.txt  

<br>

## 运行逻辑

### main

main.py是Tennisbot的入口文件。初始化了一些配置和计划任务，发送启动和欢迎消息，并启动一个Discord客户端。

get_message，send_message，set，和log分别定义了获取消息，异步发送消息，设置变量，和记录日志的类，并实例化。

<br>

### on_message

Discord客户端由discord.py库提供，负责与Discord API进行交互，处理消息和事件。

创建一个discord bot账户，复制令牌，并填入bot_config.ini中。将discord bot拉到群组中。

在on_message.py中，新建一个继承discord.Client的类，并重写on_message，和on_error函数。

on_message事件在discord群有消息时，都会触发。在on_message函数中，更新get_message实例，获取用户名，群名，及消息内容，并根据条件判断是否需要调用info_process，处理用户输入并作出回复。需要回复的消息有：所有私聊及群名包括"_tennisbot"的群消息，以及以"tennisbot"开头的消息。

在on_error函数中，拦截所有错误以防止程序崩溃。

<br>

### mdcb

在info_process.py中，定义了info_process函数，用于处理输入并回复。info_process会先将用户输入作简单处理后，传递给mdcb.py中的mdcb函数。

<br>

mdcb是mind cube的缩写，是Tennisbot的"心智魔方"。在mdcb函数中会调用大语言模型api生成回复。使用的大语言模型可以通过设置选择，目前支持gpt-4o/gpt-4o-mini。

mdcb/system.txt中定义了Tennisbot的人设，基本信息，以及本项目结构。mdcb/fucntion.txt中包含Tennisbot的所有功能的描述，以及如何使用它们。mdcb函数读取并合并这些信息，作为大语言模型的system提示词。所有的提示词均有中英2个版本。

注：gpt-4o/gpt-4o-mini支持上传function calling list，以提供一个函数列表，供大语言模型调用。但Tennisbot支持在一次输出中调用多个函数，因此没有使用这个功能。

mdcb/conv.json中包含一些few-shot对话，以增强大语言模型的能力。将它与用户聊天历史记录（在chat_log/<用户名>.json中）合并，作为大语言模型的聊天历史记录提供。

将用户的输入当作prompt，用户在discord的昵称当作User name，从设置中读取temperature和模型名称，简单设置一些logit_bias，使得模型的输出更活泼，更有人味。使用以上所有信息，调用大语言模型api生成回复。

为了节约成本，默认的max_tokens设置为200，如上一轮的回复长度超过200，则将之前的聊天记录与当前回复合并，作为新的prompt，并重新调用大语言模型api生成回复。当输出的总长度超过1000时，停止递归。

此外，Tennisbot支持poker-face模式，即不使用任何提示词，few-shot，和用户历史记录，仅使用用户输入作为prompt，调用大语言模型api生成回复，以进一步节约成本。在与Tennisbot的对话之前加一个"="，即可开启poker-face模式。

<br>

### info_process

从mdcb.py中获取回复后，info_process会从mdcb的返回中提取功能函数调用语句，并将剩下的返回内容，作为回复发送。

info_process.py中import了所有的Tennisbot功能函数，包括所有的在func_chat_log，func_email，func_file中定义的聊天记录，邮件，文件相关的功能，以及在functions.py中定义的设置和其他功能。info_process.py中还定义了一些系统运行功能函数，包括重启，关闭，访问控制台，及（在当前环境的镜像上）执行python代码。

在info_process中，使用 `result = globals()[r_list[0]](r_list[1:]) ` 来仅通过函数名调用功能函数。所有的这些功能函数均配有统一的传参方法，即 `func_name(param: list) -> str`，以方便调用。

此外，info_process函数本身也支持被mdcb调用，用于处理需要Tennisbot多轮思考的情况，即README中提到的"自动并行"。常见的例子是，当用户输入"爬取网站并总结"时，Tennisbot在第一轮info_process中先输出"调用爬取函数及调用info_process函数"。在第二轮info_process中，Tennisbot读取爬取函数的输出，再总结爬取结果。此功能超级强大且实用。

<br>

### schedules

schedules.py中定义了所有不依赖用户输入的计划任务，包括闹钟，以及检查邮件。其本身为一个循环thread，在main.py中启动，在schedule.ini中储存计划任务。

使用request.post()来发送同步请求。因为在on_message事件循环中，所有的事件都是异步的，但schedule的输出需要是同步的。

<br>

### 其他

Tennisbot支持为不同的用户/群设置不同的聊天参数，储存在files/bot_config.ini中。