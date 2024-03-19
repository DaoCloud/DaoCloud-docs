# 安装器离线包裁剪脚本使用手册

离线包包含了 DCE5.0 所有产品的离线资源，由于在实际使用过程中，客户并不需要部署所有产品，所以在安装器 v0.16.0 的离线包 `offline/utils/offline-clipper.sh`  提供了 `offline-clipper.sh` 脚本，用以裁剪离线包，以便客户根据实际情况来决定使用哪些产品的离线资源。

## 前提条件

- 裁剪仅针对 GProdcut，在进行裁剪之前，需要先了解包含的 GProdcut 有哪些，以及对应的产品代码，参考[产品清单文件 manifest.yaml](../commercial/manifest.md) 中 `components` 内的信息。

- `kubean`、`ghippo`、`kpanda` 三个组件必须存在，即默认情况会保留这三个组件

## 操作指南

- 若输入为离线包 tarball，输出为离线包 tarball，以保留 `insight` 组件为例：

```shell
offline-clipper.sh --in-tar-path ./offline-v0.15.0-amd64.tar --out-tar-path ./offline.tar --enable-only insight
```

- 若输入为离线包解压后的 `offline` 目录，输出为源离线包解压目录，以保留 `insight` 组件为例：

```shell
offline-clipper.sh --offline-path ./offline --enable-only insight
```

- 若输入为离线包 tarball，输出为离线包解压目录，以仅裁剪 `insight` 组件为例：

```shell
offline-clipper.sh --in-tar-path ./offline-v0.15.0-amd64.tar --disable-only insight
```

- 若输入为离线包解压目录，输出为离线包 tarball，以保留 `insight` 和 `skoala` 组件为例：

```shell
offline-clipper.sh --offline-path ./offline --out-tar-path ./offline.tar --enable-only insight,skoala
```

- 查看可裁剪组件名称

```shell
offline-clipper.sh --offline-path ./offline -l
```

- 查看帮助文档

```shell
offline-clipper.sh -h
```
