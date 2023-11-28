# 镜像仓库 Kangaroo

本页可下载镜像仓库模块各版本的离线安装包。

## 下载

| 版本                                            | 架构 | 文件大小 | 安装包                                                                                                                             |  校验文件 | 更新日期      |
|-----------------------------------------------| ----- |-------- |---------------------------------------------------------------------------------------------------------------------------------| ---------- |-----------|
| [0.13.0](../../kangaroo/intro/release-notes.md) | AMD 64 | 299.82MB | [:arrow_down: kangaroo_0.13.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.13.0_amd64.tar) | [:arrow_down: kangaroo_0.13.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.13.0_amd64_checksum.sha512sum) | 2023-11-28 |
| [0.12.1](../../kangaroo/intro/release-notes.md) | AMD 64 | 299.24MB | [:arrow_down: kangaroo_0.12.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.12.1_amd64.tar) | [:arrow_down: kangaroo_0.12.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.12.1_amd64_checksum.sha512sum) | 2023-11-03 |
| [0.12.0](../../kangaroo/intro/release-notes.md) | AMD 64 | 299.24MB | [:arrow_down: kangaroo_0.12.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.12.0_amd64.tar) | [:arrow_down: kangaroo_0.12.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.12.0_amd64_checksum.sha512sum) | 2023-10-29 |
| [0.11.0](../../kangaroo/intro/release-notes.md) | AMD 64 | 296.23MB | [:arrow_down: kangaroo_0.11.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.11.0_amd64.tar) | [:arrow_down: kangaroo_0.11.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.11.0_amd64_checksum.sha512sum) | 2023-09-04 |
| [v0.10.0](../../kangaroo/intro/release-notes.md) | AMD64 | 293.24 MB | [:arrow_down: kangaroo_v0.10.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.10.0_amd64.tar) | [:arrow_down: kangaroo_0.10.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kangaroo_0.10.0_amd64_checksum.sha512sum) | 2023-8-22 |

## 校验

在下载离线安装包和校验文件的目录，以 v0.10.0 为例，执行以下命令校验完整性：

```sh
echo "$(cat kangaroo_0.10.0_amd64_checksum.sha512sum)" | sha512sum -c
```

校验成功后打印结果类似于：

```none
kangaroo_0.10.0_amd64.tar: ok
```

## 安装

参阅[离线升级镜像仓库模块](../../kangaroo/intro/upgrade.md)页面进行安装。

如果是初次安装，请[申请免费体验](../../dce/license0.md)或联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。
