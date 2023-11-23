# Workbench

This page provides downloads for the offline package of different versions of the  Workbench module.

## Downloads

| Version      | Architecture | File Size | Package   | Checksum File    | Updated Date |
| ------ | ------------ | --------- | ---------------- | ------------ | ------------ |
| [0.19.5](../../amamba/intro/release-notes.md) | AMD 64       | 773.93 MB  | [:arrow_down: amamba_0.19.5_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_0.19.5_amd64.tar) | [:arrow_down: amamba_0.19.5_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_0.19.5_amd64_checksum.sha512sum) | 2023-08-30   |

## Validation

In the directory where you downloaded the offline packages and checksum files,
run the following command to validate the integrity:

```sh
echo "$(cat amamba_v0.19.0_amd64_checksum.sha512sum)" | sha512sum -c
```

If the validation is successful, it will print a result similar to:

```none
amamba_v0.19.0_amd64.tar: ok
```

## Installation

Refer to the [Offline Upgrade](../../amamba/offline-upgrade.md) page for installation instructions.

If this is your first installation, please [apply for a free trial](../../dce/license0.md)
or contact us for authorization: email info@daocloud.io or call 400 002 6898.
If you have any questions regarding license keys, please contact the DaoCloud delivery team.
