# DaoCloud is Among the First to Pass CNCF Kubernetes AI Conformance

As AI/ML workloads are driving exponential growth in demand for compute and hardware acceleration, CNCF has launched the
[Kubernetes AI Conformance](https://github.com/cncf/ai-conformance) certification standard. This standard builds on top of the
baseline [Kubernetes Conformance](https://github.com/cncf/k8s-conformance) certification and defines AI-specific features, APIs
and configuration requirements, to provide a uniform benchmark for cross-environment portability and efficient execution of AI workloads.

!!! note

    It is worth noting that any vendor’s customized Kubernetes platform or distribution must **first** obtain the Kubernetes Conformance certification before it is eligible to apply for AI Conformance.

As a leading open-source company in China, DaoCloud keeps pace with cloud-native AI. Once the community released the Kubernetes AI Conformance standard, DaoCloud immediately launched AI Conformance testing for its widely deployed Kubernetes v1.33-based
[DCE 5.0](https://docs.daocloud.io/) platform — and **successfully passed** in October 2025
([link to certificate PR](https://github.com/cncf/ai-conformance/pull/13)) — becoming the **first enterprise-grade AI/ML platform in China** to pass the certification for this version.

[DCE 5.0](https://daocloud.io/products/index.html) is a high-performance, scalable, cloud-native AI operating system. It delivers a consistent and stable experience across any infrastructure or environment, supports heterogeneous clouds, edge clouds and multi-cloud orchestration. The platform integrates service mesh and microservice technologies for full-link traffic tracing, and provides intelligent monitoring and dynamic visualization dashboards to make the health of clusters, nodes, apps and services clearly observable. It also natively supports DevOps and GitOps, enabling standardized and automated application delivery, and comes with curated databases and middleware to make ops more efficient.

DCE 5.0’s modular architecture ensures each capability is decoupled and upgradeable, while also integrating with a rich AI ecosystem to provide end-to-end solutions. Validated in production by nearly a thousand enterprise customers, it forms a robust digital foundation that helps enterprises unlock AI productivity and move toward an intelligent, AI-driven digital future.

## About AI Conformance Requirements

The AI Conformance specification defines two categories — MUST and SHOULD — covering the critical requirements for AI workloads:

- **MUST**: covers core capabilities such as accelerator resource allocation, AI inference ingress, Gang scheduling, autoscaling, performance telemetry and security access — ensuring the platform can reliably support foundational AI training/inference.
- **SHOULD**: extends to advanced functions such as GPU sharing, high-performance storage, topology-aware scheduling, confidential computing — enabling optimization and refinement of AI platforms.

### MUST

| Category | Item | Functional Requirement | Test Requirement |
| --- | --- | --- | --- |
| Accelerator | Accelerator resource exposure & allocation | Must support Dynamic Resource Allocation (DRA) API to allow more granular resource requests than simple counting | Validate all `resource.k8s.io/v1` DRA resources enabled |
| Network | Advanced AI inference ingress | Must support Kubernetes Gateway API for advanced traffic management for model inference services | Validate all `gateway.networking.k8s.io/v1` Gateway API resources enabled |
| Scheduling & Orchestration | Gang scheduling | Must allow installation and successful operation of at least one Gang scheduling implementation | Proof that at least one Gang scheduler works end-to-end |
| | Effective autoscaling for AI workloads | Cluster autoscaler must scale node groups by accelerator type | Create node pool and (A*N)+1 Pods requesting accelerators; verify scaling |
| | | HorizontalPodAutoscaler must autoscale Pods that use accelerators correctly | Configure custom metrics pipeline, Deployment and HPA; apply load and verify |
| Observability & Telemetry | Accelerator performance metrics | Must support at least one accelerator metrics solution with fine-grained KPIs | Scrape Prometheus-compatible endpoint and verify accelerator metrics |
| | AI job & inference service metrics | Must provide metrics in standard format | Deploy app, send traffic, verify metrics collected |
| Security | Secure accelerator access | Must guarantee in-container access isolation & control | Deploy Pod and verify unauthorized access denied |
| AI Framework & Operators | Robust CRDs & controllers | Must support at least one complex AI Operator installed and working | Deploy Operator, verify Pods/Webhooks/CRDs run normally |

### SHOULD

| Category | Item | Functional Requirement |
| --- | --- | --- |
| Accelerator | Driver & runtime management | Verifiable mechanisms to ensure compatible driver/runtime installed; expose driver version via DRA |
| | GPU sharing | If supported, must have clear mechanism to improve utilization for partial-GPU workloads |
| | Virtual accelerators | If vGPU supported, must expose/manage via DRA |
| | Hardware topology awareness | Node topology (accelerator & NIC layout) should be discoverable & exposed via DRA |
| Storage | High-performance storage | High IOPS/throughput block/file storage exposed via `StorageClass` |
| | | Provide at least one RWX high-performance CSI StorageClass |
| | Image pull optimization | Support fast pulling of large images — caching / streaming |
| | Data cache | Allow caching of frequently accessed data near compute nodes |
| Network | High-performance Pod-to-Pod networking | Use DRA to attach Pods to multiple NICs for high-perf networking |
| | Advanced AI inference ingress | Support Gateway API inference extensions — model hosting, LLM routing |
| | NetworkPolicy enforcement | Must have provider installed & active; enforce user `NetworkPolicy` |
| Scheduling & Orchestration | Batch job enhanced management | Support JobSet API for tightly coupled Jobs |
| | | Support Kueue API (queues, fairness, Gang) |
| | Effective autoscaling | Support heterogeneous node groups and affinity/anti-affinity / taints |
| | Accelerator topology-aware scheduling | If accelerator interconnects are discoverable, scheduler should use them |
| Security | Secure workload authentication | Mechanism for secure service access without long-lived static credentials |
| | Confidential AI | Support confidential containers in TEE |
| | Model/software supply chain security | Admission control integrated with Sigstore/Cosign & policy engines |
| | Untrusted code sandboxing | Strong isolation to protect processes/memory/network |
| Maintenance & Repair | Faulty device detection | Mechanisms to detect faulty devices (and optionally auto-heal) |
| | Advance maintenance notification | Provide early scheduled maintenance alerts |
| | Gang maintenance for highly inter-connected nodes | Support Gang maintenance to minimize disruption |

!!! note

    These items and categories may evolve with industry development and standard updates — for reference only.
    Refer to [cncf/ai-conformance README](https://github.com/cncf/ai-conformance) for the latest.

Certified platforms can officially use the AI Conformance mark — recognized by CNCF — signaling that the distribution is AI-friendly.

<figure markdown="span">
  ![logo](../images/CNCF_AI_Conformance_Logo.png){ width="200" }
</figure>

## DaoCloud Leads China — Among the World’s First

For Kubernetes v1.33, only a handful of platforms have passed so far.
The [DaoCloud DCE platform](https://daocloud.io/products/platinum-edition/index.html) was selected *together with*
Red Hat OpenShift, SUSE RKE2 and other globally recognized platforms — demonstrating that Chinese vendors are at the frontier of cloud-native AI:

- **DaoCloud DCE**
- NeoNephos Foundation Gardener
- Giant Swarm Platform
- Red Hat OpenShift Container Platform
- SUSE RKE2
- Sidero Labs Talos Linux

<figure markdown="span">
  ![v1.33 compliance list](../images/ai-conf01.png){ width="700" }
</figure>

DCE 5.0’s certification proves it can deliver standards-compliant, portable and highly reliable AI run-time — whether large-scale model training, high-performance inference, or MLOps pipelines — with efficiency and elasticity. Going forward, DaoCloud will continue to invest in cloud-native AI and provide a stronger foundation for enterprise AI transformation.
