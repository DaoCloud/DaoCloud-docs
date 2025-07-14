# Using Hydra in Bob Translate

*[Hydra]: The development codename for LLM Studio

This document explains how to call model services from Hydra in Bob Translate.

[Bob](https://bobtranslate.com/) is a macOS translation and OCR software that lets you translate and perform OCR in any application—quick, simple, and efficient!

![Bob Translate](../images/bobtranslate.png)

## Install Bob Translate

You can download and install Bob Translate from the [Mac App Store](https://apps.apple.com/cn/app/bob-%E7%BF%BB%E8%AF%91%E5%92%8C-ocr-%E5%B7%A5%E5%85%B7/id1630034110).

## Configure Bob Translate

Open the configuration page of Bob Translate, add a translation service, and select the service type as `OpenAI`.

![Bob Translate](../images/bobtranslate-2.png)

Add your API Key and API Host obtained from Hydra.

- **API Key:** Enter your API Key
- **API Host:**
    - For MaaS, use `https://chat.d.run`
    - For independently deployed model services, check the model instance details, usually `https://<region>.d.run`
- Configure custom model, e.g., `public/deepseek-r1`

![Bob Translate](../images/bobtranslate-3.png)

## Bob Translate Usage Demo

![Bob Translate](../images/bobtranslate-4.png)
