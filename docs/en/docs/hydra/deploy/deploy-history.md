---
hide:
  - toc
---

# Deploying a New Model (Legacy Version)

*[Hydra]: Internal codename for LLM Studio

This page preserves the deployment operations and form parameter descriptions from the console before v0.13.1,
for users who still need to compare against the legacy interface after upgrading.

You can deploy a model directly from the [Model Gallery](../index.md), or go to the **Model Serving** page from
the left navigation bar to deploy a model. The form parameters for model deployment are as follows:

![deploy](../images/deploy03.png)

| Parameter | Constraints / Description | Remarks |
|---|---|---|
| Select Model | Choose the model to deploy (e.g., DeepSeek-R1). Use the dropdown menu to quickly select a model that matches your business needs and task scenarios | Affects model capabilities, inference quality, and resource consumption |
| Model Service Name | Specify a name for the model service deployed this time<br>**Length**: 2–64 characters<br>**Characters**: Only lowercase letters, numbers, and hyphens (-) are allowed<br>**Rule**: Must start and end with a lowercase letter or number | Examples: `text-gen-service`, `model-01` |
| Instance Count | Configure the number of instances to deploy<br>Note: More instances provide stronger concurrency but also higher cost | **Default**: 1 |
| Deployment Cluster | Select the cluster to deploy the model service to | It is recommended to prefer a cluster that is physically closer to reduce latency |
| Namespace | Specify the target namespace for the model service deployment | |
| Model File Check | After you select the model, cluster, and namespace, the system automatically performs the model file check. | |

After a model is successfully deployed, users can **[try and test the model](../exp.md)** through chat conversations.
Meanwhile, on the Model Gallery, hovering the cursor over the card of that model displays a **Try** button for
quick access.
