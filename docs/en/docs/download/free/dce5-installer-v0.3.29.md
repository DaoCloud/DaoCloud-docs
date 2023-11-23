---
date: 2022-11-21
hide:
  - navigation
---

# DCE 5.0 Community v0.3.29

This page allows you to download the offline package and checksum file of DCE 5.0 Community.

[Return to Download Index](../index.md){ .md-button }
[More Historical Versions](./dce5-installer-history.md){ .md-button }

## Download

| Filename | Version | Architecture | File Size | Downloads | Update Date |
| ----------------------------- | ------- | -------- | -- ----------------------------------------------- | ----- ----- | -------------------------------- |
| offline-centos7-community-v0.3.29-amd64.tar | v0.3.29 | AMD64 | 9.2 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-centos7-community-v0.3.29-amd64.tar) | 2022-12-16 |
| offline-kylin-v10sp2-community-v0.3.29-arm64.tar | v0.3.29 | ARM64 | 6.9 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-kylin-v10sp2-community-v0.3.29-arm64.tar) | 2022-12-16 |

## Validation

Go to the download directory of the offline package.

=== "AMD64"

     run the following command to validate the offline package:

     ```sh
     echo "988bf4397f555804fb004a83e01169fd4cfb995d0659170197cab4d07c26aefb6c916ce42c0655d207a2ae7bddd5c28c6c66fc7645c67a174a8919e7e04 0cbd8 offline-centos7-community-v0.3.29-amd64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-centos7-community-v0.3.29-amd64.tar: OK
     ```

=== "ARM64"

     run the following command to validate the offline package:

     ```sh
     echo "86dcb1f8b155d37a19a1b6c81a74a3758f443a79a8ffd95b9f5a634d992932714d8bce9805ab52d9fffbfdcbc82873e7c7132a7d3e9a45d5fe00f46de16ab7 17 offline-kylin-v10sp2-community-v0.3.29-arm64.tar" | sha512sum -c
     ```

     If the validation is successful, it will print:

     ```none
     offline-kylin-v10sp2-community-v0.3.29-arm64.tar: OK
     ```
  
## Installation

After the offline package has been successfully validated,

=== "AMD64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-centos7-community-v0.3.29-amd64.tar
     ```

=== "ARM64"

     run the following command to extract the tarball:

     ```sh
     tar -zxvf offline-kylin-v10sp2-community-v0.3.29-arm64.tar
     ```

- For installation, refer to [DCE 5.0 Community Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, please [Free Trial](../../dce/license0.md)

## Modules

DCE 5.0 Community includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------------------------------------- ------------------------- | ------------------------ ------------------------------------- |
| Global Management | Responsible for user access control, permissions, enterprise space, audit logs, personalized appearance settings, etc. | [v0.12](../../ghippo/intro/release-notes.md#v012) |
| Container Management | Manage K8s core features such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [v0.13](../../kpanda/intro/release-notes.md#v013) |
| Insight | Provide rich graphic information such as dashboards, scene monitoring, data query, and alerts | [v0.12](../../insight/intro/releasenote.md#v012) |

## More

- [Online Documentation](../../dce/index.md)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)