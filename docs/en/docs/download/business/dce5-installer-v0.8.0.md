---
date: 2023-06-06
hide:
  - navigation
---

# DCE 5.0 Enterprise v0.8.0

This page provides offline packages and checksum files for DCE 5.0 Enterprise.

[Return to Download Index](../index.md#download-enterprise-package){ .md-button }
[More Historical Versions](./dce5-installer-history.md){ .md-button }

## Download

| Filename                    | Version | Architecture | File Size | Download Link                                                                               | Update Date |
| ---------------------------- | ------- | ------------ | --------- | ------------------------------------------------------------------------------------------- | ----------- |
| offline-v0.8.0-amd64.tar | v0.8.0  | AMD64        | 18.43GB   | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.8.0-amd64.tar) | 2023-06-06 |
| offline-v0.8.0-arm64.tar | v0.8.0  | ARM64        | 16.99GB   | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.8.0-arm64.tar) | 2023-06-06 |

## Validation

Enter the directory where the offline package is downloaded.

=== "AMD64"

    Run the following command to validate the offline package:

    ```sh
    echo "fbd3e646f5849406db1c221ab6956afd0e3dfd76e75394dfaeec06d2f2ec74934801cd7118c4bf2f51a3610dcb69fd7a010c613fcda3339abd20a1630029723e  offline-v0.8.0-amd64.tar" | sha512sum -c
    ```

    If the validation is successful, it will print:

    ```none
    offline-v0.8.0-amd64.tar: OK
    ```

=== "ARM64"

    Run the following command to validate the offline package:

    ```sh
    echo "f2854f0a90c2db16b9c206708b140069a953b68a575ce59b1dc656f84cb47c42647697067582e28e16175f4bfbcfcdb6c14d79c3d999c7646f1c58c40f1b35cc  offline-v0.8.0-arm64.tar" | sha512sum -c
    ```

    If the validation is successful, it will print:

    ```none
    offline-v0.8.0-arm64.tar: OK
    ```

## Installation

After the offline package is validated,

=== "AMD64"

    Run the following command to unpack the tar package:

    ```sh
    tar -zxvf offline-v0.8.0-amd64.tar
    ```

=== "ARM64"

    Run the following command to unpack the tar package:

    ```sh
    tar -zxvf offline-v0.8.0-arm64.tar
    ```

- For installation, refer to [DCE 5.0 Enterprise Installation Process](../../install/commercial/start-install.md).
- After successful installation, please contact us for authorization by email info@daocloud.io or call 400 002 6898.

## Modules

DCE 5.0 Enterprise includes the following modules, which can be used on demand to meet various use cases:

| Module               | Introduction                                                                 | Latest Release                                              |
| -------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Global Management    | Responsible for user access control, permissions, enterprise space, audit logs, personalized appearance settings, etc. | [0.17.1](../../ghippo/intro/release-notes.md#0171)         |
| Container Management | Manage Kubernetes core features such as clusters, nodes, workloads, Helm applications, CRD, namespaces, etc.        | [0.18.1](../../kpanda/intro/release-notes.md#0181)         |
| Insight        | Provide rich dashboard, scenario monitoring, data query, alarm and other graphical information.                      | [0.17.2](../../insight/intro/releasenote.md#0172)          |
| Workbench| Container-based DevOps application platform, supporting pipeline jobs such as Jenkins, Tekton, GitOps, etc.          | [0.17.3](../../amamba/intro/release-notes.md#0173)         |
| Multicloud MOrchestration| Centralized management of multicloud, hybrid cloud, cross-cloud resources' application orchestration, with multicloud disaster recovery, fault recovery and other capabilities.| [0.9.1](../../kairship/intro/release-notes.md#091)           |
| Microservice Engine  | Provide governance capabilities such as registration and discovery, service governance, configuration management, microservice gateway, etc. | [0.22.2](../../skoala/intro/release-notes.md#0222)         |
| Service Mesh         | The next-generation service mesh for cloud native applications based on open-source technology Istio.                    | [v0.16.2](../../mspider/intro/release-notes.md#v0162)      |
| Middleware: Elasticsearch | Currently the preferred full-text search engine.                                                               | [0.8.0](../../middleware/elasticsearch/release-notes.md#080) |
| Middleware: Kafka   | Distributed message queue service based on open-source software Kafka.                                                | [0.6.0](../../middleware/kafka/release-notes.md#060)        |
| Middleware: MinIO   | A very popular lightweight, open-source object storage solution.                                                      | [0.6.0](../../middleware/minio/release-notes.md#060)        |
| Middleware: MySQL   | The most widely used open-source relational database.                                                                  | [0.9.0](../../middleware/mysql/release-notes.md#090)        |
| Middleware: RabbitMQ| Open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP).                      | [0.11.0](../../middleware/rabbitmq/release-notes.md#0110)  |
| Middleware: Redis   | An in-memory database caching service.                                                                                 | [0.8.0](../../middleware/redis/release-notes.md#080)        |
| Container Registry     | Used to store images for K8s, DevOps, and container application development.                                          | [0.8.1](../../kangaroo/intro/release-notes.md)                            |
| Network              | Supports multiple CNI combinations for different Linux kernels.                                                      | [0.7.0](../../network/modules/spiderpool/releasenotes.md)                            |
| Storage              | Provides unified data storage services, supporting file, object, block, local storage, and easy access to storage vendor solutions. | [v0.10.2](../../storage/hwameistor/releasenotes.md)                            |

## More

- [Online documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
