---
hide:
  - toc
---

# Local Storage: hwameistor-operator

This page provides the offline installation package for hwameistor-operator,
which can be used to install the HwameiStor local storage module using this Operator.

## Download

| Version | Architecture | File Size | Package | Checksum File | Update Date |
| ------- | ------------ | --------- | ------- | ------------- | ----------- |
| [v0.13.1] | AMD 64 | 1.62 GB | [:arrow_down: hwameistor-operator_v0.13.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/hwameistor-operator_v0.13.1_amd64.tar) | [:arrow_down: hwameistor-operator_v0.13.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/hwameistor-operator_v0.13.1_amd64_checksum.sha512sum) | 2023-11-06 |

## Verification

In the directory where you downloaded the offline installation package and checksum file,
replace `v0.13.1_amd64` with the actual version, and run the following command to verify the integrity:

```sh
echo "$(cat hwameistor-operator_v0.13.1_amd64_checksum.sha512sum)" | sha512sum -c
```

If the verification is successful, the output will be similar to:

```none
hwameistor-operator_v0.13.1_amd64.tar: ok
```

## Installation

Refer to the [hwameistor-operator installation process](../../storage/hwameistor/install/deploy-operator.md)
for installation instructions.

If this is your first installation, please [apply for a free trial](../../dce/license0.md) or contact us
for authorization: email info@daocloud.io or call 400 002 6898. If you have any questions regarding the
license key, please contact the DaoCloud delivery team.
