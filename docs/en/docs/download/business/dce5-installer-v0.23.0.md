---
MTPE: windsonsea
date: 2024-12-02
hide:
  - navigation
---

# DCE 5.0 Enterprise with Installer v0.23.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Enterprise.

[Return to Download Guide](../index.md#download-dce-50-enterprise){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.23.0-amd64.tar | v0.23.0 | AMD 64 | 33.70GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.23.0-amd64.tar) | 2024-11-11 |
| offline-v0.23.0-arm64.tar | v0.23.0 | <font color="green">ARM 64</font> | 29.80GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.23.0-arm64.tar) | 2024-11-11 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "73406d404b7bfc3e3362bdb41477625d563b1b1528d796968944c2037e94e2197fbe0edd6192aacbf9fe91121ab199ecb75d11db8bed900abcc982d13a908612  offline-v0.23.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.23.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "fec2d86eb5ba4e6049b16bea1c4d55ef286ab9e9b35b5d3232c5bfa11e85773de25c4cb18ce76e6d17be60703c403119cbedc5b535940c1cc3ce20af1d81b739  offline-v0.23.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.23.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.23.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.23.0-arm64.tar
    ```

- For installation instructions, refer to [Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

DCE 5.0 Enterprise includes the following modules, which can be used on-demand to meet various application scenarios:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, and custom appearance. | [0.32.0](../../ghippo/intro/release-notes.md#v0320) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and more Kubernetes features. | [0.33.2](../../kpanda/intro/release-notes.md#v0332) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alert information. | [0.32.2](../../insight/intro/release-notes.md#v0322) |
| Workbench | A container-based DevOps application platform that supports Jenkins, Tekton, GitOps, and other pipeline jobs. | [0.32.0](../../amamba/intro/release-notes.md#v0320) |
| MultiCloud Management | Centralized management of multicloud, hybrid cloud, and cross-cloud resources for application orchestration, with capabilities such as multicloud disaster recovery and fault recovery. | [0.24.0](../../kairship/intro/release-notes.md#v0240) |
| Microservice Engine | Provides governance capabilities such as service registration, discovery, configuration management, and microservice gateway. | [0.42.1](../../skoala/intro/release-notes.md#v0421) |
| Service Mesh | Next-generation service mesh built on Istio open-source technology for cloud-native applications. | [v0.31.0](../../mspider/intro/release-notes.md#v0310) |
| Middleware Elasticsearch | Currently the preferred full-text search engine. | [0.22.0](../../middleware/elasticsearch/release-notes.md#v0220) |
| Middleware Kafka | Distributed message queue service based on the open-source software Kafka. | [0.20.0](../../middleware/kafka/release-notes.md#v0200) |
| Middleware MinIO | A lightweight, open-source object storage solution that is very popular. | [0.20.0](../../middleware/minio/release-notes.md#v0200) |
| Middleware MySQL | The most widely used open-source relational database. | [0.23.0](../../middleware/mysql/release-notes.md#v0230) |
| Middleware RabbitMQ | Open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). | [0.25.0](../../middleware/rabbitmq/release-notes.md#v0250) |
| Middleware Redis | An in-memory database caching service. | [0.23.0](../../middleware/redis/release-notes.md#v0230) |
| Container Regisry | Used to store images for K8s, DevOps, and container application development. | [0.23.0](../../kangaroo/intro/release-notes.md#v0230) |
| Networking | Supports multiple CNI combination solutions for different Linux kernels. | [0.16.1](../../network/intro/release-notes.md#v0161) |
| Storage | Provides unified data storage services, supporting file, object, block, and local storage, easily integrating with storage vendor solutions. | [v0.16.0](../../storage/hwameistor/release-notes.md#v0160) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
