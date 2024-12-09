---
MTPE: windsonsea
date: 2024-04-08
hide:
  - navigation
---

# DCE 5.0 Enterprise with Installer v0.16.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Enterprise.

[Return to Download Guide](../index.md#_2){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.16.0-amd64.tar | v0.16.0 | AMD 64 | 25.06 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.16.0-amd64.tar) | 2024-04-08 |
| offline-v0.16.0-arm64.tar | v0.16.0 | <font color="green">ARM 64</font> | 21.83 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.16.0-arm64.tar) | 2024-04-08 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "4c9b57e3c601e688c404abcb0b0e193df3bffb09b017c8608038011ec644afd2bd5403bc082949a15297c7e1e475ac36752e659fe4a4698ee56671dc3953442d  offline-v0.16.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.16.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "1db1cb58350754549d47933546bc7e00871f9973a9e3ece4d027fdc947ffeffe762294eef11fbcb3cf87d5f63cab485b5a87d227b129f85e93d687280e3b20c3  offline-v0.16.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.16.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.16.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.16.0-arm64.tar
    ```

- For installation instructions, refer to [Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

DCE 5.0 Enterprise includes the following modules, which can be used on-demand to meet various application scenarios:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, and custom appearance. | [0.25.1](../../ghippo/intro/release-notes.md#v0251) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and more Kubernetes features. | [0.26.1](../../kpanda/intro/release-notes.md#v0261) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alert information. | [0.25.3](../../insight/intro/release-notes.md#v0250) |
| Workbench | A container-based DevOps application platform that supports Jenkins, Tekton, GitOps, and other pipeline jobs. | [0.25.0](../../amamba/intro/release-notes.md#v0250) |
| MultiCloud Management | Centralized management of multicloud, hybrid cloud, and cross-cloud resources for application orchestration, with capabilities such as multicloud disaster recovery and fault recovery. | [0.17.0](../../kairship/intro/release-notes.md#v0170) |
| Microservice Engine | Provides governance capabilities such as service registration, discovery, configuration management, and microservice gateway. | [0.35.1](../../skoala/intro/release-notes.md#v0351) |
| Service Mesh | Next-generation service mesh built on Istio open-source technology for cloud-native applications. | [v0.24.1](../../mspider/intro/release-notes.md#v0241) |
| Middleware Elasticsearch | Currently the preferred full-text search engine. | [0.15.0](../../middleware/elasticsearch/release-notes.md#v0150) |
| Middleware Kafka | Distributed message queue service based on the open-source software Kafka. | [0.13.0](../../middleware/kafka/release-notes.md#v0130) |
| Middleware MinIO | A lightweight, open-source object storage solution that is very popular. | [0.13.0](../../middleware/minio/release-notes.md#v0130) |
| Middleware MySQL | The most widely used open-source relational database. | [0.16.0](../../middleware/mysql/release-notes.md#v0160) |
| Middleware RabbitMQ | Open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). | [0.18.0](../../middleware/rabbitmq/release-notes.md#v0180) |
| Middleware Redis | An in-memory database caching service. | [0.16.0](../../middleware/redis/release-notes.md#v0160) |
| Container Regisry | Used to store images for K8s, DevOps, and container application development. | [0.16.1](../../kangaroo/intro/release-notes.md#v0161) |
| Networking | Supports multiple CNI combination solutions for different Linux kernels. | [0.13.0](../../network/intro/release-notes.md#v0130) |
| Storage | Provides unified data storage services, supporting file, object, block, and local storage, easily integrating with storage vendor solutions. | [v0.14.4](../../storage/hwameistor/release-notes.md#v0144) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
