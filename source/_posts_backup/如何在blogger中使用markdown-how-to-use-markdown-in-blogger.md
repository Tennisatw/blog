---
title: 如何在Blogger中使用Markdown - How to use Markdown in Blogger
tags:
  - 推荐
  - http://schemas.google.com/blogger/2008/kind#post
  - 技术
excerpt: ''
date: 2023-09-08 23:58:00
---

<!-- more -->
有时博客会包含许多代码，使用Markdown会很方便。经多方查找，发现了一个项目，在不影响其他段落的同时，插入markdown段落。

Sometimes blogs will contain lots of code, using Markdown will be very convenient. Upon researching, I discovered a project that can insert Markdown paragraphs without affecting other paragraphs.

[https://github.com/cs905s/md-in-blogger](https://github.com/cs905s/md-in-blogger)

  

由于原文是英语，且其对使用方法的描述不甚明朗，我在此复述一下它的用法。

As its instructions aren't very clear, I will reiterate here on how to use it.

  

打开blogger的编辑网页，选择“布局”，即可进入编辑布局模式。添加一个小工具，选择HTML/JavaScript，在其内容一栏输入以下代码，然后点击保存。

Open the edit page of Blogger and select "layout" to enter edit layout mode. Add a widget, choose HTML/JavaScript, and enter the code below in its content column, then click save.

\`\`\`html
<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.9.0/styles/default.min.css"/>
<script src='//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.9.0/highlight.min.js' type='text/javascript'></script>
<script src='//cdnjs.cloudflare.com/ajax/libs/showdown/1.6.2/showdown.min.js' type='text/javascript'></script>
<script src='//cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js' type='text/javascript'></script>
<script src='//mxp22.surge.sh/markdown-highlight-in-blogger.js' type='text/javascript'></script>
\`\`\`

  

当需要使用markdown时，在博文编辑界面的左上角，将撰写视图切换为HTML视图，然后在需要的位置插入以下代码。其中省略号中可添加所需的markdown内容。

When you need to use Markdown, in the blog post editing interface's top left, switch the write view to HTML view, then insert the following code where necessary. The ellipses can be replaced with the desired Markdown content.

\`\`\`html
<pre class="markdown">  
...  
</pre>
\`\`\`

  

以下为其使用效果：

Here's what it looks like in use:

  

#### 插入代码块：Insert code block:

\`\`\`python
def test():
	pass

\`\`\`

  

#### 插入表格：Insert table:

| A | B | C |
|---|---|---|
| 4 | 9 | 2 |
| 3 | 5 | 7 |
| 8 | 1 | 6 |

  

#### 插入列表：Insert list:

1\. \[x\] 1
2. \[x\] 1
3. \[x\] 4
4. \[x\] 5
5. \[x\] 1
6. \[x\] 4

  

#### 使用注释隐藏文字：Use comments to hide text:

<!--invisible-text-0-->

  

好的，这就是它的用法了，恭喜你又掌握了一个拯救世界的利器。

Enjoy.