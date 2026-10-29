# Smart Routing

Smart Routing is designed for platform operations administrators to select policies based on per-cluster configuration models. Applications initiate requests through a unified `model=auto`, and the platform selects the target model based on request characteristics. Each cluster independently maintains one smart route, and uses the configured fallback model when no rule is matched.

## Use Cases and Value

- **Lower invocation cost:** When simple tasks also use large models, unnecessary costs may be incurred. You can assign lightweight tasks to economical models and hand complex tasks to more capable models.
- **Shorter response wait:** When lightweight requests go through a complex reasoning chain, response time may be long. You can select a suitable lightweight model based on request characteristics to improve the response experience for simple tasks.
- **Better task results:** A single model is hard to fit all scenarios. You can select models based on request intent, domain, or complexity, so that different tasks match more suitable models.

Actual cost, response time, and answer quality depend on model, resource, and rule configuration. It is recommended to test and adjust based on your business requests.

## Prerequisites

- The current user has platform administrator permissions and can access **Operations Management**.
- The target cluster has been connected to the platform, and the Gateway API and gateway-related components are ready.
- You have prepared MaaS models available for the cluster, to be used as routing targets and the fallback model. In workspace mode you can also select self-deployed models. For how to integrate MaaS models, see [MaaS Model Management](./maas.md).
- When using advanced policies, signals such as semantic embedding, request complexity, and domain classification may require a routing model and an accessible PVC. Online deployment requires the cluster to be able to download the model; offline deployment requires preparing the model files in advance.

## Create a Basic Policy

Basic policies apply to scenarios where models are selected based on time window, request length, or custom conditions.

1. Enter the **Operations Management** view, select **Smart Routing** in the left navigation bar, and click **Create Cluster Route**.
    <!-- ![Create Cluster Route](../images/auto-route-01.png) -->
2. In **Basic Information**, select the cluster and **Basic Policy**, confirm the external model name is `auto`, and proceed to the next step.
    <!-- ![Basic Information](../images/auto-router-01.png) -->
3. In **Policy Configuration**, add rules as needed and select a target model for each rule. You can configure the following rules:

    | Rule Type | Configuration Description |
    | --- | --- |
    | Time-window Rule | Set the start time, end time, and effective date, and select the target model. |
    | Request-length Rule | Set the minimum and maximum estimated Token counts and select the target model. Supports `K` (thousand) and `M` (million) units. |
    | Custom Policy Rule | Fill in the rule name, expression, and target model. You can view fields and examples via **Syntax Guide** on the page. |

    !!! note

        - Multiple rules have an OR relationship: if any rule is matched, its target model is used.
        - If no rule is matched, the fallback model is used.

    <!-- ![Policy Configuration](../images/auto-route-03.png) -->

4. When no rules are configured, the system automatically uses the fallback model. Configure at least one rule and select the **Fallback Model**, then confirm the configuration to create the route.

5. Return to the list and wait for the route to become ready before performing invocation verification.

## Create an Advanced Policy

Advanced policies identify request characteristics through signals and then select the target model based on decisions. They are suitable for selecting models by intent, domain, or task complexity.

1. Enter the **Operations Management** view, select **Smart Routing** in the left navigation bar, and click **Create Cluster Route**.

2. In **Basic Information**, select the cluster and **Advanced Policy**, then go to **Signal Configuration**.
    <!-- ![Signal Configuration](../images/auto-route-04.png) -->

3. Enable signal types as needed and add rules:

    | Signal Type | Configuration Description |
    | --- | --- |
    | Semantic Embedding | Fill in candidate phrases, similarity threshold, and aggregation method; determine a match based on the similarity between the request and candidate phrases. |
    | Domain Classification | Select the categories to match from the domain categories provided on the page. |
    | Request Complexity | Configure simple samples, difficult samples, and a threshold to distinguish requests of different complexity. |
    | Context Length | Configure the minimum and maximum Token counts to match by request length. |

    <!-- ![Signal Configuration](../images/auto-route-05.png) -->

    !!! note

        - The Embedding model, PVC, and deployment method used by Semantic Embedding and Request Complexity must be consistent.
        - Domain Classification uses a classification model; the Context Length signal does not require deploying a classification model.

4. Go to **Decision Configuration**, add a decision, fill in the name, priority, condition relationship, and target model, and select the signal conditions to combine.
    <!-- ![Decision Configuration](../images/auto-route-06.png) -->

    !!! note

        - When no decision is configured, the system automatically uses the fallback model. Configure at least one decision and select the **Fallback Model**, then confirm the configuration to create the route.

## Invoke and Verify

After the route is ready, you can use the API Key to invoke the model service of the entry cluster. Set `model` to `auto` in the request body:

```shell
curl 'https://<entry-cluster-address>/v1/chat/completions' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <API_KEY>' \
  -d '{
    "model": "auto",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

Replace the entry address and API Key with the values from your actual environment. For how to obtain an API Key, see [API Key Management](../apikey.md).

## Manage Smart Routing

In the Smart Routing list or details page, you can perform the following operations:

- **Edit:** Adjust the routing configuration of the current cluster and save the update.
- **Enable or Disable:** Control whether Smart Routing is enabled for the cluster.
- **Delete:** After confirmation, delete the Smart Routing configuration for the cluster; to use it again, you must recreate it.

<!-- ![Smart Routing List](../images/auto-route-07.png) -->
