---
MTPE: windsonsea
date: 2024-06-27
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.18.0

This page provides downloads for the offline installation package and verification files for DCE 5.0 Community.

[Return to Download Guide](../index.md){ .md-button } [More Version History](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| --------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.18.0-amd64.tar | v0.18.0 | AMD 64 | 7.72GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.18.0-amd64.tar) | 2024-06-11 |
| offline-community-v0.18.0-arm64.tar | v0.18.0 | <font color="green">ARM 64</font> | 7.31GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.18.0-arm64.tar) | 2024-06-11 |

## Verification

Go to the offline installation package download directory.

=== "AMD 64"

    Run the following command to verify the installation package:

    ```sh
    echo "362456c766c327167e413eefba2b8774c25285e55b48d6df019cbbf76e71f7442cd1a8b01a9e309bc31cad0f70f287a2f73b8aed2750797cad29e0ea545f2e47  offline-community-v0.18.0-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.18.0-amd64.tar: OK
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to verify the installation package:

    ```sh
    echo "9e61a5346039840d7b9123ec1b53cdd71f233095584c0b817fe43269a193c9c79260e861924660eb71482917830b6f19a754e2e1350414278cfbe302126c8036  offline-community-v0.18.0-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, the following will be printed:

    ```none
    offline-community-v0.18.0-arm64.tar: OK
    ```

## Installation

After successfully verifying the offline package,

=== "AMD 64"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.18.0-amd64.tar
    ```

=== "<font color="green">ARM 64</font>"

    Run the following command to decompress the tar package:

    ```sh
    tar -zxvf offline-community-v0.18.0-arm64.tar
    ```

- For installation instructions, refer to [Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [apply for a free community experience](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspace and hierarchy, audit logs, personalized appearance settings, etc. | [0.27.0](../../ghippo/intro/release-notes.md#0270) |
| Container Management | Manages clusters, nodes, workloads, Helm applications, CRDs, namespaces, and other core Kubernetes functionalities. | [0.28.1](../../kpanda/intro/release-notes.md#0281) |
| Insight | Provides rich dashboards, scene monitoring, data querying, and alarm information. | [0.27.0](../../insight/intro/releasenote.md#0270) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a Bug](https://github.com/DaoCloud/DaoCloud-docs/issues)
