---
MTPE: windsonsea
date: 2024-05-11
---

# Deployment Architecture

DaoCloud offers three deployment architectures: [beginner mode](#beginner-mode), [4-nodes](#4-node-mode), and [7-nodes](#7-node-mode-1--6).

The following table provides an overview of the terms used in the architecture:

| Name | Description  |
| ---- | ------------ |
| Bootstrap Node | The bootstrapping node, also known as the bootstrap node, installs and executes the deployment program. It runs the container registry and chart museum required by the platform. |
| Global Service Cluster| This cluster is responsible for deploying all components and utilizes [Kubean](https://github.com/kubean-io/kubean) to manage the cluster's lifecycle. |
| Workload Cluster | The workload cluster supports business applications and services. It should be deployed after successfully installing the product. |
| Product Component Module | All component modules, including global management, container management, observability, service mesh, and other product modules that vary by product edition. |

## Beginner Mode

The beginner mode is suitable for individual customers and requires only one host. However,
it is recommended to install the product in minimal mode by adding the `-z` parameter after the installation command.

![Beginner Mode Diagram](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/allinone.png)

## 4-Node Mode

The 4-node mode consists of one bootstrapping node and three master nodes within the cluster. It is recommended for PoC or test environments.

![4-Node Mode Diagram](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/four.png)

## 7-Node Mode (1 + 6)

The 7-node mode includes one bootstrapping node, three master nodes within the cluster, and three worker nodes exclusively dedicated to the Elasticsearch component. This mode is recommended for production environments.

![7-Node Mode Diagram](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/seven.png)
