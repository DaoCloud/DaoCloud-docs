# Using Hydra in Cherry Studio

*[Hydra]: The development codename for LLM Studio

[🍒 Cherry Studio](https://cherry-ai.com/) is an LLM desktop client that supports integration with multiple LLM providers, including OpenAI, GPT-3, Hydra, and more.

![Cherry Studio](../images/cherry-studio.jpg)

## Install Cherry Studio

You can download the installer from the [Cherry Studio official website](https://cherry-ai.com/).

It supports MacOS, Windows, and Linux clients.

## Configure Cherry Studio

Open the configuration page in Cherry Studio, add a model provider, for example named `d.run`, with the provider type set to `OpenAI`.

![Cherry Studio](../images/cherry-studio-2.png)

Add your API Key and API Host obtained from d.run.

- **API Key:** Enter your API Key
- **API Host:**
    - For MaaS, use `https://chat.d.run`
    - For independently deployed model services, check the model instance details, usually `https://<region>.d.run`

### Manage Available Models

Cherry Studio will automatically detect the model list, and you can enable the models you need in the list.

![Cherry Studio](../images/cherry-studio-4.png)

## Cherry Studio Usage Demo

![Cherry Studio](../images/cherry-studio-5.png)
