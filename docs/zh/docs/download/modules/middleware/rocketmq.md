---
hide:
  - toc
---

# RocketMQ

本页可下载 RocketMQ 各版本的离线安装包。

## 下载

| 版本 | 架构 | 文件大小 | 安装包 | 校验文件 | 更新日期 |
| ---- | --- | ------- | ----- | ------ | ------- |
| [v0.5.0](../../../middleware/rocketmq/release-notes.md) | ARM 64 | 614.32 MB | [:arrow_down: rocketmq_0.5.0_arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-rocketmq_0.5.0_arm64.tar) | [:arrow_down: rocketmq_0.5.0_arm64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-rocketmq_0.5.0_arm64_checksum.sha512sum) | 2024-04-03 |
| [v0.5.0](../../../middleware/rocketmq/release-notes.md) | AMD 64 | 624.48 MB | [:arrow_down: rocketmq_0.5.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-rocketmq_0.5.0_amd64.tar) | [:arrow_down: rocketmq_0.5.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-rocketmq_0.5.0_amd64_checksum.sha512sum) | 2024-04-03 |
| [v0.4.0](../../../middleware/rocketmq/release-notes.md) | AMD 64 | 622.91 MB | [:arrow_down: rocketmq_0.4.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-rocketmq_0.4.0_amd64.tar) | [:arrow_down: rocketmq_0.4.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-rocketmq_0.4.0_amd64_checksum.sha512sum) | 2024-02-01 |
| [v0.3.0](../../../middleware/rocketmq/release-notes.md) | AMD 64 | 622.81 MB | [:arrow_down: rocketmq_0.3.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-rocketmq_0.3.0_amd64.tar) | [:arrow_down: rocketmq_0.3.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-rocketmq_0.3.0_amd64_checksum.sha512sum) | 2024-01-04 |
| [v0.2.0](../../../middleware/rocketmq/release-notes.md) | AMD 64 | 360.39 MB | [:arrow_down: rocketmq_0.2.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-rocketmq_0.2.0_amd64.tar) | [:arrow_down: rocketmq_0.2.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-rocketmq_0.2.0_amd64_checksum.sha512sum) | 2023-12-10 |
| [v0.1.1](../../../middleware/rocketmq/release-notes.md) | AMD 64 | 354.39 MB | [:arrow_down: rocketmq_0.1.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-rocketmq_0.1.1_amd64.tar) | [:arrow_down: rocketmq_0.1.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-rocketmq_0.1.1_amd64_checksum.sha512sum) | 2023-11-02 |

## 校验

在下载离线安装包和校验文件的目录，执行以下命令校验完整性：

```sh
echo "$(cat mcamel-rocketmq_0.1.1_amd64_checksum.sha512sum)" | sha512sum -c
```

校验成功后打印结果类似于：

```none
mcamel-rocketmq_0.1.1_amd64.tar: OK
```

## 安装

如果是初次安装，请[申请免费体验](../../../dce/license0.md)或联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。
