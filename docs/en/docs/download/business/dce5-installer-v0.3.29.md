---
date: 2022-11-25
hide:
  - navigation
---

# DCE 5.0 Enterprise v0.3.29

This page allows you to download the offline package and checksum file of DCE 5.0 Enterprise.

[Return to Download Index](../index.md#download-enterprise-package){ .md-button }
[More Historical Versions](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| -------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-centos7-v0.3.29-amd64.tar | v0.3.29 | AMD64 | 22.9 GB | [:arrow_down: Download](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-centos7-v0.3.29-amd64.tar) | 2022-12-16 |
| offline-kylin-v10sp2-v0.3.29-arm64.tar | v0.3.29 | ARM64 | 19.9 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-kylin-v10sp2-v0.3.29-arm64.tar) | 2022-12-16 |

## Validation

Go to the download directory of the offline package.

=== "AMD64"

     run the following command to validate the offline package:

     ```sh
     echo "ef7fd779d3b5bc50bccf80e29934002c60f53143319c80dd9aad85fc1404ac7d309997e0d9c829612c1b400cd4d4861fb1b6f91efee8c236ada930cbb44ca1c1 off line-centos7-v0.3.29-amd64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-centos7-v0.3.29-amd64.tar: OK
     ```

=== "ARM64"

     run the following command to validate the offline package:

     ```sh
     echo "1cc8b41bfaad23cb1b14170b68ee581d2eb384fe6d803ce34a1a09f1d41e7640768cca8a7f8a3f6a881ecfddaaa73756247676b6e0bc72b7ca651cc855ce2ff4 offline-k ylin-v10sp2-v0.3.29-arm64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-kylin-v10sp2-v0.3.29-arm64.tar: OK
     ```

## Installation

After the offline package has been successfully validated,

=== "AMD64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-centos7-v0.3.29-amd64.tar
     ```

=== "ARM64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-kylin-v10sp2-v0.3.29-arm64.tar
     ```

- For installation, refer to [DCE 5.0 Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, please contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

The DCE 5.0 Enterprise includes the following modules, which are plug-and-play to meet various use cases:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, personalized appearance settings, etc. | [v0.12](../../ghippo/intro/release-notes.md#v012) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [v0.13](../../kpanda/intro/release-notes.md#v013) |
| Insight | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [v0.12](../../insight/intro/releasenote.md#v012) |
| Workbench | A container-based DevOps application platform that supports pipeline operations such as Jenkins, Tekton, GitOps, etc. | [v0.10](../../amamba/intro/release-notes.md#v010) |
| Multicloud Management| Centralized management of application orchestration of multicloud, hybrid cloud, and cross-cloud resources, with multicloud disaster recovery and fault recovery capabilities| [v0.4](../../kairship/intro/release-notes.md# v04) |
| Microservice Engine | Provide registration discovery, service governance, configuration management, microservice gateway and other governance capabilities | [v0.12](../../skoala/intro/release-notes.md#v012) |
| Service Mesh | A next-generation service mesh for cloud native applications based on Istio open source technology | [v0.11](../../mspider/intro/release-notes.md#v011) |
| middleware Elasticsearch | current preferred full-text search engine | [v0.3](../../middleware/elasticsearch/release-notes.md#v03) |
| Middleware Kafka | Distributed message queue service based on open source software Kafka | [v0.1](../../middleware/kafka/release-notes.md#v01) |
| Middleware MinIO | A very popular lightweight, open source object storage solution | [v0.1](../../middleware/minio/release-notes.md#v01) |
| Middleware MySQL | The most widely used open source relational database | [v0.4](../../middleware/mysql/release-notes.md#v04) |
| Middleware RabbitMQ | Open source message broker software implementing the Advanced Message Queuing Protocol (AMQP) | [v0.6](../../middleware/rabbitmq/release-notes.md#v06) |
| Middleware Redis | An in-memory database caching service | [v0.3](../../middleware/redis/release-notes.md#v03) |
| Container Registry | Images for storing K8s, DevOps, and container application development | [Release Notes](../../kangaroo/intro/release-notes.md) |
| Network | Support multiple CNI combinations for different Linux kernels | [Release Notes](../../network/modules/spiderpool/releasenotes.md) |
| Storage | Provide unified data storage services, support files, objects, blocks, and local storage, and easily access storage vendor solutions | [Release Notes](../../storage/hwameistor/releasenotes.md) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)