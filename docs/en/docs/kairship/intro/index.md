---
hide:
  - toc
---

# What is Multicloud Management?

Cloud computing has been developing in China for nearly 15 years, and with the maturity of technology, enterprise are not satisfied with simply moving their applications to the cloud. Instead, more complex multicloud requirements have emerged. The development process of cloud computing from single cloud to multicloud is illustrated below:

![evolution](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/what01.png)

At the early stage, enterprises simply migrated their applications to the cloud. However, now they want to select clouds and customize their own multicloud environment.

According to statistics, cloud solutions may be divided into five kinds, and the solutions with multiple clouds totally account for 84% market share:

| Cloud Solutions       | Market Share |
| ------------------------ | ------------ |
| multiple public clouds + multiple private clouds | 43% |
| multiple public clouds + one private cloud | 29% |
| one public cloud + multiple private clouds | 12% |
| one public cloud + one private cloud | 9% |
| one single public or private cloud | 7% |

As the table shows, multicloud has become the mainstream in the market. This also explains why DaoCloud crafted the Multicloud Management module in DCE 5.0.

MultiCloud Management is an application-centric platform for efficiently managing applications across
multiple clouds. It allows centralized management of multicloud and hybrid-cloud environments,
providing cross-cloud deployment, release, and operational components. Elastic scaling of
applications based on cluster resources supports global load balancing, and it provides
disaster recovery that fully addresses the disaster recovery problem for multicloud applications.

The control plane of MultiCloud Management is responsible for several vital functions. Firstly,
it handles multicloud instance lifecycle management utilizing the Karmada framework. Additionally,
it serves as a unified traffic entry point for multicloud products, supporting OpenAPI, Kairship UI,
and internal module GRPC calls [14]. It acts as a proxy for API requests to multicloud instances in
the native style of Karmada and aggregates cluster information, including monitoring, management, and
control within multicloud models. Furthermore, it facilitates the management and monitoring of
resources such as multicloud workloads and enables potential permission operations in the future.

MultiCloud Management distinguishes itself from its counterparts with exceptional competitiveness,
offering developers the ease of using multiple clouds effortlessly, just like a single Kubernetes
cluster. Rich scheduling actions enable efficient workload allocation to specific clusters based on
various criteria. The platform provides an out-of-the-box experience, combining a user-friendly UI
and high-performance features making it ideal for seamless production usage. Additionally, it
facilitates centralized application management across diverse clusters, Supporting numerous cloud
providers such as Huawei CCE, Microsoft Azure, Amazon EKS, SUSE Rancher, VMware Tanzu, Aliyun ACK,
and others. The solution ensures seamless integration with Kubernetes-native APIs, streamlining
application development and deployment workflows in single-cluster environments.

[Download DCE 5.0](../../download/index.md){ .md-button .md-button--primary }
[Install DCE 5.0](../../install/index.md){ .md-button .md-button--primary }
