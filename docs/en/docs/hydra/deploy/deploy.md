---
hide:
  - toc
---

# Deploying a New Model

*[Hydra]: Internal codename for LLM Studio

You can deploy a model either from the [Model Gallery](../index.md) or the [Model Deployment](./index.md) page. Below are the configuration parameters explained:

![deploy](../images/deploy01.png)

- **Select Model**: Choose the model you want to deploy (e.g., DeepSeek-R1). Use the dropdown menu to quickly find a model that matches your business needs and task scenarios.

    ![deploy](../images/deploy02.png)

- **Model Service Name**: Must meet the following requirements:

    - **Length**: Between 2 and 64 characters
    - **Allowed characters**: Lowercase letters, numbers, and hyphens (`-`)
    - **Naming rule**: Must start and end with a lowercase letter or number
    - **Examples**: `text-gen-service`, `model-01`

- **Region**:

    - Select the deployment region for your service (e.g., “Shanghai Zone 7”)
    - Choose the region based on your business coverage and latency requirements

- **Instance Count**:

    - Configure the number of instances to deploy (default: 1)
    - **Note**: More instances improve concurrency but also increase cost
