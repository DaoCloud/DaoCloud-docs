# Overview

The **Overview** page from the workspace perspective is designed for workspace administrators (tenant administrators) and provides a comprehensive view of the runtime status, usage, costs, models, and risks of OpenClaw instances within the current workspace.

Through this page, you can quickly understand:

* How many Agents are currently running
* Whether Token consumption is abnormal
* Whether invocations are stable
* Which users or instances consume the most resources
* Which models are primarily being used

## Purpose

The **Overview** page helps workspace administrators understand the overall usage and operational status of Agents within the workspace. It is not a configuration page for a single instance, but rather an operational dashboard.

It is primarily used to:

* View the overall scale of OpenClaw instances in the workspace
* View active users, instance counts, and API Key counts
* View Token quotas, Token consumption, and usage trends
* View stability metrics such as error rates and invocation counts
* View resource consumption of top users or top instances
* View the usage distribution of different models
* Assist in evaluating costs, risks, and business value

![Overview](../images/wsoverview.png)

## Terminology

### Active Users / Total Users

Represents the number of users who actually used ClawOS/OpenClaw capabilities during the statistical period, as well as the total number of users in the workspace who have access to the platform.

The label **+1 compared with the previous period** indicates that the number of active users has increased by one compared with the previous statistical period.

### Token Quota

Represents the total amount of Tokens available to the workspace during the current statistical period. For example, `10,000,000` means that the workspace can use up to 10 million Tokens during the current month.

The progress bar below displays the percentage already consumed. For example, `Used 3,215,678 (32%)` means that 3,215,678 Tokens have been consumed, accounting for 32% of the total quota.

Token quotas help administrators control model invocation costs and prevent a single workspace or team from consuming model resources without limits.

!!! note

```
In the current prototype, "Current Month" means that this metric is calculated based on the calendar month or the monthly cycle configured by the platform.
```

### Total Instances

Represents the total number of OpenClaw instances created within the current workspace.

* **Running**: The instance is operating normally and can receive requests and execute tasks.
* **Abnormal**: The instance has issues such as startup failures, runtime errors, configuration errors, or failed health checks.

This metric helps administrators quickly assess the overall deployment scale and health status of Agents in the workspace.

### API Keys

Represents the number of API Keys that are configured or currently in use within the workspace. API Keys are typically used by OpenClaw to invoke foundation models, platform gateways, or other external services.

This metric helps administrators understand the scale of credential usage and assists in troubleshooting invocation failures, model unavailability, or cost anomalies.

### Today's Token Consumption

Represents the cumulative number of Tokens consumed by all OpenClaw instances in the current workspace on the current day.

This metric is useful for quickly identifying abnormal spikes in daily consumption.

### Token Usage

Represents the total Token consumption during the statistical period and distinguishes between input Tokens and output Tokens:

* **Input**: Tokens sent to the model, including user messages, context, tool outputs, and knowledge base retrieval results
* **Output**: Tokens consumed by model-generated responses, plans, code, summaries, and other generated content

**Token Usage** = Input Tokens + Output Tokens.

### Invocation Count

Represents the number of times OpenClaw instances or model services were invoked during the statistical period. Invocation count can be used to observe platform usage frequency.

* If Token usage increases while invocation count decreases, individual tasks may have become more complex.
* If invocation count increases without a significant increase in Token usage, more users may be performing lightweight tasks.

### Error Rate in the Last 7 Days

Represents the ratio of failed invocations to total invocations during the last seven days. The error rate reflects platform stability.

Common sources of errors include:

* Model invocation failures
* Expired or invalid API Keys
* Network access failures
* Skill execution failures
* Tool invocation timeouts
* Abnormal instance states

## Trend Charts

### Token Request Trend

Displays the trend of Token usage during the statistical period. Administrators can use this chart to identify sudden increases, decreases, or recurring peaks.

### Invocation Trend

Displays changes in invocation volume during the statistical period and is used to observe Agent activity.

* If invocation volume continues to increase, Agent usage frequency within the workspace is growing.
* If invocation volume suddenly drops, you may need to check instance status, messaging channel configurations, API Keys, or user access permissions.

## Costs and Models

### Top Users / Instances

This section is used to identify the users or instances with the highest Token consumption.

* **User Dimension**: Displays Token usage by different users, helping administrators understand which users are most active and which users may incur higher costs.
* **Instance Dimension**: Displays Token usage by different OpenClaw instances, helping administrators identify high-consumption instances and determine whether they are supporting critical business workloads or experiencing abnormal invocations.

### Model Usage Distribution

Displays the proportion of Token consumption by different models during the current statistical period. This metric helps administrators understand the model usage structure and supports cost governance.

For example, if high-cost models account for a large proportion of usage, administrators may consider configuring model routing, applying budget limits, or recommending lower-cost models for certain scenarios.

### Time Range

Some cards on the page support time range filtering, such as the last 7 days, last 30 days, or the current month. After switching the time range, related metrics and trend charts are updated accordingly.
