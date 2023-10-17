# RabbitMQ

This page allows you to download offline installation packages for different versions of RabbitMQ.

## Download

| Version                                                       | Architecture | File Size | Installation Package                                                                                                               | Checksum File | Update Date |
|------------------------------------------------------------| ----- |-------- |---------------------------------------------------------------------------------------------------------------------------------| ---------- |------------|
| [v0.13.1](../../../middleware/rabbitmq/release-notes.md)      | AMD 64 | 296.23MB | [:arrow_down: rabbitmq_0.13.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/rabbitmq_0.13.1_amd64.tar) | [:arrow_down: rabbitmq_0.13.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/rabbitmq_0.13.1_amd64_checksum.sha512sum) | 2023-10-10 |

## Verification

In the directory where you downloaded the offline installation package and checksum file, execute the following command to verify the integrity:

```sh
echo "$(cat rabbitmq_0.13.1_amd64_checksum.sha512sum)" | sha512sum -c
```

Upon successful verification, the output will be similar to:

```none
rabbitmq_0.13.1_amd64.tar: OK
```

## Installation

If this is your first time installing, please [apply for a free trial](../../../dce/license0.md) or contact us for authorization: email info@daocloud.io or call 400 002 6898.
If you have any questions related to license keys, please contact the DaoCloud delivery team.
