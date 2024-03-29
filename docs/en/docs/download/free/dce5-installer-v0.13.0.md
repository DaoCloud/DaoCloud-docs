---
date: 2023-12-07
hide:
  - navigation
---

# DCE 5.0 Community v0.13.0

This page provides offline installation packages and verification files for DCE 5.0 Community.

[Return to Download Guide](../index.md){ .md-button } [More Historical Versions](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| -------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.13.0-amd64.tar | v0.13.0 | AMD 64 | 6.96 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.13.0-amd64.tar) | 2023-12-07 |
| offline-community-v0.13.0-arm64.tar | v0.13.0 | <font color="green">ARM 64</font> | 6.57 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.13.0-arm64.tar) | 2023-12-07 |

## Verification

Go to the directory where the offline installation package is downloaded.

=== "AMD64"

    Run the following command to verify the installation package:

    ```sh
    echo "18e286418b6aa0da03280fd5e2745f1aa2cfc9c0e8b09a7c76f0a397e4eafb2c06f9f3344d19df2a85b739a961f8f1957d2d91c4a04239fd44dc15cb3d4a52ab  offline-community-v0.13.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, it will print:

    ```none
    offline-community-v0.13.0-amd64.tar: OK
    ```

=== "ARM64"

    Run the following command to verify the installation package:

    ```sh
    echo "bde7028f83e58ff6a8211b0b5339ecb98b4014c0325b93d101c06cffc5766cd2ea59b9b8a148fab7007c88b861eb9e63278bb489d78ad0a097117efa1f39018f  offline-community-v0.13.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, it will print:

    ```none
    offline-community-v0.13.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD64"

    Run the following command to extract the tar package:

    ```sh
    tar -zxvf offline-community-v0.13.0-amd64.tar
    ```

=== "ARM64"

    Run the following command to extract the tar package:

    ```sh
    tar -zxvf offline-community-v0.13.0-arm64.tar
    ```

- For installation instructions, refer to [Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [Apply for a Free Community Experience](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, personalized appearance settings, etc. | [0.22.1](../../ghippo/intro/release-notes.md#0221) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and other core Kubernetes features | [0.23.0](../../kpanda/intro/release-notes.md#0230) |
| Observability | Provides rich dashboards, scenario monitoring, data queries, alerts, and other graphical and textual information | [0.22.0](../../insight/intro/releasenote.md#0220) |

## More

- [Online Documentation](../../dce/index.md)
- [Report Bugs](https://github.com/DaoCloud/DaoCloud-docs/issues)
