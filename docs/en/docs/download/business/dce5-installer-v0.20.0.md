---
MTPE: windsonsea
date: 2024-08-14
hide:
  - navigation
---

# DCE 5.0 Enterprise with Installer v0.20.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Enterprise.

[Return to Download Guide](../index.md#download-dce-50-enterprise){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.20.0-amd64.tar | v0.20.0 | AMD 64 | 27.04 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.20.0-amd64.tar) | 2024-08-09 |
| offline-v0.20.0-arm64.tar | v0.20.0 | <font color="green">ARM 64</font> | 23.80 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.20.0-arm64.tar) | 2024-08-09 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "5951220033c7d2a397d1875dac12d48f1ddf7f1ef617322a0a4300948d1d4adbaa4b9f37dd987e5295aaeb9e025ad679e5028c6e6d853733a39dc79155ad1e91  offline-v0.20.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.20.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "4db2e04016a4329ceae802827cf2f5b975b9277651115b5b4a36a10ee33cbbd644c4b2d3ad4debcb15bce079e8a123791144da0221f7680c91cd025c715e89b7  offline-v0.20.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.20.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.20.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.20.0-arm64.tar
    ```

- For installation instructions, refer to [Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

DCE 5.0 Enterprise includes the following modules, which can be used on-demand to meet various application scenarios:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, and custom appearance. | [0.29.0](../../ghippo/intro/release-notes.md#v0290) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and more Kubernetes features. | [0.30.1](../../kpanda/intro/release-notes.md#v0300) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alert information. | [0.29.0](../../insight/intro/release-notes.md#v0290) |
| Workbench | A container-based DevOps application platform that supports Jenkins, Tekton, GitOps, and other pipeline jobs. | [0.29.1](../../amamba/intro/release-notes.md#v0290) |
| MultiCloud Management | Centralized management of multicloud, hybrid cloud, and cross-cloud resources for application orchestration, with capabilities such as multicloud disaster recovery and fault recovery. | [0.21.1](../../kairship/intro/release-notes.md#v0210) |
| Microservice Engine | Provides governance capabilities such as service registration, discovery, configuration management, and microservice gateway. | [0.39.2](../../skoala/intro/release-notes.md#v0392) |
| Service Mesh | Next-generation service mesh built on Istio open-source technology for cloud-native applications. | [v0.28.0](../../mspider/intro/release-notes.md#v0280) |
| Middleware Elasticsearch | Currently the preferred full-text search engine. | [0.19.0](../../middleware/elasticsearch/release-notes.md#v0190) |
| Middleware Kafka | Distributed message queue service based on the open-source software Kafka. | [0.17.0](../../middleware/kafka/release-notes.md#v0180) |
| Middleware MinIO | A lightweight, open-source object storage solution that is very popular. | [0.17.0](../../middleware/minio/release-notes.md#v0170) |
| Middleware MySQL | The most widely used open-source relational database. | [0.20.0](../../middleware/mysql/release-notes.md#v0210) |
| Middleware RabbitMQ | Open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). | [0.22.0](../../middleware/rabbitmq/release-notes.md#v0230) |
| Middleware Redis | An in-memory database caching service. | [0.20.0](../../middleware/redis/release-notes.md#v0200) |
| Container Regisry | Used to store images for K8s, DevOps, and container application development. | [0.20.0](../../kangaroo/intro/release-notes.md#v0200) |
| Networking | Supports multiple CNI combination solutions for different Linux kernels. | [0.15.1](../../network/intro/release-notes.md#v0151) |
| Storage | Provides unified data storage services, supporting file, object, block, and local storage, easily integrating with storage vendor solutions. | [v0.14.8](../../storage/hwameistor/release-notes.md#v0148) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
