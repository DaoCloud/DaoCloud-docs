# Container Management

This page provides offline installation packages for different versions of the observability module.

## Download

| Version                                           | Architecture | File Size | Installation Package                                                                                                             | Checksum File                                                                                                                            | Updated Date |
|--------------------------------------------------|--------------|-----------|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|--------------|
| [v0.19.0](../../kpanda/intro/release-note.md)    | AMD64        | 2.41GB    | [:arrow_down: kpanda_v0.19.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_v0.19.0_amd64.tar) | [:arrow_down: kpanda_v0.19.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_v0.19.0_amd64_checksum.sha512sum) | 2023-7-06   |

## Checksum

To verify the integrity of the downloaded offline installation package and checksum file,
run the following command in the directory:

```sh
echo "$(cat kpanda_v0.19.0_amd64_checksum.sha512sum)" | sha512sum -c
```

If the verification is successful, the result will be similar to:

```none
kpanda_v0.19.0_amd64.tar: ok
```

## Installation

If this is your first installation, please [apply for a free trial](../../dce/license0.md) or contact us for authorization:
email info@daocloud.io or call 400 002 6898.
If you have any questions regarding license keys, please contact the DaoCloud delivery team.
