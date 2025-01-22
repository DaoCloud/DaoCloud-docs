---
MTPE: windsonsea
date: 2023-06-06
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.8.0

This page provides offline packages and checksum files for DCE 5.0 Community.

[Return to Download Index](../index.md){ .md-button }
[Legacy Packages](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | Size | Download | Date |
| -------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.8.0-amd64.tar | v0.8.0 | AMD 64 | 6.01 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.8.0-amd64.tar) | 2023-06-06 |
| offline-community-v0.8.0-arm64.tar | v0.8.0 | <font color="green">ARM 64</font> | 5.64 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.8.0-arm64.tar) | 2023-06-06 |

## Verification

Enter the directory where the offline package is downloaded.

=== "AMD 64"

    Run the following command to verify the offline package:

    ```sh
    echo "886f1e1622115e3d2bfa6e41e26ba3c02419177ee7cae422000b28f6e9cd9b2b370a8a737be90328ee1b048c02811b4b31443638960b3cd24acf9ce0b9848320  offline-community-v0.8.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, it will print:

    ```none
    offline-community-v0.8.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the offline package:

    ```sh
    echo "73ccc2305196caa7c8152369016b5bc2fa38f874028f94961482ec5610158c7e7e8b4c3f7a335e473a28953e5ffeff27bb6ee7d132b3b1ae8e49ddd711993c21  offline-community-v0.8.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, it will print:

    ```none
    offline-community-v0.8.0-arm64.tar: OK
    ```

## Installation

After the offline package is verifyd,

=== "AMD 64"

    Run the following command to unpack the tar package:

    ```sh
    tar -zxvf offline-community-v0.8.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to unpack the tar package:

    ```sh
    tar -zxvf offline-community-v0.8.0-arm64.tar
    ```

- For installation, refer to [DCE 5.0 Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [apply for a free community trial](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, and custom appearance. | [0.17.1](../../ghippo/intro/release-notes.md#v0171) |
| Container Management | Manage Kubernetes core features such as clusters, nodes, workloads, Helm applications, CRD, namespaces, etc. | [0.18.1](../../kpanda/intro/release-notes.md#v0181) |
| Insight | Provide rich dashboard, scenario monitoring, data query, alert and other graphical information.        | [0.17.2](../../insight/intro/release-notes.md#v0170) |

## More

- [Online documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
