# 服务网格 Mspider

本页可下载服务网格模块各版本的离线安装包。

## 下载

| 版本                                            | 架构 | 文件大小 | 安装包                                                                                                                             |  校验文件 | 更新日期      |
|-----------------------------------------------| ----- |-------- |---------------------------------------------------------------------------------------------------------------------------------| ---------- |-----------|
| [v0.21.1](../../mspider/intro/release-notes.md) | AMD 64 | 905.15MB | [:arrow_down: mspider_v0.21.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.21.1_amd64.tar) | [:arrow_down: mspider_v0.21.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.21.1_amd64_checksum.sha512sum) | 2023-12-05 |
| [v0.21.0](../../mspider/intro/release-notes.md) | AMD 64 | 905.15MB | [:arrow_down: mspider_v0.21.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.21.0_amd64.tar) | [:arrow_down: mspider_v0.21.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.21.0_amd64_checksum.sha512sum) | 2023-12-04 |
| [v0.20.3](../../mspider/intro/release-notes.md) | AMD 64 | 949.49MB | [:arrow_down: mspider_v0.20.3_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.20.3_amd64.tar) | [:arrow_down: mspider_v0.20.3_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.20.3_amd64_checksum.sha512sum) | 2023-10-27 |
| [v0.20.2](../../mspider/intro/release-notes.md) | AMD 64 | 949.41 MB | [:arrow_down: mspider_v0.20.2_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.20.2_amd64.tar) | [:arrow_down: mspider_v0.20.2_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.20.2_amd64_checksum.sha512sum) | 2023-10-18 |
| [v0.20.1](../../mspider/intro/release-notes.md) | AMD 64 | 949.41 MB | [:arrow_down: mspider_v0.20.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.20.1_amd64.tar) | [:arrow_down: mspider_v0.20.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.20.1_amd64_checksum.sha512sum) | 2023-10-13 |
| [v0.20.0](../../mspider/intro/release-notes.md) | AMD 64 | 949.40 MB | [:arrow_down: mspider_v0.20.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.20.0_amd64.tar) | [:arrow_down: mspider_v0.20.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.20.0_amd64_checksum.sha512sum) | 2023-10-12 |
| [v0.19.0](../../mspider/intro/release-notes.md) | AMD 64 | 866.88 MB | [:arrow_down: mspider_v0.19.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.19.0_amd64.tar) | [:arrow_down: mspider_v0.19.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.19.0_amd64_checksum.sha512sum) | 2023-08-31 |
| [v0.18.0](../../mspider/intro/release-notes.md) | AMD64 | 2.41 GB | [:arrow_down: mspider_v0.18.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.18.0_x86_64.tar) | [:arrow_down: mspider_v0.18.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/mspider_v0.18.0_x86_64_checksum.sha512sum) | 2023-08-23 |

## 校验

在下载离线安装包和校验文件的目录，以 v0.18.0 为例，执行以下命令校验完整性：

```sh
echo "$(cat mspider_v0.18.0_amd64_checksum.sha512sum)" | sha512sum -c
```

校验成功后打印结果类似于：

```none
mspider_v0.18.0_amd64.tar: ok
```

## 安装

如果是初次安装，请[申请免费体验](../../dce/license0.md)或联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。
