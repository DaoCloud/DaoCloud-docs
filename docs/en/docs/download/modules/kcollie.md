# Cluster Inspection

This page provides offline installation packages for different versions of the Cluster Inspection module.

## Download

| Version     | Architecture | File Size | Package         | Checksum File           | Updated Date |
|------------|--------------|-----------|----------|----------------------|--------------|
| [v0.4.0](../../dce/dce-rn/20230731.md) | AMD64        | 205.11 MB    | [:arrow_down: kcollie_v0.4.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcollie_v0.4.0_amd64.tar) | [:arrow_down: kcollie_v0.4.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcollie_v0.4.0_amd64_checksum.sha512sum) | 2023-08-08   |

## Verification

To verify the integrity of the downloaded offline installation package and checksum file,
take `v0.4.0_amd64` as an example, run the following command in the directory:

```sh
echo "$(cat kcollie_v0.4.0_amd64_checksum.sha512sum)" | sha512sum -c
```

If the verification is successful, the result will be similar to:

```none
kcollie_v0.4.0_amd64.tar: ok
```

## Installation

Refer to the [Offline Upgrade Cluster Inspection Module](../../kpanda/user-guide/inspect/offline-upgrade.md) for installation instructions.

If this is your first installation, please [apply for a free trial](../../dce/license0.md)
or contact us for authorization: email info@daocloud.io or call 400 002 6898.
If you have any questions regarding license keys, please contact the DaoCloud delivery team.
