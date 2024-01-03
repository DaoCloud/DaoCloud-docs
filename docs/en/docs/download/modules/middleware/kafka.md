---
hide:
  - toc
---

# Kafka

This page provides downloadable offline packages for various versions of Kafka.

## Download

| Version | Architecture | File Size | Package   | Checksum File | Updated Date |
| ------ | ------------ | --------- | ---------- | ------------ | ------------ |
| [v0.10.0](../../../middleware/kafka/release-notes.md) | AMD 64 | 964.64 MB | [:arrow_down: kafka_0.10.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-kafka_0.10.0_amd64.tar) | [:arrow_down: kafka_0.10.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-kafka_0.10.0_amd64_checksum.sha512sum) | 2023-12-10 |
| [v0.9.0](../../../middleware/kafka/release-notes.md) | AMD 64 | 957.66 MB | [:arrow_down: kafka_0.9.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-kafka_0.9.0_amd64.tar) | [:arrow_down: kafka_0.9.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-kafka_0.9.0_amd64_checksum.sha512sum) | 2023-11-02 |
| [v0.8.1](../../../middleware/kafka/release-notes.md) | AMD 64 | 957.22 MB | [:arrow_down: kafka_0.8.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-kafka_0.8.1_amd64.tar) | [:arrow_down: kafka_0.8.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-kafka_0.8.1_amd64_checksum.sha512sum) | 2023-10-20 |

## Validation

To validate the integrity of the downloaded offline package and checksum file, run the following command in the directory where they are located:

```sh
echo "$(cat kafka_0.8.1_amd64_checksum.sha512sum)" | sha512sum -c
```

If the validation is successful, the printed result will be similar to:

```none
kafka_0.8.1_amd64.tar: OK
```

## Installation

If this is your first time installing Kafka, please [apply for a free trial](../../../dce/license0.md) or contact us for authorization: email info@daocloud.io or call 400 002 6898.
If you have any questions regarding license keys, please reach out to the DaoCloud delivery team.
