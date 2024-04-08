---
MTPE: windsonsea
date: 2023-01-03
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.3.30

This page allows you to download the offline package and checksum file of DCE 5.0 Community.

[Return to Download Index](../index.md){ .md-button }
[More Historical Versions](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Download | Update Date |
| -------- | ------- | ------------ | --------- | -------- | ----------- |
| offline-community-v0.3.30-amd64.tar | v0.3.30 | AMD 64 | 5.73 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.3.30-amd64.tar) | 2023-01-03 |
| offline-community-v0.3.30-arm64.tar | v0.3.30 | <font color="green">ARM 64</font> | 5.16 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.3.30-arm64.tar) | 2023-01-03 |

## Validation

Go to the download directory of the offline package.

=== "AMD 64"

     run the following command to validate the offline package:

     ```sh
     echo "469c98d6a60c7055f3e4159ffcdb6f65bb44cade4345400ad1b4067f8c3c89ef057983accaf413f76dc71b9a5592e0ef97600fa731bd715acacbdab1c653601b offline-com munity-v0.3.30-amd64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-community-v0.3.30-amd64.tar: OK
     ```

=== "<font color="green">ARM 64</font>"

     run the following command to validate the offline package:

     ```sh
     echo "9d965d49d3b09231fadae7fe713da7284b408e36f6d24d2863678dc4edf239abedc68a47e5d020bf02688ad197803a908db379e481340e13c86735fa29fd8d14 offline-community-v0.3.30-arm64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-community-v0.3.30-arm64.tar: OK
     ```

## Installation

After the offline package has been successfully validated,

=== "AMD 64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-community-v0.3.30-amd64.tar
     ```

=== "<font color="green">ARM 64</font>"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-community-v0.3.30-arm64.tar
     ```

- For installation, refer to [DCE 5.0 Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, [Free Trial](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, personalized appearance settings, etc. | [v0.13](../../ghippo/intro/release-notes.md#v013) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [v0.14](../../kpanda/intro/release-notes.md#v014) |
| Insight | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [v0.13](../../insight/intro/releasenote.md#v013) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)