---
date: 2023-04-07
hide:
  - navigation
---

# DCE 5.0 Enterprise v0.6.0

This page allows you to download the offline package and checksum file of DCE 5.0 Enterprise.

[Return to Download Index](../index.md#download-enterprise-package){ .md-button }
[More Historical Versions](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Downloads | Update Date |
| ----------------------------- | ------- | -------- | -- ----------------------------------------------- | ----- ----- | -------------------------------- |
| offline-v0.6.0-amd64.tar | v0.6.0 | AMD64 | 16.36GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.6.0-amd64.tar) | 2023-04-07 |
| offline-v0.6.0-arm64.tar | v0.6.0 | ARM64 | 15.12GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.6.0-arm64.tar) | 2023-04-07 |

## Validation

Go to the download directory of the offline package.

=== "AMD64"

    run the following command to validate the offline package:

    ```sh
    echo "4e810a67268f8e0125a486018c3da8e8165d16cd0206d6d6e0560773caf8983cfe2b0827692e3ac6efbd26345c0bbfed58139ff01affd96d525b59f7967cec5d9 offline. var0-var1" sum -c
    ```

    If the validation is successful, it will print:

    ```none
    offline-v0.6.0-amd64.tar: OK
    ```

=== "ARM64"

    run the following command to validate the offline package:

    ```sh
    echo "4c778c6aad168e19bdffec234c5096795b6b7cfa9c5d17c9d9e64cb7ddc526263d6f0d863c631e2e4cc5d205866f29a69d9a38c92b8c751af0ed1db25304ba7d4.offline-varm0" um -c
    ```

    If the validation is successful, it will print:

    ```none
    offline-v0.6.0-arm64.tar: OK
    ```

## Installation

After the offline package has been successfully validated,

=== "AMD64"

    run the following command to extract the tarball:

    ```sh
    tar -zxvf offline-v0.6.0-amd64.tar
    ```

=== "ARM64"

    run the following command to extract the tarball:

    ```sh
    tar -zxvf offline-v0.6.0-arm64.tar
    ```

- For installation, refer to [DCE 5.0 Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, please contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules


The DCE 5.0 Enterprise includes the following modules, which are plug-and-play to meet various use cases:


| Modules | Introduction | What's New |
| -------------------- | ---------------------------- ----------------------------------------------- | ----- -------------------------------------------------- ------ |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, personalized appearance settings, etc. | [0.15.0](../../ghippo/intro/release-notes.md#v0150) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [0.16.0](../../kpanda/intro/release-notes.md#v0160) |
| Insight | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [0.15.4](../../insight/intro/releasenote.md#v0154) |
| Workbench | A container-based DevOps application platform that supports pipeline operations such as Jenkins, Tekton, GitOps, etc. | [0.15.1](../../amamba/intro/release-notes.md#v0151) |
| Multicloud Management| Centralized management of application orchestration of multicloud, hybrid cloud, and cross-cloud resources, with multicloud disaster recovery and fault recovery capabilities| [0.7.4](../../kairship/intro/release-notes.md# v074) |
| Microservice Engine | Provide registration discovery, service governance, configuration management, microservice gateway and other governance capabilities | [0.19.1](../../skoala/intro/release-notes.md#v0191) |
| Service Mesh | A next-generation service mesh for cloud native applications based on Istio open source technology | [v0.14.3](../../mspider/intro/release-notes.md#v0143) |
| Middleware Elasticsearch | Currently the preferred full-text search engine | [0.6.0](../../middleware/elasticsearch/release-notes.md#v060) |
| Middleware Kafka | Distributed message queue service based on the open source software Kafka | [0.4.0](../../middleware/kafka/release-notes.md#v040) |
| Middleware MinIO | A very popular lightweight, open source object storage solution | [0.4.1](../../middleware/minio/release-notes.md#v041) |
| Middleware MySQL | The most widely used open source relational database | [0.7.0](../../middleware/mysql/release-notes.md#v070) |
| Middleware RabbitMQ | Open source message broker software implementing the Advanced Message Queuing Protocol (AMQP) | [0.9.1](../../middleware/rabbitmq/release-notes.md#v091) |
| Middleware Redis | An in-memory database caching service | [0.6.2](../../middleware/redis/release-notes.md#v062) |
| Container registry | Used to store images for K8s, DevOps and container application development | [0.6.2](../../kangaroo/intro/release-notes.md#v062) |
| Network | Support multiple CNI combinations for different Linux kernels | [0.5.0](../../network/modules/spiderpool/releasenotes.md#v050) |
| Storage | Provide unified data storage services, support files, objects, blocks, and local storage, and easily access storage vendor solutions | [v0.9.2](../../storage/hwameistor/releasenotes.md#v092) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
