---
title: SD WebUI 2： 如何设置Stable Diffusion WebUI？ - SD WebUI 2： How to set Stable Diffusion WebUI?
permalink: post/8/
excerpt: <br>
date: 2023-05-04 21:16:02
tags: 
 - 技术 - Technology
 - 编程 - Programming
categories: 
 - SD WebUI
---

书接上文，在安装了SD WebUI之后，就可以直接使用了。但是，为了更好的使用SD WebUI，需要调整一些它的初始参数。以下是一些我试出来，还算合理的初始参数。

Continuing from where we left off, after installing SD WebUI, it can be used directly. However, to optimize the use of SD WebUI, some initial parameters need to be adjusted. Here are some reasonable initial parameters that I have tried and tested.

<br>

找到ui-config.json文件，修改以下参数。

Find the ui-config.json file and modify the following parameters.

```
"txt2img/Sampling method/value": "DPM++ 2M Karras",
"txt2img/Sampling steps/value": 30,
"txt2img/Hires. fix/value": true,
"txt2img/Denoising strength/value": 0.5,
"img2img/Sampling method/value": "DPM++ 2M Karras",
"img2img/Sampling steps/value": 80,
```

<br>

同样，找到config.json文件，修改以下参数。

Same, find the config.json file and modify the following parameters.

```
"save_txt": true
"quicksettings": "sd_model_checkpoint, sd_vae,",
```

<br>

除此之外，还可以安装一些插件来增强SD WebUI的性能。介绍几个我自己正在用的插件。安装这些插件的方法很简单，复制插件的网址，打开SD WebUI的Extention栏，选择Install from URL，粘贴到URL for extension's git repository里就好了。

In addition to the adjustments mentioned above, you can also install some plugins to enhance the performance of SD WebUI. I'll introduce a few plugins that I'm currently using myself. Installing these plugins is quite simple: copy the plugin's web address, open the "Extension" tab in SD WebUI, choose "Install from URL," and paste the URL into the "URL for extension's git repository" field.

<br>

Controlnet：超级全能的控制姿势的插件

Controlnet: A versatile plugin for controlling poses

[https://github.com/Mikubill/sd-webui-controlnet](https://github.com/Mikubill/sd-webui-controlnet)

<br>

Latent Couple：控制构图的插件

Latent Couple: A plugin for controlling composition

[https://github.com/opparco/stable-diffusion-webui-two-shot](https://github.com/opparco/stable-diffusion-webui-two-shot)

<br>

Lycoris：使用Lycoris必备的插件

Lycoris: A must-have plugin for using Lycoris

[https://github.com/KohakuBlueleaf/a1111-sd-webui-locon](https://github.com/KohakuBlueleaf/a1111-sd-webui-locon)

<br>

Cutoff：防止颜色污染的插件，有些作用

Cutoff: A plugin to prevent color contamination, somewhat useful

[https://github.com/hnmr293/sd-webui-cutoff](https://github.com/hnmr293/sd-webui-cutoff)

<br>

这其中，要使用controlnet，还需下载匹配的模型。网址如下。

To use Controlnet, you also need to download the corresponding model. The link is as follows.

[https://huggingface.co/webui/ControlNet-modules-safetensors/tree/main](https://huggingface.co/webui/ControlNet-modules-safetensors/tree/main)

<br>

下载好模型后，将其移动到stable-diffusion-webui/extensions/sd-webui-controlnet/models里。

After downloading the model, move it to the stable-diffusion-webui/extensions/sd-webui-controlnet/models .