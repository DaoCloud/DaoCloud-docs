# VM Container

On this page, you can download the offline installation packages for different versions of the VM Container module.

## Download

| Version                                                  | Architecture | File Size | Installation Package                                                                                                     | Checksum File | Release Date |
| -------------------------------------------------------- | ------------ | --------- | ----------------------------------------------------------------------------------------------------------------------- | ------------- | ------------ |
| [v0.2.0](../../kpanda/intro/release-notes.md) | AMD64        | 37.1 MB   | [:arrow_down: virtnest_v0.2.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/virtnest_v0.2.0_amd64.tar) | [:arrow_down: virtnest_v0.2.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/virtnest_v0.2.0_amd64_checksum.sha512sum) | 2023-10-20   |

## Verification

To verify the integrity of the downloaded offline installation package and checksum file in the directory, using `v0.2.0_amd64` as an example, run the following command:

```sh
echo "$(cat virtnest_v0.2.0_amd64_checksum.sha512sum)" | sha512sum -c
```

If the verification succeeds, the printed result will be similar to:

```none
virtnest_v0.2.0_amd64.tar: ok
```

## Installation

Refer to the [VM Container](../../virtnest/install/offline-install.md) installation process for installation instructions.

If this is your first installation, please apply for a free trial or contact us for authorization: Email info@daocloud.io or call 400 002 6898.
If you have any questions related to license keys, please contact the DaoCloud delivery team.
