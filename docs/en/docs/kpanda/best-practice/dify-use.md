# Quickly Build Dify LLM Application Development Platform

[Dify](https://dify.ai) is an open-source large language model (LLM) application development platform that provides one-stop capabilities including Agent workflow, RAG Pipeline, rich integrations, and observability, enabling users to quickly build production-grade generative AI applications.

This article mainly introduces how to use __Helm Application__ in DCE to deploy __dify-chart__ plugin, quickly build Dify LLM application development platform, and implement usage examples of Dify application/workflow based on Qwen-turbo.

## Prerequisites

Before installing __dify-chart__ plugin, the following prerequisites must be met:

- Container Management module has [integrated with Kubernetes cluster](../clusters/integrate-cluster.md) or [created a Kubernetes cluster](../clusters/create-cluster.md), and can access the cluster's UI.

- The current operating user should have [NS Editor](../permissions/permission-brief.md#ns-editor) or higher permissions. For details, refer to [Namespace Authorization](../namespaces/createns.md).

## Installation Process

Follow these steps to install __dify-chart__ plugin for the cluster and build the Dify LLM application development platform.

1. Find the target cluster where you want to install __dify-chart__ plugin in the cluster list. Click the cluster name, then click __Helm Applications__ -> __Helm Templates__ in the left navigation bar. Enter __dify-chart__ in the search bar.

    ![Cluster Details](../images/dify-install01.png)

2. Read the __dify-chart__ plugin introduction, select the version and click __Install__. This article uses __0.0.2__ version as an example.

    ![Click Install](../images/dify-install02.png)

3. Fill in and configure parameters, then click __Next__.

    === "Basic Parameters"

        ![Fill Parameters](../images/dify-install03.png)

        - Name: Required parameter, enter the plugin name. Note that the name can be at most 63 characters, can only contain lowercase letters, numbers and separators ("-"), and must start and end with lowercase letters or numbers, e.g., dify-chart.
        - Namespace: The namespace where the plugin is installed. You can choose an existing namespace or create a new one. For example, create __dify__ namespace.
        - Version: Plugin version, e.g., __0.0.2__.
        - Delete on Failure: Optional parameter. When enabled, it will default to enable installation waiting. If installation fails, it will delete installation-related resources.
        - Wait for Ready: Optional parameter. When enabled, it will wait for all associated resources under the application to be in ready state before marking the application installation as successful.
        - Detailed Logs: Optional parameter. When enabled, it will output detailed logs of the installation process.

        !!! note

            After enabling __Wait for Ready__ and/or __Delete on Failure__, the application will take a relatively long time to be marked as __Running__ .

    === "Parameter Configuration"

        ![Configure Service Parameters](../images/dify-install04.png)

        - __service__ :
            - __type__ : The access method of the Dify application. Keep the default __Nodeport__ node access.
            - __nodePort__ : The access port, defaulting to __30000__ .
            - __nodeIP__ : The externally accessible node IP, defaulting to __127.0.0.1__ , which needs to be replaced with the node IP of the current cluster.


4. After confirming that the YAML is correct, click __OK__ to complete the installation of the __dify-chart__ plugin. The system will then automatically redirect to the __Helm Applications__ list page. After a few minutes, refresh the page and you will see the application that was just installed.
    ![View Status](../images/dify-install06.png)

## Quick Access

1. You can access it directly through the configured __nodeIP__ : __nodePort__ , or click __Services__ -> __dify-nginx-nodeport__ -> __External Access__ in the UI to access the built Dify platform.

    ![Service Access](../images/dify-use16.jpeg)

2. Enter the administrator initialization password to verify and enter the initialization page. The default administrator initialization password is __password__ .

    ![Access Page](../images/dify-use01.png)


3. Set the administrator account of the Dify application, which is used to create applications and manage LLM providers. Click __Settings__ to complete the initialization.

    ![Administrator Account](../images/dify-use02.png)

4. Log in with the administrator account set in the previous step to enter the Dify platform home page.

    ![Application Home Page](../images/dify-use15.png)

## Usage Example

This article takes the quick building of a __Chinese-English Translation__ application/workflow as an example to do a simple practice on the Dify platform built in the DCE target cluster.

### Model Integration

1. On the Dify platform home page, click __Username__ in the upper right corner to enter the __Settings__ page.

    ![Settings](../images/dify-use03.png)

2. Click __Settings__ -> __Model Providers__ to enter the model list and select the required model.

    ![Model Providers](../images/dify-use04.png)

3. Configure the basic parameters of the model and click __Confirm__ to add the LLM service. This article takes __Tongyi Qianwen__ as an example.

    ![Configure Parameters](../images/dify-use05.png)

    - Model Type: Dify classifies models into the following 4 categories according to usage scenarios: LLM Model, TTS Model, Text Embedding Model and Rerank Model.
    - Model Name: The specific name of the required model, e.g., qwen-turbo.
    - API Key: The core credential for calling the model service, used to verify user identity and protect data security.
    - Model Context Length: The maximum number of tokens (including input and output) that the model can retain when processing text at a time. Exceeding the context length will cause historical conversations to be discarded. Default: 4096.
    - Maximum Token Limit: The maximum number of tokens the model outputs at a time. Default: 4096.
    - Function Calling: Allows the model to call external tools or APIs when generating text. Default: __Not Supported__ .

### Build an Application

Steps to create a __Text Generation__ application:

1.  On the Dify platform home page, click __Create Application__ -> __Create Blank Application__ , select the application type, and fill in the __Application Name & Icon__ and __Description__ to create the application.

    ![Create Application](../images/dify-use06.png)

2.  After the application is created, you will be automatically redirected to the application overview page. Click __Orchestrate__ in the left menu to orchestrate the application. The __Debug and Preview__ area on the right side of the interface allows you to debug and preview the application.

    ![Orchestrate Application](../images/dify-use07.png)

    - Prefix Prompt: Prompts are used to constrain AI to give professional replies, making the responses more precise. Users can use the built-in prompt generator to write suitable prompts.
    - Variables: Variables will be presented in the form of a form for users to fill in before the conversation. The values of the variables in the prompt will be replaced with the values filled in by the user. The maximum length can be set, for example, {{query}}.
    - Context: Context can be understood as the background information provided to the LLM, and is often used to fill in the output variables of knowledge retrieval.

3.  Click __Publish__ in the upper right corner to complete the quick building of a simple application.

    ![Publish Application](../images/dify-use08.png)

4.  Click __Publish__ -> __Run__ in sequence to access the home page of the created application for use.

    ![Use Application](../images/dify-use09.png)

### Workflow Configuration

Dify workflows are divided into two types:

-  __Chatflow__: Oriented to conversational scenarios, including customer service, semantic search, and other conversational applications that require multi-step logic when building responses.
-  __Workflow__: Oriented to automation and batch processing scenarios, suitable for applications such as high-quality translation, data analysis, content generation, and email automation.

Steps to create a __Workflow__ workflow:

1.  On the __Create Application__ -> __Create Blank Application__ page, select Workflow, and fill in the __Application Name & Icon__ and __Description__ to create the workflow.

    ![Create Workflow](../images/dify-use10.png)

2.  After creation, you will be automatically redirected to the orchestration page. Add nodes by right-clicking or clicking the __+ sign__ at the end of the previous node to orchestrate the workflow.

    ![Orchestrate Workflow](../images/dify-use11.png)

3.  Add an __LLM__ node, call the LLM, then fill in and configure the parameters.

    ![Call the LLM](../images/dify-use12.png)

    - Model: Call the LLM to answer questions, e.g., qwen-turbo.
    - Context: Context can be understood as the background information provided to the LLM, and is often used to fill in the output variables of knowledge retrieval.
    - Prompt: An easy-to-use prompt orchestration page. If you select a Chat model, you can customize the SYSTEM / USER / ASSISTANT parts.
    - Vision: Enabling the vision feature will allow the model to receive images as input and answer user questions based on the understanding of the image content.
    - Output Variables: The content generated by the LLM.
    - Error Retry: After enabling the error retry feature, the node will automatically retry according to a preset policy when an error occurs. You can adjust the maximum number of retries and the interval between retries to set the retry policy.
    - Exception Handling: Provides diversified node error handling policies, which can throw fault information when an error occurs at the current node without interrupting the main process; or continue to complete the task through an alternative path.

4.  Add the __End__ node to complete the workflow orchestration. Click __Run__ in the upper right corner to debug and preview the workflow.

    ![Debug Workflow](../images/dify-use13.png)

5.  Click __Publish__ in the upper right corner to complete the quick building of a simple workflow.

    ![Call the LLM](../images/dify-use14.png)

For more features of the Dify application development platform, refer to [Dify Official Documentation](https://dify.ai).
