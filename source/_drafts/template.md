---
title: {{ title }}
date: {{ date }}
permalink: post/auto_increment_id/
excerpt: '暂无预览 - No preview available'
tags: 
---

分段
<br>

分隔符
---

插入图片：

![](1.png)
这张图片不能显示在摘要中。

{% asset_img 1.png graph2 %}
这张图片可以显示在摘要中。

![](1.png){ width=200px }

<br>

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
<a href="/post/0/xx.txt" download>Addendum xx</a>

<br>

敏感：
<p class="tennisbot" id="如果需要的话，左上角有google翻译<br>There is Google Translate button in the upper left corner, if needed">由于本文可能稍有敏感，这里仅展示英文版。</p>