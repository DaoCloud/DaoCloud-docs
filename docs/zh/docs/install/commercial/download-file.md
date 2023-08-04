---
hide:
  - toc
---

# 文件下载

本页列出了安装器和镜像包的下载地址。

## 下载离线镜像包

### AMD 架构离线镜像包

1. 在火种节点上下载离线镜像包，可从[下载中心](../../download/index.md)下载其他版本的离线包。

    ```shell
    # 假定 VERSION 为 v0.4.0
    export VERSION=v0.4.0
    wget https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-centos7-$VERSION-amd64.tar
    ```

2. 解压离线包。

    ```bash
    tar -xvf offline-centos7-$VERSION-amd64.tar
    ```

### ARM 架构离线镜像包

1. 在火种节点上下载离线镜像包，可从[下载中心](../../download/index.md)下载其他版本的离线包。

    ```shell
    # 假定 VERSION 为 v0.4.0
    export VERSION=v0.4.0
    wget https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-kylin-v10sp2-$VERSION-arm64.tar
    ```

2. 解压离线包。

    ```bash
    tar -xvf offline-kylin-v10sp2-$VERSION-arm64.tar
    ```

## 下载 ISO 操作系统镜像文件

| CPU  架构 | 操作系统版本                                        | 下载地址                                                     |
| --------- | --------------------------------------------------- | ------------------------------------------------------------ |
| AMD64    | Centos 7                                            | https://mirrors.tuna.tsinghua.edu.cn/centos/7.9.2009/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso |
| ARM64    | Kylin Linux Advanced Server release V10 (Sword) SP2 | 申请地址：https://www.kylinos.cn/scheme/server/1.html<br />注意：麒麟操作系统需要提供个人信息才能下载使用，下载时请选择 V10 (Sword) SP2 |
