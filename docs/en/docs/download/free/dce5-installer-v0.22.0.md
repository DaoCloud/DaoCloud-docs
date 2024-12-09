---
MTPE: windsonsea
date: 2024-10-10
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.22.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Community.

[Return to Download Guide](../index.md){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.22.0-amd64.tar | v0.22.0 | AMD 64 | 7.68 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.22.0-amd64.tar) | 2024-10-10 |
| offline-community-v0.22.0-arm64.tar | v0.22.0 | <font color="green">ARM 64</font> | 7.29 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.22.0-arm64.tar) | 2024-10-10 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "bcb9e42952889a428b28b8b60c2afa1791781981e3652cc4292d4107d29e483e940678c2a7e2f790264cb90c72a72721a82986d8107931202ec3a3c7f407b8e3  offline-community-v0.22.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.22.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "2e7b6e4f2a325adf6f68e94e34615a73e509a01253a0ce2357fe1fee89eb851a2f86f6798c813812eced407e30ea5d246ae386dde50b0ac4262517946b0fe846  offline-community-v0.22.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.22.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.22.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.22.0-arm64.tar
    ```

- For installation instructions, refer to [Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [apply for a free community experience](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, and custom appearance. | [0.31.0](../../ghippo/intro/release-notes.md#v0310) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and more Kubernetes features. | [0.32.2](../../kpanda/intro/release-notes.md#v0320) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alert information. | [0.31.0](../../insight/intro/release-notes.md#v0310) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
