# 一键下载所有离线包

本页提供了脚本来一键下载安装 DCE 5.0 所需的离线包。

## 下载脚本

    ```bash
    export VERSION= v0.8.0
    curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/download_packages_${VERSION}.sh
    chmod +x download_packages_${VERSION}.sh
    ```

## 执行脚本

    ```bash
    ./download_packages_${VERSION}.sh ${DISTRO} ${INSTALLER_VERSION} ${ARCH}
    ```

参数说明：

| 参数 | 默认值 | 有效值范围 |
|  ----  | ----  | ----  |
| VERSION | 当前下载脚本版本 | 目前仅 v0.8.0 版本支持 |
| INSTALLER_VERSION | 指定下载 DCE 5.0 的版本 | 有效 DCE 5.0 的发行版本即可 |
| DISTRO | `centos7` | `centos7` `kylinv10` `redhat8` `ubuntu2004` |
| ARCH | `amd64` | `amd64` `arm64` |

!!! note

    - amd64 支持的操作系统：centos7、redhat8、ubuntu2004
    - arm64 支持的操作系统：kylinv10
