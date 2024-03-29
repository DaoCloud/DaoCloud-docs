---
date: 2024-02-26
hide:
  - navigation
---

# DCE 5.0 Community v0.15.1

This page provides downloads for the offline installation package and verification files for DCE 5.0 Community.

[Return to Download Guide](../index.md){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.15.1-amd64.tar | v0.15.1 | AMD 64 | 7.44 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.15.1-amd64.tar) | 2024-02-26 |
| offline-community-v0.15.1-arm64.tar | v0.15.1 | <font color="green">ARM 64</font> | 7.05 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.15.1-arm64.tar) | 2024-02-26 |

## Verification

Go to the offline installation package download directory.

=== "AMD64"

    Run the following command to verify the installation package:

    ```sh
    echo "84a3e0523e292417d13bc22fb4b0ce7a1c974f2fed3d5dffb195c55190f10d672131ea4a22d458b73a0ae55837ee08bc520e7010e014dfdec909c21796566dbd  offline-community-v0.15.1-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.15.1-amd64.tar: OK
    ```

=== "ARM64"

    Run the following command to verify the installation package:

    ```sh
    echo "5e43cbe3226dd472f656c7daa23f871e01019cea46b76675d409a272fcc1f7c160801b67dc13156a000979678061df6024758757e7011fad41fe7799167ad332  offline-community-v0.15.1-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.15.1-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.15.1-amd64.tar
    ```

=== "ARM64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.15.1-arm64.tar
    ```

- For installation instructions, refer to [Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [apply for a free community experience](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, personalized appearance settings, etc. | [0.24.0](../../ghippo/intro/release-notes.md#0240) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and other core Kubernetes functionalities. | [0.25.1](../../kpanda/intro/release-notes.md#0251) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alarm information. | [0.24.0](../../insight/intro/releasenote.md#0240) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
