---
MTPE: windsonsea
date: 2024-05-11
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.17.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Community.

[Return to Download Guide](../index.md){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.17.0-amd64.tar | v0.17.0 | AMD 64 | 7.61 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.17.0-amd64.tar) | 2024-05-09 |
| offline-community-v0.17.0-arm64.tar | v0.17.0 | <font color="green">ARM 64</font> | 7.21 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.17.0-arm64.tar) | 2024-05-09 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "2c88ae3bad973140cccf5019f0bcee87e12795d644bd101111d1436080ce95d5281d33fcf28df50da0718b28fb42ee82f3ea8dea2ddcdc723e6258e26411396f  offline-community-v0.17.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.17.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "b3f6d61fa072de06b7daa142238d2a02716c28588e63ebe632a45b4933a4e481f4049318b7facf0c6c235d3810ed8628b33f59543d2579e5df3d8e9d0aefffa3  offline-community-v0.17.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.17.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.17.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.17.0-arm64.tar
    ```

- For installation instructions, refer to [Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [apply for a free community experience](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, personalized appearance settings, etc. | [0.26.0](../../ghippo/intro/release-notes.md#0260) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and other core Kubernetes functionalities. | [0.27.0](../../kpanda/intro/release-notes.md#0270) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alarm information. | [0.26.0](../../insight/intro/releasenote.md#0260) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
