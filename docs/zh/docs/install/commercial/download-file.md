---
hide:
  - toc
---

# 文件下载

本页列出了安装器和镜像包的下载地址。

## 下载二进制安装器

在准备好的火种节点上下载 `dce5-installer` 二进制文件。

### AMD 架构二进制

```bash
# 假定 VERSION 为 v0.3.29
export VERSION=v0.3.29
curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
```

### ARM 架构二进制

```bash
# 假定 VERSION 为 v0.3.29
export VERSION=v0.3.29
curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION-linux-arm64
```

## 下载离线镜像包

### AMD 架构离线镜像包

1. 从[下载中心](../../download/dce5.md)下载离线包，或者在火种节点上下载离线镜像包。

    ```shell
    # 假定 VERSION 为 v0.3.29
    export VERSION=v0.3.29
    wget https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-centos7-$VERSION-amd64.tar
    ```

2. 解压离线包。

    ```bash
    tar -zxvf offline-centos7-$VERSION-amd64.tar
    ```

### ARM 架构离线镜像包

1. 从[下载中心](../../download/dce5.md)下载离线包，或者在火种节点上下载离线镜像包。

    ```shell
    # 假定 VERSION 为 v0.3.29
    export VERSION=v0.3.29
    wget https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-kylin-v10sp2-$VERSION-arm64.tar
    ```

2. 解压离线包。

    ```bash
    tar -zxvf offline-kylin-v10sp2-$VERSION-arm64.tar
    ```