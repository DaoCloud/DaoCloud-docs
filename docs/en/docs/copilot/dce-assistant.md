# DCE Assistant

DCE Assistant is designed for platform administrators, operations engineers, and GPU resource administrators. It supports querying platform information, checking cluster health, troubleshooting Pod failures, and analyzing GPU resource bottlenecks through natural language, helping users understand running conditions, locate problems, and develop handling plans.

DCE Assistant is built on DeepSeek Harness and completes tasks by combining the model API, Skills, and platform tools. Skills define the processing methods for specific tasks, tools access platform and running data, and analysis results can be presented as text, tables, and charts.

## Core Capabilities

### Platform Information Query

Queries platform resources and related information based on user needs, providing a basis for status assessment and problem analysis.

- **Resource query**: Queries clusters, namespaces, workloads, and other resources to understand resource configuration and current status.
- **Multi-module access**: Accesses the module APIs already integrated by DCE CLI, including Global Management, Container Management, Observability, AI Lab, LLM Studio, Application Workbench, Billing Management, and more.

The information available for query depends on the modules installed in the target environment, API versions, and access permissions. CLI access to a module indicates the corresponding data access capability; specialized diagnosis or business analysis of that module still requires the support of the corresponding Skills.

### Cluster Health Check and Diagnosis

Checks the running status of clusters, nodes, and Pods, and identifies anomalies and their impact based on events.

- **Cluster status check**: Checks whether a cluster is accessible and running normally.
- **Node and Pod anomaly detection**: Identifies nodes that are not ready, cordoned, or under resource pressure, and summarizes abnormal Pods and their namespaces.
- **Correlation analysis**: Analyzes possible causes by combining node conditions, Pod status, and events, and provides problem priorities and handling suggestions.

### Pod Failure Diagnosis

Collects the status, events, container logs, and related configurations of a specified Pod, and analyzes the causes of startup failures or running anomalies.

- **Common failure troubleshooting**: Covers anomalies such as Pending, CrashLoopBackOff, OOMKilled, ImagePullBackOff, and Evicted.
- **Related resource check**: Checks the owning workload, the node where the Pod runs, resource limits, node selectors, affinity and toleration configurations, and more.
- **Diagnosis explanation**: Lists the events, exit codes, container statuses, or key logs that support the judgment, and provides follow-up handling suggestions.

### GPU Capacity and Bottleneck Analysis

Analyzes the resource capacity, allocation, and actual usage of one or more GPU clusters, and estimates the resource pressure after workload growth.

- **Capacity and headroom analysis**: Views the number of GPUs, allocated resources, core utilization, and memory usage, distinguishing scheduling headroom from actual computing headroom.
- **Workload growth estimation**: Combines the current load, GPU workloads, and HPA configurations to analyze possible computing, scheduling, or memory bottlenecks after traffic growth.
- **Solution comparison**: Based on resource headroom and bottleneck types, proposes suggestions such as scaling out, rate limiting, routing adjustment, or resource reconfiguration, with the basis and assumptions explained.

GPU bottleneck analysis requires actual capacity and utilization data. When QPS data is unavailable, utilization-based estimation can be performed with explicit assumptions; when necessary resource or utilization data is missing, the data needs to be supplemented first. Estimation results are for planning assistance only; actual carrying capacity still needs to be verified with business workloads and performance tests.

## Typical Use Cases

You can directly describe the goal, resource scope, and concerns without looking up specific APIs or commands first. For example:

| Scenario | Example Question | Main Result |
| --- | --- | --- |
| Query platform resources | List the clusters I can access in the current environment. | Cluster list and related information |
| Check cluster health | Check the health status of the prod cluster and point out the issues that need priority. | Key metrics, abnormal resources, impact, and suggestions |
| Troubleshoot Pod failures | Analyze why the api-xxx Pod in the default namespace of the prod cluster keeps restarting. | Status, events, and log evidence, possible causes, and handling suggestions |
| Analyze GPU bottlenecks | If inference traffic increases by 30%, which GPU clusters may hit bottlenecks first? | Resource headroom, load estimation, and bottleneck assessment of each cluster |
| Compare solutions | For the GPU bottleneck above, compare the applicable conditions of scaling out, rate limiting, and routing adjustment. | Basis, applicable conditions, and expected impact of each solution |

The cluster, namespace, and Pod names above are question examples only; replace them with actual objects when using the assistant. Providing a clear resource scope, time range, and load conditions helps produce more accurate results.

## How It Works

DCE Assistant organizes conversations and analysis tasks through DeepSeek Harness. The model API handles requirement understanding and reasoning, Skills provide analysis methods, and the CLI and data plugins handle data access and result presentation.

| Component | Main Responsibility |
| --- | --- |
| Conversation interface | Receives user questions and presents answers and analysis results |
| DeepSeek Harness | Manages conversation context, loads Skills, and organizes model interactions and tool calls |
| Model API | Understands requirements, reasons over the data returned by tools, and generates answers |
| Skills | Define the check steps, analysis methods, output requirements, and capability boundaries of a task |
| CLI tools | Query platform and running data through DCE CLI and other tools |
| Data plugins | Retrieve and normalize data, and prepare display information for charts and tables |

## UI and Result Presentation

You can start a conversation, enter questions, and continue follow-up questions around the returned results in the workspace. The specific UI entries, model names, and example prompts are subject to the actual installed version and configuration.

## Skills and Capability Extension

The main capabilities of DCE Assistant rely on the Skills provided by [daocloud-skills](https://github.com/DaoCloud/daocloud-skills). These Skills define the methods for platform queries, failure diagnosis, and resource analysis, and determine which problems the assistant can handle. The following table lists the current main capabilities and corresponding Skills. The actual capability scope is subject to the loaded Skills and their versions:

| Skill | Capability Scope |
| --- | --- |
| [dce](https://github.com/DaoCloud/daocloud-skills/blob/main/skills/dce/SKILL.md) | Supports platform information queries and data retrieval |
| [container-management:cluster-diagnosis](https://github.com/DaoCloud/daocloud-skills/blob/main/skills/container-management-cluster-diagnosis/SKILL.md) | Cluster health check and anomaly diagnosis |
| [container-management:pod-diagnosis](https://github.com/DaoCloud/daocloud-skills/blob/main/skills/container-management-pod-diagnosis/SKILL.md) | Pod failure diagnosis |
| [container-management:gpu-bottleneck-analysis](https://github.com/DaoCloud/daocloud-skills/blob/main/skills/container-management-gpu-bottleneck-analysis/SKILL.md) | GPU capacity and bottleneck analysis |

Extending or updating Skills can add analysis methods and applicable scenarios. New capabilities also require corresponding query tools, platform APIs, data sources, and access permissions. Data plugins provide presentation capabilities and do not replace the business methods and data required for specialized analysis.

## Usage Requirements and Boundaries

- **Environment and permissions**: Before use, a usable model API, query tools, and DCE authentication information must be configured. The resources and data actually accessible are constrained by the permissions of the identity in use.
- **Data availability**: Diagnosis and analysis depend on the status, events, logs, and metrics that the platform can return. When data is insufficient, the missing information and its impact on conclusions should be stated.
- **Judgment and suggestions**: The assistant currently only provides queries, analysis, judgments, and suggestions, and does not perform resource changes on behalf of users. Operations such as restart, deletion, scaling, and routing adjustment need to be completed by users themselves.
- **Analysis and verification**: Failure cause judgment and capacity estimation should be verified with evidence, assumptions, and actual business conditions. The suggestions provided by the assistant are for operations assistance and resource planning.

[Learn about daocloud-skills](https://github.com/DaoCloud/daocloud-skills){ .md-button }
[View compatibility notes](./compatibility.md){ .md-button }
