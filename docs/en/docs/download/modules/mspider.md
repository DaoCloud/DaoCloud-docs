# Service Mesh

On this page, you can download offline installation packages for different versions of the service mesh module.

## Download

| Version   | Architecture | File Size |  Package      | Checksum File                    | Update Date |
|----------|--------------|-----------|----------------|----------|-------------|
| [v0.18.0](../../mspider/intro/release-notes.md) | AMD64        | 2.41 GB   | [:arrow_down: mspider_v0.18.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.18.0_x86_64.tar) | [:arrow_down: mspider_v0.18.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.18.0_x86_64_checksum.sha512sum) | 2023-08-23   |

## Verification

In the directory where you downloaded the offline installation package and checksum file,
run the following command to verify the integrity:

```sh
echo "$(cat mspider_v0.18.0_amd64_checksum.sha512sum)" | sha512sum -c
```

If the verification is successful, the result will be similar to:

```none
mspider_v0.18.0_amd64.tar: ok
```

## Installation

If this is your first installation, please [apply for a free trial](../../dce/license0.md)
or contact us for authorization: send an email to info@daocloud.io or call 400 002 6898.
If you have any questions regarding license keys, please contact the DaoCloud delivery team.
