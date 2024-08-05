---
MTPE: windsonsea
Date: 2024-08-05
hide:
  - toc
---

# System Namespaces

DCE 5.0 Service Mesh comes with several system namespaces.
Please refrain from deploying business applications and services to these namespaces.
The namespaces and their purposes are described below.

| Category                 | Namespace          | Purpose                                            |
| ------------------------ | ------------------ | -------------------------------------------------- |
| Istio System Namespace   | istio-system       | Hosts Istio control plane components and resources |
|                          | istio-operator     | Deploys and manages Istio Operator                 |
| K8s System Namespace     | kube-system        | Control plane components                           |
|                          | kube-public        | Cluster configurations and certificates            |
|                          | kube-node-lease    | Monitors and maintains node activity               |
| DCE 5.0 System Namespace | amamba-system      | Workbench                                          |
|                          | ghippo-system      | Global management                                  |
|                          | insight-system     | Insight                                            |
|                          | ipavo-system       | Homepage dashboard                                 |
|                          | kairship-system    | MultiCloud Management                              |
|                          | kant-system        | Cloud Edge Collaboration                           |
|                          | kangaroo-system    | Container Registry                                 |
|                          | kcoral-system      | Application Backup                                 |
|                          | kubean-system      | Cluster Lifecycle Management (Kubean)              |
|                          | kpanda-system      | Container Management                               |
|                          | local-path-storage | Local storage                                      |
|                          | mcamel-system      | Middleware                                         |
|                          | mspider-system     | Service Mesh                                       |
|                          | skoala-system      | Microservice Engine                                |
|                          | spidernet-system   | Network module                                     |
|                          | virtnest-system    | Virtual machine                                    |
|                          | baize-system       | Intelligent Engine                                 |
