# DCE 5.0 Community Edition v0.3.29

This page can download the offline installation package and verification file of DCE 5.0 Community Edition.

## Download

| File Name | Version | Architecture | File Size | Downloads | Date Updated |
| ----------------------------- | ------- | -------- | -- ----------------------------------------------- | ----- ----- | -------------------------------- |
| offline-centos7-community-v0.3.29-amd64.tar | v0.3.29 | AMD 64 | 9.2 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5 /offline-centos7-community-v0.3.29-amd64.tar) | 2022-12-16 |
| offline-kylin-v10sp2-community-v0.3.29-arm64.tar | v0.3.29 | ARM 64 | 6.9 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise /dce5/offline-kylin-v10sp2-community-v0.3.29-arm64.tar) | 2022-12-16 |

## Validation

Enter the download directory of the offline installation package.

=== "AMD 64"

    Execute the following command to verify the installation package:

    ```sh
    echo "988bf4397f555804fb004a83e01169fd4cfb995d0659170197cab4d07c26aefb6c916ce42c0655d207a2ae7bddd5c28c6c66fc7645c67a174a8919e7e040cbd8  offline-centos7-community-v0.3.29-amd64.tar" | sha512sum -c
    ```

    If the verification is successful, it will print:

    ```none
    offline-centos7-community-v0.3.29-amd64.tar: OK
    ```

=== "ARM 64"

    Execute the following command to verify the installation package:

    ```sh
    echo "86dcb1f8b155d37a19a1b6c81a74a3758f443a79a8ffd95b9f5a634d992932714d8bce9805ab52d9fffbfdcbc82873e7c7132a7d3e9a45d5fe00f46de16ab717  offline-kylin-v10sp2-community-v0.3.29-arm64.tar" | sha512sum -c
    ```

    If the verification is successful, it will print:

    ```none
    offline-kylin-v10sp2-community-v0.3.29-arm64.tar: OK
    ```
  
## Install

After successfully verifying the offline package,

=== "AMD 64"

    Execute the following command to extract the tarball:

    ```sh
    tar -zxvf offline-centos7-community-v0.3.29-amd64.tar
    ```

=== "ARM 64"

    Execute the following command to extract the tarball:

    ```sh
    tar -zxvf offline-kylin-v10sp2-community-v0.3.29-arm64.tar
    ```

- For installation, please refer to [Community Edition Installation Process](../../install/community/k8s/online.md#_2)
- After successful installation, please [apply for free community experience](../../dce/license0.md)

## Modules

DCE 5.0 Community Edition includes the following modules by default:

| Modules | Introduction | What's New |
| -------- | ----------------------------------------- ------------------------- | ------------------------ ------------------------------------- |
| Global Management | Responsible for user access control, permissions, enterprise space, audit logs, personalized appearance settings, etc. | [v0.11](../../ghippo/01ProductBrief/release-notes.md#v011) |
| Container Management | Manage K8s core functions such as clusters, nodes, workloads, Helm applications, CRDs, and namespaces | [v0.12](../../kpanda/03ProductBrief/release-notes.md#v012) |
| Observability | Provide rich graphic information such as dashboards, scene monitoring, data query, and alarms | [v0.11](../../insight/03ProductBrief/releasenote.md#v011) |

## More

- [Online Documentation](https://docs.daocloud.io/dce/what-is-dce/)
- [Report a bug](https://github.com/DaoCloud/DaoCloud-docs/issues)