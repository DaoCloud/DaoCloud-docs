# Quickly Build Dify LLM Application Development Platform

[Dify](https://dify.ai) is an open-source large language model (LLM) application development platform that provides one-stop capabilities including Agent workflow, RAG Pipeline, rich integrations, and observability, enabling users to quickly build production-grade generative AI applications.

This article mainly introduces how to use __Helm Application__ in DCE 5.0 to deploy __dify-chart__ plugin, quickly build Dify LLM application development platform, and implement usage examples of Dify application/workflow based on Qwen-turbo.

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
