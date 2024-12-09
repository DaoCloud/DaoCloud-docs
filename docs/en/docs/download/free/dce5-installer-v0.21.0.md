---
MTPE: windsonsea
date: 2024-09-09
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.21.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Community.

[Return to Download Guide](../index.md){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.21.0-amd64.tar | v0.21.0 | AMD 64 | 7.68 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.21.0-amd64.tar) | 2024-08-09 |
| offline-community-v0.21.0-arm64.tar | v0.21.0 | <font color="green">ARM 64</font> | 7.29 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.21.0-arm64.tar) | 2024-08-09 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "318755dd2dfc5587e03d6299858e25ea5c4031c535bee5481ae5a54f0c6531104506a42414cd07c4bf1ee86d38d240bf158e00f95a8fc32bbe0d50f87bead014  offline-community-v0.21.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.21.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "53b5eed76284f4a03c5bb34160c30c65ef1703f206653cdba4eb81fcb204e57ad55991cdf89bbc4ecb3e64fbbb172dba501e8e36cd176e4d005b996c4c0e0043  offline-community-v0.21.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.21.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.21.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.21.0-arm64.tar
    ```

- For installation instructions, refer to [Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [apply for a free community experience](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, and custom appearance. | [0.30.0](../../ghippo/intro/release-notes.md#v0300) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and more Kubernetes features. | [0.31.1](../../kpanda/intro/release-notes.md#v0310) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alert information. | [0.30.1](../../insight/intro/release-notes.md#v0300) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
