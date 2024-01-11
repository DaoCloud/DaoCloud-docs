---
MTPE: windsonsea
date: 2023-07-07
hide:
  - navigation
---

# DCE 5.0 Enterprise with Installer v0.9.0

This page allows you to download the offline package and checksum files for DCE 5.0 Enterprise.

[Return to Download Index](../index.md#download-enterprise-package){ .md-button }
[More Historical Versions](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| -------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.9.0-amd64.tar      | v0.9.0  | AMD64        | 19.01 GB   | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.9.0-amd64.tar)                  | 2023-07-07   |
| offline-v0.9.0-arm64.tar      | v0.9.0  | ARM64        | 17.37 GB   | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.9.0-arm64.tar)                  | 2023-07-07   |

## Validation

Navigate to the directory where the offline package is downloaded.

=== "AMD64"

    Run the following command to validate the package:

    ```sh
    echo "520ef719605042cd2b9289de795d609cde7f0aff9f7189d43e31bbe016b33debc715f8e0de24c8f3c3685d54f7d6b2595651bcfa9695c9b98210d161cfddc241  offline-v0.9.0-amd64.tar" | sha512sum -c
    ```

    If the validation is successful, the result will be similar to:

    ```none
    offline-v0.9.0-amd64.tar: OK
    ```

=== "ARM64"

    Run the following command to validate the package:

    ```sh
    echo "ae541aa5c2150af45b6dc3c3e432205683211d1b5d8ec816b37344c2234f3c05fbe2be7526b4b5832c5db0439c7d501ce2f1c1492aa5cfe045bbdd321d662e22  offline-v0.9.0-arm64.tar" | sha512sum -c
    ```

    If the validation is successful, the result will be similar to:

    ```none
    offline-v0.9.0-arm64.tar: OK
    ```

## Installation

After the offline package has been successfully validated,

=== "AMD64"

    Run the following command to extract the tar file:

    ```sh
    tar -zxvf offline-v0.9.0-amd64.tar
    ```

=== "ARM64"

    Run the following command to extract the tar file:

    ```sh
    tar -zxvf offline-v0.9.0-arm64.tar
    ```

- For installation instructions, refer to [DCE 5.0 Enterprise Installation Process](../../install/commercial/start-install.md).
- After successful installation, please contact us for authorization: email info@daocloud.io or call 400 002 6898.

## Modules

DCE 5.0 Enterprise includes the following modules that can be used on-demand to meet various application scenarios:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management     | Responsible for user access control, permissions, enterprise spaces, etc.    | [0.18.1](../../ghippo/intro/release-notes.md#v0181)    |
| Container Management  | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, etc.| [0.19.0](../../kpanda/intro/release-notes.md#v0190)    |
| Insight         | Provides rich dashboards, scene monitoring, data queries, alerts, etc.       | [0.18.2](../../insight/intro/releasenote.md#v0182)     |
| Workbench | Container-based DevOps application platform, supporting Jenkins, Tekton, GitOps, and more pipeline jobs. | [0.18.1](../../amamba/intro/release-notes.md#v0181)      |
| MultiCloud Management | Centralized management of multi-cloud, hybrid cloud, cross-cloud resources for application orchestration, with multi-cloud disaster recovery and fault recovery capabilities. | [0.10.3](../../kairship/intro/release-notes.md#v0103)   |
| Microservice Engine   | Provides governance capabilities such as service registration and discovery, service governance, configuration management, and microservice gateway  |
| Service Mesh          | Next-generation service mesh built on Istio open-source technology for cloud native applications. | [v0.17.0](../../mspider/intro/release-notes.md#v0170)    |
| Middleware Elasticsearch | Currently the preferred full-text search engine.                                      | [0.9.0](../../middleware/elasticsearch/release-notes.md#v090) |
| Middleware Kafka        | Distributed message queue service based on the open-source software Kafka.            | [0.7.0](../../middleware/kafka/release-notes.md#v070)          |
| Middleware MinIO        | A popular lightweight, open-source object storage solution.                            | [0.7.0](../../middleware/minio/release-notes.md#v070)          |
| Middleware MySQL        | The most widely used open-source relational database.                                  | [0.10.0](../../middleware/mysql/release-notes.md#v0100)           |
| Middleware RabbitMQ     | Open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). | [0.12.0](../../middleware/rabbitmq/release-notes.md#v0120)        |
| Middleware Redis        | An in-memory database caching service.                                                | [0.9.0](../../middleware/redis/release-notes.md#v090)           |
| Container Registry       | Used to store images for K8s, DevOps, and container application development.            | [0.9.1](../../dce/dce-rn/20230630.md)                            |
| Network                | Supports various CNI combinations for different Linux kernels.                        | [0.8.0](../../dce/dce-rn/20230630.md)                            |
| Storage                | Provides unified data storage services, supporting file, object, block, and local storage, easily integrates with storage vendors' solutions. | [v0.10.4](../../dce/dce-rn/20230630.md)                            |

## More

- [Online Documentation](../../dce/index.md)
- [Report Bugs](https://github.com/DaoCloud/DaoCloud-docs/issues)