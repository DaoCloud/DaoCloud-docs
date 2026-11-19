# Deploy a Model Service - User

This tutorial deploys a model from the Model Gallery as an invocable inference service in [LLM Studio](../hydra/intro/index.md).

## Prerequisites

- A work cluster has been created, with the cluster and namespace available. See [Create a Work Cluster](join-cluster.md).
- You have signed in to the console with a user that has the LLM Studio permission.

## Steps

1. In the left navigation, click **LLM Studio** to enter the **Model Gallery**.

2. Browse or search for the target model (e.g. DeepSeek-R1), then click the **Deploy** button on the model card to enter the deployment page.

3. Fill in the deployment parameters as needed and click **OK**:

    | Parameter | Description |
    |---|---|
    | Model Selection | Choose from the Model Gallery or custom models, e.g. DeepSeek-R1 |
    | Model Service Name | Lowercase letters, numbers, and hyphens (`-`), 2–64 characters, e.g. `text-gen-service` |
    | Instances | More instances mean higher concurrency and higher cost. The default is 1 |
    | Deployment Cluster | Select the [work cluster you created](join-cluster.md); prefer the cluster with GPU nodes |
    | Namespace | The target namespace bound to the cluster |
    | Runtime Framework | Choose an inference runtime based on the model and scenario |

    Keep the remaining parameters (distributed inference, queue scheduling, etc.) at their defaults for a quick trial.

4. After the deployment completes, check the **Model Services** list in the left navigation. The service status changes from **Deploying** to **Running**.

## Verification

Once the model service status is **Running**, you can select the service in [Model Playground](call-model.md) to chat directly, or verify its availability through an API call.

## Next Step

Try out the model online or call it via API — see [Try Out and Call Models](call-model.md). To learn about managing and scaling model services, see [Model Services](../hydra/deploy/index.md).
