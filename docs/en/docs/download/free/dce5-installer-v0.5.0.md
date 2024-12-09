---
MTPE: windsonsea
date: 2023-03-06
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.5.0

This page allows you to download the offline package and checksum file of DCE 5.0 Community.

[Return to Download Index](../index.md){ .md-button }
[Legacy Packages](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| -------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.5.0-amd64.tar | v0.5.0 | AMD 64 | 5.62 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.5.0-amd64.tar) | 2023-03-06 |
| offline-community-v0.5.0-arm64.tar | v0.5.0 | <font color="green">ARM 64</font> | 5.27 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.5.0-arm64.tar) | 2023-03-06 |

## Verification

Go to the download directory of the offline package.

=== "AMD 64"

     run the following command to verify the offline package:

     ```sh
     echo "1c8b629dc6f842a6406a198ee5bffd2f751464745b9f4b4ef8899492691a58bdf5e0b204df6cb013285f0326a709ea10fff1c7d71ea88fe7f17b3f820c8503 61 offline-community-v0.5.0-amd64.tar" | sha512sum -c
     ```

     If the verification is successful, it will print:

     ```none
     offline-community-v0.5.0-amd64.tar: OK
     ```

=== "<font color="green">ARM 64</font>"

     run the following command to verify the offline package:

     ```sh
     echo "4f060c189b29b3d08bce8287db48232809220162574a59fbd8050ffca414f0d0ba3adf3d68cb2f66fe868aab4059fa3c205bcb7058952d6df51acc23cac32c40 off line-community-v0.5.0-arm64.tar" | sha512sum -c
     ```

     If the verification is successful, it will print:

     ```none
     offline-community-v0.5.0-arm64.tar: OK
     ```

## Installation

After the offline package has been successfully verifyd,

=== "AMD 64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-community-v0.5.0-amd64.tar
     ```

=== "<font color="green">ARM 64</font>"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-community-v0.5.0-arm64.tar
     ```

- For installation, refer to [DCE 5.0 Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [Free Trial](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, and custom appearance. | [0.14.0](../../ghippo/intro/release-notes.md#v0140) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [0.15.1](../../kpanda/intro/release-notes.md#v0150) |
| Insight | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [0.14.6](../../insight/intro/release-notes.md#v0146) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)