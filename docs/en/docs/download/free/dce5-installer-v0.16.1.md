---
MTPE: windsonsea
date: 2024-04-10
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.16.1

This page provides downloads for the offline installation package and verification files for DCE 5.0 Community.

[Return to Download Guide](../index.md){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.16.1-amd64.tar | v0.16.1 | AMD 64 | 7.50 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.16.1-amd64.tar) | 2024-04-09 |
| offline-community-v0.16.1-arm64.tar | v0.16.1 | <font color="green">ARM 64</font> | 7.05 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.16.1-arm64.tar) | 2024-04-09 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "e21ba57969b765b0d34645150af38b4870939edd49e49426842703bb34b6459526ba9e472242a0604a8d882f5c341cd5a725268ced9c9941f8aaad7d187dfe8c  offline-community-v0.16.1-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.16.1-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "46a1252dd68194699ce27ac821f939c57eccc9ff8979be30b8b65554b4a1ac169960e6493bfebf5f523d059622d7ce4a5388763295383cc7fde36113ee76b87b  offline-community-v0.16.1-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.16.1-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.16.1-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.16.1-arm64.tar
    ```

- For installation instructions, refer to [Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [apply for a free community experience](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, personalized appearance settings, etc. | [0.25.1](../../ghippo/intro/release-notes.md#0251) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and other core Kubernetes functionalities. | [0.26.1](../../kpanda/intro/release-notes.md#0261) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alarm information. | [0.25.3](../../insight/intro/releasenote.md#0253) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
