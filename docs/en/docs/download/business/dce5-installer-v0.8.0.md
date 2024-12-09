---
MTPE: windsonsea
date: 2023-06-06
hide:
  - navigation
---

# DCE 5.0 Enterprise with Installer v0.8.0

This page provides offline packages and checksum files for DCE 5.0 Enterprise.

[Return to Download Index](../index.md#download-enterprise-package){ .md-button }
[Legacy Packages](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| -------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.8.0-amd64.tar | v0.8.0 | AMD 64 | 18.43 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.8.0-amd64.tar) | 2023-06-06 |
| offline-v0.8.0-arm64.tar | v0.8.0 | <font color="green">ARM 64</font> | 16.99 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.8.0-arm64.tar) | 2023-06-06 |

## Verification

Enter the directory where the offline package is downloaded.

=== "AMD 64"

    Run the following command to verify the offline package:

    ```sh
    echo "fbd3e646f5849406db1c221ab6956afd0e3dfd76e75394dfaeec06d2f2ec74934801cd7118c4bf2f51a3610dcb69fd7a010c613fcda3339abd20a1630029723e  offline-v0.8.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, it will print:

    ```none
    offline-v0.8.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the offline package:

    ```sh
    echo "f2854f0a90c2db16b9c206708b140069a953b68a575ce59b1dc656f84cb47c42647697067582e28e16175f4bfbcfcdb6c14d79c3d999c7646f1c58c40f1b35cc  offline-v0.8.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, it will print:

    ```none
    offline-v0.8.0-arm64.tar: OK
    ```

## Installation

After the offline package is verifyd,

=== "AMD 64"

    Run the following command to unpack the tar package:

    ```sh
    tar -zxvf offline-v0.8.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to unpack the tar package:

    ```sh
    tar -zxvf offline-v0.8.0-arm64.tar
    ```

- For installation, refer to [DCE 5.0 Enterprise Installation Process](../../install/commercial/start-install.md).
- After successful installation, please contact us for authorization by email info@daocloud.io or call 400 002 6898.

## Modules

DCE 5.0 Enterprise includes the following modules, which can be used on demand to meet various use cases:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, and custom appearance. | [0.17.1](../../ghippo/intro/release-notes.md#v0171) |
| Container Management | Manage Kubernetes core features such as clusters, nodes, workloads, Helm applications, CRD, namespaces, etc. | [0.18.1](../../kpanda/intro/release-notes.md#v0181) |
| Insight | Provide rich dashboard, scenario monitoring, data query, alert and other graphical information. | [0.17.2](../../insight/intro/release-notes.md#v0170) |
| Workbench| Container-based DevOps application platform, supporting pipeline jobs such as Jenkins, Tekton, GitOps, etc. | [0.17.3](../../amamba/intro/release-notes.md#v0173) |
| Multicloud MOrchestration| Centralized management of multicloud, hybrid cloud, cross-cloud resources' application orchestration, with multicloud disaster recovery, fault recovery and other capabilities.| [0.9.1](../../kairship/intro/release-notes.md#v091) |
| Microservice Engine | Provide governance capabilities such as registration and discovery, service governance, configuration management, microservice gateway, etc. | [0.22.2](../../skoala/intro/release-notes.md#v0222) |
| Service Mesh | The next-generation service mesh for cloud native applications based on open-source technology Istio. | [v0.16.2](../../mspider/intro/release-notes.md#v0162) |
| Middleware: Elasticsearch | Currently the preferred full-text search engine. | [0.8.0](../../middleware/elasticsearch/release-notes.md#v080) |
| Middleware: Kafka | Distributed message queue service based on open-source software Kafka. | [0.6.0](../../middleware/kafka/release-notes.md#v0100) |
| Middleware: MinIO | A very popular lightweight, open-source object storage solution. | [0.6.0](../../middleware/minio/release-notes.md#v0100) |
| Middleware: MySQL | The most widely used open-source relational database. | [0.9.0](../../middleware/mysql/release-notes.md#v090) |
| Middleware: RabbitMQ| Open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). | [0.11.0](../../middleware/rabbitmq/release-notes.md#v0110) |
| Middleware: Redis | An in-memory database caching service. | [0.8.0](../../middleware/redis/release-notes.md#v080) |
| Container Registry | Used to store images for K8s, DevOps, and container application development. | [0.8.1](../../kangaroo/intro/release-notes.md#v080) |
| Network | Supports multiple CNI combinations for different Linux kernels. | [0.7.0](../../network/intro/release-notes.md#v070) |
| Storage | Provides unified data storage services, supporting file, object, block, local storage, and easy access to storage vendor solutions. | [v0.10.2](../../storage/hwameistor/release-notes.md#v0102) |

## More

- [Online documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
