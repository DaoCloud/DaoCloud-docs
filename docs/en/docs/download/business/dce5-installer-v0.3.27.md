---
date: 2022-11-23
hide:
  - navigation
---

# DCE 5.0 Enterprise v0.3.27

This page can download the offline installation package and verification file of DCE 5.0 Enterprise.

[Return to Download Index](../index.md#download-enterprise-package){ .md-button }
[More Historical Versions](./dce5-installer-history.md){ .md-button }

## Download

| File name | Package |
| ------------------- | ----------------------------- -------------------------------------------------- --------------------- |
| offline-v0.3.27.tar | [:arrow_down: Download](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.3.27.tar) |

## Verification

Go to the download directory of the offline installation package. run the following command to verify the installation package:

```sh
echo "f637ec103af6e77d1af85bf0708bef71aee123ce4ac71c4a0adef539492cdbb1661a479d3e999cd51aa7cb47d49e001565908b237ef7999140e3435f6219bb08 offline -v0.3.27.tar" | sha512sum -c
```

If the validation is successful, it will print:

```none
offline-v0.3.27.tar: OK
```

## Install

After successfully verifying the offline package, please refer to [Enterprise Package installation process](../../install/commercial/start-install.md) to install.

After successful installation, please contact us for authorization: email info@daocloud.io or call 400 002 6898.

## Modules

The DCE 5.0 Enterprise includes the following modules, which are plug-and-play on-demand to meet various use cases:

| Modules | Introduction | What's New |
| ---------- | -------------------------------------- ---------------------------------- | --------------- ---------------------------------------------- |
| Global Management | Responsible for user access control, permissions, enterprise space, audit logs, personalized appearance settings, etc. | [Release Notes](../../ghippo/intro/release-notes.md) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [v0.12.0](../../kpanda/intro/release-notes.md#v0120) |
| Observability | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [v0.11.1](../../insight/intro/releasenote.md#v0111) |
| Workbench | A container-based DevOps application platform that supports pipeline operations such as Jenkins, Tekton, GitOps, etc. | [Release Notes](../../amamba/intro/release-notes.md) |
| Multicloud Management | Centralized management of application orchestration of multicloud, hybrid cloud, and cross-cloud resources, with multicloud disaster recovery and fault recovery capabilities | [v0.3.0](../../kairship/intro/release-notes.md) |
| Microservice Engine | Provides governance capabilities such as registration discovery, service governance, configuration management, and microservice gateway | [Release Notes](../../skoala/intro/release-notes.md) |
| Service Mesh | A next-generation service mesh for cloud native applications based on Istio open source technology | [v0.10.0](../../mspider/intro/release-notes.md) |
| Middleware | Contains selected middleware such as RabbitMQ, Kafka, Elasticsearch, MySQL, Redis, MinIO, etc. | [Release Notes](../../middleware/index.md) |
| Container Registry | Images for storing K8s, DevOps, and container application development | [Release Notes](../../kangaroo/intro/release-notes.md) |
| Network | Support multiple CNI combinations for different Linux kernels | [Release Notes](../../network/modules/spiderpool/releasenotes.md) |
| Storage | Provide unified data storage services, support files, objects, blocks, and local storage, and easily access storage vendor solutions | [Release Notes](../../storage/hwameistor/releasenotes.md) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
