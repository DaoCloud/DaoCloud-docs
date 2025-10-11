---
hide:
  - toc
---

# Model Deployment Management

Platform administrators can manage model deployments in **Operations Management**, including creating, editing, deleting, starting, and stopping model deployment configuration files.

!!! note

    Here, you are creating **model deployment configuration files**, not the model files themselves.
    To manage or download model files, please refer to [Managing Model Files with Dataset](../dataset.md).

## Model Deployment List

This list displays all created model deployment configurations, including the model name and the number of available configurations for each.

![Model Deployment Management List](images/list.png)

## Create

On the main page of model deployment management, click the **Create** button at the top right to enter the model deployment configuration creation page.

On the creation page, users need to:

1. **Select Model**: The model list is consistent with the list in "Model Gallery." To add new models, please go to "Model Gallery."
2. **Configure Resources and Runtime Information**: Including resource quotas (CPU cores, memory size, GPU type, GPU count, single GPU memory, etc.) and runtime parameters (such as max model length, runtime framework, framework version, etc.).
3. **Support Multiple Configurations**: Users can add multiple different deployment configurations for the same model.

After completing the configuration, click **Confirm** to finish creation.

![Model Deployment Management Model Selection](images/select.png)

![Model Deployment Management Creation](images/create.png)

## View Details

Users can click a model in the list to view detailed information of created configurations, including resource allocation and runtime parameters.

![Model Deployment Management Details](images/xiangqing.png)
