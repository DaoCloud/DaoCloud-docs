---
date: 2023-11-08
hide:
  - navigation
---

# DCE 5.0 Community v0.12.0

This page provides downloads for the offline package and checksum files for DCE 5.0 Community.

[Return to Download Index](../index.md){ .md-button }
[More Historical Versions](./dce5-installer-history.md){ .md-button }

## Downloads

| Filename | Version | Architecture | File Size | Download | Update Date |
| -------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.12.0-amd64.tar | v0.12.0 | AMD 64 | 6.03 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.12.0-amd64.tar) | 2023-09-08 |
| offline-community-v0.12.0-arm64.tar | v0.12.0 | <font color="green">ARM 64</font> | 5.65 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.12.0-arm64.tar) | 2023-09-08 |

## Validation

Navigate to the directory where the offline package is downloaded.

=== "AMD64"

    Run the following command to validate the package:

    ```sh
    echo "6a2bc869f2ec916dff35a5a473f13dcccef8126d664089ea0465e1a343eececf5a357520244990c765c9de608b765e26b8950bf0322b26b5e53491826d1d919a  offline-v0.12.0-amd64.tar" | sha512sum -c
    ```

    If the validation is successful, the output will be:

    ```none
    offline-community-v0.12.0-amd64.tar: OK
    ```

=== "ARM64"

    Run the following command to validate the package:

    ```sh
    echo "c7fba9dfe0979caa2910b9aa2674e3a744455b185f9ee8e70264d8833e962df3361fb85d9d5d33be8fc643e36d9929e3d7af37ead66e7d30483d76dc77faa04c  offline-v0.12.0-arm64.tar" | sha512sum -c
    ```

    If the validation is successful, the output will be:

    ```none
    offline-community-v0.12.0-arm64.tar: OK
    ```

## Installation

After the offline package has been successfully validated,

=== "AMD64"

    Run the following command to extract the tar package:

    ```sh
    tar -zxvf offline-community-v0.12.0-amd64.tar
    ```

=== "ARM64"

    Run the following command to extract the tar package:

    ```sh
    tar -zxvf offline-community-v0.12.0-arm64.tar
    ```

- For installation instructions, refer to the [Community Installation Guide](../../install/community/k8s/online.md#_2).
- After successful installation, [apply for a free community experience](../../dce/license0.md).

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, enterprise spaces, audit logs, personalized appearance settings, etc. | [0.21.0](../../ghippo/intro/release-notes.md#0210) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and other core Kubernetes features. | [0.22.0](../../kpanda/intro/release-notes.md#0220) |
| Insight | Provides rich dashboards, scenario monitoring, data querying, alerts, and other graphical and textual information. | [0.21.1](../../insight/intro/releasenote.md#insight-server-v0210) |

## More

- [Online Documentation](../../dce/index.md)
- [Report Bugs](https://github.com/DaoCloud/DaoCloud-docs/issues)
