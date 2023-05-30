# Deployment architecture

DCE 5.0 provides three deployment architectures: all-in-one, 4 nodes, and 7 nodes.

The following table describes the terms involved in the architecture:

| Name | introduction |
| ------------ | ------------------------------------ -------------------------------------------------- -------------------- |
| bootstrapping node | bootstrapping node is also called boostrap node, it installs and executes the deployment program, and runs the container registry and chart museum required by the platform. |
| Global Service Cluster | Used to deploy all components of DCE 5.0, and [Kubean](https://github.com/kubean-io/kubean), where Kubean is used to manage the life cycle of the cluster. |
| Work cluster | Support business applications and services (deploy the work cluster after successfully installing DCE) |
| DCE Componet | All components of DCE 5.0, including product modules such as global management, container management, observability, Workbench, Multicloud Management, container registry, microservice engine, service mesh, and middleware. |

## All-in-one

The all-in-one mode only requires one host, and it is only recommended for individual customers to use this mode to install DCE 5.0.
When using the all-in-one mode, it is recommended to install DCE 5.0 minimally, that is, add the `-z` parameter after the installation command.

![allinone](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/allinone.png)

## 4 node mode

The 4-node mode consists of 1 bootstrapping node and 3 master nodes of the cluster. It is only recommended to install DCE 5.0 in this mode for PoC or test environments.

![four](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/four.png)

## 7 node mode (1 + 6)

The 7-node mode consists of 1 bootstrapping node, 3 master nodes of the cluster, and 3 working nodes of the cluster, among which the working node is the exclusive node of the Elasticsearch component.
It is recommended that customers use this mode to install DCE 5.0 in the production environment.

![seven](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/seven.png)
