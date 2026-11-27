---
hide:
  - toc
---

# Deploy a Model with the Optimized Template

Optimized templates are pre-configured for specific combinations of model, GPU, and inference engine, including the orchestration framework, inference mode, and inference parameters, helping you quickly create a model service.

## Prerequisites

You have completed [deployment preparation](prerequisites.md) and confirmed that:

- Model files are ready and the current workspace can access the model weights.
- The GPU resources of the target cluster meet the template requirements.
- You have the operation permissions for the target cluster and namespace.

## Steps

1. Navigate to **Turbo Inference** > **Model Services** in the left navigation bar and click **New Deployment**.

2. Select **Optimized Template** as the deployment method. Filter templates by the target model and GPU resources, and select a matching template card.

    <!-- ![Filter and select an optimized template on the Create Model Deployment page](images/optimized-template.png) English screenshot pending -->

    | Template Information | Selection Criteria |
    | --- | --- |
    | Applicable Model | Check whether the model name and version on the card match the available weights. |
    | Orchestration Framework and Inference Mode | Choose llm-d or Dynamo, and PD Disaggregated or PD Aggregated, according to the deployment plan. |
    | GPU Requirements | Check the GPU model, GPU memory, and count, and confirm that the cluster can meet the resource requirements of the selected template. |
    | Template Description | Hover over the template card and check the inference engine version and other applicable conditions in the template description. |

3. Select the **Target Cluster** and **Namespace**, and fill in the basic information.

    | Parameter | Description | Recommended Value or Example |
    | --- | --- | --- |
    | Service Name | Identifies this model service deployment in the platform. | `glm53-pd` |
    | Alias | Optional. Enter an easily recognizable service description. | GLM 5.3 PD-disaggregated service |
    | Model Source | Select the source of the model weights. | PVC |
    | Model Access Name | Enter the model ID used when calling the API. | For example `glm-5.3`. Refer to the service details when calling. |
    | PVC Name | Select the PVC in the target namespace that stores the model weights. | Select the weight PVC corresponding to the template. After creating a new PVC, click the refresh button to update the list. |
    | Model Subpath | Enter the model directory within the PVC. | Use the actual directory. Leave empty if the weights are in the PVC root directory. |
    | Mount Path | Use the container mount path displayed on the page. | Default `/mnt/data`. |

4. Switch between role tabs in **Resource Configuration**. The orchestration framework and inference mode are determined by the template. GPU count, parallelism strategies, and inference parameters are pre-filled by the template; you only need to adjust the editable fields according to the actual environment. For field descriptions, see [resource configuration steps of the generic template](generic-template.md#configure-resources).

5. Click **Preview YAML**, verify the service configuration, and click **Submit and Deploy**.

6. Return to the **Model Services** list and confirm that the service status is **Available** and the resource running status is **Running**. Enter the service details to check the roles and configurations in **Topology & Config**, and the readiness of each role on the **Resources** page. After the service is running, view healthy instances and instance trends in **Service Observability**. For page locations and status examples, see [service verification steps of the generic template](generic-template.md#verify-service).
