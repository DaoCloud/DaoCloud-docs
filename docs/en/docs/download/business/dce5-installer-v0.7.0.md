---
date: 2023-05-09
hide:
  - navigation
---

# DCE 5.0 Enterprise v0.7.0

This page allows you to download the offline package and checksum file of DCE 5.0 Enterprise.

[Return to Download Index](../index.md#download-enterprise-package){ .md-button }
[More Historical Versions](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| -------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.7.0-amd64.tar | v0.7.0 | AMD64 | 17.29GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.7.0-amd64.tar) | 2023-05-09 |
| offline-v0.7.0-arm64.tar | v0.7.0 | ARM64 | 15.89GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.7.0-arm64.tar) | 2023-05-09 |

## Validation

Go to the download directory of the offline package.

=== "AMD64"

     run the following command to validate the offline package:

     ```sh
     echo "d6d88a2274f75c952e079c8f0702d3bf6c2fae7d75771bd02e8539f2afd3933bdf153e5cb41237ce5285b04fd6fb6075389ea80f16713bdfbe620f86509e ee42 offline-v0.7.0-amd64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-v0.7.0-amd64.tar: OK
     ```

=== "ARM64"

     run the following command to validate the offline package:

     ```sh
     echo "b159b5c7b8c224eb76a532ea0a2f2c55143cb240a1b7aa2ea97ab6acf244ff8cc0e74a46150c4ffa8d79409950573067ff5f9f8841fecb2af36ed20c4ffc048d offline- v0.7.0-arm64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-v0.7.0-arm64.tar: OK
     ```

## Installation

After the offline package has been successfully validated,

=== "AMD64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-v0.7.0-amd64.tar
     ```

=== "ARM64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-v0.7.0-arm64.tar
     ```

- For installation, refer to [DCE 5.0 Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, please contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

The DCE 5.0 Enterprise includes the following modules, which are plug-and-play to meet various use cases:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, personalized appearance settings, etc. | [0.16.1](../../ghippo/intro/release-notes.md#0161) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [0.17.0](../../kpanda/intro/release-notes.md#0170) |
| Insight | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [0.16.1](../../insight/intro/releasenote.md#0161) |
| Workbench | A container-based DevOps application platform that supports pipeline operations such as Jenkins, Tekton, GitOps, etc. | [0.16.1](../../amamba/intro/release-notes.md#0161) |
| Multicloud Management| Centralized management of application orchestration of multicloud, hybrid cloud, and cross-cloud resources, with multicloud disaster recovery and fault recovery capabilities| [0.8.1](../../kairship/intro/release-notes.md# 081) |
| Microservice Engine | Provide registration discovery, service governance, configuration management, microservice gateway and other governance capabilities | [0.21.2](../../skoala/intro/release-notes.md#0212) |
| Service Mesh | A next-generation service mesh for cloud native applications based on Istio open source technology | [v0.15.1](../../mspider/intro/release-notes.md#v0151) |
| middleware Elasticsearch | current preferred full-text search engine | [0.7.2](../../middleware/elasticsearch/release-notes.md#072) |
| Middleware Kafka | Distributed message queue service based on the open source software Kafka | [0.5.2](../../middleware/kafka/release-notes.md#052) |
| Middleware MinIO | A very popular lightweight, open source object storage solution | [0.5.2](../../middleware/minio/release-notes.md#052) |
| Middleware MySQL | The most widely used open source relational database | [0.8.2](../../middleware/mysql/release-notes.md#082) |
| Middleware RabbitMQ | Open source message broker software implementing the Advanced Message Queuing Protocol (AMQP) | [0.10.2](../../middleware/rabbitmq/release-notes.md#0102) |
| Middleware Redis | An in-memory database caching service | [0.7.2](../../middleware/redis/release-notes.md#072) |
| Container registry | Used to store images for K8s, DevOps and container application development | [0.7.2](../../kangaroo/intro/release-notes.md) |
| Network | Support multiple CNI combinations for different Linux kernels | [0.6.0](../../network/modules/spiderpool/releasenotes.md) |
| Storage | Provide unified data storage services, support files, objects, blocks, and local storage, and easily access storage vendor solutions | [v0.9.3](../../storage/hwameistor/releasenotes.md) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)