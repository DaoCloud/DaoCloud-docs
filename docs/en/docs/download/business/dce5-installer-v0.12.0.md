---
date: 2023-11-08
hide:
  - navigation
---

# DCE 5.0 Enterprise v0.12.0

This page allows you to download the offline package and checksum files for DCE 5.0 Enterprise.

[Return to Download Index](../index.md#_2){ .md-button }
[More Historical Versions](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| ------------------ | ------ | ---- | ------- | ---------- | -------- |
| offline-v0.12.0-amd64.tar | v0.12.0 | AMD64 | 23.30 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.12.0-amd64.tar) | 2023-11-08 |
| offline-v0.12.0-arm64.tar | v0.12.0 | ARM64 | 20.20 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.12.0-arm64.tar) | 2023-11-08 |

## Validation

Navigate to the directory where the offline package was downloaded.

=== "AMD64"

    Run the following command to validate the offline package:

    ```sh
    echo "6a2bc869f2ec916dff35a5a473f13dcccef8126d664089ea0465e1a343eececf5a357520244990c765c9de608b765e26b8950bf0322b26b5e53491826d1d919a  offline-v0.12.0-amd64.tar" | sha512sum -c
    ```

    If the validation is successful, it will print:

    ```none
    offline-v0.12.0-amd64.tar: OK
    ```

=== "ARM64"

    Run the following command to validate the offline package:

    ```sh
    echo "c7fba9dfe0979caa2910b9aa2674e3a744455b185f9ee8e70264d8833e962df3361fb85d9d5d33be8fc643e36d9929e3d7af37ead66e7d30483d76dc77faa04c  offline-v0.12.0-arm64.tar" | sha512sum -c
    ```

    If the validation is successful, it will print:

    ```none
    offline-v0.12.0-arm64.tar: OK
    ```

## Installation

After the offline package has been successfully validated,

=== "AMD64"

    Run the following command to extract the tar package:

    ```sh
    tar -zxvf offline-v0.12.0-amd64.tar
    ```

=== "ARM64"

    Run the following command to extract the tar package:

    ```sh
    tar -zxvf offline-v0.12.0-arm64.tar
    ```

- For installation instructions, refer to [DCE 5.0 Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, please contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

DCE 5.0 Enterprise includes the following modules that can be used on-demand to meet various application scenarios:

| Module | Description | Latest Updates |
| --- | ---- | ------ |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, personalized appearance settings, etc. | [0.21.0](../../ghippo/intro/release-notes.md#0210) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and other core Kubernetes functionalities | [0.22.0](../../kpanda/intro/release-notes.md#0220) |
| Insight | Provides rich dashboards, scenario monitoring, data querying, alerting, and graphical information | [0.21.1](../../insight/intro/releasenote.md#insight-server-v0210) |
| Workbench | Container-based DevOps application platform that supports Jenkins, Tekton, GitOps, and other pipeline jobs | [0.21.0](../../amamba/intro/release-notes.md#0210) |
| Multi-Cloud Orchestration | Centralized management of multi-cloud, hybrid cloud, and cross-cloud resources, with capabilities such as multi-cloud disaster recovery and fault recovery | [0.13.1](../../kairship/intro/release-notes.md#0131) |
| Microservice Engine | Provides governance capabilities such as service discovery, service governance, configuration management, and microservice gateway | [0.28.1](../../skoala/intro/release-notes.md#0281) |
| Service Mesh | Next-generation service mesh for cloud-native applications based on Istio open-source technology | [v0.20.3](../../mspider/intro/release-notes.md#v0203) |
| Middleware Elasticsearch | Currently the preferred full-text search engine | [0.11.0](../../middleware/elasticsearch/release-notes.md#0110) |
| Middleware Kafka | Distributed message queue service based on the open-source software Kafka | [0.9.0](../../middleware/kafka/release-notes.md#090) |
| Middleware MinIO | A lightweight, open-source object storage solution that is highly popular | [0.9.0](../../middleware/minio/release-notes.md#090) |
| Middleware MySQL | The most widely used open-source relational database | [0.12.0](../../middleware/mysql/release-notes.md#0120) |
| Middleware RabbitMQ | Open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP) | [0.14.0](../../middleware/rabbitmq/release-notes.md#0140) |
| Middleware Redis | An in-memory database caching service | [0.12.0](../../middleware/redis/release-notes.md#0120) |
| Container Registry | Used to store images for K8s, DevOps, and container application development | [0.11.0](../../kangaroo/intro/release-notes.md#v0110) |
| Networking | Supports multiple CNI combinations for different Linux kernels | [0.10.1](../../network/modules/spiderpool/releasenotes.md#v0101) |
| Storage | Provides unified data storage services, supports file, object, block, and local storage, and easily integrates with storage vendor solutions | [v0.13.1](../../storage/hwameistor/releasenotes.md#v0131) |
| Cloud Edge Collaboration | Extends containerized capabilities to the edge | [v0.5.1](../../kant/intro/release-notes.md#v050) |

## More

- [Online Documentation](../../dce/index.md)
- [Report Bugs](https://github.com/DaoCloud/DaoCloud-docs/issues)
