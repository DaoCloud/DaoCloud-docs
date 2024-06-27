---
MTPE: windsonsea
date: 2024-06-27
hide:
  - navigation
---

# DCE 5.0 Enterprise with Installer v0.18.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Enterprise.

[Return to Download Guide](../index.md#_2){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-v0.18.0-amd64.tar | v0.18.0 | AMD 64 | 26.44GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.18.0-amd64.tar) | 2024-06-11 |
| offline-v0.18.0-arm64.tar | v0.18.0 | <font color="green">ARM 64</font> | 23.32GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.18.0-arm64.tar) | 2024-06-11 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "65e08b1f1e66d1eee2360aad4c27a3dbf085b14c037afed4648daaf5d19c3a035c163aa98e5bfcc04bb0b23015e959136040efc40d3514cd7762ec4a5e611979  offline-v0.18.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.18.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "1aeaf75d10d2c16fb24b33d9fff322bd8801c05d4df4241aac9235671b32b24a049da7780cd55125aaa5464f46e6b47af17b3d4598e962c292b3ac317cabef07  offline-v0.18.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-v0.18.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.18.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-v0.18.0-arm64.tar
    ```

- For installation instructions, refer to [Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

DCE 5.0 Enterprise includes the following modules, which can be used on-demand to meet various application scenarios:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, personalized appearance settings, etc. | [0.27.0](../../ghippo/intro/release-notes.md#v0270) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and other core Kubernetes functionalities. | [0.28.1](../../kpanda/intro/release-notes.md#v0281) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alarm information. | [0.27.0](../../insight/intro/releasenote.md#v0270) |
| Workbench | A container-based DevOps application platform that supports Jenkins, Tekton, GitOps, and other pipeline jobs. | [0.27.0](../../amamba/intro/release-notes.md#v0270) |
| MultiCloud Management | Centralized management of multi-cloud, hybrid cloud, and cross-cloud resources for application orchestration, with capabilities such as multi-cloud disaster recovery and fault recovery. | [0.19.0](../../kairship/intro/release-notes.md#v0190) |
| Microservice Engine | Provides governance capabilities such as service registration, discovery, configuration management, and microservice gateway. | [0.37.1](../../skoala/intro/release-notes.md#v0371) |
| Service Mesh | Next-generation service mesh built on Istio open-source technology for cloud-native applications. | [v0.26.0](../../mspider/intro/release-notes.md#v0260) |
| Middleware Elasticsearch | Currently the preferred full-text search engine. | [0.17.0](../../middleware/elasticsearch/release-notes.md#v0170) |
| Middleware Kafka | Distributed message queue service based on the open-source software Kafka. | [0.15.0](../../middleware/kafka/release-notes.md#v0150) |
| Middleware MinIO | A lightweight, open-source object storage solution that is very popular. | [0.15.0](../../middleware/minio/release-notes.md#v0150) |
| Middleware MySQL | The most widely used open-source relational database. | [0.18.0](../../middleware/mysql/release-notes.md#v0180) |
| Middleware RabbitMQ | Open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). | [0.20.0](../../middleware/rabbitmq/release-notes.md#v0200) |
| Middleware Redis | An in-memory database caching service. | [0.18.0](../../middleware/redis/release-notes.md#v0180) |
| Container Regisry | Used to store images for K8s, DevOps, and container application development. | [0.18.1](../../kangaroo/intro/release-notes.md#v0181) |
| Networking | Supports multiple CNI combination solutions for different Linux kernels. | [0.15.0](../../dce/dce-rn/20240530.md) |
| Storage | Provides unified data storage services, supporting file, object, block, and local storage, easily integrating with storage vendor solutions. | [v0.14.6](../../storage/hwameistor/releasenotes.md#v0146) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
