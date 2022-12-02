---
hide:
  - toc
---

# 文件下载

本页列出了安装器和镜像包的下载地址。

## 下载二进制安装器

在准备好的火种节点上下载 `dce5-installer` 二进制文件。

```bash
# 假定 VERSION 为 v0.3.28
export VERSION=v0.3.28
curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
```

## 下载离线镜像包

1. 从[下载中心](../../download/dce5.md)下载离线包，或者在火种节点上下载离线镜像包。

    ```shell
    # 假定 VERSION 为 v0.3.28
    export VERSION=v0.3.28
    wget https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-$VERSION.tar
    ```

2. 解压离线包。

    ```bash
    tar -zxvf offline-$VERSION.tar
    ```
