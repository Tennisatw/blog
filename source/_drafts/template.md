---
title: {{ title }}
date: {{ date }}
permalink: post/auto_increment_id/
excerpt: ''
tags: 
 - 1
 - 2
categories:
---

在文件名前加上`_`可以使其不被编译。

分段
<br>

分隔符
---

插入图片：

![](1.png)
这张图片不能显示在摘要中。

{% asset_img 1.png graph2 %}
这张图片可以显示在摘要中。

<img src="/post/70/xx.png" alt="graph3" />

可以调整图片大小：

![](1.png){ width=200px }
![](1.png){ height=40% }

并排显示图片
<img src="/post/70/xy.png" style="width:400px; display:inline-block; margin-right: 1px;" />
<img src="/post/70/xz.png" style="width:400px; display:inline-block;" />

<br>

<div style="text-align: center; font-size: smaller;">
居中与缩小字号的图例
</div>

Tennisbot发表评论：

<p class="tennisbot" id="Tennisbot会说出这句话">显示内容</p>
这句话会有阴影。

或者
<p class="Tennisbot会说出这句话" id="tennisbot_0">显示内容</p>

<br>

插入代码：

```python
print("Hello, World!")
```

插入可下载文件：
<a href="/post/5/xx.txt" download>Addendum xx</a>

<br>

敏感：
<p class="tennisbot" id="如果需要的话，左上角有google翻译<br>There is Google Translate button in the upper left corner, if needed">由于本文可能稍有敏感，这里仅展示英文版。</p>