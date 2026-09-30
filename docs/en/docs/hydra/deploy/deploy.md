---
hide:
  - toc
---

# Deploying a New Model

*[Hydra]: Internal codename for LLM Studio

Publish the selected model on a target cluster as a callable model service, filling in deployment parameters
such as resources, runtime, and instances as needed. You can initiate a deployment from the
[Model Gallery](../index.md), [Model Management](../model-management/index.md), or the left navigation
**Model Serving - Deploy New Model**. The following sections describe the steps and the meaning of each parameter.

![deploy](../images/deploy-new-02.png)

## Prerequisites

- The target cluster and namespace are available.
- To deploy a custom model, you have completed the model metadata, deployment template, or model weight file
  configuration in [Create Model](../model-management/index.md).

## Steps

1. Enter LLM Studio, and in the left navigation bar, click **Model Serving**.
2. On the model service list page, click **Deploy New Model** (or click the **Deploy** button on the
   Model Gallery or Model Management page).
3. Fill in the deployment parameters as needed and click **Confirm**.

    ## Parameter Descriptions

    | Parameter | Constraints / Description | Remarks |
    |---|---|---|
    | Model Source | Select the model source: Model Gallery or a custom model | A custom model must have been created in Model Management |
    | Model Selection | Select the model to deploy (e.g., DeepSeek-R1). You can quickly filter models through the dropdown menu | Affects model capabilities, inference quality, and resource consumption |
    | Model Service Name | Specify a name for the model service deployed this time<br>**Length**: 2–64 characters<br>**Characters**: Only lowercase letters, numbers, and hyphens (-) are allowed<br>**Rule**: Must start and end with a lowercase letter or number | Examples: `text-gen-service`, `model-01` |
    | Instance Count | Configure the number of instances to deploy<br>Note: More instances provide stronger concurrency but also higher cost | **Default**: 1 |
    | Deployment Cluster | Select the cluster to deploy the model service to | It is recommended to prefer a cluster that is physically closer to reduce latency |
    | Namespace | Specify the target namespace for the model service deployment | Bound to the cluster |
    | Deployment Template | Select a configured deployment template | Supports quick reuse of resource and runtime configurations |
    | Model Weight File | Select a configured model weight file | Recommended when deploying a custom model |
    | Runtime Framework | Select the inference runtime framework | Supports selection based on the model and scenario |
    | Distributed Inference | When enabled, you can configure the number of deployment nodes per instance | Suitable for scenarios where a single node has insufficient resources |
    | Queue Scheduling | You can configure the scheduling policy, priority, and more | Supports priority and topology-aware scheduling capabilities |

    ![deploy](../images/deploy-new-03.png)

## After Deployment

After the model is deployed successfully, you can:

- View the service status and details in the model service list. See [Manage Model Services](./inference-manage.md).
- Verify service availability through online trials. See [Playground](../exp.md).
- Call the model through the API. See [Model Invocation](../api-call.md).
