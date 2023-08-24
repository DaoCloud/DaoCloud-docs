---
date: 2023-01-05
---

# DCE 5.0 Enterprise v0.4.0-rc2

This page can download the offline installation package and verification file of DCE 5.0 Enterprise.

## Download

| File Name | Version | Architecture | File Size | Downloads | Date Updated |
| ----------------------------- | ------- | -------- | -- ----------------------------------------------- | ----- ----- | -------------------------------- |
| offline-centos7-v0.4.0-rc2-amd64.tar | v0.4.0-rc2 | AMD64 | 16.33GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-centos7-v0.4.0-rc2-amd64.tar) | 2023-01-05 |
| offline-kylin-v10sp2-v0.4.0-rc2-arm64.tar | v0.4.0-rc2 | ARM64 | 14.96GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-kylin-v10sp2-v0.4.0-rc2-arm64.tar) | 2023-01-05 |

## Verification

Go to the download directory of the offline installation package.

=== "AMD64"

     run the following command to verify the installation package:

     ```sh
     echo "9fdc24ea0eda2994cb1ab253d3c6f079b76b138618fb5601176be5a4d660893c3cc64dfb151e32d57a1f843c6b598bed270a20654e6cd8d815c7901124b04 431 offline-centos7-v0.4.0-rc2-amd64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-centos7-v0.4.0-rc2-amd64.tar: OK
     ```

=== "ARM64"

     run the following command to verify the installation package:

     ```sh
     echo "ec6eca321a80f26f70c11739eb15dc67914579af610e2fb9cb49fcf8d9691de2ceddac7cfd8bd40ce3f3927cfea3166d15366f06909fcbbf15a330bc718fd358 off line-kylin-v10sp2-v0.4.0-rc2-arm64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-kylin-v10sp2-v0.4.0-rc2-arm64.tar: OK
     ```

## Install

After successfully verifying the offline package,

=== "AMD64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-centos7-v0.4.0-rc2-amd64.tar
     ```

=== "ARM64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-kylin-v10sp2-v0.4.0-rc2-arm64.tar
     ```

- For installation, please refer to [Enterprise Package installation process](../../install/commercial/start-install.md)
- After successful installation, please contact us for authorization: email info@daocloud.io or call 400 002 6898

## Modules

The DCE 5.0 Enterprise includes the following modules, which are plug-and-play on-demand to meet various use cases:

| Modules | Introduction | What's New |
| -------------------- | ---------------------------- ----------------------------------------------- | ----- -------------------------------------------------- ------ |
| Global Management | Responsible for user access control, permissions, enterprise space, audit logs, personalized appearance settings, etc. | [v0.11](../../ghippo/intro/release-notes.md#v011) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [v0.12](../../kpanda/intro/release-notes.md#v012) |
| Observability | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [v0.11](../../insight/intro/releasenote.md#v011) |
| Workbench | A container-based DevOps application platform that supports pipeline operations such as Jenkins, Tekton, GitOps, etc. | [v0.9](../../amamba/intro/release-notes.md#v09) |
| Multicloud Management | Centralized management of application orchestration of multicloud, hybrid cloud, and cross-cloud resources, with multicloud disaster recovery and fault recovery capabilities | [v0.3](../../kairship/intro/release-notes.md# v03) |
| Microservice Engine | Provides governance capabilities such as registration discovery, service governance, configuration management, and microservice gateway | [v0.11](../../skoala/intro/release-notes.md#v011) |
| Service Mesh | A next-generation service mesh for cloud-native applications based on Istio open source technology | [v0.10](../../mspider/intro/release-notes.md#v010) |
| Middleware Elasticsearch | Currently preferred full-text search engine | [v0.3](../../middleware/elasticsearch/release-notes.md#v034) |
| Middleware Kafka | Distributed message queue service based on the open source software Kafka | [v0.1](../../middleware/kafka/release-notes.md#v012) |
| Middleware MinIO | A very popular lightweight, open source object storage solution | [v0.1](../../middleware/minio/release-notes.md#v012) |
| Middleware MySQL | The most widely used open source relational database | [v0.4](../../middleware/mysql/release-notes.md#v04) |
| Middleware RabbitMQ | Open source message broker software implementing the Advanced Message Queuing Protocol (AMQP) | [v0.6](../../middleware/rabbitmq/release-notes.md#v06) |
| Middleware Redis | An in-memory database caching service | [v0.2](../../middleware/redis/release-notes.md#v02) |
| Container Registry | Images for storing K8s, DevOps, and container application development | [Release Notes](../../kangaroo/release-notes.md) |
| Network | Support multiple CNI combinations for different Linux kernels | [Release Notes](../../network/intro/releasenotes.md) |
| Storage | Provide unified data storage services, support files, objects, blocks, and local storage, and easily access storage vendor solutions | [Release Notes](../../storage/hwameistor/releasenotes.md) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)