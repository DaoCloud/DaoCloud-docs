---
date: 2023-09-08
hide:
  - navigation
---

# DCE 5.0 Enterprise v0.11.0

This page provides downloads for the offline package and checksum files of DCE 5.0 Enterprise.

[Return to Download Index](../index.md#download-enterprise-package){ .md-button }
[More Historical Versions](./dce5-installer-history.md){ .md-button }

## Downloads

| Filename | Version | Architecture | File Size | Download | Update Date |
| -------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.11.0-amd64.tar              | v0.11.0  | AMD64        | 21.28 GB   | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.11.0-amd64.tar) | 2023-09-08 |
| offline-v0.11.0-arm64.tar              | v0.11.0  | ARM64        | 17.60 GB   | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.11.0-arm64.tar) | 2023-09-08 |

## Validation

Navigate to the download directory of the offline package.

=== "AMD64"

    Run the following command to validate the offline package:

    ```sh
    echo "58b57b7b4441b311ad390ecc4b34def1c18f3df61f4daa61bdc9bb987f22504c10d71bdd24e39996d566cc9965cdd7ba26dbc3d71bfbe982b82b17aa20ff0751  offline-v0.11.0-amd64.tar" | sha512sum -c
    ```

    If the validation is successful, it will print:

    ```none
    offline-v0.11.0-amd64.tar: OK
    ```

=== "ARM64"

    Run the following command to validate the offline package:

    ```sh
    echo "70b4f637f27d97c716f94d11acf9527f03ddd32a8899557494550a3d644bc4f5ba5c5a6b89bac9023b0a4da88c38a4b3e3ba9d3320bc7eeff483921f31d546cf  offline-v0.11.0-arm64.tar" | sha512sum -c
    ```

    If the validation is successful, it will print:

    ```none
    offline-v0.11.0-arm64.tar: OK
    ```

## Installation

After the offline package has been successfully validated,

=== "AMD64"

    Run the following command to extract the tar package:

    ```sh
    tar -zxvf offline-v0.11.0-amd64.tar
    ```

=== "ARM64"

    Run the following command to extract the tar package:

    ```sh
    tar -zxvf offline-v0.11.0-arm64.tar
    ```

- For installation instructions, refer to [DCE 5.0 Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, please contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

DCE 5.0 Enterprise includes the following modules,
which are plug-and-play to meet various application scenarios:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, enterprise spaces, audit logs, personalized appearance settings, etc. | [0.20.1](../../ghippo/intro/release-notes.md#0201) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRD, namespaces, and other core features of K8s. | [0.21.0](../../kpanda/intro/release-notes.md#0210) |
| Insight   | Provides rich dashboards, scenario monitoring, data queries, alerts, and other graphical information. | [0.20.0](../../insight/intro/releasenote.md#0200)     |
| Workbench | Container-based DevOps application platform, supports Jenkins, Tekton, GitOps, and other pipeline jobs. | [0.20.0](../../amamba/intro/release-notes.md#0200) |
| MultiCloud Orchestration | Centralized management of multi-cloud, hybrid cloud, and cross-cloud resource application orchestrations, with multi-cloud disaster recovery and fault tolerance capabilities. | [0.12.0](../../kairship/intro/release-notes.md#0120) |
| Microservice Engine | Provides governance capabilities such as service registration and discovery, service governance, configuration management, and microservice gateway |
| Service Mesh | Next-generation service mesh built on the open-source technology Istio, designed for cloud native applications. | [v0.19.0](../../mspider/intro/release-notes.md#v0190) |
| Middleware Elasticsearch | Currently the preferred full-text search engine. | [0.10.0](../../middleware/elasticsearch/release-notes.md#0100) |
| Middleware Kafka | Distributed message queue service based on the open-source software Kafka. | [0.8.0](../../middleware/kafka/release-notes.md#080) |
| Middleware MinIO | A popular lightweight, open-source object storage solution. | [0.8.0](../../middleware/minio/release-notes.md#080) |
| Middleware MySQL | The most widely used open-source relational database. | [0.11.0](../../middleware/mysql/release-notes.md#0110) |
| Middleware RabbitMQ | Open-source message broker software implementing the Advanced Message Queuing Protocol (AMQP). | [0.13.0](../../middleware/rabbitmq/release-notes.md#0130) |
| Middleware Redis | In-memory database caching service. | [0.11.0](../../middleware/redis/release-notes.md#0110) |
| Container Repository | Used for storing images for K8s, DevOps, and container application development. | [0.11.0](../../dce/dce-rn/20230630.md) |
| Networking | Supports various CNI combinations for different Linux kernels. | [0.9.0](../../dce/dce-rn/20230731.md) |
| Storage | Provides unified data storage services, supporting file, object, block, and local storage with easy integration of storage vendor solutions. | [v0.10.8](../../dce/dce-rn/20230630.md) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
