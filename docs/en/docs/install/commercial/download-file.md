---
hide:
  - toc
---

# Download Document

This page lists the download addresses of installers and image packages.

## Download binary installer

Download the `dce5-installer` binary on a prepared tinder node.

```bash
# Assume VERSION is v0.3.29
export VERSION=v0.3.29
curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
```

## Download offline image package

1. Download the offline package from [Download Center](../../download/dce5.md), or download the offline image package on the Tinder node.

    ```shell
    # Assume VERSION is v0.3.29
    export VERSION=v0.3.29
    wget https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-centos7-$VERSION-amd64.tar
    ```

2. Unzip the offline package.

    ```bash
    tar -zxvf offline-centos7-$VERSION-amd64.tar
    ```