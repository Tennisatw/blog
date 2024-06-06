---
title: 如何制作词云 - How to make wordcloud
tags:
  - http://schemas.google.com/blogger/2008/kind#post
  - 编程
excerpt: ''
date: 2023-09-17 03:56:00
---

<!-- more -->
下图是一张词云的照片。

The image below is a photo of a wordcloud.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgd8JcUU8VtvQ730UoAe9orILSHY4gJg82RaG9oa57r6JL1-nLkNq33cKbsMccWw_Fj20DT74Nb4N-nzkMkTG491Vt4X487-xB7VRgrK3iIOSf7AOBbML4zqG0L4DUB_4FHt7EgSgI-7fe4KE7pKe3YYdQxeBPetDvMOsKOenX1LIIkUWR5V6H-ksi9RrY/s320/wordcloud.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgd8JcUU8VtvQ730UoAe9orILSHY4gJg82RaG9oa57r6JL1-nLkNq33cKbsMccWw_Fj20DT74Nb4N-nzkMkTG491Vt4X487-xB7VRgrK3iIOSf7AOBbML4zqG0L4DUB_4FHt7EgSgI-7fe4KE7pKe3YYdQxeBPetDvMOsKOenX1LIIkUWR5V6H-ksi9RrY/s800/wordcloud.png)

  

  

首先，安装wordcloud包。对于汉语用户，需额外安装jieba包。

Firstly, install the wordcloud package. For Chinese users, install an additional package, jieba.

  

\`\`\`bash
pip install jieba
pip install wordcloud
\`\`\`

  

上图词云的文本来源是本篇博客，通过爬虫爬取内容，再用BeautifulSoup包解码。读者也可以从文本中读取，或者直接向程序中粘贴文本来源。

The text for the word cloud above was obtained from this blog post, extracted through web scraping, and then decoded with the BeautifulSoup package. Readers could also read from a text file or directly paste the text into the program. 

\`\`\`python
url = 'https://blog.tennisatw.com/2023/09/how-to-make-wordcloud.html'
r = requests.get(url=url).text
soup = BeautifulSoup(r, 'lxml')
paragraphs = soup.find\_all('p')

blog\_text = ''
for text in paragraphs:
    blog\_text += text.text
\`\`\`

\`\`\`python
blog\_text = '文本 text'
\`\`\`

  

如果是汉语用户，由于汉语词汇中间没有空格，需使用jieba分词，执行以下代码：

For Chinese users, as Chinese vocabulary does not contain spaces in between words, the jieba package is needed for word segmentation. Run the following code.

\`\`\`python
ls = jieba.lcut(blog\_text)
text = ' '.join(ls)
\`\`\`

  

以下为全部代码：

Below is the complete code:

\`\`\`python
import requests
from bs4 import BeautifulSoup
import jieba
import wordcloud

url = 'https://blog.tennisatw.com/2023/09/how-to-make-wordcloud.html'
r = requests.get(url=url).text
soup = BeautifulSoup(r, 'lxml')
paragraphs = soup.find\_all('p')

blog\_text = ''
for text in paragraphs:
    blog\_text += text.text

ls = jieba.lcut(blog\_text)
text = ' '.join(ls)

stopwords = wordcloud.STOPWORDS | {"的", "是", "了", "我"}

wc = wordcloud.WordCloud(font\_path="msyh.ttc",
                         width=800,
                         height=600,
                         background\_color='white',
                         max\_words=80,
                         max\_font\_size=150,
                         stopwords=stopwords)

wc.generate(text)
wc.to\_file("wordcloud.png")

\`\`\`