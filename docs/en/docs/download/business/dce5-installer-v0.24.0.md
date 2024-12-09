---
MTPE: windsonsea
date: 2024-12-09
hide:
  - navigation
---

# DCE 5.0 Enterprise with Installer v0.24.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Enterprise.

[Return to Download Guide](../index.md#download-dce-50-enterprise){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.24.0-amd64.tar | v0.24.0 | AMD 64 | 32.73 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.24.0-amd64.tar) | 2024-12-09 |
| offline-v0.24.0-arm64.tar | v0.24.0 | <font color="green">ARM 64</font> | 28.93 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.24.0-arm64.tar) | 2024-12-09 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "5f08a51c93d105582db16cc7427ef61634441079a2aff5372312931233ca5335313dbf0c51d4aab04c2c585a1f01511ee94b0c939a472981357a0af303e4dad7  offline-v0.24.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.24.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "a46695726de2a7f1353f4fd23aa9bbdb80ae508d8290ed503ad614d2e44b5684cfc3e0f457768dad40dbe5b1aa33510c2b783cb9a73c82e4a69f9b35e3160e18  offline-v0.24.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.24.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.24.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.24.0-arm64.tar
    ```

- For installation instructions, refer to [Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

DCE 5.0 Enterprise includes the following modules, which can be used on-demand to meet various application scenarios:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, and custom appearance. | [0.33.0](../../ghippo/intro/release-notes.md#v0330) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and more Kubernetes features. | [0.34.0](../../kpanda/intro/release-notes.md#v0340) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alert information. | [0.33.1](../../insight/intro/release-notes.md#v0331) |
| Workbench | A container-based DevOps application platform that supports Jenkins, Tekton, GitOps, and other pipeline jobs. | [0.33.0](../../amamba/intro/release-notes.md#v0330) |
| MultiCloud Management | Centralized management of multicloud, hybrid cloud, and cross-cloud resources for application orchestration, with capabilities such as multicloud disaster recovery and fault recovery. | [0.24.0](../../kairship/intro/release-notes.md#v0240) |
| Microservice Engine | Provides governance capabilities such as service registration, discovery, configuration management, and microservice gateway. | [0.43.2](../../skoala/intro/release-notes.md#v0432) |
| Service Mesh | Next-generation service mesh built on Istio open-source technology for cloud-native applications. | [v0.32.0](../../mspider/intro/release-notes.md#v0320) |
| Middleware Elasticsearch | Currently the preferred full-text search engine. | [0.23.0](../../middleware/elasticsearch/release-notes.md#v0230) |
| Middleware Kafka | Distributed message queue service based on the open-source software Kafka. | [0.21.0](../../middleware/kafka/release-notes.md#v0210) |
| Middleware MinIO | A lightweight, open-source object storage solution that is very popular. | [0.21.0](../../middleware/minio/release-notes.md#v0210) |
| Middleware MySQL | The most widely used open-source relational database. | [0.24.0](../../middleware/mysql/release-notes.md#v0240) |
| Middleware RabbitMQ | Open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). | [0.26.0](../../middleware/rabbitmq/release-notes.md#v0260) |
| Middleware Redis | An in-memory database caching service. | [0.24.0](../../middleware/redis/release-notes.md#v0240) |
| Container Regisry | Used to store images for K8s, DevOps, and container application development. | [0.24.0](../../kangaroo/intro/release-notes.md#v0240) |
| Networking | Supports multiple CNI combination solutions for different Linux kernels. | [0.16.2](../../network/intro/release-notes.md#v0162) |
| Storage | Provides unified data storage services, supporting file, object, block, and local storage, easily integrating with storage vendor solutions. | [v0.16.1](../../storage/hwameistor/release-notes.md#v0161) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
