---
MTPE: windsonsea
date: 2023-03-06
hide:
  - navigation
---

# DCE 5.0 Enterprise with Installer v0.5.0

This page allows you to download the offline package and checksum file of DCE 5.0 Enterprise.

[Return to Download Index](../index.md#download-enterprise-package){ .md-button }
[Legacy Packages](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| -------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.5.0-amd64.tar | v0.5.0 | AMD 64 | 15.86 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.5.0-amd64.tar) | 2023-03-06 |
| offline-v0.5.0-arm64.tar | v0.5.0 | <font color="green">ARM 64</font> | 14.56 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.5.0-arm64.tar) | 2023-03-06 |

## Verification

Go to the download directory of the offline package.

=== "AMD 64"

     run the following command to verify the offline package:

     ```sh
     echo "83f0bc6522eb525bc8d3c2478cf68235972d583171a1e471d45f338d1acde6f66a5ed68144bfd6a067b2462a1c27e17d95c13408b8cbd83fd93d1dbe1527 79a3 offline-v0.5.0-amd64.tar" | sha512sum -c
     ```

     If the verification is successful, it will print:

     ```none
     offline-v0.5.0-amd64.tar: OK
     ```

=== "<font color="green">ARM 64</font>"

     run the following command to verify the offline package:

     ```sh
     echo "ca857e62f67fba0c734a3e51658cf0900311db116dfb2dc82ed54cc8b8387ad0e3d53e95a0df06e913cf62038858d585593990587bdf802790e2fa6050759ec 2 offline-v0.5.0-arm64.tar" | sha512sum -c
     ```

     If the verification is successful, it will print:

     ```none
     offline-v0.5.0-arm64.tar: OK
     ```

## Installation

After the offline package has been successfully verifyd,

=== "AMD 64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-v0.5.0-amd64.tar
     ```

=== "<font color="green">ARM 64</font>"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-v0.5.0-arm64.tar
     ```

- For installation, refer to [DCE 5.0 Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, please contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

The DCE 5.0 Enterprise includes the following modules, which are plug-and-play to meet various use cases:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, and custom appearance. | [0.14.0](../../ghippo/intro/release-notes.md#v0140) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [0.15.1](../../kpanda/intro/release-notes.md#v0150) |
| Insight | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [0.14.6](../../insight/intro/release-notes.md#v0146) |
| Workbench | A container-based DevOps application platform that supports pipeline operations such as Jenkins, Tekton, GitOps, etc. | [0.14.4](../../amamba/intro/release-notes.md#v0140) |
| Multicloud Management| Centralized management of application orchestration of multicloud, hybrid cloud, and cross-cloud resources, with multicloud disaster recovery and fault recovery capabilities| [0.6.2](../../kairship/intro/release-notes.md#v063) |
| Microservice Engine | Provide registration discovery, service governance, configuration management, microservice gateway and other governance capabilities | [0.18.0](../../skoala/intro/release-notes.md#v0180) |
| Service Mesh | A next-generation service mesh for cloud native applications based on Istio open source technology | [v0.13.1](../../mspider/intro/release-notes.md#v0131) |
| Middleware Elasticsearch | Currently preferred full-text search engine | [0.5.0](../../middleware/elasticsearch/release-notes.md#v050) |
| Middleware Kafka | Distributed message queue service based on the open source software Kafka | [0.3.0](../../middleware/kafka/release-notes.md#v030) |
| Middleware MinIO | A very popular lightweight, open source object storage solution | [0.3.0](../../middleware/minio/release-notes.md#v030) |
| Middleware MySQL | The most widely used open source relational database | [0.6.0](../../middleware/mysql/release-notes.md#v060) |
| Middleware RabbitMQ | Open source message broker software implementing the Advanced Message Queuing Protocol (AMQP) | [0.8.0](../../middleware/rabbitmq/release-notes.md#v080) |
| Middleware Redis | An in-memory database caching service | [0.5.0](../../middleware/redis/release-notes.md#v050) |
| Container registry | Used to store images for K8s, DevOps and container application development | [0.5.2](../../kangaroo/intro/release-notes.md#v050) |
| Network | Support multiple CNI combinations for different Linux kernels | [0.4.4](../../network/intro/release-notes.md#v044) |
| Storage | Provide unified data storage services, support files, objects, blocks, and local storage, and easily access storage vendor solutions | [v0.8.0](../../storage/hwameistor/release-notes.md) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)