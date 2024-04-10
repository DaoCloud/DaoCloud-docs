---
MTPE: windsonsea
date: 2024-04-10
hide:
  - navigation
---

# DCE 5.0 Enterprise with Installer v0.16.1

This page provides downloads for the offline installation package and verification files for DCE 5.0 Enterprise.

[Return to Download Guide](../index.md#_2){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.16.1-amd64.tar | v0.16.1 | AMD 64 | 25.06 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.16.1-amd64.tar) | 2024-04-09 |
| offline-v0.16.1-arm64.tar | v0.16.1 | <font color="green">ARM 64</font> | 21.83 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.16.1-arm64.tar) | 2024-04-09 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "87494dc7ebb6bd07f91eb7de3c95cfd4984816482bbef9f3271d603a06f133d0c8d04983c197926560b1b32ae3d77673329514d9d7925705ad33bc9572de58a0  offline-v0.16.1-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.16.1-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "39e0ad9273bbc844f3b2769830a8001d5f5582ee9487ef62bbb7438fce94b1f794ad4186d345b42a2b2f5829ee70d29c6a0853dc3d8ece5b1818ee80db33b116  offline-v0.16.1-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.16.1-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.16.1-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.16.1-arm64.tar
    ```

- For installation instructions, refer to [Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

DCE 5.0 Enterprise includes the following modules, which can be used on-demand to meet various application scenarios:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, personalized appearance settings, etc. | [0.25.1](../../ghippo/intro/release-notes.md#v0251) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and other core Kubernetes functionalities. | [0.26.1](../../kpanda/intro/release-notes.md#v0261) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alarm information. | [0.25.3](../../insight/intro/releasenote.md#v0253) |
| Workbench | A container-based DevOps application platform that supports Jenkins, Tekton, GitOps, and other pipeline jobs. | [0.25.0](../../amamba/intro/release-notes.md#v0250) |
| MultiCloud Management | Centralized management of multi-cloud, hybrid cloud, and cross-cloud resources for application orchestration, with capabilities such as multi-cloud disaster recovery and fault recovery. | [0.17.0](../../kairship/intro/release-notes.md#v0170) |
| Microservice Engine | Provides governance capabilities such as service registration, discovery, configuration management, and microservice gateway. | [0.35.1](../../skoala/intro/release-notes.md#v0351) |
| Service Mesh | Next-generation service mesh built on Istio open-source technology for cloud-native applications. | [v0.24.1](../../mspider/intro/release-notes.md#v0241) |
| Middleware Elasticsearch | Currently the preferred full-text search engine. | [0.15.0](../../middleware/elasticsearch/release-notes.md#v0150) |
| Middleware Kafka | Distributed message queue service based on the open-source software Kafka. | [0.13.0](../../middleware/kafka/release-notes.md#v0130) |
| Middleware MinIO | A lightweight, open-source object storage solution that is very popular. | [0.13.0](../../middleware/minio/release-notes.md#v0130) |
| Middleware MySQL | The most widely used open-source relational database. | [0.16.0](../../middleware/mysql/release-notes.md#v0160) |
| Middleware RabbitMQ | Open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). | [0.18.0](../../middleware/rabbitmq/release-notes.md#v0180) |
| Middleware Redis | An in-memory database caching service. | [0.16.0](../../middleware/redis/release-notes.md#v0160) |
| Container Regisry | Used to store images for K8s, DevOps, and container application development. | [0.16.1](../../kangaroo/intro/release-notes.md#v0161) |
| Networking | Supports multiple CNI combination solutions for different Linux kernels. | [0.13.0](../../dce/dce-rn/20240130.md) |
| Storage | Provides unified data storage services, supporting file, object, block, and local storage, easily integrating with storage vendor solutions. | [v0.14.4](../../storage/hwameistor/releasenotes.md#v0144) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
