# Using Hydra in VSCode and Cline

*[Hydra]: The development codename for LLM Studio

[Cline](https://cline.bot/) is a VSCode extension that helps you use Hydra’s model services directly in VSCode.

## Install Cline

Search for the Cline extension in VSCode and install it.

![Cline](../images/cline-in-vscode.png)

You can also download and use the RooCode extension, which is a fork of Cline.

> Cline’s predecessor was Claude Dev; RooCode (RooCline) is a fork based on Cline.

If your network cannot download the extension directly, consider downloading the `.vsix` file from the VSCode Marketplace and install it via `Install from VSIX` in VSCode.

- [Cline](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev)  
- [RooCode](https://marketplace.visualstudio.com/items?itemName=RooVeterinaryInc.roo-cline): a fork of Cline

## Configure Cline

Open Cline’s configuration page:

![Cline](../images/cline-in-vscode-2.png)

- **API Provider:** Select OpenAI Compatible
- **Base URL:** Enter `https://chat.d.run`
- **API Key:** Enter your API Key
- **Model ID:** Enter your Model ID
    - Can be obtained from Hydra’s Model Gallery, MaaS models start with `public/deepseek-r1`
    - For independently deployed model services, get it from the model service list

![Cline](../images/cline-in-vscode-3.png)

## Cline Usage Demo

![Cline](../images/cline-in-vscode-4.png)
