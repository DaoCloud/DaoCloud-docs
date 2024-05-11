---
MTPE: windsonsea
date: 2024-05-11
hide:
  - navigation
---

# DCE 5.0 Enterprise with Installer v0.17.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Enterprise.

[Return to Download Guide](../index.md#_2){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.17.0-amd64.tar | v0.17.0 | AMD 64 | 26.89 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.17.0-amd64.tar) | 2024-05-09 |
| offline-v0.17.0-arm64.tar | v0.17.0 | <font color="green">ARM 64</font> | 23.45 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.17.0-arm64.tar) | 2024-05-09 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "7bbe92a32e740811c75e9159c73a7736bf52ad4cd737555fe147ccfe8907759ddfb8e8bf43780702c568beb6fe5c651a1f1fc0a59f48044d049de3ef521b8b41  offline-v0.17.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.17.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "0f78091b373ca817a8ea6e41e6f028d3538c87e93e70653ebb9b019bbb25619ddbd72853ada5a8f186639c4e970132bab2b75cb53f52762bdaed9f55cee0f848  offline-v0.17.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.17.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.17.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.17.0-arm64.tar
    ```

- For installation instructions, refer to [Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

DCE 5.0 Enterprise includes the following modules, which can be used on-demand to meet various application scenarios:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, personalized appearance settings, etc. | [0.26.0](../../ghippo/intro/release-notes.md#v0260) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and other core Kubernetes functionalities. | [0.27.0](../../kpanda/intro/release-notes.md#v0270) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alarm information. | [0.26.0](../../insight/intro/releasenote.md#v0260) |
| Workbench | A container-based DevOps application platform that supports Jenkins, Tekton, GitOps, and other pipeline jobs. | [0.26.1](../../amamba/intro/release-notes.md#v0261) |
| MultiCloud Management | Centralized management of multi-cloud, hybrid cloud, and cross-cloud resources for application orchestration, with capabilities such as multi-cloud disaster recovery and fault recovery. | [0.18.0](../../kairship/intro/release-notes.md#v0180) |
| Microservice Engine | Provides governance capabilities such as service registration, discovery, configuration management, and microservice gateway. | [0.36.1](../../skoala/intro/release-notes.md#v0361) |
| Service Mesh | Next-generation service mesh built on Istio open-source technology for cloud-native applications. | [v0.25.0](../../mspider/intro/release-notes.md#v0250) |
| Middleware Elasticsearch | Currently the preferred full-text search engine. | [0.16.0](../../middleware/elasticsearch/release-notes.md#v0160) |
| Middleware Kafka | Distributed message queue service based on the open-source software Kafka. | [0.14.0](../../middleware/kafka/release-notes.md#v0140) |
| Middleware MinIO | A lightweight, open-source object storage solution that is very popular. | [0.14.0](../../middleware/minio/release-notes.md#v0140) |
| Middleware MySQL | The most widely used open-source relational database. | [0.17.1](../../middleware/mysql/release-notes.md#v0171) |
| Middleware RabbitMQ | Open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). | [0.19.0](../../middleware/rabbitmq/release-notes.md#v0190) |
| Middleware Redis | An in-memory database caching service. | [0.17.0](../../middleware/redis/release-notes.md#v0170) |
| Container Regisry | Used to store images for K8s, DevOps, and container application development. | [0.17.0](../../kangaroo/intro/release-notes.md#v0170) |
| Networking | Supports multiple CNI combination solutions for different Linux kernels. | [0.13.0](../../dce/dce-rn/20240130.md) |
| Storage | Provides unified data storage services, supporting file, object, block, and local storage, easily integrating with storage vendor solutions. | [v0.14.4](../../storage/hwameistor/releasenotes.md#v0144) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
