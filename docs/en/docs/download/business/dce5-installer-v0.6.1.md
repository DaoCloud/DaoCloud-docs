---
MTPE: windsonsea
date: 2023-04-12
hide:
  - navigation
---

# DCE 5.0 Enterprise with Installer v0.6.1

This page allows you to download the offline package and checksum file of DCE 5.0 Enterprise.

[Return to Download Index](../index.md#download-enterprise-package){ .md-button }
[Legacy Packages](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| -------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.6.1-amd64.tar | v0.6.1 | AMD 64 | 16.37 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.6.1-amd64.tar) | 2023-04-12 |
| offline-v0.6.1-arm64.tar | v0.6.1 | <font color="green">ARM 64</font> | 15.15 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.6.1-arm64.tar) | 2023-04-12 |

## Verification

Go to the download directory of the offline package.

=== "AMD 64"

     run the following command to verify the offline package:

     ```sh
     echo "00a785ba2f3b2abe7f634410ae08b798771d2d9de27b7d39e9ed6a9d9eff0e04ea544478b04f75610190b7f46c33179711ac5be6ecd219ea4f407c38850d350c offline-v0.6.1-amd64.tar" | sha512sum -c
     ```

     If the verification is successful, it will print:

     ```none
     offline-v0.6.1-amd64.tar: OK
     ```

=== "<font color="green">ARM 64</font>"

     run the following command to verify the offline package:

     ```sh
     echo "1ebbd5fb7841d9e36e972ec6316cf43f62fe770401026fa07e9da58908f71b9ef9ae30c4b345efc60fb1a8ee3a6a2ba1f1e50b9858da223b56dca17a32548733 off line-v0.6.1-arm64.tar" | sha512sum -c
     ```

     If the verification is successful, it will print:

     ```none
     offline-v0.6.1-arm64.tar: OK
     ```

## Installation

After the offline package has been successfully verifyd,

=== "AMD 64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-v0.6.1-amd64.tar
     ```

=== "<font color="green">ARM 64</font>"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-v0.6.1-arm64.tar
     ```

- For installation, refer to [DCE 5.0 Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, please contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

The DCE 5.0 Enterprise includes the following modules, which are plug-and-play to meet various use cases:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, and custom appearance. | [0.15.0](../../ghippo/intro/release-notes.md#v0150) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [0.16.1](../../kpanda/intro/release-notes.md#v0160) |
| Insight | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [0.15.4](../../insight/intro/release-notes.md#v0154) |
| Workbench | A container-based DevOps application platform that supports pipeline operations such as Jenkins, Tekton, GitOps, etc. | [0.15.1](../../amamba/intro/release-notes.md#v0151) |
| Multicloud Management| Centralized management of application orchestration of multicloud, hybrid cloud, and cross-cloud resources, with multicloud disaster recovery and fault recovery capabilities| [0.7.4](../../kairship/intro/release-notes.md#v074) |
| Microservice Engine | Provide registration discovery, service governance, configuration management, microservice gateway and other governance capabilities | [0.19.4](../../skoala/intro/release-notes.md#v0194) |
| Service Mesh | A next-generation service mesh for cloud native applications based on Istio open source technology | [v0.14.3](../../mspider/intro/release-notes.md#v0143) |
| Middleware Elasticsearch | Currently preferred full-text search engine | [0.6.0](../../middleware/elasticsearch/release-notes.md#v060) |
| Middleware Kafka | Distributed message queue service based on the open source software Kafka | [0.4.0](../../middleware/kafka/release-notes.md#v040) |
| Middleware MinIO | A very popular lightweight, open source object storage solution | [0.4.1](../../middleware/minio/release-notes.md#v041) |
| Middleware MySQL | The most widely used open source relational database | [0.7.0](../../middleware/mysql/release-notes.md#v070) |
| Middleware RabbitMQ | Open source message broker software implementing the Advanced Message Queuing Protocol (AMQP) | [0.9.1](../../middleware/rabbitmq/release-notes.md#v091) |
| Middleware Redis | An in-memory database caching service | [0.6.2](../../middleware/redis/release-notes.md#v062) |
| Container registry | Used to store images for K8s, DevOps and container application development | [0.6.2](../../kangaroo/intro/release-notes.md#v062) |
| Network | Support multiple CNI combinations for different Linux kernels | [0.5.0](../../network/intro/release-notes.md#v050) |
| Storage | Provide unified data storage services, support files, objects, blocks, and local storage, and easily access storage vendor solutions | [v0.9.2](../../storage/hwameistor/release-notes.md#v092) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)