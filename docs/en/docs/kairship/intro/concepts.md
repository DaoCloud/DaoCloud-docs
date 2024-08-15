---
MTPE: ModetaNiu
DATE: 2024-07-18
hide:
  - toc
---

# Basic Concepts

This section defines the core concepts behind Multicloud Management to help you delve into how it works.

- Resource Template: Multicloud Management uses Kubernetes Native API definitions as united resource templates, making it easy to integrate with existing tools already adopted by Kubernetes.
- Propogation Policy (PP): Multicloud Management provides an independent propagation policy API to address multicluster scheduling and propagation requirements.
    - Mapping and workload support 1:n. Users do not need to specify scheduling constraints at each creation of a multicloud applications.
    - By using default policies, users can interact directly with the Kubernetes API.

- Override Policy (OP): Multicloud Management provides an independent Override Policy API, specifically for automatiically differentiating cluster-related configurations.
    - Cover image prefix based on member cluster regions.
    - Override StorageClass based on the cloud service provider.
