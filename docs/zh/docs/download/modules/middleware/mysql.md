# MySQL

本页可下载 MySQL 各版本的离线安装包。

## 下载

| 版本 | 架构 | 文件大小 | 安装包 | 校验文件 | 更新日期 |
| --- | ---- | ------ | ------ | ------ | ------- |
| [v0.13.0](../../../middleware/mysql/release-notes.md) | AMD 64 | 1.17 GB | [:arrow_down: mysql_0.13.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-mysql_0.13.0_amd64.tar) | [:arrow_down: mysql_0.13.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-mysql_0.13.0_amd64_checksum.sha512sum) | 2023-12-10 |
| [v0.12.0](../../../middleware/mysql/release-notes.md) | AMD 64 | 1.17 GB | [:arrow_down: mysql_0.12.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-mysql_0.12.0_amd64.tar) | [:arrow_down: mysql_0.12.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-mysql_0.12.0_amd64_checksum.sha512sum) | 2023-11-02 |
| [v0.11.1](../../../middleware/mysql/release-notes.md) | AMD 64 | 1.17 GB | [:arrow_down: mysql_0.11.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-mysql_0.11.1_amd64.tar) | [:arrow_down: mysql_0.11.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mcamel-mysql_0.11.1_amd64_checksum.sha512sum) | 2023-10-20 |

## 校验

在下载离线安装包和校验文件的目录，执行以下命令校验完整性：

```sh
echo "$(cat mcamel-mysql_0.11.1_amd64_checksum.sha512sum)" | sha512sum -c
```

校验成功后打印结果类似于：

```none
mcamel-mysql_0.11.1_amd64.tar: OK
```

## 安装

如果是初次安装，请[申请免费体验](../../../dce/license0.md)或联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。