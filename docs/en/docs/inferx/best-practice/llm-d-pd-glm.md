# Deploy a PD-disaggregated GLM 5.3 Service with the Optimized Template

This best practice describes how to use llm-d and an optimized template to deploy a PD-disaggregated GLM 5.3 inference service. After deployment, you can send inference requests through the service entry point.

## Prerequisites

- You have completed [deployment preparation](../model-services/prerequisites.md).
- The template library contains an llm-d PD-disaggregated template for the target GLM model and GPU. If no matching template is found, contact the administrator.

## Steps

1. Navigate to **Turbo Inference** > **Model Services** in the left navigation bar and click **New Deployment**.

2. Select **Optimized Template** as the deployment method.

3. Search for the target GLM model in the template library, filter by **GPU type**, **orchestration framework** (llm-d), and **inference mode** (PD Disaggregated), and select a template.

    <!-- ![Filter GLM deployment templates](images/glm-template.png) English screenshot pending -->

4. Fill in the deployment environment and model information.

    | Parameter | Description | Recommended Value or Example |
    | --- | --- | --- |
    | Target Cluster | Select a cluster whose GPU resources meet the template requirements. | When using the H20 template above, select an H20 cluster that meets the GPU count requirements. |
    | Namespace | Select the namespace where the model weight PVC resides. | The same namespace as the required PVC. |
    | Service Name | Enter a name used to identify the deployment instance in the platform. | `glm-53-pd` |
    | Alias | Enter an easily recognizable service name as needed. | GLM 5.3 PD-disaggregated service |
    | Model Access Name | Enter the model ID passed in when calling the API. | When deploying the above model, you can enter `public/glm-5.3`. |
    | PVC Name | Select the PVC that stores the target model weights. | Select the PVC that matches the target model. After creating a new PVC, click the refresh button to update the list. |
    | Model Subpath | Enter the model weight directory within the PVC. | Use the actual directory, e.g. `/glm-5.3`. Leave empty if the weights are in the PVC root directory. |

5. Confirm that the **orchestration framework** is llm-d and the **inference mode** is **PD Disaggregated**. Check each role one by one in **Resource Configuration**. Parameters such as GPU type, GPUs per instance, and parallelism strategies are pre-filled by the optimized template; you only need to adjust the editable fields according to the actual deployment environment.

    | Role | Responsibility | Configuration Recommendation |
    | --- | --- | --- |
    | `prefill` | Processes input and generates the KV Cache. | Check the replicas and vLLM image address, and confirm that the image version meets the template requirements. |
    | `decode` | Generates output tokens step by step. | Check the replicas and vLLM image address, and confirm that the image version meets the template requirements. |
    | `routing-proxy` | Deployed with the `decode` instance, coordinates request handoff between the prefill and decode stages. | Check the accompanying image address. |
    | `llm-d-router` | Routes inference requests. | Check the replicas and image version. Configure replicas based on request concurrency and the processing capacity of prefill and decode instances. |

    <!-- ![Check the resource configuration of the prefill role](images/glm-template-resources.jpg) English screenshot pending -->

6. Click **Preview YAML**, verify the service configuration, and click **Submit and Deploy**.

7. Return to the **Model Services** list and confirm that the service status is **Available** and the resource running status is **Running**. Click the service card to view details, check the configuration of each role in **Topology & Config**, and confirm resource readiness on the **Resources** page. If deployment is abnormal, click **Logs** in the **Actions** column of the corresponding Pod row. After the service is running, view healthy instances and instance trends in **Service Observability**. For page locations and status examples, see [service verification steps of the generic template](../model-services/generic-template.md#verify-service).

8. Refer to [Expose Model Service Externally (Hydra/Knoway)](export-by-hydra.md), choose an access method supported by your environment, and send an inference request to confirm that the model returns results.
