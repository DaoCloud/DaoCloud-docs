---
hide:
  - toc
---

# Basic concept

The glossary in this section defines the core concepts behind multicloud orchestration to help you build a mental model of how multicloud orchestration works.

- Resource templates: Multicloud orchestration software defines Kubernetes Native APIs for federated resource templates, allowing easy integration with existing tools already adopted by Kubernetes.
- Deployment strategy: Multicloud orchestration software provides an independent propagation (set) strategy API to define multi-cluster scheduling and propagation requirements.
    - Mapping and workload support 1:n. Users do not need to specify scheduling constraints every time they create a federated application.
    - With the default policy, users can directly interact with the Kubernetes API.

- Differentiated policies: The multicloud orchestration software provides an independent Override Policy API for specifically automating cluster-related configurations.
    - Override image prefixes based on member cluster regions.
    - Override StorageClass based on cloud provider used.