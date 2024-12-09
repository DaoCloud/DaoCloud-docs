---
MTPE: windsonsea
date: 2023-01-12
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.4.0

This page allows you to download the offline package and checksum file of DCE 5.0 Community.

[Return to Download Index](../index.md){ .md-button }
[Legacy Packages](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| -------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.4.0-amd64.tar | v0.4.0 | AMD 64 | 5.73 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.4.0-amd64.tar) | 2023-01-12 |
| offline-community-v0.4.0-arm64.tar | v0.4.0 | <font color="green">ARM 64</font> | 5.16 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.4.0-arm64.tar) | 2023-01-12 |

## Verification

Go to the download directory of the offline package.

=== "AMD 64"

     run the following command to verify the offline package:

     ```sh
     echo "41f7705d2be5487a721b936ba16b89ad2f35011b0d1a98d71d29ab51cf36ef2bf34283be384e76b0438c172ff9e236c44c33843e9855e9af253b1db4b84144fe offline-community-v0.4.0-amd64.tar" | sha512sum -c
     ```

     If the verification is successful, it will print:

     ```none
     offline-community-v0.4.0-amd64.tar: OK
     ```

=== "<font color="green">ARM 64</font>"

     run the following command to verify the offline package:

     ```sh
     echo "1d0476965fd73002c379639353b0bd0e09cefe99156ef448c42a4c10aff60a9836981c86e914ba3f614617a455b67a8c3ce4d82d53b3e47a22222c34020d0 a00 offline-community-v0.4.0-arm64.tar" | sha512sum -c
     ```

     If the verification is successful, it will print:

     ```none
     offline-community-v0.4.0-arm64.tar: OK
     ```

## Installation

After the offline package has been successfully verifyd,

=== "AMD 64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-community-v0.4.0-amd64.tar
     ```

=== "<font color="green">ARM 64</font>"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-community-v0.4.0-arm64.tar
     ```

- For installation, refer to [DCE 5.0 Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [Free Trial](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, and custom appearance. | [v0.13.2](../../ghippo/intro/release-notes.md#v0132) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [v0.14.0](../../kpanda/intro/release-notes.md#v0140) |
| Insight | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [v0.13.2](../../insight/intro/release-notes.md#v0132) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)