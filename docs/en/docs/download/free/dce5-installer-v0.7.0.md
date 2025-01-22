---
MTPE: windsonsea
date: 2023-05-09
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.7.0

This page allows you to download the offline package and checksum file of DCE 5.0 Community.

[Return to Download Index](../index.md){ .md-button }
[Legacy Packages](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| -------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.7.0-amd64.tar | v0.7.0 | AMD 64 | 5.96 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.7.0-amd64.tar) | 2023-05-09 |
| offline-community-v0.7.0-arm64.tar | v0.7.0 | <font color="green">ARM 64</font> | 5.60 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.7.0-arm64.tar) | 2023-05-09 |

## Verification

Go to the download directory of the offline package.

=== "AMD 64"

     run the following command to verify the offline package:

     ```sh
     echo "e80596e138a932d0d28101440ae22fbb319f048ad92043507e0202696ebc4a39717e65cbc12b6a6c02f5c9eb8c9fe7d027f381f037b6ae5dc1c21af00106e 2b7 offline-community-v0.7.0-amd64.tar" | sha512sum -c
     ```

     If the verification is successful, it will print:

     ```none
     offline-community-v0.7.0-amd64.tar: OK
     ```

=== "<font color="green">ARM 64</font>"

     run the following command to verify the offline package:

     ```sh
     echo "3f68086d55ba413473eb3abae5756779ef22bc264950d0a3ef21714977463e3ac7fa01a574a0488f3a547fc6a2c9d0b979e1e3a02c9632b222f879c5e0a32b 78 offline-community-v0.7.0-arm64.tar" | sha512sum -c
     ```

     If the verification is successful, it will print:

     ```none
     offline-community-v0.7.0-arm64.tar: OK
     ```

## Installation

After the offline package has been successfully verifyd,

=== "AMD 64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-community-v0.7.0-amd64.tar
     ```

=== "<font color="green">ARM 64</font>"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-community-v0.7.0-arm64.tar
     ```

- For installation, refer to [DCE 5.0 Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [Free Trial](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, and custom appearance. | [0.16.1](../../ghippo/intro/release-notes.md#v0161) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [0.17.0](../../kpanda/intro/release-notes.md#v0170) |
| Insight | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [0.16.1](../../insight/intro/release-notes.md#v0160) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)