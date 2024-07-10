---
MTPE: windsonsea
date: 2024-07-09
hide:
  - navigation
---

# DCE 5.0 Enterprise with Installer v0.19.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Enterprise.

[Return to Download Guide](../index.md#_2){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.19.0-amd64.tar | v0.19.0 | AMD 64 | 26.84 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.19.0-amd64.tar) | 2024-07-09 |
| offline-v0.19.0-arm64.tar | v0.19.0 | <font color="green">ARM 64</font> | 23.56 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.19.0-arm64.tar) | 2024-07-09 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "68083b73a9e666300d8bed5a50b7555be6db67783d594244ee7cd8bd5d720fca95190261be7a9039a8aab54bb38ac6ba121946bbdbfd8f9921187ce8405cde8b  offline-v0.19.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.19.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "45bf9b52f4b3337fa41f8a7112c8a1bc88a95bed96a34c34e79052cb4572669ccbcfd9689346771a8256eefe1588d0adb5404891282fca5934280059628b6472  offline-v0.19.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.19.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.19.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.19.0-arm64.tar
    ```

- For installation instructions, refer to [Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

DCE 5.0 Enterprise includes the following modules, which can be used on-demand to meet various application scenarios:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, personalized appearance settings, etc. | [0.28.0](../../ghippo/intro/release-notes.md#v0280) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and other core Kubernetes functionalities. | [0.29.1](../../kpanda/intro/release-notes.md#v0291) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alarm information. | [0.28.0](../../insight/intro/releasenote.md#v0280) |
| Workbench | A container-based DevOps application platform that supports Jenkins, Tekton, GitOps, and other pipeline jobs. | [0.28.2](../../amamba/intro/release-notes.md#v0282) |
| MultiCloud Management | Centralized management of multi-cloud, hybrid cloud, and cross-cloud resources for application orchestration, with capabilities such as multi-cloud disaster recovery and fault recovery. | [0.20.1](../../kairship/intro/release-notes.md#v0201) |
| Microservice Engine | Provides governance capabilities such as service registration, discovery, configuration management, and microservice gateway. | [0.38.2](../../skoala/intro/release-notes.md#v0382) |
| Service Mesh | Next-generation service mesh built on Istio open-source technology for cloud-native applications. | [v0.27.0](../../mspider/intro/release-notes.md#v0270) |
| Middleware Elasticsearch | Currently the preferred full-text search engine. | [0.18.0](../../middleware/elasticsearch/release-notes.md#v0180) |
| Middleware Kafka | Distributed message queue service based on the open-source software Kafka. | [0.16.0](../../middleware/kafka/release-notes.md#v0160) |
| Middleware MinIO | A lightweight, open-source object storage solution that is very popular. | [0.16.0](../../middleware/minio/release-notes.md#v0160) |
| Middleware MySQL | The most widely used open-source relational database. | [0.19.0](../../middleware/mysql/release-notes.md#v0190) |
| Middleware RabbitMQ | Open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). | [0.21.0](../../middleware/rabbitmq/release-notes.md#v0210) |
| Middleware Redis | An in-memory database caching service. | [0.19.0](../../middleware/redis/release-notes.md#v0190) |
| Container Regisry | Used to store images for K8s, DevOps, and container application development. | [0.19.0](../../kangaroo/intro/release-notes.md#v0190) |
| Networking | Supports multiple CNI combination solutions for different Linux kernels. | [0.15.0](../../dce/dce-rn/20240530.md) |
| Storage | Provides unified data storage services, supporting file, object, block, and local storage, easily integrating with storage vendor solutions. | [v0.14.7](../../storage/hwameistor/releasenotes.md#v0147) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
