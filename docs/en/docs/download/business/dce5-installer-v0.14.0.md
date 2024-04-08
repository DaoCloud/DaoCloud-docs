---
MTPE: windsonsea
date: 2024-01-09
hide:
  - navigation
---

# DCE 5.0 Enterprise with Installer v0.14.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Enterprise.

[Return to Download Guide](../index.md#_2){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.14.0-amd64.tar | v0.14.0 | AMD 64 | 21.7 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.14.0-amd64.tar) | 2024-01-09 |
| offline-v0.14.0-arm64.tar | v0.14.0 | <font color="green">ARM 64</font> | 24.8 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.14.0-arm64.tar) | 2024-01-09 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "e59457614320c71f4327149236a3045a120f96ac3b74365109b04b88f4fa39dbce72239e6f3d8252843c86f7b1e86e1da6102c1efd596a8c034e5ae0075704d2  offline-v0.14.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.14.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "16789ec50ceb9c17aa0fae22cc5e1b7c9630616ccc0cd276d5b8aeb9c191fbe8fde7ac0380453f8ef404ee602f2f20fefbaaa15e081f1957e378df6c747d4181  offline-v0.14.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.14.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.14.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.14.0-arm64.tar
    ```

- For installation instructions, refer to [Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

DCE 5.0 Enterprise includes the following modules, which can be used on-demand to meet various application scenarios:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, personalized appearance settings, etc. | [0.23.0](../../ghippo/intro/release-notes.md#v0230) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and other core Kubernetes functionalities. | [0.24.1](../../kpanda/intro/release-notes.md#v0241) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alarm information. | [0.23.0](../../insight/intro/releasenote.md#v0230) |
| Workbench | A container-based DevOps application platform that supports Jenkins, Tekton, GitOps, and other pipeline jobs. | [0.23.0](../../amamba/intro/release-notes.md#v0230) |
| MultiCloud Management | Centralized management of multi-cloud, hybrid cloud, and cross-cloud resources for application orchestration, with capabilities such as multi-cloud disaster recovery and fault recovery. | [0.15.0](../../kairship/intro/release-notes.md#v0150) |
| Microservice Engine | Provides governance capabilities such as service registration, discovery, configuration management, and microservice gateway. | [0.31.2](../../skoala/intro/release-notes.md#v0312) |
| Service Mesh | Next-generation service mesh built on Istio open-source technology for cloud-native applications. | [v0.22.0](../../mspider/intro/release-notes.md#v0220) |
| Middleware Elasticsearch | Currently the preferred full-text search engine. | [0.13.0](../../middleware/elasticsearch/release-notes.md#v0130) |
| Middleware Kafka | Distributed message queue service based on the open-source software Kafka. | [0.11.0](../../middleware/kafka/release-notes.md#v0110) |
| Middleware MinIO | A lightweight, open-source object storage solution that is very popular. | [0.11.0](../../middleware/minio/release-notes.md#v0110) |
| Middleware MySQL | The most widely used open-source relational database. | [0.14.0](../../middleware/mysql/release-notes.md#v0140) |
| Middleware RabbitMQ | Open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). | [0.16.0](../../middleware/rabbitmq/release-notes.md#v0160) |
| Middleware Redis | An in-memory database caching service. | [0.14.0](../../middleware/redis/release-notes.md#v0140) |
| Container Regisry | Used to store images for K8s, DevOps, and container application development. | [0.14.0](../../kangaroo/intro/release-notes.md#v0140) |
| Networking | Supports multiple CNI combination solutions for different Linux kernels. | [0.12.1](../../dce/dce-rn/20231231.md) |
| Storage | Provides unified data storage services, supporting file, object, block, and local storage, easily integrating with storage vendor solutions. | [v0.14.0](../../dce/dce-rn/20231231.md) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
