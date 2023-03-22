---
date: 2022-11-23
hide:
  - navigation
---

# DCE 5.0 Commercial Edition v0.3.28

This page can download the offline installation package of DCE 5.0 Commercial Edition.

## Download

| Version Name | File Size | Installer | Date Updated |
| ------------------- | -------- | -------------------- -------------------------------------------------- ------------------------------ | ---------- |
| offline-v0.3.28.tar | 21 GB | [:arrow_down: Download](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.3.28.tar) | 2022- 11-18 |

## Validation

Enter the download directory of the offline installation package. Execute the following command to verify the installation package:

```sh
echo "88d89872d04d95ee44073c70460c2eb3ae4785a150fbfce672a5882c6f7d77f0d8f58359c5c8695e80d7e5fce93431c0c5ecum6b710c080f4840d5adbb25daeb55 offline.2sha -v
```

If the verification is successful, it will print:

```none
offline-v0.3.28.tar: OK
```

## Install

After successfully verifying the offline package, unpack the tar package:

```sh
tar -zxvf offline-v0.3.28.tar
```

Then refer to [Install DCE 5.0 Commercial Edition](../../install/intro.md#_3) to install.
If it is the first installation, please perform [genuine authorization](https://qingflow.com/f/e3291647).
If you have any license key related questions, please contact DaoCloud delivery team.

## Modules

The DCE 5.0 commercial edition includes the following modules, which are plug-and-play on-demand to meet various application scenarios:

| Modules | Introduction | Module Versions |
| -------------------- | ---------------------------- ----------------------------------------------- | ----- -------------------------------------------------- ------ |
| Global Management | Responsible for user access control, permissions, enterprise space, audit logs, personalized appearance settings, etc. | [v0.11](../../ghippo/01ProductBrief/release-notes.md#v011) |
| Container Management | Manage K8s core functions such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [v0.12](../../kpanda/03ProductBrief/release-notes.md#v012) |
| Observability | Provide rich graphic information such as dashboards, scene monitoring, data query, and alarms | [v0.11](../../insight/intro/releasenote.md#v011) |
| Application Workbench | A container-based DevOps application platform that supports pipeline operations such as Jenkins, Tekton, GitOps, etc. | [v0.9](../../amamba/01ProductBrief/release-notes.md#v09) |
| Multicloud orchestration| Centralized management of application orchestration of multicloud, hybrid cloud, and cross-cloud resources, with multicloud disaster recovery and fault recovery capabilities| [v0.3](../../kairship/01product/release-notes.md# v03) |
| Microservice Engine | Provides governance capabilities such as registration discovery, service governance, configuration management, and microservice gateway | [v0.11](../../skoala/intro/release-notes.md#v011) |
| Service Mesh | A next-generation service mesh for cloud-native applications based on Istio open source technology | [v0.10](../../mspider/01Intro/release-notes.md#v010) |
| Middleware Elasticsearch | Currently preferred full-text search engine | [v0.3](../../middleware/elasticsearch/release-notes.md#v034) |
| Middleware Kafka | Distributed message queue service based on the open source software Kafka | [v0.1](../../middleware/kafka/release-notes.md#v012) |
| Middleware MinIO | A very popular lightweight, open source object storage solution | [v0.1](../../middleware/minio/release-notes.md#v012) |
| Middleware MySQL | The most widely used open source relational database | [v0.4](../../middleware/mysql/release-notes.md#v04) |
| Middleware RabbitMQ | Open source message broker software implementing the Advanced Message Queuing Protocol (AMQP) | [v0.6](../../middleware/rabbitmq/release-notes.md#v06) |
| Middleware Redis | An in-memory database caching service | [v0.2](../../middleware/redis/release-notes.md#v02) |
| container registry | Images for storing K8s, DevOps, and container application development | [Release Notes](../../release/rn5.0.md) |
| Network | Support multiple CNI combinations for different Linux kernels | [Release Notes](../../release/rn5.0.md) |
| Storage | Provide unified data storage services, support files, objects, blocks, and local storage, and easily access storage vendor solutions | [Release Notes](../../release/rn5.0.md) |

## More

- [Online Documentation](../../dce/what-is-dce.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)