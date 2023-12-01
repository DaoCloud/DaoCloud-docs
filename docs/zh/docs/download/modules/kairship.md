# 多云编排 Kairship

本页可下载多云编排模块各版本的离线安装包。

## 下载

| 版本                                            | 架构 | 文件大小 | 安装包                                                                                                                             |  校验文件 | 更新日期      |
|-----------------------------------------------| ----- |-------- |---------------------------------------------------------------------------------------------------------------------------------| ---------- |-----------|
| [v0.14.0](../../kairship/intro/release-notes.md) | AMD 64 | 524.58MB | [:arrow_down: kairship_v0.14.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kairship_v0.14.0_amd64.tar) | [:arrow_down: kairship_v0.14.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kairship_v0.14.0_amd64_checksum.sha512sum) | 2023-12-01 |
| [v0.13.1](../../kairship/intro/release-notes.md) | AMD 64 | 527.09MB | [:arrow_down: kairship_v0.13.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kairship_v0.13.1_amd64.tar) | [:arrow_down: kairship_v0.13.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kairship_v0.13.1_amd64_checksum.sha512sum) | 2023-11-03 |
| [v0.13.0](../../kairship/intro/release-notes.md) | AMD 64 | 527.09MB | [:arrow_down: kairship_v0.13.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kairship_v0.13.0_amd64.tar) | [:arrow_down: kairship_v0.13.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kairship_v0.13.0_amd64_checksum.sha512sum) | 2023-10-26 |
| [v0.12.0](../../kairship/intro/release-notes.md) | AMD 64 | 525.11MB | [:arrow_down: kairship_v0.12.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kairship_v0.12.0_amd64.tar) | [:arrow_down: kairship_v0.12.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kairship_v0.12.0_amd64_checksum.sha512sum) | 2023-09-01 |
| [v0.11.0](../../kairship/intro/release-notes.md) | AMD64 | 486 MB | [:arrow_down: kairship_v0.11.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kairship_v0.4.0_amd64.tar) | [:arrow_down: kairship_v0.11.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/kairship_v0.4.0_amd64_checksum.sha512sum) | 2023-7-31 |

## 校验

在下载离线安装包和校验文件的目录，以 v0.11.0 为例，执行以下命令校验完整性：

```sh
echo "$(cat kairship_v0.11.0_amd64_checksum.sha512sum)" | sha512sum -c
```

校验成功后打印结果类似于：

```none
kairship_v0.4.0_amd64.tar: ok
```

## 安装

如果是初次安装，请[申请免费体验](../../dce/license0.md)或联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。
