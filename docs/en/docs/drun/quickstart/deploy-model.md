# Deploy a Model Service - User

This tutorial deploys a model from the [Model Gallery](../hydra/index.md) as an invocable model service in [LLM Studio](../hydra/intro/index.md).

## Prerequisites

- A work cluster is available with usable clusters and namespaces. See [Create a Work Cluster](join-cluster.md).
- Sign in to the console with a user who has the LLM Studio role.

## Steps

1. In the left navigation bar, click **LLM Studio** and go to the **Model Gallery**.

2. Browse or search for the target model (e.g. DeepSeek-R1), click **Deploy** on the model card to open the deployment page;
   you can also click **Deploy New Model** on the **Model Serving** list page.

3. Fill in the deployment parameters as needed and click **OK**:

    | Parameter | Description |
    |---|---|
    | Model Source | Select from the Model Gallery or custom models; custom models must be created in [Create Model](../hydra/models/index.md) first |
    | Model | Select the model to deploy (e.g. DeepSeek-R1) |
    | Service Name | Lowercase letters, digits, and hyphens (`-`), 2–64 characters, e.g. `text-gen-service` |
    | Replicas | More replicas mean higher concurrency but higher cost. Default: 1 |
    | Deployment Cluster | Select the [work cluster](join-cluster.md), preferably the one with GPU nodes |
    | Namespace | The target namespace bound to the cluster |
    | Runtime Framework | Select an inference runtime based on the model and scenario |

    Keep the remaining parameters (distributed inference, queue scheduling, etc.) at their defaults for a quick start.

4. After the deployment completes, check on the **Model Serving** list page that the service status changes from **Deploying** to **Running**.

## Verify

Once the model service is **Running**, you can chat with it directly in the [Playground](call-model.md), or verify availability through an API call.

## Next step

To try the model online or call it via API, see [Experience and Call Models](call-model.md). For management and scaling of model services, see [Model Serving](../hydra/deploy/index.md).
