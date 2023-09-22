---
date: 2023-09-08
---

# DCE 5.0 Community v0.11.0

This page provides downloads for the offline installation package and verification files of DCE 5.0 Community.

## Downloads

| Filename        | Version  | Architecture | File Size | Download         | Updated On |
| -------- | -------- | ------------ | --------- | -------------- | ---------- |
| offline-community-v0.11.0-amd64.tar     | v0.11.0  | AMD64        | 6.03 GB    | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.11.0-amd64.tar) | 2023-09-08 |
| offline-community-v0.11.0-arm64.tar     | v0.11.0  | ARM64        | 5.65 GB    | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.11.0-arm64.tar) | 2023-09-08 |

## Verification

Navigate to the download directory of the offline installation package.

=== "AMD64"

    Run the following command to verify the installation package:

    ```sh
    echo "54326e5b62cd7bb2711904adff5d2128e647dcd0993ae7109645889d3c923a8c590ae6d1623a85e846e9a0acf7f0149936c686a1544f7b933d4444b33916d876  offline-community-v0.11.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, it will print:

    ```none
    offline-community-v0.11.0-amd64.tar: OK
    ```

=== "ARM64"

    Run the following command to verify the installation package:

    ```sh
    echo "25b7688637e57eea4488386a28f9357601ff53f497f439808a34a91e02ba2ceb8f7b92a74fd7184602efdb853e81472f8de7b53a04f9a93903f0131a4acac1be  offline-community-v0.11.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, it will print:

    ```none
    offline-community-v0.11.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD64"

    Run the following command to extract the tar package:

    ```sh
    tar -zxvf offline-community-v0.11.0-amd64.tar
    ```

=== "ARM64"

    Run the following command to extract the tar package:

    ```sh
    tar -zxvf offline-community-v0.11.0-arm64.tar
    ```

- For installation instructions, please refer to [DCE 5.0 Community Installation](../../install/community/k8s/online.md#_2)
- After successful installation, please apply for a [Free Community Experience](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Module     | Description           | Latest Updates                      |
| ---------- | --------------------- | ----------------------------------- |
| Global Management | Responsible for user access control, permissions, enterprise spaces, audit logs, personalized appearance settings, etc. | [0.20.1](../../ghippo/intro/release-notes.md#0201) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRD, namespaces, and other core features of K8s. | [0.21.0](../../kpanda/intro/release-notes.md#0210) |
| Observability | Provides rich dashboards, scenario monitoring, data queries, alerts, and other graphical information. | [0.20.0](../../insight/intro/releasenote.md#0200) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
