---
date: 2024-01-09
hide:
  - navigation
---

# DCE 5.0 Community v0.14.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Community.

[Return to Download Guide](../index.md){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.14.0-amd64.tar | v0.14.0 | AMD64 | 7.3 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.14.0-amd64.tar) | 2024-01-09 |
| offline-community-v0.14.0-arm64.tar | v0.14.0 | ARM64 | 6.9 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.14.0-arm64.tar) | 2024-01-09 |

## Verification

Go to the offline installation package download directory.

=== "AMD64"

    Run the following command to verify the installation package:

    ```sh
    echo "e29a7441c5bba74a76b2ca22c698c86d8720d89b40eddab2d0eedcddad79ebfdc5c91cc0b743f714102a279f26985f14e3e1691bf91d78dd617c135dcf7204ff  offline-community-v0.14.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.14.0-amd64.tar: OK
    ```

=== "ARM64"

    Run the following command to verify the installation package:

    ```sh
    echo "e793ff6ee9f2ea69f4a4c7e7c1a75e303098f9125a89360a6ca9b355e53b419e5029f721a608aa4c83921eb047098c436288653f25b900cb8cc32989c965d466  offline-community-v0.14.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.14.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.14.0-amd64.tar
    ```

=== "ARM64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.14.0-arm64.tar
    ```

- For installation instructions, refer to [Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [apply for a free community experience](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, personalized appearance settings, etc. | [0.23.0](../../ghippo/intro/release-notes.md#0230) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and other core Kubernetes functionalities. | [0.24.1](../../kpanda/intro/release-notes.md#0241) |
| Observability | Provides rich dashboards, scene monitoring, data querying, and alarm information. | [0.23.0](../../insight/intro/releasenote.md#0230) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
