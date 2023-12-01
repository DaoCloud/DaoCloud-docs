# 应用备份 Kcoral

本页可下载应用备份模块各版本的离线安装包。

## 下载

| 版本                                            | 架构 | 文件大小 | 安装包                                                                                                                             |  校验文件 | 更新日期       |
|-----------------------------------------------| ----- |-------- |---------------------------------------------------------------------------------------------------------------------------------| ---------- |------------|
| [v0.7.0](../../kpanda/intro/release-notes.md) | AMD 64 | 59.40MB | [:arrow_down: kcoral_v0.7.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.7.0_amd64.tar) | [:arrow_down: kcoral_v0.7.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.7.0_amd64_checksum.sha512sum) | 2023-12-01 |
| [v0.6.1](../../kpanda/intro/release-notes.md) | AMD 64 | 59.38MB | [:arrow_down: kcoral_v0.6.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.6.1_amd64.tar) | [:arrow_down: kcoral_v0.6.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.6.1_amd64_checksum.sha512sum) | 2023-11-07 |
| [v0.6.0](../../kpanda/intro/release-notes.md) | AMD 64 | 59.38MB | [:arrow_down: kcoral_v0.6.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.6.0_amd64.tar) | [:arrow_down: kcoral_v0.6.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.6.0_amd64_checksum.sha512sum) | 2023-10-26 |
| [v0.5.0](../../kpanda/intro/release-notes.md) | AMD 64 | 59.30MB | [:arrow_down: kcoral_v0.5.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.5.0_amd64.tar) | [:arrow_down: kcoral_v0.5.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.5.0_amd64_checksum.sha512sum) | 2023-09-01 |
| [v0.4.0](../../kpanda/intro/release-notes.md) | AMD64 | 59.29 MB | [:arrow_down: kcoral_v0.4.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.4.0_amd64.tar) | [:arrow_down: kcoral_v0.4.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kcoral_v0.4.0_amd64_checksum.sha512sum) | 2023-08-08 |

## 校验

在下载离线安装包和校验文件的目录，以 v0.4.0 为例，执行以下命令校验完整性：

```sh
echo "$(cat kcoral_v0.4.0_amd64_checksum.sha512sum)" | sha512sum -c
```

校验成功后打印结果类似于：

```none
kcoral_v0.4.0_amd64.tar: ok
```

## 安装

参阅[离线升级备份恢复模块](../../kpanda/user-guide/backup/offline-upgrade.md)进行安装。

如果是初次安装，请[申请免费体验](../../dce/license0.md)或联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。
