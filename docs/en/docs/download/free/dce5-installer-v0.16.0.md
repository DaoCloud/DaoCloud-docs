---
MTPE: windsonsea
date: 2024-04-08
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.16.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Community.

[Return to Download Guide](../index.md){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.16.0-amd64.tar | v0.16.0 | AMD 64 | 7.50 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.16.0-amd64.tar) | 2024-03-14 |
| offline-community-v0.16.0-arm64.tar | v0.16.0 | <font color="green">ARM 64</font> | 7.05 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.16.0-arm64.tar) | 2024-03-14 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "3d26f2068f0341fe3e3418158b9d9a5244eb1c0cc443909592903040a8929736a1944ff5ae196404fa6362e60515014d50dc6128ef65714597ff1b1cca42620b  offline-community-v0.16.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.16.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "a01cc80ae0405e858cfa56b2ffd7a8dd8267744edc2ab31c60e8e3ba46de5afe87880d909d2157f47c2ba062380faab965d761cc7216b9031dd3e33dea7de4eb  offline-community-v0.16.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.16.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.16.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.16.0-arm64.tar
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
