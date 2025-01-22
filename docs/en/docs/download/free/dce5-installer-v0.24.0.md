---
MTPE: windsonsea
date: 2024-12-09
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.24.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Community.

[Return to Download Guide](../index.md){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.24.0-amd64.tar | v0.24.0 | AMD 64 | 8.65 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.24.0-amd64.tar) | 2024-12-09 |
| offline-community-v0.24.0-arm64.tar | v0.24.0 | <font color="green">ARM 64</font> | 8.14 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.24.0-arm64.tar) | 2024-12-09 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "38f6b313ef8d043e5b435429bea11e728dd93bd289a268bc620370f947b741cee88b7f2c8f1617238f6b2da5414ebb58aa8d90f45d64652b34b3134a33091f7a  offline-community-v0.24.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.24.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "0ea15822b60fe07d4fab654ff7c009fad53f57636b44d523c15b6c81996d3a3d56c14d547c56df48a11de1c522c9b1960c62bb612b93a45bf947d19823ceec25  offline-community-v0.24.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.24.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.24.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.24.0-arm64.tar
    ```

- For installation instructions, refer to [Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [apply for a free community experience](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, and custom appearance. | [0.33.0](../../ghippo/intro/release-notes.md#v0330) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and more Kubernetes features. | [0.34.0](../../kpanda/intro/release-notes.md#v0340) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alert information. | [0.33.1](../../insight/intro/release-notes.md#v0331) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
