---
date: 2022-11-17
hide:
  - navigation
---

# DCE 5.0 Community v0.3.28

This page allows you to download the offline package of DCE 5.0 Community.

[Return to Download Index](../index.md){ .md-button }
[More Historical Versions](./dce5-installer-history.md){ .md-button }

## Download

| Version Name | File Size | Installer | Update Date |
| ------------ | -------- | ---------- | ---------- |
| offline-community-v0.3.28.tar | 5.8 GB | [:arrow_down: Download](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.3.28.tar ) | 2022-11-18 |

## Validation

Go to the download directory of the offline package, run the following command to validate the offline package:

```sh
echo "4e1d839ee51f6ff837e2363576cd7ccb794bf81de5fac3c840d14781abc3e077f9014466a3f21d29b83af12643e59e4fa310ecd08831266d2b361ba9e9b81933 offline-community-v0.3.28.tar" | sha512sum -c
```

If the validation is successful, it will print:

```none
offline-community-v0.3.28.tar: OK
```

## Installation

After the offline package has been successfully validated, unpack the tarball:

```sh
tar -zxvf offline-community-v0.3.28.tar
```

Then refer to [DCE 5.0 Community Installation Process](../../install/index.md#_2) to install.
If you are installing for the first time or have forgotten your license key, please [apply for a free community experience](../../dce/license0.md).

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | Module Versions |
| -------- | ----------------------------------------- ------------------------- | ------------------------ ------------------------------------- |
| Global Management | Responsible for user access control, permissions, workspaces and folders, audit logs, personalized appearance settings, etc. | [v0.11](../../ghippo/intro/release-notes.md#v011) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [v0.12](../../kpanda/intro/release-notes.md#v012) |
| Insight | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [v0.11](../../insight/intro/releasenote.md#v011) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)