# 应用工作台 Amamba

本页可下载应用工作台模块各版本的离线安装包。

## 下载

| 版本                                             | 架构 | 文件大小 | 安装包                                                                                                                             |  校验文件 | 更新日期      |
|------------------------------------------------| ----- |-------- |---------------------------------------------------------------------------------------------------------------------------------| ---------- |-----------|
| [0.20.0-alpha.3](../../amamba/intro/release-notes.md) | AMD 64 | 809.88MB | [:arrow_down: amamba_0.20.0-alpha.3_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_0.20.0-alpha.3_amd64.tar) | [:arrow_down: amamba_0.20.0-alpha.3_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_0.20.0-alpha.3_amd64_checksum.sha512sum) | 2023-08-30 |
| [v0.19.0](../../amamba/intro/release-notes.md) | AMD 64 | 459.27MB | [:arrow_down: amamba_v0.19.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.19.0_amd64.tar) | [:arrow_down: amamba_v0.19.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/amamba_v0.19.0_amd64_checksum.sha512sum) | 2023-07-07 |

## 校验

在下载离线安装包和校验文件的目录，执行以下命令校验完整性：

```sh
echo "$(cat amamba_v0.19.0_amd64_checksum.sha512sum)" | sha512sum -c
```

校验成功后打印结果类似于：

```none
amamba_v0.19.0_amd64.tar: ok
```

## 安装

如果是初次安装，请[申请免费体验](../../dce/license0.md)或联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。
