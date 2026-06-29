# Overview (Administrator View)

The Platform Administrator Overview is designed to monitor the overall usage, resource consumption, instance status, and user/API Key distribution of the ClawOS platform from a **global perspective**. It helps administrators quickly determine whether the platform is operating in a healthy, stable, and manageable state.

Unlike the [Overview](../workspace/overview.md) in the workspace view, this page is intended for **platform administrators** and displays aggregated data across all workspaces for platform-level operations and governance.

## Purpose

The **Overview** page is an operational dashboard from the ClawOS administrator perspective rather than a configuration page for a specific instance or workspace.

It is primarily used to:

* View the overall platform request volume and Token consumption
* Monitor the scale and health of running instances
* Analyze resource consumption across workspaces, users, and models
* Identify high-consumption users, API Keys, and major request sources
* Detect traffic peaks, abnormal spikes, and cost risks
* Assist with quota management, cost accounting, capacity planning, and troubleshooting

## Filters and Time Range

Administrators can filter and view platform data within a specified time range using the following dimensions:

* **Workspace**
* **Requested Model**: The model selected by users or instances when making requests
* **Upstream Model**: The underlying model actually invoked by the platform

Some cards on the page support time range filtering, such as the last 7 days, last 30 days, or the current month. After switching the time range, related metrics and trend charts are updated accordingly.

## Key Metrics

The top section of the page displays the following key metrics:

| Category | Metrics |
| -------- | ------- |
| **Requests and Tokens** | Total requests, input Tokens, output Tokens, average Tokens per request |
| **Users and Credentials** | Number of active users, number of active API Keys |
| **Instance Status** | Total instances, running instances, stopped instances, failed instances |

These metrics help administrators quickly assess the current platform load, resource consumption scale, and overall instance health.

## Trend Charts

Trend charts are used to observe changes in key metrics over time, making it easier to identify traffic peaks, abnormal spikes, or fluctuations in resource consumption.

Common trends include:

* **Platform Request Trend**
* **Token Consumption Trend**
* **Average Tokens per Request Trend**
* **Active User Trend**

If request volume or Token consumption suddenly increases during a certain period, administrators may need to further investigate distribution analysis and ranking details to determine whether abnormal requests or cost risks exist.

## Distribution Analysis

The distribution analysis section shows the proportion of resource usage across different dimensions, helping administrators understand the structure of resource consumption.

### Workspace Distribution

Displays the proportion of total Token consumption by workspace to identify which workspaces consume the majority of platform resources.

### Upstream Model Distribution

Displays the proportion of usage across the underlying models actually invoked by the platform, helping administrators understand the current model consumption structure.

### Requested Model Distribution

Displays the proportion of usage across the models selected by users or instances, helping administrators understand model preferences from the business perspective.

## Rankings and Details

The rankings and details section provides Top rankings and high-value user details to help administrators identify major request sources.

| Section | Description |
| ------- | ----------- |
| **Top Users** | Ranked by request count or Token consumption to identify the most active or highest-consuming users |
| **Top API Keys** | Identifies high-consumption or frequently used API Keys |
| **High-Value User Details** | Displays details such as request count, input Tokens, and output Tokens for key users |

By combining these data points, administrators can further track resource consumers and support quota management, cost accounting, anomaly investigation, and user operations.

## Advanced Analysis

In addition to standard request and Token metrics, platform administrators can also view the following advanced analytics:

* **Multimodal Statistics**: Trends of input/output image counts and pixel volumes
* **Usage Heatmap**: Hourly usage heatmap on weekdays to observe peak usage periods
* **Model Mapping Deviation**: Deviations between requested models and upstream models to identify model routing anomalies
* **Abnormal Data Scanning**: Identifies unexpected request behaviors or potential data issues

## Key Value

The Platform Administrator Overview is designed to help answer the following questions:

* What is the overall platform usage?
* Which workspaces, users, or models consume the most resources?
* Which users or API Keys are the primary request sources?
* Are the instances running healthily?
* Are there abnormal requests, sudden cost increases, or model usage deviations?

To view the operational status of a specific workspace, see [Workspace Overview](../workspace/overview.md).
