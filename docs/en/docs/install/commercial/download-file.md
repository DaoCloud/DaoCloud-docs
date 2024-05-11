---
MTPE: windsonsea
date: 2024-05-11
hide:
   - toc
---

# Download Document

This page lists the download addresses of installers and image packages.

## Download offline image package

### AMD architecture offline image package

1. Download the offline image package on the bootstrapping node. You can download other versions of the offline package from [Download Center](../../download/index.md).

     ```shell
     # Assume VERSION is v0.4.0
     export VERSION=v0.4.0
     wget https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-centos7-$VERSION-amd64.tar
     ```

2. Unzip the offline package.

     ```bash
     tar -xvf offline-centos7-$VERSION-amd64.tar
     ```

### ARM architecture offline image package

1. Download the offline image package on the bootstrapping node. You can download other versions of the offline package from [Download Center](../../download/index.md).

     ```shell
     # Assume VERSION is v0.4.0
     export VERSION=v0.4.0
     wget https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-kylin-v10sp2-$VERSION-arm64.tar
     ```

2. Unzip the offline package.

     ```bash
     tar -xvf offline-kylin-v10sp2-$VERSION-arm64.tar
     ```

## Download the ISO offline package

| CPU Architecture | Operating System Version | Download URL |
| --------- | --------------------------------------- ------------ | ------------------------------------- ----------------------- |
| AMD64 | Centos 7 | https://mirrors.tuna.tsinghua.edu.cn/centos/7.9.2009/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso |
| ARM64 | Kylin Linux Advanced Server release V10 (Sword) SP2 | Application address: https://www.kylinos.cn/scheme/server/1.html<br />Note: Kylin operating system needs to provide personal information to download and use, please choose V10 (Sword) SP2 when downloading |
