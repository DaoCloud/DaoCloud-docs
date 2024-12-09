---
MTPE: windsonsea
date: 2024-10-10
hide:
  - navigation
---

# DCE 5.0 Enterprise with Installer v0.22.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Enterprise.

[Return to Download Guide](../index.md#download-dce-50-enterprise){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.22.0-amd64.tar | v0.22.0 | AMD 64 | 27.33 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.22.0-amd64.tar) | 2024-10-10 |
| offline-v0.22.0-arm64.tar | v0.22.0 | <font color="green">ARM 64</font> | 24.29 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.22.0-arm64.tar) | 2024-10-10 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "dbe6013bcbc912cb369081e0b96477e854d50f1ca307527ee6fa6bb5cbde3b6a5e1e796aef30382a358559823b67c83d8c4cd995f6b02925121ab50b9438cd3e  offline-v0.22.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.22.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "5280abb3c9e4709d2c316033cabf1834761819ce625f19510ce020d8b835367d3497bc2a2349e35cc4bf52630e9ee1a1993f6ab84067125959ddd60be316aa6a  offline-v0.22.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.22.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.22.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.22.0-arm64.tar
    ```

- For installation instructions, refer to [Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

DCE 5.0 Enterprise includes the following modules, which can be used on-demand to meet various application scenarios:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, and custom appearance. | [0.31.0](../../ghippo/intro/release-notes.md#v0310) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and more Kubernetes features. | [0.32.2](../../kpanda/intro/release-notes.md#v0320) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alert information. | [0.30.1](../../insight/intro/release-notes.md#v0300) |
| Workbench | A container-based DevOps application platform that supports Jenkins, Tekton, GitOps, and other pipeline jobs. | [0.31.0](../../amamba/intro/release-notes.md#v0310) |
| MultiCloud Management | Centralized management of multicloud, hybrid cloud, and cross-cloud resources for application orchestration, with capabilities such as multicloud disaster recovery and fault recovery. | [0.23.0](../../kairship/intro/release-notes.md#v0230) |
| Microservice Engine | Provides governance capabilities such as service registration, discovery, configuration management, and microservice gateway. | [0.41.3](../../skoala/intro/release-notes.md#v0413) |
| Service Mesh | Next-generation service mesh built on Istio open-source technology for cloud-native applications. | [v0.30.0](../../mspider/intro/release-notes.md#v0300) |
| Middleware Elasticsearch | Currently the preferred full-text search engine. | [0.21.1](../../middleware/elasticsearch/release-notes.md#v0210) |
| Middleware Kafka | Distributed message queue service based on the open-source software Kafka. | [0.19.0](../../middleware/kafka/release-notes.md#v0190) |
| Middleware MinIO | A lightweight, open-source object storage solution that is very popular. | [0.19.0](../../middleware/minio/release-notes.md#v0190) |
| Middleware MySQL | The most widely used open-source relational database. | [0.22.0](../../middleware/mysql/release-notes.md#v0220) |
| Middleware RabbitMQ | Open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). | [0.24.0](../../middleware/rabbitmq/release-notes.md#v0240) |
| Middleware Redis | An in-memory database caching service. | [0.22.0](../../middleware/redis/release-notes.md#v0220) |
| Container Regisry | Used to store images for K8s, DevOps, and container application development. | [0.22.0](../../kangaroo/intro/release-notes.md#v0220) |
| Networking | Supports multiple CNI combination solutions for different Linux kernels. | [0.15.1](../../network/intro/release-notes.md#v0151) |
| Storage | Provides unified data storage services, supporting file, object, block, and local storage, easily integrating with storage vendor solutions. | [v0.15.0](../../storage/hwameistor/release-notes.md#v0150) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
