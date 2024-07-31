---
MTPE: windsonsea
date: 2024-07-09
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.19.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Community.

[Return to Download Guide](../index.md){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.19.0-amd64.tar | v0.19.0 | AMD 64 | 7.56 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.19.0-amd64.tar) | 2024-07-09 |
| offline-community-v0.19.0-arm64.tar | v0.19.0 | <font color="green">ARM 64</font> | 7.17 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.19.0-arm64.tar) | 2024-07-09 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "c8590de895266adf7492baab3e6634ff0a204c0000ff651b08d9c65460e8bf528a745e580cf5e25bbb5011ff39723d9ad41039c759c94211584f770f59901e89  offline-community-v0.19.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.19.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "9b70bb3df3b82f9f4f1e6a51425be1b23e0ab34c7032aa3d59ab10fda07a48ff8dd3c12addb1bb7b0b158a52e61980c595822269e319918d341a535d77bd83af  offline-community-v0.19.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.19.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.19.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.19.0-arm64.tar
    ```

- For installation instructions, refer to [Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [apply for a free community experience](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, personalized appearance settings, etc. | [0.28.0](../../ghippo/intro/release-notes.md#0280) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and other core Kubernetes functionalities. | [0.29.1](../../kpanda/intro/release-notes.md#0291) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alarm information. | [0.28.0](../../insight/intro/releasenote.md#0280) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
