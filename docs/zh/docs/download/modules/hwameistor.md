---
hide:
  - toc
---

# 本地存储：hwameistor-operator

本页可下载 hwameistor-operator 的离线安装包，然后通过这个 Operator 安装 HwameiStor 本地存储模块。

## 下载

| 版本 | 架构   | 文件大小 | 安装包  | 校验文件 | 更新日期 |
| --- | ------ | ------- | ----- | ------- | ------- |
| [v0.13.1] | AMD 64 | 1.62 GB   | [:arrow_down: hwameistor-operator_v0.13.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/hwameistor-operator_v0.13.1_amd64.tar) | [:arrow_down: hwameistor-operator_v0.13.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/hwameistor-operator_v0.13.1_amd64_checksum.sha512sum) | 2023-11-06 |

## 校验

在下载离线安装包和校验文件的目录，以 `v0.13.1_amd64` 为例，执行以下命令校验完整性：

```sh
echo "$(cat hwameistor-operator_v0.13.1_amd64_checksum.sha512sum)" | sha512sum -c
```

校验成功后打印结果类似于：

```none
hwameistor-operator_v0.13.1_amd64.tar: ok
```

## 安装

参阅 [hwameistor-operator 安装流程](../../storage/hwameistor/install/deploy-operator.md)进行安装。

如果是初次安装，请[申请免费体验](../../dce/license0.md)或联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
如果有任何许可密钥相关的问题，请联系 DaoCloud 交付团队。
