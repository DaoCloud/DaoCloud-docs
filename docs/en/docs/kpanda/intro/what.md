---
hide:
  - toc
---

# What is container management?

Container management is a cloud-native application-oriented container management platform built on the basis of Kubernetes open-source technology. Based on the native multi-cluster architecture, it decouples the underlying infrastructure platform, realizes unified management of multi-cloud and multi-cluster, simplifies the process of enterprise applications to the cloud, and reduces operational costs. Dimension management and labor costs. Create Kubernetes clusters conveniently, helping enterprises quickly build enterprise-level container cloud platforms. The main functions of the container management module are as follows:

**Cluster Management**

- Unified management of clusters, which supports any Kubernetes cluster within a specific version range to be included in the scope of container management, and realizes unified management of on-cloud, off-cloud, multi-cloud, and hybrid cloud container cloud platforms.
- Rapid deployment of clusters, based on DaoCloud's independent open source project [Kubean](https://github.com/kubean-io/kubean), supports rapid deployment of enterprise-level Kubernetes clusters through the Web UI interface, and quickly builds enterprise-level container cloud platforms, Adapt to the underlying environment of physical machines and virtual machines.
- One-click cluster upgrade, one-click upgrade of Kubernetes version, unified management system component upgrade.
- The cluster is highly available, with built-in cluster disaster recovery and backup capabilities, ensuring that the business system can be restored in the event of host failure, computer room interruption, natural disasters, etc., improving the stability of the production environment and reducing the risk of business interruption.
- Full lifecycle management of clusters, realizing full lifecycle management of self-built cloud native clusters.
- Open API capability, providing native Kubernetes OpenAPI capability.

**Application Management**

- One-stop deployment, decoupling the underlying Kubernetes platform, one-stop deployment and operation and maintenance of business applications, and realizing the full life cycle management of applications.
- Elastic scaling of application load, supports manual/automatic scaling of application load, supports horizontal scaling, vertical scaling, and scheduled scaling, and calmly handles traffic peaks.
- The full life cycle of the application, supporting full life cycle management such as application viewing, updating, deletion, rollback, event viewing, and upgrading.
- Unified management capability across cluster loads.

**Strategy Management**

Supports formulation of network policies, quota policies, resource limit policies, disaster recovery policies, and security policies at the namespace or cluster granularity.

- Network policy, supports the formulation of network policies at the granularity of namespace or cluster, and limits the communication rules between pods and network "entities" on the network plane.
- Quota policy, which supports setting quota policies at namespace or cluster granularity to limit the resource usage of namespaces in the cluster.
- Resource limit policy, which supports setting resource limit policies at namespace or cluster granularity, and constrains the use of resources by applications in the corresponding namespace.
- Disaster recovery strategy, supports the setting of disaster recovery strategy at the granularity of namespace or cluster, realizes disaster recovery backup with namespace as the dimension, and ensures the security of the cluster.
- Security policy, which supports setting security policies at namespace or cluster granularity, and defines different isolation levels for Pods.

**Product logical architecture**



[Download DCE 5.0](../../download/dce5.md){ .md-button .md-button--primary }
[Install DCE 5.0](../../install/intro.md){ .md-button .md-button--primary }
[Free Trial Now](../../dce/license0.md){ .md-button .md-button--primary }