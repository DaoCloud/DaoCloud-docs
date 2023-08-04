---
date: 2023-01-03
---

# DCE 5.0 Community Package v0.3.30

This page can download the offline installation package and verification file of DCE 5.0 Community Package.

## Download

| File Name | Version | Architecture | File Size | Downloads | Date Updated |
| ----------------------------- | ------- | -------- | -- ----------------------------------------------- | ----- ----- | -------------------------------- |
| offline-community-v0.3.30-amd64.tar | v0.3.30 | AMD64 | 5.73GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.3.30-amd64.tar) | 2023-01-03 |
| offline-community-v0.3.30-arm64.tar | v0.3.30 | ARM64 | 5.16GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.3.30-arm64.tar) | 2023-01-03 |

## Verification

Go to the download directory of the offline installation package.

=== "AMD64"

     run the following command to verify the installation package:

     ```sh
     echo "469c98d6a60c7055f3e4159ffcdb6f65bb44cade4345400ad1b4067f8c3c89ef057983accaf413f76dc71b9a5592e0ef97600fa731bd715acacbdab1c653601b offline-com munity-v0.3.30-amd64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-community-v0.3.30-amd64.tar: OK
     ```

=== "ARM64"

     run the following command to verify the installation package:

     ```sh
     echo "9d965d49d3b09231fadae7fe713da7284b408e36f6d24d2863678dc4edf239abedc68a47e5d020bf02688ad197803a908db379e481340e13c86735fa29fd8d14 offline-community-v0.3.30-arm64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-community-v0.3.30-arm64.tar: OK
     ```

## Install

After successfully verifying the offline package,

=== "AMD64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-community-v0.3.30-amd64.tar
     ```

=== "ARM64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-community-v0.3.30-arm64.tar
     ```

- For installation, please refer to [Community Package Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, please [apply for free community experience](../../dce/license0.md)

## Modules

DCE 5.0 Community Package includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------------------------------------- ------------------------- | ------------------------ ------------------------------------- |
| Global Management | Responsible for user access control, permissions, enterprise space, audit logs, personalized appearance settings, etc. | [v0.13](../../ghippo/intro/release-notes.md#v013) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [v0.14](../../kpanda/intro/release-notes.md#v014) |
| Observability | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [v0.13](../../insight/intro/releasenote.md#v013) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)