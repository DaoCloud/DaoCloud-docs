---
date: 2023-01-05
---

# DCE Community v0.4.0-rc2

This page can download the offline installation package and verification file of DCE Community.

## Download

| File Name | Version | Architecture | File Size | Downloads | Date Updated |
| ----------------------------- | ------- | -------- | -- ----------------------------------------------- | ----- ----- | -------------------------------- |
| offline-community-v0.4.0-rc2-amd64.tar | v0.4.0-rc2 | AMD64 | 5.73GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.4.0-rc2-amd64.tar) | 2023-01-05 |
| offline-community-v0.4.0-rc2-arm64.tar | v0.4.0-rc2 | ARM64 | 5.16GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.4.0-rc2-arm64.tar) | 2023-01-05 |

## Verification

Go to the download directory of the offline installation package.

=== "AMD64"

     run the following command to verify the installation package:

     ```sh
     echo "a9501539eb5e0241e4c3035e0870637d770b12e18971cb5dae1288682db4aa299fe42c964f556fa80d27e2ea6723b65a741f11f7a5f3696915c0a4f970154 80e offline-community-v0.4.0-rc2-amd64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-community-v0.4.0-rc2-amd64.tar: OK
     ```

=== "ARM64"

     run the following command to verify the installation package:

     ```sh
     echo "7f79739afd14804172d876d8421b6768ce2d040f225b9d251bdd21118fa58ec9d82204a7a3f660d3673afc77b6be838d60f710a357b047bdbf8b65addd0e5977 offline-community-v0.4.0-rc2-arm64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-community-v0.4.0-rc2-arm64.tar: OK
     ```

## Install

After successfully verifying the offline package,

=== "AMD64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-community-v0.4.0-rc2-amd64.tar
     ```

=== "ARM64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-community-v0.4.0-rc2-arm64.tar
     ```

- For installation, please refer to [Community Package Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, please [apply for free community experience](../../dce/license0.md)

## Modules

DCE Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------------------------------------- ------------------------- | ------------------------ ------------------------------------- |
| Global Management | Responsible for user access control, permissions, enterprise space, audit logs, personalized appearance settings, etc. | [v0.11](../../ghippo/intro/release-notes.md#v011) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [v0.12](../../kpanda/intro/release-notes.md#v012) |
| Observability | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [v0.11](../../insight/intro/releasenote.md#v011) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)