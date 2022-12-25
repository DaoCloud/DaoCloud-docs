---
date: 2022-11-17
hide:
  - navigation
---

# DCE 5.0 Community Edition v0.3.28

This page can download the offline installation package of DCE 5.0 Community Edition.

## Download

| Version Name | File Size | Installer | Date Updated |
| ----------------------------- | -------- | ---------- -------------------------------------------------- -------------------------------------------------- | ---------- |
| offline-community-v0.3.28.tar | 5.8 GB | [:arrow_down: Download](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-v0.3.28.tar ) | 2022-11-18 |

## Validation

Enter the download directory of the offline installation package. Execute the following command to verify the installation package:

```sh
echo "4e1d839ee51f6ff837e2363576cd7ccb794bf81de5fac3c840d14781abc3e077f9014466a3f21d29b83af12643e59e4fa310ecd08831266d2b361ba9e9b81933  offline-community-v0.3.28.tar" | sha512sum -c
```

If the verification is successful, it will print:

```none
offline-community-v0.3.28.tar: OK
```

## Install

After successfully verifying the offline package, unpack the tarball:

```sh
tar -zxvf offline-community-v0.3.28.tar
```

Then refer to [Community Edition Installation Process](../../install/intro.md#_2) to install.
If you are installing for the first time or have forgotten your license key, please [Free Trial](../../dce/license0.md).

## Modules

DCE 5.0 Community Edition includes the following modules by default:

| Modules | Introduction | Module Versions |
| -------- | ----------------------------------------- ------------------------- | ------------------------ ------------------------------------- |
| Global Management | Responsible for user access control, permissions, enterprise space, audit logs, personalized appearance settings, etc. | [v0.11](../../ghippo/01ProductBrief/release-notes.md#v011) |
| Container Management | Manage K8s core functions such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [v0.12](../../kpanda/03ProductBrief/release-notes.md#v012) |
| Observability | Provide rich graphic information such as dashboards, scene monitoring, data query, and alarms | [v0.11](../../insight/03ProductBrief/releasenote.md#v011) |

## More

- [Online Documentation](../../dce/what-is-dce.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)