---
hide:
  - toc
---

# 仪表盘 Ipavo

本页可下载仪表盘模块各版本的离线安装包。

## 下载

| 版本 | 架构 | 文件大小 | 安装包 | 校验文件 | 更新日期  |
| ---- | --- | ------ | ----- | ------- | -------- |
| [v0.13.0](../../insight/intro/release-notes.md) | <font color="green">ARM 64</font> | 50.32 MB | [:arrow_down: ipavo_v0.13.0_arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ipavo_v0.13.0_arm64.tar) | [:arrow_down: ipavo_v0.13.0_arm64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ipavo_v0.13.0_arm64_checksum.sha512sum) | 2024-10-28 |
| [v0.13.0](../../insight/intro/release-notes.md) | AMD 64 | 52.65 MB | [:arrow_down: ipavo_v0.13.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ipavo_v0.13.0_amd64.tar) | [:arrow_down: ipavo_v0.13.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ipavo_v0.13.0_amd64_checksum.sha512sum) | 2024-10-28 |
| v0.12.4 | AMD 64 | 51 MB | [:arrow_down: ipavo_v0.12.4_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ipavo_v0.12.4_amd64.tar) | [:arrow_down: ipavo_v0.12.4_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ipavo_v0.12.4_amd64_checksum.sha512sum) | 2024-10-12 |
| v0.12.4 | <font color="green">ARM 64</font> | 51 MB | [:arrow_down: ipavo_v0.12.4_arm64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ipavo_v0.12.4_arm64.tar) | [:arrow_down: ipavo_v0.12.4_arm64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ipavo_v0.12.4_arm64_checksum.sha512sum) | 2024-10-12 |

## 校验

在下载离线安装包和校验文件的目录，以 v0.12.4_amd64 为例，执行以下命令校验完整性：

```sh
echo "$(cat ipavo_v0.12.4_amd64_checksum.sha512sum)" | sha512sum -c
```

校验成功后打印结果类似于：

```none
ipavo_v0.12.4_amd64.tar: ok
```

如果是初次安装，请[申请免费体验](../../dce/license0.md)或联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。
