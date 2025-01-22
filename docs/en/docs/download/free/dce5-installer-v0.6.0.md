---
MTPE: windsonsea
date: 2023-04-07
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.6.0

This page allows you to download the offline package and checksum file of DCE 5.0 Community.

[Return to Download Index](../index.md){ .md-button }
[Legacy Packages](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| -------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.6.0-amd64.tar | v0.6.0 | AMD 64 | 5.89 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.6.0-amd64.tar) | 2023-04-07 |
| offline-community-v0.6.0-arm64.tar | v0.6.0 | <font color="green">ARM 64</font> | 5.52 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.6.0-arm64.tar) | 2023-04-07 |

## Verification

Go to the download directory of the offline package.

=== "AMD 64"

     run the following command to verify the offline package:

     ```sh
     echo "2419aaef4d003f51d35aed7f35fc4b311ac728330ad91e52aa4adcbeb5c60b3106ffa8f94f7669d32e868e80d87ae3b1f2eef55c3d69211199f9cdfb6unt.vm-v804 offline-am" | sha512sum -c
     ```

     If the verification is successful, it will print:

     ```none
     offline-community-v0.6.0-amd64.tar: OK
     ```

=== "<font color="green">ARM 64</font>"

     run the following command to verify the offline package:

     ```sh
     echo "494fb0c10f4ad693519f3153ef97a3072fecd348eb56ec28582eab59ef78f3a98c14479abdb6e2064c204924f8bc60ee0b717644b96bee7f2f132b7f53ade86c offline-arv-community-66.5" 2sum -c
     ```

     If the verification is successful, it will print:

     ```none
     offline-community-v0.6.0-arm64.tar: OK
     ```

## Installation

After the offline package has been successfully verifyd,

=== "AMD 64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-community-v0.6.0-amd64.tar
     ```

=== "<font color="green">ARM 64</font>"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-community-v0.6.0-arm64.tar
     ```

- For installation, refer to [DCE 5.0 Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [Free Trial](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, and custom appearance. | [0.15.0](../../ghippo/intro/release-notes.md#v0150) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [0.16.0](../../kpanda/intro/release-notes.md#v0160) |
| Insight | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [0.15.4](../../insight/intro/release-notes.md#v0154) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
