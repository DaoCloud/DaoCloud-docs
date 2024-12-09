---
MTPE: windsonsea
date: 2024-08-14
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.20.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Community.

[Return to Download Guide](../index.md){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.20.0-amd64.tar | v0.20.0 | AMD 64 | 7.68 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.20.0-amd64.tar) | 2024-08-09 |
| offline-community-v0.20.0-arm64.tar | v0.20.0 | <font color="green">ARM 64</font> | 7.29 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.20.0-arm64.tar) | 2024-08-09 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "f673e53594e89f657755db0a6fd57857d8445f4ccdc49e9f4d8582f04eacc951ed0bfc619601a0a04a43862e2058babaab82317dd7b32672ecf95a1ea9f49b14  offline-community-v0.20.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.20.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "d22cd4e867953e9004e569236c5cddac54a864fdc5d425de5be43bfc9fafc7cc8abf2fb02392b59fd24a0d54e4e176268a77c70cb0071db570ef1277c36f8233  offline-community-v0.20.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.20.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.20.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.20.0-arm64.tar
    ```

- For installation instructions, refer to [Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [apply for a free community experience](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, and custom appearance. | [0.29.0](../../ghippo/intro/release-notes.md#v0290) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and more Kubernetes features. | [0.30.1](../../kpanda/intro/release-notes.md#v0300) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alert information. | [0.29.0](../../insight/intro/release-notes.md#v0290) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
