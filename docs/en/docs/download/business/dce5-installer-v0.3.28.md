---
MTPE: windsonsea
date: 2022-11-23
hide:
  - navigation
---

# DCE 5.0 Enterprise with Installer v0.3.28

This page allows you to download the offline package of DCE 5.0 Enterprise.

[Return to Download Index](../index.md#download-enterprise-package){ .md-button }
[Legacy Packages](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Size | Download | Date |
| -------- | -------- | ---------- | ---------- |
| offline-v0.3.28.tar | 21 GB | [:arrow_down: Download](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.3.28.tar) | 2022- 11-18 |

## Verification

Go to the download directory of the offline package, run the following command to verify the offline package:

```sh
echo "88d89872d04d95ee44073c70460c2eb3ae4785a150fbfce672a5882c6f7d77f0d8f58359c5c8695e80d7e5fce93431c0c5ec6b710c080f4840d8adbb25daeb55 offline-v0.3.28.tar" | sha512sum -c
```

If the verification is successful, it will print:

```none
offline-v0.3.28.tar: OK
```

## Installation

After the offline package has been successfully verifyd, unpack the tarball:

```sh
tar -zxvf offline-v0.3.28.tar
```

Then refer to [Install DCE 5.0 Enterprise](../../install/index.md#_3) to install.
For first-time installation, please contact us for authorization: email info@daocloud.io or call 400 002 6898.
If you have any license key related questions, please contact DaoCloud delivery team.

## Modules

The DCE 5.0 Enterprise includes the following modules, which are plug-and-play to meet various use cases:

| Modules | Description | Versions |
| ------- | ----------- | -------- |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, and custom appearance. | [v0.11](../../ghippo/intro/release-notes.md#v0110) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [v0.12](../../kpanda/intro/release-notes.md#v0130) |
| Insight | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [v0.11](../../insight/intro/release-notes.md#v011) |
| Workbench | A container-based DevOps application platform that supports pipeline operations such as Jenkins, Tekton, GitOps, etc. | [v0.9](../../amamba/intro/release-notes.md#v090) |
| Multicloud Management | Centralized management of application orchestration of multicloud, hybrid cloud, and cross-cloud resources, with multicloud disaster recovery and fault recovery capabilities | [v0.3](../../kairship/intro/release-notes.md#v030) |
| Microservice Engine | Provides governance capabilities such as registration discovery, service governance, configuration management, and microservice gateway | [v0.11](../../skoala/intro/release-notes.md#v0122) |
| Service Mesh | A next-generation service mesh for cloud native applications based on Istio open source technology | [v0.10](../../mspider/intro/release-notes.md#v0111) |
| Middleware Elasticsearch | Currently preferred full-text search engine | [v0.3](../../middleware/elasticsearch/release-notes.md#v034) |
| Middleware Kafka | Distributed message queue service based on the open source software Kafka | [v0.1](../../middleware/kafka/release-notes.md#v012) |
| Middleware MinIO | A very popular lightweight, open source object storage solution | [v0.1](../../middleware/minio/release-notes.md#v012) |
| Middleware MySQL | The most widely used open source relational database | [v0.4](../../middleware/mysql/release-notes.md#v040) |
| Middleware RabbitMQ | Open source message broker software implementing the Advanced Message Queuing Protocol (AMQP) | [v0.6](../../middleware/rabbitmq/release-notes.md#v061) |
| Middleware Redis | An in-memory database caching service | [v0.2](../../middleware/redis/release-notes.md#v022) |
| Container Registry | Images for storing K8s, DevOps, and container application development | [Release Notes](../../kangaroo/intro/release-notes.md) |
| Network | Support multiple CNI combinations for different Linux kernels | [Release Notes](../../network/intro/release-notes.md) |
| Storage | Provide unified data storage services, support files, objects, blocks, and local storage, and easily access storage vendor solutions | [Release Notes](../../storage/hwameistor/release-notes.md) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)