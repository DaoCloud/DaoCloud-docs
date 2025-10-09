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

- **Model Service Name:** Must meet the following requirements:

    - Length: 2 - 64 characters
    - Characters: Only lowercase letters, numbers, and hyphens (-) are allowed; must start and end with a lowercase letter or number
    - Example: text-gen-service or model-01

- **Number of Instances**

    - Configure the number of instances to deploy. Default: 1
    - Notes: More instances increase the service's concurrency capability, but also increase cost

- **Deployment Cluster:** Select the cluster for deployment. It is recommended to choose the closest cluster.  
- **Namespace:** Specify the target namespace for deployment.  
- **Model File Check:** After selecting the model, cluster, and namespace, the system will automatically perform the model file check.  
