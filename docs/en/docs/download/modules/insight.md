---
hide:
   - navigation
---

# Insight

On this page, you can download the offline installation packages of each version of the observability module.

## Download

| Filename | Version | Architecture | File Size | Installer | Date Updated |
| ------------------------------ | ------------------ ------------------------------------- | ----- |------- - | ------------------------------------------------ -------------------------------------------------- -------- | ---------- |
| insight_v0.13.1_amd64.tar | [v0.13.2](../../insight/intro/releasenote.md) | AMD64 | 2.41 GB | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/insight_v0.13.1_amd64.tar) | 2022-12-30 |

## Validation

In the directory where the offline installation package was downloaded, execute the following command to verify the integrity:

```sh
echo "cb246c2fb275780a87bb37f915cf58fb3097aa99606afd112aff2c0bb7716816ed96ca10260a0dffed0228bb33fa466310b10e8dad6c49c12351fbe48036bbbf  dist/offline/insight_v0.13.1_amd64.tar" | sha512sum -c
```

If the verification is successful, it will print:

```none
insight.tar: ok
```

## Install

Refer to [Observability](../../insight/user-guide/01quickstart/offlineInstall.md) installation process for installation.

If it is the first installation, please [apply for free trial](../../dce/license0.md) or [genuine authorization](https://qingflow.com/f/e3291647).
If you have any license key related questions, please contact DaoCloud delivery team.
