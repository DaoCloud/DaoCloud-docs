# RocketMQ

On this page, you can download the offline installation packages for different versions of RocketMQ.

## Download

| Version                                                  | Architecture | File Size  | Installation Package                                                                                                     | Checksum File | Release Date |
| -------------------------------------------------------- | ------------ | ---------- | ----------------------------------------------------------------------------------------------------------------------- | ------------- | ------------ |
| [v0.1.1](../../../middleware/rocketmq/release-notes.md) | AMD64        | 354.39 MB  | [:arrow_down: rocketmq_0.1.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-rocketmq_0.1.1_amd64.tar) | [:arrow_down: rocketmq_0.1.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-rocketmq_0.1.1_amd64_checksum.sha512sum) | 2023-11-02   |

## Verification

To verify the integrity of the downloaded offline installation package and checksum file in the directory, run the following command:

```sh
echo "$(cat mcamel-rocketmq_0.1.1_amd64_checksum.sha512sum)" | sha512sum -c
```

If the verification succeeds, the printed result will be similar to:

```none
mcamel-rocketmq_0.1.1_amd64.tar: OK
```

## Installation

If this is your first installation, please apply for a free trial or contact us for authorization: Email info@daocloud.io or call 400 002 6898.
If you have any questions related to license keys, please contact the DaoCloud delivery team.
