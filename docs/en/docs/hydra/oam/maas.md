---
hide:
  - toc
---

# MaaS Model Management

**MaaS Model Management** is a core module of the large model platform. It is designed for platform operators, providing full lifecycle management capabilities such as model integration, activation/deactivation, rate limiting, and load balancing. Through this module, administrators can quickly integrate private or open-source models into the platform and expose them as standardized API services.

## Create a MaaS Model

You need to fill the following fields one by one:

| Field Name | Description | Required |
| ----------- | ------------ | -------- |
| Model Name | Select a model from the model marketplace list | Yes |
| Cluster | When configuring a MaaS model, you must select an "entry cluster." The platform automatically generates an access path for the model based on this cluster, which can be used by the large model service platform, APIs, or external systems | Yes |
| Model ID | The name of the model provided by the upstream endpoint, e.g., `deepseek-chat` | Yes |
| Endpoint | The full HTTP(S) address of the upstream service, e.g., `https://api.deepseek.com` | Yes |
| API Key | Fill in if the upstream service requires token authentication | No |

### Rate Limiting Rules (Optional)

If rate limiting is required, you can enable this configuration.

**Effective Target:** Can be applied to either an API Key or an existing workspace.

!!! note

    - **Effective target: API Key** — Limits the total number of calls made to the model by a single API Key within a workspace.
    - **Effective target: Existing workspace** — Limits the total number of model calls made by all API Keys within the workspace.

- **Workspace:** Select the workspace to apply the rule  
- **API Key ID:** Select the API Key to apply the rule  
- **limit:** The maximum number of requests a single Key can make within the specified duration (in seconds), e.g., 100  
- **duration:** Time period in seconds, e.g., 60  
- Multiple rules can be added

### Load Balancing Policies

Currently, only the **round-robin** policy is supported.

1. **Round-robin (default):** Sequentially forwards requests to multiple endpoints  
2. **Random:** Randomly selects an endpoint  
3. **Weighted:** Requires specifying weight values in the dropdown, with a total of 100  

## MaaS Model Management List

In the MaaS model management list, users can view all created MaaS models, including the model name, model ID, model tags, status, entry cluster address, and gateway status.  
Click **Enable** to make the model visible in the **User View** under the model marketplace.

!!! note

    **Prerequisite:** The model must be **published to the model marketplace** via the model marketplace management module in the operations management platform.

