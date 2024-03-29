---
hide:
  - toc
---

# 容器管理 Kpanda

本页可下载容器管理模块各版本的离线安装包。

## 下载

| 版本 | 架构 | 文件大小 | 安装包 | 校验文件 | 更新日期 |
| ---- | --- | ------ | ------ | ------ | ------- |
| [0.25.1](../../kpanda/intro/release-notes.md) | AMD 64 | 589.01 MB | [:arrow_down: kpanda_0.25.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.25.1_amd64.tar) | [:arrow_down: kpanda_0.25.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.25.1_amd64_checksum.sha512sum) | 2024-02-02 |
| [0.25.0](../../kpanda/intro/release-notes.md) | AMD 64 | 589.01 MB | [:arrow_down: kpanda_0.25.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.25.0_amd64.tar) | [:arrow_down: kpanda_0.25.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.25.0_amd64_checksum.sha512sum) | 2024-01-31 |
| [0.23.0](../../kpanda/intro/release-notes.md) | AMD 64 | 616.29 MB | [:arrow_down: kpanda_0.23.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.23.0_amd64.tar) | [:arrow_down: kpanda_0.23.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.23.0_amd64_checksum.sha512sum) | 2023-12-04 |
| [0.22.2](../../kpanda/intro/release-notes.md) | AMD 64 | 615.81 MB | [:arrow_down: kpanda_0.22.2_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.22.2_amd64.tar) | [:arrow_down: kpanda_0.22.2_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.22.2_amd64_checksum.sha512sum) | 2023-11-14 |
| [0.21.1](../../kpanda/intro/release-notes.md) | AMD 64 | 716.15 MB | [:arrow_down: kpanda_0.21.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.21.1_amd64.tar) | [:arrow_down: kpanda_0.21.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kpanda_0.21.1_amd64_checksum.sha512sum) | 2023-09-15 |

## 校验

在下载离线安装包和校验文件的目录，以 v0.22.2 为例，执行以下命令校验完整性：

```sh
echo "$(cat kpanda_v0.22.2_amd64_checksum.sha512sum)" | sha512sum -c
```

校验成功后打印结果类似于：

```none
kpanda_v0.22.2_amd64.tar: ok
```

## 安装

参阅[离线升级容器管理模块](../../kpanda/intro/offline-upgrade.md)进行安装。

如果是初次安装，请[申请免费体验](../../dce/license0.md)或联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。
