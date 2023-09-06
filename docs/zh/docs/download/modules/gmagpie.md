# 运营管理

本页可下载运营管理模块各版本的离线安装包。

## 下载

| 版本                                                   | 架构 | 文件大小 | 安装包                                                                                                     |  校验文件 | 更新日期   |
| ------------------------------------------------------ | ----- |-------- | ---------------------------------------------------------------------------------------------------------- | ---------- | ---------- |
| [v0.4.1](../../gmagpie/intro/release-notes.md) | AMD 64 | 93.72MB | [:arrow_down: gmagpie_v0.4.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.4.1_amd64.tar) | [:arrow_down: gmagpie_v0.4.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.4.1_amd64_checksum.sha512sum) | 2023-08-29 |
| [v0.3.2](../../dce/dce-rn/20230630.md) | AMD 64 | 91.85 MB | [:arrow_down: gmagpie_v0.3.2_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.3.2_amd64.tar) | [:arrow_down: gmagpie_v0.3.2_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.3.2_amd64_checksum.sha512sum) | 2023-08-02 |
| [v0.3.0](../../dce/dce-rn/20230630.md) | AMD 64 | 56.90 MB | [:arrow_down: gmagpie_v0.3.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.3.0_amd64.tar) | [:arrow_down: gmagpie_v0.3.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.3.0_amd64_checksum.sha512sum) | 2023-06-28 |
| [v0.2.2](../../ghippo/user-guide/report-billing/index.md) | AMD64 | 37.1 MB | [:arrow_down: gmagpie_v0.2.2_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.2.2_amd64.tar) | [:arrow_down: gmagpie_v0.2.2_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/gmagpie_v0.2.2_amd64_checksum.sha512sum) | 2023-5-30 |

## 校验

在下载离线安装包和校验文件的目录，以 `v0.2.2_amd64` 为例，执行以下命令校验完整性：

```sh
echo "$(cat gmagpie_v0.2.2_amd64_checksum.sha512sum)" | sha512sum -c
```

校验成功后打印结果类似于：

```none
gmagpie_v0.2.2_amd64.tar: ok
```

## 安装

参阅[运营管理](../../ghippo/user-guide/report-billing/gmagpie-offline-install.md)安装流程进行安装。

如果是初次安装，请[申请免费体验](../../dce/license0.md)或联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。
