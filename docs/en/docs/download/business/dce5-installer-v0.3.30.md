---
date: 2023-01-03
---

# DCE 5.0 Enterprise v0.3.30

This page can download the offline installation package and verification file of DCE 5.0 Enterprise.

## Download

| File Name | Version | Architecture | File Size | Downloads | Date Updated |
| ----------------------------- | ------- | -------- | -- ----------------------------------------------- | ----- ----- | -------------------------------- |
| offline-centos7-v0.3.30-amd64.tar | v0.3.30 | AMD64 | 16.33GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-centos7-v0.3.30-amd64.tar) | 2023-01-03 |
| offline-kylin-v10sp2-v0.3.30-arm64.tar | v0.3.30 | ARM64 | 14.96GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-kylin-v10sp2-v0.3.30-arm64.tar) | 2023-01-03 |

## Verification

Go to the download directory of the offline installation package.

=== "AMD64"

     run the following command to verify the installation package:

     ```sh
     echo "08ccfce8e3f551e82bdb89f26d0e9bb9b0f40e02cd5bcd0db8662c70d22932f24b2958ab3ea71e0ec497d8ad75a1cc134cdd24eabbfe9003c3c120c83d4d0417 offline-cent os7-v0.3.30-amd64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-centos7-v0.3.30-amd64.tar: OK
     ```

=== "ARM64"

     run the following command to verify the installation package:

     ```sh
     echo "a970526876754b763d8cc3df32ac522075ad2e08989a9bbad08b3a9be75366be6208f6e8d2865ee05c07291545373ef045bfc6fb31179df1ad2140b2b8741998 offline-kylin-v10sp2-v0.3.30-arm64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-kylin-v10sp2-v0.3.30-arm64.tar: OK
     ```

## Install

After successfully verifying the offline package,

=== "AMD64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-centos7-v0.3.30-amd64.tar
     ```

=== "ARM64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-kylin-v10sp2-v0.3.30-arm64.tar
     ```

- For installation, please refer to [Enterprise Package installation process](../../install/commercial/start-install.md)
- After successful installation, please contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

The DCE 5.0 Enterprise includes the following modules, which are plug-and-play on-demand to meet various use cases:

| Modules | Introduction | What's New |
| -------------------- | ---------------------------- ----------------------------------------------- | ----- -------------------------------------------------- ------ |
| Global Management | Responsible for user access control, permissions, enterprise space, audit logs, personalized appearance settings, etc. | [v0.13](../../ghippo/intro/release-notes.md#v013) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [v0.14](../../kpanda/intro/release-notes.md#v014) |
| Observability | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [v0.13](../../insight/intro/releasenote.md#v013) |
| Workbench | A container-based DevOps application platform that supports pipeline operations such as Jenkins, Tekton, GitOps, etc. | [v0.12](../../amamba/intro/release-notes.md#v012) |
| Multicloud Management | Centralized management of application orchestration of multicloud, hybrid cloud, and cross-cloud resources, with multicloud disaster recovery and fault recovery capabilities | [v0.5](../../kairship/intro/release-notes.md# v05) |
| Microservice Engine | Provide registration discovery, service governance, configuration management, microservice gateway and other governance capabilities | [v0.16](../../skoala/intro/release-notes.md#v016) |
| Service Mesh | A next-generation service mesh for cloud-native applications based on Istio open source technology | [v0.12](../../mspider/intro/release-notes.md#v012) |
| middleware Elasticsearch | current preferred full-text search engine | [v0.4](../../middleware/elasticsearch/release-notes.md#v04) |
| Middleware Kafka | Distributed message queue service based on open source software Kafka | [v0.2](../../middleware/kafka/release-notes.md#v02) |
| Middleware MinIO | A very popular lightweight, open source object storage solution | [v0.2](../../middleware/minio/release-notes.md#v02) |
| Middleware MySQL | The most widely used open source relational database | [v0.5](../../middleware/mysql/release-notes.md#v05) |
| Middleware RabbitMQ | Open source message broker software implementing the Advanced Message Queuing Protocol (AMQP) | [v0.7](../../middleware/rabbitmq/release-notes.md#v07) |
| Middleware Redis | An in-memory database caching service | [v0.4](../../middleware/redis/release-notes.md#v04) |
| Container Registry | Images for storing K8s, DevOps, and container application development | [Release Notes](../../kangaroo/release-notes.md) |
| Network | Support multiple CNI combinations for different Linux kernels | [Release Notes](../../network/modules/spiderpool/releasenotes.md) |
| Storage | Provide unified data storage services, support files, objects, blocks, and local storage, and easily access storage vendor solutions | [Release Notes](../../storage/hwameistor/releasenotes.md) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)