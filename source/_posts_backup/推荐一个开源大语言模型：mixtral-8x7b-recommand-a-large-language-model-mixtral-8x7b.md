---
title: '推荐一个开源大语言模型：Mixtral-8x7b - Recommand a Large Language Model: Mixtral-8x7b'
tags:
  - 推荐
  - http://schemas.google.com/blogger/2008/kind#post
  - 技术
excerpt: ''
date: 2024-01-08 15:06:00
---

<!-- more -->
大语言模型(LLM)是用来生成文本的AI模型。举一个例子：ChatGPT就是一个闭源的大语言模型。

Large Language Models (LLMs) are AI models designed for text generation. For example, ChatGPT is a closed-source large language model.

  

相比于闭源的模型，开源的模型免费，并且没有审核限制，可以随意使用。但一般的开源大语言模型的水平往往很差。

Mixtral-8x7b是一个由Mistral AI公司发布的开源的大语言模型，截至目前，它的“水平”是开源模型中最高的，在大多数测试中其性能与gpt3.5类似。

In contrast to closed-source models, open-source models are free and lack moderation restrictions, allowing unrestricted use. However, the quality of most open-source LLMs is generally subpar.

Mixtral-8x7b is an open-source large language model released by Mistral AI. As of now, it is the highest-performing open-source model, with capabilities similar to GPT-3.5 in most tests.

  

Mixtral-8x7b可以在这里使用。点击链接，在右下角选择模型处选择Mixtral-8x7b-instruct，就可以开始与它对话了。

Mixtral-8x7b can be accessed here. By clicking the link, selecting 'Mixtral-8x7b-instruct' at the bottom right, you can start conversing with it.

[https://labs.perplexity.ai/](https://labs.perplexity.ai/)

  

此外，也可以在Google Colab部署Mixtral-8x7b。

Additionally, Mixtral-8x7b can be deployed on Google Colab.

[https://github.com/dvmazur/mixtral-offloading/blob/master/notebooks/demo.ipynb](https://github.com/dvmazur/mixtral-offloading/blob/master/notebooks/demo.ipynb)

  

这是一个使用了Moe的offloading方法来优化Mixtral-8x7b的notebook。下载此notebook文件 (demo.ipynb)，然后上传至google colab上，依次运行每个代码块，等待模型加载完成（即最后一个代码块的输出处出现输入框），在输入框输入，就可以与Mixtral-8x7b对话了。

This is a notebook utilizing the Mixture of Experts (MoE) offloading method to optimize Mixtral-8x7b. Download the notebook file (demo.ipynb), upload it to Google Colab, run each code block sequentially, and wait for the model to load (indicated by an input box appearing at the output of the last code block). Input your text, and then, you can converse with Mixtral-8x7b.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjBz4EgR9iu3QAPspqsruCQaxRyX9-mQqCCdP0VbPXLBBVKsqRoW2bpkVH-bmenUIpgdh3Kp9TrW2be5Hijfioq-iIejsapyYojwWL2n1zJRkKUjg-vOCmJk4HNRsGQ3BKLKI_T-uJI2G7PvNgG36i3X9OpjiLb15w5QZeuduEwk2talnqv4sh3fd4H4C4)](https://blogger.googleusercontent.com/img/a/AVvXsEjBz4EgR9iu3QAPspqsruCQaxRyX9-mQqCCdP0VbPXLBBVKsqRoW2bpkVH-bmenUIpgdh3Kp9TrW2be5Hijfioq-iIejsapyYojwWL2n1zJRkKUjg-vOCmJk4HNRsGQ3BKLKI_T-uJI2G7PvNgG36i3X9OpjiLb15w5QZeuduEwk2talnqv4sh3fd4H4C4)

  

虽说Mixtral-8x7b的水平不输gpt3.5，但是离gpt4还有一定差距。可以向gpt问这个问题：“鲁迅为什么打周树人”，gpt4会指出鲁迅和周树人是同一个人，而gpt3.5就会胡言乱语。

用同样的问题测试Mixtral-8x7b，它虽然并不胡言乱语，但它也深陷在自己的“幻觉”中，说明Mixtral-8x7b水平与gpt4仍有差距。

Although Mixtral-8x7b matches GPT-3.5 in performance, it still falls short of GPT-4. For instance, when asked, "Why did Lu Xun hit Zhou Shuren?" GPT-4 correctly identifies Lu Xun and Zhou Shuren as the same person, while GPT-3.5 produces nonsensical responses. 

When tested with the same question, Mixtral-8x7b, though not nonsensical, still falls into its own 'illusions,' indicating a gap between it and GPT-4.

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjkPFj1bRoJOXT9_mGHo7po-hgfJsaQbJalHvgGX0o5mIDd6FF38V4JxXb6U9Wd6ZeEtE96zmutHCBbhnJxjLMuHyZyM1LgcuXiUGdTiTm0b9s7W-DuQ1qaFRWPgbKnxzsDG0ax5-A193m6dRm7yHn9MD6xVcjQclXqWwd0rAJaFy-8Cfo2cgF1PPKk3JE=w640-h364)](https://blogger.googleusercontent.com/img/a/AVvXsEjkPFj1bRoJOXT9_mGHo7po-hgfJsaQbJalHvgGX0o5mIDd6FF38V4JxXb6U9Wd6ZeEtE96zmutHCBbhnJxjLMuHyZyM1LgcuXiUGdTiTm0b9s7W-DuQ1qaFRWPgbKnxzsDG0ax5-A193m6dRm7yHn9MD6xVcjQclXqWwd0rAJaFy-8Cfo2cgF1PPKk3JE)