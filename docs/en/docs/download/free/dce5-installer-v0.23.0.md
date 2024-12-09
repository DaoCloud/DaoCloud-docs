---
MTPE: windsonsea
date: 2024-12-02
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.23.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Community.

[Return to Download Guide](../index.md){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.23.0-amd64.tar | v0.23.0 | AMD 64 | 7.85GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.23.0-amd64.tar) | 2024-11-11 |
| offline-community-v0.23.0-arm64.tar | v0.23.0 | <font color="green">ARM 64</font> | 7.38GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.23.0-arm64.tar) | 2024-11-11 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "ff2d8f143be1abcd5833fe334f0d2f8414b1411cc0c314f1ab230816cf45136e794ece9a4ca89007ff654a6915ac80be416dd4f1acca0f6323a2be7d9070f169  offline-community-v0.23.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.23.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "a4c3901d7d84f1691abeeb825a23338c0eb32aa8c751062fe2d4540fafbea168401bfa7c9e9827ce8d35dcb30b7e44ac30bc833ccbcaed0e36c2f086bcab1ca6  offline-community-v0.23.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.23.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.23.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.23.0-arm64.tar
    ```

- For installation instructions, refer to [Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [apply for a free community experience](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, and custom appearance. | [0.32.0](../../ghippo/intro/release-notes.md#v0320) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and more Kubernetes features. | [0.33.2](../../kpanda/intro/release-notes.md#v0332) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alert information. | [0.32.2](../../insight/intro/release-notes.md#v0322) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
