---
title: 如何制作词云 - How to make wordcloud
permalink: post/26/
excerpt: 暂无预览 - No preview available
date: 2023-09-17 03:56:21
tags: 编程 - Programming
---

下图是本文词云的照片。

The image below is a photo of a wordcloud.

![](1.png)

<p><br></p>

首先，安装wordcloud包。对于汉语用户，需额外安装jieba包。

Firstly, install the wordcloud package. For Chinese users, install an additional package, jieba.

```bash
pip install jieba
pip install wordcloud
```

<p><br></p>

上图词云的文本来源是本篇博客，通过爬虫爬取内容，再用BeautifulSoup包解码。读者也可以从文本中读取，或者直接向程序中粘贴文本来源。

The text for the word cloud above was obtained from this blog post, extracted through web scraping, and then decoded with the BeautifulSoup package. Readers could also read from a text file or directly paste the text into the program. 

```python
url = 'https://blog.tennisatw.com/post/26/'
r = requests.get(url=url).text
soup = BeautifulSoup(r, 'lxml')
paragraphs = soup.find_all('p')

blog_text = ''
for text in paragraphs:
    blog_text += text.text
```
```python
blog_text = '文本 text'
```
<p><br></p>

如果是汉语用户，由于汉语词汇中间没有空格，需使用jieba分词，执行以下代码：

For Chinese users, as Chinese vocabulary does not contain spaces in between words, the jieba package is needed for word segmentation. Run the following code.

```python
ls = jieba.lcut(blog_text)
text = ' '.join(ls)
```
<p><br></p>

以下为全部代码：

Below is the complete code:

```python
import requests
from bs4 import BeautifulSoup
import jieba
import wordcloud

url = 'https://blog.tennisatw.com/post/26/'
r = requests.get(url=url).text
soup = BeautifulSoup(r, 'lxml')
paragraphs = soup.find_all('p')

blog_text = ''
for text in paragraphs:
    blog_text += text.text

ls = jieba.lcut(blog_text)
text = ' '.join(ls)

stopwords = wordcloud.STOPWORDS | {"的", "是", "了", "我"}

wc = wordcloud.WordCloud(font_path="msyh.ttc",
                         width=800,
                         height=600,
                         background_color='white',
                         max_words=80,
                         max_font_size=150,
                         stopwords=stopwords)

wc.generate(text)
wc.to_file("wordcloud.png")

```