# Microservice Engine Skoala

On this page, you can download offline installation packages for various versions of the microservice engine module, including Helm Chart and images for the Skoala management component, as well as Helm Chart and images for the Skoala-Init cluster initialization component.

## Download

| Version                                                  | Architecture | File Size | Installation Package                                                                                       | Checksum File | Updated Date |
| --------------------------------------------------------- | ------------- | ---------- | ---------------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| [v0.28.1](../../skoala/intro/release-notes.md) | AMD 64 | 1.34GB | [:arrow_down: skoala_v0.28.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.28.1_amd64.tar) | [:arrow_down: skoala_v0.28.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.28.1_amd64_checksum.sha512sum) | 2023-11-01 |
| [v0.28.0](../../kpanda/intro/release-notes.md) | AMD64         | 1.3 GB     | [:arrow_down: skoala_v0.28.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.28.0_amd64.tar) | [:arrow_down: skoala_v0.28.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/skoala_v0.28.0_amd64_checksum.sha512sum) | 2023-10-25   |

## Verification

In the directory where you downloaded the offline installation package and checksum file, run the following command to verify the integrity:

```sh
echo "$(cat skoala_v0.28.0_amd64_checksum.sha512sum)" | sha512sum -c
```

If the checksum is successful, the command will print a result similar to:

```none
skoala_v0.28.0_amd64.tar: ok
```

## Installation

If this is your first installation, please apply for a free trial or contact us for authorization: email info@daocloud.io or call 400 002 6898.
If you have any questions regarding the license key, please contact the DaoCloud delivery team.
