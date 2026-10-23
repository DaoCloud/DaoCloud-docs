# Security Policy Management

Security Policy Management is designed for platform administrators to configure AI gateway security policies per cluster.
After policies are applied to the gateway plugin in a worker cluster, model requests and responses can be inspected and handled according to the configured action, such as blocking the request, logging only, returning a random replacement response, or masking matched content.

This capability depends on Higress integrated with the Knoway gateway. It requires LLM Studio **v0.15.0** or later, with Higress enabled on the worker cluster. For how to enable Higress, see [Upgrade Notes](../intro/upgrade-notes.md).

## Prerequisites

- The current user has platform administrator permissions and can access the **Admin Console**.
- The target worker cluster has hydra-agent installed, and `knoway.higress.enabled` is turned on as described in the upgrade notes.
- The policy list only shows clusters that already have the gateway security plugin configuration. If the list is empty, finish installing and upgrading Higress-related components and CRDs first.

## Entry Point

1. Sign in to the platform and open the **Admin Console**.
2. In the left navigation, choose **Security** → **Policy Management**.

![Policy management list](images/security-policy-list.png)

## View the Policy List

The policy list shows gateway security configurations by cluster. The main fields are:

| Field | Description |
| ----- | ----------- |
| Cluster | Worker cluster name |
| Policy Types | Currently enabled policy types; multiple types can be enabled together |
| Created At | When the cluster policy configuration was created |
| Updated At | When the configuration was last updated |

You can search by **cluster** name in the search box. Click **Edit** on a row to open the policy editor for that cluster.

!!! note

    There is no separate **Create Policy** entry. Policies are edited per cluster against an existing gateway plugin configuration. Clusters without Higress installation do not appear in the list.

## Edit a Policy

1. In the policy list, find the target cluster and click **Edit**.
2. On the **Edit Policy** page, **Cluster** is read-only.
3. Under **Policy Configuration**, enable the policies you need, fill in the parameters, and save.

![Edit policy](images/security-policy-edit.png)

!!! note

    Enabled policies with configured parameters take effect. Disabled policies are not applied.

### Policy Types and Fields

| Policy Type | Description | Configurable Fields | Actions |
| ----------- | ----------- | ------------------- | ------- |
| Regex Match Policy | Match user input against regular expressions line by line to detect risk patterns such as jailbreak phrases and prompt injection | **Match Strategy**: Trigger on any match / Trigger only when all match; **Regex Patterns** (one regex per line); when **Random Replace** is selected, also configure **Random Replace Responses** (one response per line) | Block Request, Log, Random Replace, Mask Replace |
| Sensitive Word Policy | Detect whether the input contains configured sensitive words for compliance and content safety | **Match Strategy**: Trigger on any word hit / Trigger only when all words hit; **Sensitive Words** (one word per line); when **Random Replace** is selected, also configure **Random Replace Responses** | Block Request, Log, Random Replace, Mask Replace |
| JSON Schema Validation Policy | Validate the request body structure (field types, required fields, and so on) against a JSON Schema | Enable toggle and **Action**. The UI does not provide online editing of the Schema body itself | Block Request, Log |
| JWT Validation Policy | Read a JWT from the specified request header and verify validity (signature, expiration, and so on) | **Header Name**; **Token Required**: Required / Optional | Block Request, Log |
| Model Allow / Block List Policy | Allow only specified models via an allowlist, or deny specified models via a blocklist | **Mode**: Allowlist (only models in the list are allowed) / Blocklist (models in the list are blocked); **Select Models** (multi-select enabled MaaS models in the cluster); **Model Regex** (one regex per line, useful for matching a model series) | Block Request, Log |

### Action Descriptions

| Action | Description |
| ------ | ----------- |
| Block Request | Reject the call when the policy is matched |
| Log | Forward the request normally and write a security audit log for later investigation |
| Random Replace | Do not return the model output; randomly return one of the configured response texts |
| Mask Replace | Return the content after masking the matched parts |

### Configuration Validation

Before saving, note the following validation rules:

- When **Regex Match Policy** is enabled, provide at least one regex pattern.
- When **Sensitive Word Policy** is enabled, provide at least one sensitive word.
- When the action is **Random Replace**, provide at least one random replace response.
- When **Model Allow / Block List Policy** is enabled, select at least one model or provide at least one model regex.

The edit page also provides **Common examples** that you can adapt for typical regex and sensitive-word patterns.

## Notes

- Policies take effect per cluster. Different worker clusters under the same platform are independent and must be edited separately.
- Models available in the **Model Allow / Block List** come from enabled MaaS models in that cluster. Complete onboarding and enablement in [MaaS Models](./maas.md) first.
- After you save policy changes, they apply to new gateway requests. Validate rules and actions in a test environment before enabling **Block Request** in production.
- Triggered events can be queried and exported in [Security Audit Logs](./security-audit-logs.md).
