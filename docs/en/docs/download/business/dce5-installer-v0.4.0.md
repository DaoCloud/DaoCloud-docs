---
date: 2023-01-12
hide:
  - navigation
---

# DCE 5.0 Enterprise v0.4.0

This page allows you to download the offline package and checksum file of DCE 5.0 Enterprise.

[Return to Download Index](../index.md#download-enterprise-package){ .md-button }
[More Historical Versions](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Downloads | Update Date |
| ----------------------------- | ------- | -------- | -- ----------------------------------------------- | ----- ----- | -------------------------------- |
| offline-centos7-v0.4.0-amd64.tar | v0.4.0 | AMD64 | 16.33GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-centos7-v0.4.0-amd64.tar) | 2023-01-12 |
| offline-kylin-v10sp2-v0.4.0-arm64.tar | v0.4.0 | ARM64 | 14.96GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-kylin-v10sp2-v0.4.0-arm64.tar) | 2023-01-12 |

## Validation

Go to the download directory of the offline package.

=== "AMD64"

     run the following command to validate the offline package:

     ```sh
     echo "5b94cb38a07b2f629d14a66b9a986bce11b0e584803072dd54956b142ed3c4c6967de337e4f8a27a726e94c20ad697ebaa080433fa062e9029b2f1983fa8b80 d offline-centos7-v0.4.0-amd64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-centos7-v0.4.0-amd64.tar: OK
     ```

=== "ARM64"

     run the following command to validate the offline package:

     ```sh
     echo "eea9853a8dcdcb1ddf73aff771326757d21fe130eedfc1fafa8457b521d5fe014ca11adbde48ff3d49c7d5af530c1e9fbdd8e18a9a190b77f09a277b8acc8ee4 offline-kylin -v10sp2-v0.4.0-arm64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-kylin-v10sp2-v0.4.0-arm64.tar: OK
     ```

## Installation

After the offline package has been successfully validated,

=== "AMD64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-centos7-v0.4.0-amd64.tar
     ```

=== "ARM64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-kylin-v10sp2-v0.4.0-arm64.tar
     ```

- For installation, refer to [DCE 5.0 Enterprise Installation Process](../../install/commercial/start-install.md)
- After successful installation, please contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

The DCE 5.0 Enterprise includes the following modules, which are plug-and-play to meet various use cases:

| Modules | Introduction | What's New |
| -------------------- | ---------------------------- ----------------------------------------------- | ----- -------------------------------------------------- ------ |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, personalized appearance settings, etc. | [v0.13.2](../../ghippo/intro/release-notes.md#v0132) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [v0.14.0](../../kpanda/intro/release-notes.md#v0140) |
| Insight | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [v0.13.2](../../insight/intro/releasenote.md#v0132) |
| Workbench | A container-based DevOps application platform that supports pipeline operations such as Jenkins, Tekton, GitOps, etc. | [v0.12.0](../../amamba/intro/release-notes.md#v0120) |
| Multicloud Management| Centralized management of application orchestration of multicloud, hybrid cloud, and cross-cloud resources, with multicloud disaster recovery and fault recovery capabilities| [v0.5.1](../../kairship/intro/release-notes.md# v051) |
| Microservice Engine | Provide registration discovery, service governance, configuration management, microservice gateway and other governance capabilities | [v0.16.1](../../skoala/intro/release-notes.md#v0161) |
| Service Mesh | A next-generation service mesh for cloud native applications based on Istio open source technology | [v0.12.1](../../mspider/intro/release-notes.md#v0121) |
| Middleware Elasticsearch | Currently preferred full-text search engine | [v0.4.0](../../middleware/elasticsearch/release-notes.md#v040) |
| Middleware Kafka | Distributed message queue service based on open source software Kafka | [v0.2.0](../../middleware/kafka/release-notes.md#v020) |
| Middleware MinIO | A very popular lightweight, open source object storage solution | [v0.2.0](../../middleware/minio/release-notes.md#v020) |
| Middleware MySQL | The most widely used open source relational database | [v0.5.0](../../middleware/mysql/release-notes.md#v050) |
| Middleware RabbitMQ | Open source message broker software implementing the Advanced Message Queuing Protocol (AMQP) | [v0.7.0](../../middleware/rabbitmq/release-notes.md#v070) |
| Middleware Redis | An in-memory database caching service | [v0.4.1](../../middleware/redis/release-notes.md#v041) |
| Container registry | Used to store images for K8s, DevOps and container application development | [v0.4.0](../../kangaroo/intro/release-notes.md) |
| Network | Support multiple CNI combinations for different Linux kernels | [v0.4.2](../../network/modules/spiderpool/releasenotes.md) |
| Storage | Provide unified data storage services, support files, objects, blocks, and local storage, and easily access storage vendor solutions | [0.7.1](../../storage/hwameistor/releasenotes.md) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)