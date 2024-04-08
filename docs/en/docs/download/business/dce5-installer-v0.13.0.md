---
MTPE: windsonsea
date: 2023-12-07
hide:
  - navigation
---

# DCE 5.0 Enterprise with Installer v0.13.0

On this page, you can download the offline installation package and verification files for DCE 5.0 Enterprise.

[Back to Download Overview](../index.md#_2){ .md-button } [More Release Versions](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| -------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.13.0-amd64.tar | v0.13.0 | AMD 64 | 23.41 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.13.0-amd64.tar) | 2023-12-07 |
| offline-v0.13.0-arm64.tar | v0.13.0 | <font color="green">ARM 64</font> | 20.15 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.13.0-arm64.tar) | 2023-12-07 |

## Verification

Go to the directory where the offline installation package is downloaded.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "a426d3af779a424012221e03e040dcdeaf3cf2ec45efee9f6aa05bb508b7787373e01b4d229b8e29ee97bb77bfc4f9cc24f6fefc918a981f226ed0edba665bb2  offline-v0.13.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.13.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "25d9ce974aae272ccdbe3aaedc319e2692afb6f87e072a250a2e7f90997c0655fd04956533be5bdb8d3ea6f6641c0418087894a853f925fec0b432fb2d8ce8f9  offline-v0.13.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.13.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to extract the tar package:

    ```sh
    tar -zxvf offline-v0.13.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to extract the tar package:

    ```sh
    tar -zxvf offline-v0.13.0-arm64.tar
    ```

- For installation instructions, please refer to the [Commercial Edition Installation Process](../../install/commercial/start-install.md).
- After successful installation, please contact us for authorization: email info@daocloud.io or call 400 002 6898.

## Modules

DCE 5.0 Enterprise includes the following modules that can be used on-demand to meet various application scenarios:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, enterprise spaces, audit logs, personalized appearance settings, and more | [0.22.1](../../ghippo/intro/release-notes.md#v0221) |
| Container Management | Manage clusters, nodes, workloads, Helm applications, CRDs, namespaces, and other core Kubernetes features | [0.23.0](../../kpanda/intro/release-notes.md#v0230) |
| Observability | Provides rich dashboards, scenario monitoring, data querying, alerts, and more graphical and textual information | [0.22.0](../../insight/intro/releasenote.md#v0220) |
| Workbench | Container-based DevOps application platform that supports Jenkins, Tekton, GitOps, and other pipeline jobs | [0.22.0](../../amamba/intro/release-notes.md#v0220) |
| Multi-Cloud Orchestration | Centrally manages multi-cloud, hybrid cloud, and cross-cloud resources for application orchestration, including multi-cloud disaster recovery and fault recovery capabilities | [0.14.0](../../kairship/intro/release-notes.md#v0140) |
| Microservice Engine | Provides governance capabilities such as service registration and discovery, configuration management, and microservice gateway | [0.30.0](../../skoala/intro/release-notes.md#v0300) |
| Service Mesh | Next-generation service mesh based on the open-source Istio technology for cloud-native applications | [v0.21.2](../../mspider/intro/release-notes.md#v0212) |
| Middleware Elasticsearch | Currently the preferred full-text search engine | [0.12.0](../../middleware/elasticsearch/release-notes.md#v0120) |
| Middleware Kafka | Distributed message queue service based on the open-source software Kafka | [0.10.0](../../middleware/kafka/release-notes.md#v0100) |
| Middleware MinIO | A popular lightweight, open-source object storage solution | [0.10.0](../../middleware/minio/release-notes.md#v0100) |
| Middleware MySQL | The most widely used open-source relational database | [0.13.0](../../middleware/mysql/release-notes.md#v0130) |
| Middleware RabbitMQ | Open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP) | [0.15.0](../../middleware/rabbitmq/release-notes.md#v0150) |
| Middleware Redis | An in-memory database caching service | [0.13.0](../../middleware/redis/release-notes.md#v0130) |
| Container Registry | Stores images for K8s, DevOps, and container application development | [0.13.1](../../dce/dce-rn/20231130.md) |
| Networking | Supports various CNI combinations for different Linux kernels | [0.11.1](../../dce/dce-rn/20231130.md) |
| Storage | Provides unified data storage services, supports file, object, block, and local storage, and easily integrates with storage vendor solutions | [v0.13.3](../../dce/dce-rn/20231130.md) |

## More

- [Online Documentation](../../dce/index.md)
- [Report Bugs](https://github.com/DaoCloud/DaoCloud-docs/issues)
