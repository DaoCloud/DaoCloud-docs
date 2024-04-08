---
MTPE: windsonsea
date: 2022-11-23
hide:
  - navigation
---

# DCE 5.0 Community with Installer v0.3.27

This page allows you to download the offline package and checksum file of DCE 5.0 Community.

[Return to Download Index](../index.md){ .md-button }
[More Historical Versions](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Package |
| -------- | ------- |
| offline-community-v0.3.27.tar | [:arrow_down: Download](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.3.27.tar) |

## Validation

Go to the download directory of the offline package, run the following command to validate the offline package:

```sh
echo "7a2f07fd9d09c827347d2994c0b6d4852f55e1f6de149e7b95e29625c4081eba3d415d3dbb261d226d8179c3251ac8e67c2de898d3eb6a58ff218f79fd31d4 2e offline-community-v0.3.27.tar" | sha512sum -c
```

If the validation is successful, it will print:

```none
offline-community-v0.3.27.tar: OK
```

## Installation

After the offline package has been successfully validated, unpack the tarball:

```sh
tar -zxvf offline-community-v0.3.28.tar
```

Then refer to [DCE 5.0 Community Installation Process](../../install/community/k8s/online.md#_2) to install.

After successful installation, [Free Trial](../../dce/license0.md).

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------- | ---------- |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, personalized appearance settings, etc. | [Release Notes](../../ghippo/intro/release-notes.md) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [v0.12.0](../../kpanda/intro/release-notes.md#v0120) |
| Insight | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [v0.11.1](../../insight/intro/releasenote.md#v0111) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)