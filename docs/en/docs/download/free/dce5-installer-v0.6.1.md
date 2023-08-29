---
date: 2023-04-12
---

# DCE 5.0 Community Package v0.6.1

This page can download the offline installation package and verification file of DCE 5.0 Community Package.

## Download

| File Name | Version | Architecture | File Size | Downloads | Date Updated |
| ----------------------------- | ------- | -------- | -- ----------------------------------------------- | ----- ----- | -------------------------------- |
| offline-community-v0.6.1-amd64.tar | v0.6.1 | AMD64 | 5.89GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.6.1-amd64.tar) | 2023-04-12 |
| offline-community-v0.6.1-arm64.tar | v0.6.1 | ARM64 | 5.52GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.6.1-arm64.tar) | 2023-04-12 |

## Verification

Go to the download directory of the offline installation package.

=== "AMD64"

     run the following command to verify the installation package:

     ```sh
     echo "f452f0b5757220b7630334916209275207c7f4672da80bb2de721d186f57bfc5744155a514a88f0271ec9a02f90f831baa4bcb32fd3b169d0255773916f1 0c32 offline-community-v0.6.1-amd64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-community-v0.6.1-amd64.tar: OK
     ```

=== "ARM64"

     run the following command to verify the installation package:

     ```sh
     echo "2036e4b4a0d0fa9016b6bc0ceb28b2f6dd7ec9f856f2ef976dacdedd8d9e0500dbf47c7f070d70954fc9a3fd6adf060e550cf52a2343443531c85493e308de9f off line-community-v0.6.1-arm64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-community-v0.6.1-arm64.tar: OK
     ```

## Install

After successfully verifying the offline package,

=== "AMD64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-community-v0.6.1-amd64.tar
     ```

=== "ARM64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-community-v0.6.1-arm64.tar
     ```

- For installation, please refer to [Community Package Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, please [apply for free community experience](../../dce/license0.md)

## Modules

DCE 5.0 Community Package includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------------------------------------- ------------------------- | ------------------------ ------------------------------------- |
| Global Management | Responsible for user access control, permissions, enterprise space, audit logs, personalized appearance settings, etc. | [0.15.0](../../ghippo/intro/release-notes.md#0150) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [0.16.1](../../kpanda/intro/release-notes.md#0161) |
| Observability | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [0.15.4](../../insight/intro/releasenote.md#0154) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)