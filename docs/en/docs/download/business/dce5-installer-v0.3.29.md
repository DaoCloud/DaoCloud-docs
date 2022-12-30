# DCE 5.0 Commercial Edition v0.3.29

This page can download the offline installation package and verification file of DCE 5.0 commercial version.

## Download

| File Name | Version | Architecture | File Size | Downloads | Date Updated |
| ------------------- | ------- | -------- | ------------ ----------------------------------------- | ---------- | ------------------- |
| offline-centos7-v0.3.29-amd64.tar | v0.3.29 | AMD 64 | 22.9 GB | [:arrow_down: Download](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-centos7-v0.3.29-amd64.tar) | 2022-12-16 |
| offline-kylin-v10sp2-v0.3.29-arm64.tar | v0.3.29 | ARM 64 | 19.9 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5 /offline-kylin-v10sp2-v0.3.29-arm64.tar) | 2022-12-16 |

## Validation

Enter the download directory of the offline installation package.

=== "AMD 64"

    Execute the following command to verify the installation package:

    ```sh
    echo "ef7fd779d3b5bc50bccf80e29934002c60f53143319c80dd9aad85fc1404ac7d309997e0d9c829612c1b400cd4d4861fb1b6f91efee8c236ada930cbb44ca1c1  offline-centos7-v0.3.29-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, it will print:

    ```none
    offline-centos7-v0.3.29-amd64.tar: OK
    ```

=== "ARM 64"

    Execute the following command to verify the installation package:

    ```sh
    echo "1cc8b41bfaad23cb1b14170b68ee581d2eb384fe6d803ce34a1a09f1d41e7640768cca8a7f8a3f6a881ecfddaaa73756247676b6e0bc72b7ca651cc855ce2ff4  offline-kylin-v10sp2-v0.3.29-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, it will print:

    ```none
    offline-kylin-v10sp2-v0.3.29-arm64.tar: OK
    ```

## Install

After successfully verifying the offline package,

=== "AMD 64"

    Execute the following command to extract the tarball:

    ```sh
    tar -zxvf offline-centos7-v0.3.29-amd64.tar
    ```

=== "ARM 64"

    Execute the following command to extract the tarball:

    ```sh
    tar -zxvf offline-kylin-v10sp2-v0.3.29-arm64.tar
    ```

- For installation, please refer to [Commercial version installation process](../../install/commercial/start-install.md)
- After successful installation, please proceed to [genuine authorization](https://qingflow.com/f/e3291647)

## Modules

The DCE 5.0 commercial edition includes the following modules, which are plug-and-play on-demand to meet various application scenarios:

| Modules | Introduction | What's New |
| -------------------- | ---------------------------- ----------------------------------------------- | ----- -------------------------------------------------- ------ |
| Global Management | Responsible for user access control, permissions, enterprise space, audit logs, personalized appearance settings, etc. | [v0.11](../../ghippo/01ProductBrief/release-notes.md#v011) |
| Container Management | Manage K8s core functions such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [v0.12](../../kpanda/03ProductBrief/release-notes.md#v012) |
| Observability | Provide rich graphic information such as dashboards, scene monitoring, data query, and alarms | [v0.11](../../insight/03ProductBrief/releasenote.md#v011) |
| Application Workbench | A container-based DevOps application platform that supports pipeline operations such as Jenkins, Tekton, GitOps, etc. | [v0.9](../../amamba/01ProductBrief/release-notes.md#v09) |
| Multicloud orchestration| Centralized management of application orchestration of multicloud, hybrid cloud, and cross-cloud resources, with multicloud disaster recovery and fault recovery capabilities| [v0.3](../../kairship/01product/release-notes.md# v03) |
| Microservice Engine | Provides governance capabilities such as registration discovery, service governance, configuration management, and microservice gateway | [v0.11](../../skoala/intro/release-notes.md#v011) |
| Service Mesh | A next-generation service mesh for cloud-native applications based on Istio open source technology | [v0.10](../../mspider/01Intro/release-notes.md#v010) |
| Middleware Elasticsearch | Currently preferred full-text search engine | [v0.3](../../middleware/elastic-search/release-notes.md#v034) |
| Middleware Kafka | Distributed message queue service based on the open source software Kafka | [v0.1](../../middleware/kafka/release-notes.md#v012) |
| Middleware MinIO | A very popular lightweight, open source object storage solution | [v0.1](../../middleware/minio/release-notes.md#v012) |
| Middleware MySQL | The most widely used open source relational database | [v0.4](../../middleware/mysql/release-notes.md#v04) |
| Middleware RabbitMQ | Open source message broker software implementing the Advanced Message Queuing Protocol (AMQP) | [v0.6](../../middleware/rabbitmq/release-notes.md#v06) |
| Middleware Redis | An in-memory database caching service | [v0.2](../../middleware/redis/release-notes.md#v02) |
| container registry | Images for storing K8s, DevOps, and container application development | [Release Notes](../../release/rn5.0.md) |
| Network | Support multiple CNI combinations for different Linux kernels | [Release Notes](../../release/rn5.0.md) |
| Storage | Provide unified data storage services, support files, objects, blocks, and local storage, and easily access storage vendor solutions | [Release Notes](../../release/rn5.0.md) |

## More

- [Online Documentation](https://docs.daocloud.io/dce/what-is-dce/)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)