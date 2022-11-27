# 全局管理

## 下载

| 文件名称 | 版本 | Release Note | 文件大小 | 安装包 | checksum | 更新日期 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| ghippo-0.12.0-dev-5-amd64.bundle.tar | 0.12.0-dev-5 | [查看](../../ghippo/01ProductBrief/release-notes.md) |  | [下载](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ghippo-0.12.0-dev-5-amd64.bundle.tar) | [下载](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ghippo-0.12.0-dev-5-amd64-checksum.txt) | 2022-11-27 |

## 校验

下载 checksum 文件，且将此文件与离线安装包置于同一个目录。执行以下命令校验安装包：

```sh
echo "$(cat checksum.txt)" | sha512sum -c
```

校验成功会打印：

```none
ghippo.tar: ok
```

## 安装

成功校验离线安装包之后，请参[全局管理](../../ghippo/install/offlineInstall.md)安装流程进行安装。

成功安装之后请进行正版授权。
