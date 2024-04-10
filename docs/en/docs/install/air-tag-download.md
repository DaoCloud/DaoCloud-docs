---
MTPE: windsonsea
date: 2024-03-07
---

# Download All Offline Packages with One-Click

This page provides a script to easily download all the offline packages required for installing DCE 5.0.

## Download Script

```bash
export VERSION=v0.16.1
curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/download_packages_${VERSION}.sh
chmod +x download_packages_${VERSION}.sh
```

## Run Script

```bash
./download_packages_${VERSION}.sh ${DISTRO} ${VERSION} ${ARCH}
```

**Parameters:**

| Parameter | Default Value | Valid Values |
| ---- | ---- | ---- |
| VERSION | Current script version | Only supports v0.8.0 currently |
| DISTRO | `centos7` | `centos7` `kylinv10` `redhat8` `ubuntu2004` |
| ARCH | `amd64` | `amd64` `arm64` |

!!! note

    - Supported operating systems for amd64: centos7, redhat8, ubuntu2004
    - Supported operating system for arm64: kylinv10
