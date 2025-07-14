# Using Hydra in Lobe Chat

*[Hydra]: The development codename for LLM Studio

[Lobe Chat](https://lobehub.com/zh) is an open-source modern design AI chat framework.  
It supports multiple AI providers (OpenAI/Claude 3/Gemini/Ollama/Qwen/DeepSeek), knowledge bases (file upload/knowledge management/RAG), multimodal features (vision/TTS/plugins/artwork), and offers one-click free deployment of your private ChatGPT/Claude applications.

![Lobe Chat](../images/lobe-chat.png)

## Install Lobe Chat

You can refer to the [Lobe Chat official documentation](https://lobehub.com/zh/docs/self-hosting/start) to download and install it.  
Lobe Chat offers multiple deployment and installation methods.

This document uses Docker as an example to explain how to use Hydra’s model services.

```bash
# Lobe Chat supports configuring API Key and API Host directly at deployment
$ docker run -d -p 3210:3210 \
    -e OPENAI_API_KEY=sk-xxxx \  # Enter your API Key
    -e OPENAI_PROXY_URL=https://chat.d.run/v1 \  # Enter your API Host
    -e ENABLED_OLLAMA=0 \
    -e ACCESS_CODE=drun \
    --name lobe-chat \
    lobehub/lobe-chat:latest
```

## Configure Lobe Chat

Lobe Chat also supports adding model provider configurations after deployment.

![Lobe Chat](../images/lobe-chat-2.png)

Add your API Key and API Host obtained from Hydra.

* **API Key:** Enter your API Key
* **API Host:**

    * For MaaS, use `https://chat.d.run`
    * For independently deployed model services, check model instance details, usually `https://<region>.d.run`

* Configure custom model, e.g., `public/deepseek-r1`

## Lobe Chat Usage Demo

![Lobe Chat](../images/lobe-chat-3.png)
