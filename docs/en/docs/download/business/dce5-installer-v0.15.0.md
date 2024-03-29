---
MTPE: windsonsea
date: 2024-02-19
hide:
  - navigation
---

# DCE 5.0 Enterprise v0.15.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Enterprise.

[Return to Download Guide](../index.md#_2){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.15.0-amd64.tar | v0.15.0 | AMD 64 | 21.7 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.15.0-amd64.tar) | 2024-01-09 |
| offline-v0.15.0-arm64.tar | v0.15.0 | <font color="green">ARM 64</font> | 24.8 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.15.0-arm64.tar) | 2024-01-09 |

## Verification

Go to the offline installation package download directory.

=== "AMD64"

    Run the following command to verify the installation package:

    ```sh
    echo "a397805def3a1a4fe73c77937d930b978b3fc3d8b618e3aec22ba52ba9c4a8237b57824fbb9592702a94cc1ce994def990e02562c67e1235382ff117d17f8e99  offline-v0.15.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.15.0-amd64.tar: OK
    ```

=== "ARM64"

    Run the following command to verify the installation package:

    ```sh
    echo "ad3d7482d9616953800da1d5b19b0b86b063560a1a691a83d431731516a3a058221babd4d47e8e258704e459c2f1f384cd60231906ed7b71580910f1b82b41a0  offline-v0.15.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.15.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.15.0-amd64.tar
    ```

=== "ARM64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.15.0-arm64.tar
    ```

- For installation instructions, refer to [Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

DCE 5.0 Enterprise includes the following modules, which can be used on-demand to meet various application scenarios:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, personalized appearance settings, etc. | [0.24.0](../../ghippo/intro/release-notes.md#v0240) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and other core Kubernetes functionalities. | [0.25.1](../../kpanda/intro/release-notes.md#v0251) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alarm information. | [0.24.0](../../insight/intro/releasenote.md#v0240) |
| Workbench | A container-based DevOps application platform that supports Jenkins, Tekton, GitOps, and other pipeline jobs. | [0.24.0](../../amamba/intro/release-notes.md#v0240) |
| MultiCloud Management | Centralized management of multi-cloud, hybrid cloud, and cross-cloud resources for application orchestration, with capabilities such as multi-cloud disaster recovery and fault recovery. | [0.16.0](../../kairship/intro/release-notes.md#v0160) |
| Microservice Engine | Provides governance capabilities such as service registration, discovery, configuration management, and microservice gateway. | [0.33.2](../../skoala/intro/release-notes.md#v0332) |
| Service Mesh | Next-generation service mesh built on Istio open-source technology for cloud-native applications. | [v0.23.0](../../mspider/intro/release-notes.md#v0230) |
| Middleware Elasticsearch | Currently the preferred full-text search engine. | [0.14.0](../../middleware/elasticsearch/release-notes.md#v0140) |
| Middleware Kafka | Distributed message queue service based on the open-source software Kafka. | [0.12.0](../../middleware/kafka/release-notes.md#v0120) |
| Middleware MinIO | A lightweight, open-source object storage solution that is very popular. | [0.12.0](../../middleware/minio/release-notes.md#v0120) |
| Middleware MySQL | The most widely used open-source relational database. | [0.15.0](../../middleware/mysql/release-notes.md#v0150) |
| Middleware RabbitMQ | Open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). | [0.17.0](../../middleware/rabbitmq/release-notes.md#v0170) |
| Middleware Redis | An in-memory database caching service. | [0.15.0](../../middleware/redis/release-notes.md#v0150) |
| Container Regisry | Used to store images for K8s, DevOps, and container application development. | [0.15.0](../../kangaroo/intro/release-notes.md#v0150) |
| Networking | Supports multiple CNI combination solutions for different Linux kernels. | [0.13.0](../../dce/dce-rn/20240130.md) |
| Storage | Provides unified data storage services, supporting file, object, block, and local storage, easily integrating with storage vendor solutions. | [v0.14.1](../../dce/dce-rn/20231231.md) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
