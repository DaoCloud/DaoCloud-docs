---
date: 2023-07-17
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.9.0

This page allows you to download the offline package and checksum files for DCE 5.0 Community.

[Return to Download Index](../index.md){ .md-button }
[More Historical Versions](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| -------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.9.0-amd64.tar   | v0.9.0  | AMD64        | 6.14 GB    | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.9.0-amd64.tar)   | 2023-07-07   |
| offline-community-v0.9.0-arm64.tar   | v0.9.0  | ARM64        | 5.77 GB    | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.9.0-arm64.tar)   | 2023-07-07   |

## Validation

Navigate to the directory where the offline package is downloaded.

=== "AMD64"

    Run the following command to validate the package:

    ```sh
    echo "b77127bbde1003501d32d58ca408c6bc6637cbe85d20696ce7403b1ded7340638cc7c7a447fe52b055ff7068e3d85399f6a68a7b9d47cd0e7bbfc4c77be4dab2  offline-community-v0.9.0-amd64.tar" | sha512sum -c
    ```

    If the validation is successful, the result will be similar to:

    ```none
    offline-community-v0.9.0-amd64.tar: OK
    ```

=== "ARM64"

    Run the following command to validate the package:

    ```sh
    echo "001a369379dc3299b6d0e00e46c83b9567323c2d52620d85815917a552fbc13c2d7076a2ad71eaff7dfbfe7ed82f68e5d30c0e53f47fa5055ef07588b4355bc3  offline-community-v0.9.0-arm64.tar" | sha512sum -c
    ```

    If the validation is successful, the result will be similar to:

    ```none
    offline-community-v0.9.0-arm64.tar: OK
    ```

## Installation

After the offline package has been successfully validated,

=== "AMD64"

    Run the following command to extract the tar file:

    ```sh
    tar -zxvf offline-community-v0.9.0-amd64.tar
    ```

=== "ARM64"

    Run the following command to extract the tar file:

    ```sh
    tar -zxvf offline-community-v0.9.0-arm64.tar
    ```

- For installation instructions, refer to [DCE 5.0 Community Installation Process](../../install/community/k8s/online.md#_2).
- After successful installation, please apply for a free community license: [License Application](../../dce/license0.md).

## Modules

DCE 5.0 Community includes the following default modules:

| Module          | Description                                                                                     | Latest Release                                                |
| --------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Global Management     | Responsible for user access control, permissions, enterprise spaces, audit logs, and customization settings.    | [0.18.1](../../ghippo/intro/release-notes.md#0181)    |
| Container Management  | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and other core Kubernetes features.       | [0.19.0](../../kpanda/intro/release-notes.md#0190)    |
| Insight         | Provides rich dashboards, scene monitoring, data queries, alerts, and other graphical information.             | [0.18.2](../../insight/intro/releasenote.md#0182)     |

## More

- [Online Documentation](../../dce/index.md)
- [Report Bugs](https://github.com/DaoCloud/DaoCloud-docs/issues)
