---
hide:
  - toc
---

# 文件下载

本页列出了安装器和镜像包的下载地址。

## 二进制安装器下载

在准备好的火种节点上下载 `dce5-installer` 二进制文件。

```bash
# 假定 VERSION 为 v0.3.24
export VERSION=v0.3.24
curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
```

## 离线镜像包下载

1. 在火种节点上下载离线镜像包。

    ```shell
    # 假定 VERSION 为 v0.3.24
    export VERSION=v0.3.24
    wget https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-$VERSION.tar
    ```

2. 解压离线包。

    ```bash
    tar -zxvf offline-$VERSION.tar
    ```
