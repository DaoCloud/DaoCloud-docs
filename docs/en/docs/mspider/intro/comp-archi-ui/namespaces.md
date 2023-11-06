---
hide:
  - toc
---

# System Namespaces

DCE 5.0 Service Mesh comes with several system namespaces.
Please refrain from deploying business applications and services to these namespaces.
The namespaces and their purposes are described below.

| Category             | Namespace          | Purpose                        |
| -------------------- | ------------------ | ----------------------------- |
| Istio System Namespace | istio-system       | Hosts Istio control plane components and resources |
|                      | istio-operator     | Deploys and manages Istio Operator |
| K8s System Namespace   | kube-system        | Control plane components      |
|                      | kube-public        | Cluster configurations, certificates, etc. |
|                      | kube-node-lease    | Monitors and maintains node activity |
| DCE 5.0 System Namespace | amamba-system      | Workbench         |
|                      | ghippo-system      | Global management             |
|                      | insight-system     | Observability                 |
|                      | ipavo-system       | Homepage dashboard            |
|                      | kairship-system    | Multicloud orchestration       |
|                      | kant-system        | Cloud-edge collaboration       |
|                      | kangaroo-system    | Container registry              |
|                      | kcoral-system      | Application backup             |
|                      | kubean-system      | Cluster lifecycle management  |
|                      | kpanda-system      | Container management          |
|                      | local-path-storage | Local storage                 |
|                      | mcamel-system      | Middleware                    |
|                      | mspider-system     | Service mesh                  |
|                      | skoala-system      | Microservice engine            |
|                      | spidernet-system   | Network module                |