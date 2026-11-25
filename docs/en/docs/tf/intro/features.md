---
hide:
  - toc
---

# d.run Token Factory Features

The platform covers the production and operation workflow of the Token Factory, providing role-based entry points and data views for service consumption, service management, production operations, and business analysis.

<div class="grid cards" markdown>

- :material-account-outline:{ .lg .middle } __Business Users__

    ---

    Try and invoke models in the Model Plaza, deploy dedicated inference services with one click, use AI apps and GPU instances, and view your own usage and spending records at any time.

- :material-cog-outline:{ .lg .middle } __Service Administrators__

    ---

    Manage model publishing and service integration, configure invocation rules, routing policies, and content security policies, and assign access permissions to different teams.

</div>

<div class="grid cards" markdown>

- :material-server:{ .lg .middle } __Ops Engineers__

    ---

    Manage infrastructure and resource scheduling, deploy high-performance inference services, monitor service performance in real time, and handle alerts and runtime faults promptly.

- :material-chart-box-outline:{ .lg .middle } __Business Analysts__

    ---

    Analyze capacity, customer usage and spending, revenue and costs, and fund usage; run budget management and investment calculations, making every unit of compute accountable and profitable.

</div>

## Features

| Category | Module | Feature | Description |
| :--- | :--- | :--- | :--- |
| Cloud Native AI | [LLM Studio](../hydra/intro/index.md) | [Model Experience](../hydra/exp.md) | Find text generation, image understanding, and image generation models in the Model Plaza and choose the one that fits your business. Trial and compare multiple models online to check response quality before integrating them into your business |
| | | [Model Deployment](../hydra/deploy/index.md) | Deploy mainstream open-source and proprietary models as dedicated inference services and view service status. Supports multi-node multi-GPU distributed deployment |
| | | [API Access](../hydra/api-call.md) | Provides OpenAI-compatible APIs and invocation examples, supporting clients such as Cherry Studio, Cline, LobeChat, and Bob, so business systems and development tools can invoke models with ease |
| | | [API Key Management](../hydra/apikey.md) | Create and manage invocation keys, and control application access to model services |
| | | Usage Statistics | View invocation and Token consumption by model, API Key, and time to understand how each application is used, supporting budget management and application adjustments |
| | [Service Management & Token Governance](../hydra/intro/index.md) | [Manage Models](../hydra/models/model-manage.md) | Import, create, publish, and take models offline, and manage the model catalog available to users |
| | | [MaaS Model Management](../hydra/oam/maas.md) | Integrate self-built services or upstream model APIs, with the platform providing a unified invocation entry point for users |
| | | [Smart Routing](../hydra/oam/auto-route.md) | Distribute requests through routing, load balancing, and backup paths to improve service availability |
| | | Rate Limiting | Supports traffic limits at the global, tenant, and API Key levels to reduce the impact of request bursts on shared services |
| | | [Security Policy Management](../hydra/oam/security-policy.md) | Manage content risks in model invocations through content policies such as sensitive-word detection, regular-expression matching, and integrated safety models |
| | | Analytics Center | Track input and output Token usage by model and tenant, and analyze trends in revenue, cost, and gross margin |
| | [Turbo Inference](../inferx/index.md) | High-Performance Model Deployment | Deploy high-performance inference services on NVIDIA and various domestic accelerators combined with mainstream inference frameworks, supporting multi-node multi-GPU and P/D separation, with resources planned around the distinct characteristics of prefilling and decoding |
| | | KV Cache Reuse | Reuse repeated prefix computation through KV Cache offloading and Redhare tiered caching, expanding cache capacity with local and remote memory and storage to reduce repeated computation in long-context and multi-turn tasks |
| | | Curated Template Library | Provides a rich set of curated deployment templates around mainstream inference engines and distributed orchestration frameworks such as vLLM, SGLang, LLM\-D, and Dynamo, easing throughput, memory, and latency bottlenecks |
| | | Model Acceptance Testing | Validate model API compatibility, functionality, and performance before going live, so that optimization results meet both model quality and service quality requirements as the standard for production services |
| | | Service Observability | Correlates service throughput, P/D queues, cache hit rates, GPU, and network metrics to distinguish request growth, compute shortage, caching, and communication issues, supporting continuous performance tuning and troubleshooting |
| | [Compute Cloud](../zestu/index.md) | [Instance Management](../zestu/instance.md) | Create instances with the GPU specification you need and manage running resources by task |
| | | [Development Access](../zestu/instance/jupyter.md) | Access instances through JupyterLab, SSH, or VS Code for code debugging, algorithm experiments, and service deployment |
| | | [Payment Options](../zestu/instance-prepaid.md) | Supports pay-as-you-go or annual/monthly subscription, for short-term experiments and long-running workloads respectively |
| | [AI Apps](../dak/index.md) | [Knowledge Q&A](../dak/user-guide/app-center/create-app.md) | Answer questions by combining enterprise knowledge with conversation context, with support for answer rating and feedback |
| | | Application Integration | Use services through application links and H5 pages, or integrate them into business systems through OpenAPI |
| Cloud Native Infra | [GPU Resources and Scheduling](../kpanda/intro/index.md) | [Heterogeneous GPU Management](../kpanda/user-guide/gpu/index.md) | Identify and manage NVIDIA GPUs and domestic AI accelerators such as Ascend in a unified manner, supporting management and scheduling of different card types in the same cluster for mixed hardware environments |
| | | [GPU Sharing](../kpanda/user-guide/gpu/vgpu_quota.md) | Supports full-card, vGPU, and MIG resource modes. On supported hardware, allocate quotas by memory or compute so multiple tasks share a GPU and idle resources are reduced |
| | | [AI Task and Service Scheduling](../kpanda/user-guide/gpu/volcano/volcano-gang-scheduler.md) | Allocate resources based on task GPU requirements and node topology, supporting scheduling modes such as Gang scheduling and topology-aware scheduling, as well as multi-node inference for models of different scales |
| | [Networking and Storage](../network/intro/index.md) | Container Networking | Configure networks through multi-CNI, Multus, SpiderPool, and other components, with IP pools managing address allocation |
| | | High-Performance Communication | RDMA configuration meets AI task requirements for low-latency, high-bandwidth communication |
| | | [Persistent Storage](../storage/index.md) | Connect existing storage or cloud-native local storage through CSI, providing persistent volumes for model files, datasets, and stateful services |
| Operations | [Cockpit](../crane/intro/index.md) | [Capacity-to-Billing Conversion Analysis](../crane/user-guide/singlepage.md) | Compare available capacity, actual output, and billed Tokens to analyze compute utilization and the conversion of output into billed consumption |
| | | Customer and Model Analytics | Analyze consumption structure and business performance of different models by combining customer usage, revenue contribution, consumption concentration, and model rankings |
| | | [Cost Efficiency Comparison](../crane/user-guide/finops.md) | Compare utilization, per-card output, and per-Token cost across GPU models to evaluate the operating efficiency of resources and models. Revenue analysis requires complete cost and consumption data |
| | | [Production Status Analysis](../crane/user-guide/production-operations.md) | View throughput, time to first Token (TTFT), time per output Token (TPOT), queues, GPU pools, and SLA. Correlate alerts, scheduling, and scaling events to analyze the causes of metric changes |
| | [Copilot Workbench](../copilot/index.md) | Platform Information Queries | Answer questions by combining resource, service, monitoring, and consumption data, reducing the manual work of switching pages and collecting information |
| | | Problem Analysis | Analyze possible causes of capacity, performance, cost, and runtime anomalies, compare solutions, and list conditions that still need verification |
| | | Investment Calculation | Calculate annual revenue, net cash flow, and static payback period from devices, throughput, prices, load, and costs; compare business scenarios while keeping assumptions and data sources |
| | [Billing Center](../leopard/index.md) | [Billing and Orders](../leopard/orders.md) | Bill by product usage and rules, with pay-as-you-go or periodic payment, distinguishing regular input, output, and cached Tokens; records service purchases and resource changes |
| | | [Bills and Transactions](../leopard/bills.md) | Aggregate, filter, and export bills by account, product, region, and billing period, and record balance changes for easy reconciliation and fund verification |
| | | [Accounts and Credit Limits](../leopard/credit_limit.md) | Supports account top-ups, balance reminders, and fund sharing between primary and sub-accounts; allocate quotas to sub-accounts to control budgets |
| | | [Offers and Rewards](../leopard/voucher.md) | Track invitation progress and issue vouchers by campaign rules, deducting them by validity period and scope, with the remainder charged against the cash balance |
| OAM | [Insight](../insight/intro/index.md) | Inference Performance Monitoring | Focus on request throughput, time to first Token (TTFT), time per output Token (TPOT), and request errors to understand service responsiveness and stability |
| | | GPU Resource Monitoring | Analyze inference workload and resource usage by combining GPU utilization, memory usage, and node resources, supporting capacity planning and performance optimization |
| | | Inference Troubleshooting | Correlate request traces, service logs, resource metrics, and runtime events to find the causes of slow requests, failed invocations, and service anomalies |
| | | [Alert Management](../insight/user-guide/alert-center/index.md) | Provides alerts and notifications for service latency, errors, and resource anomalies, so ops engineers can handle service faults promptly |
| | [Global Management](../ghippo/intro/index.md) | [Identity and Access Management](../ghippo/user-guide/access-control/index.md) | Supports local accounts and external identity sources such as LDAP, OIDC, and OAuth 2.0, assigning permissions through user groups, roles, and workspaces to isolate resources across users |
| | | [Platform Governance and Settings](../ghippo/user-guide/platform-setting/index.md) | Records key operations, supports security auditing and accountability, and centrally configures sessions, password policies, notification services, and platform appearance |
