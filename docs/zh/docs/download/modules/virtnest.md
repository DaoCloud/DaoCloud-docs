# 虚拟机管理

本页可下载虚拟机管理模块各版本的离线安装包。

## 下载

| 版本 | 架构 | 文件大小 | 安装包 | 校验文件 | 更新日期 |
| ---- | --- | ------- | ---- | ------- | ------- |
| [v0.4.0](../../virtnest/intro/release-notes.md) | AMD 64 | 1.43 GB | [:arrow_down: virtnest_v0.4.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/virtnest_v0.4.0_amd64.tar) | [:arrow_down: virtnest_v0.4.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/virtnest_v0.4.0_amd64_checksum.sha512sum) | 2023-11-30 |
| [v0.3.0](../../virtnest/intro/release-notes.md) | AMD 64 | 1.45 GB | [:arrow_down: virtnest_v0.3.0_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/virtnest_v0.3.0_amd64.tar) | [:arrow_down: virtnest_v0.3.0_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/virtnest_v0.3.0_amd64_checksum.sha512sum) | 2023-11-06 |

## 校验

在下载离线安装包和校验文件的目录，以 `v0.3.0_amd64` 为例，执行以下命令校验完整性：

```sh
echo "$(cat virtnest_v0.3.0_amd64_checksum.sha512sum)" | sha512sum -c
```

校验成功后打印结果类似于：

```none
virtnest_v0.3.0_amd64.tar: ok
```

## 安装

参阅[虚拟机容器](../../virtnest/install/offline-install.md)安装流程进行安装。

如果是初次安装，请[申请免费体验](../../dce/license0.md)或联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。
