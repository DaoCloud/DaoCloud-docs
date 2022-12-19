---
hide:
  - navigation
---

# Global management

On this page, you can download the offline installation packages of various versions of the global management module.

## download

| file name | version | file size | package | update date |
| ------------------------------ | ------------------ --------------------------------------- | -------- | ---- -------------------------------------------------- -------------------------------------------------- -- | ---------- |
| ghippo-0.12.1-amd64.bundle.tar | [v0.12.1](../../ghippo/01ProductBrief/release-notes.md) | 442 MB | [:arrow_down: Download](https:// proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/ghippo-0.12.1-amd64.bundle.tar) | 2022-11-29 |

## validation

In the directory where the offline installation package was downloaded, execute the following command to verify the integrity:

```sh
echo "16f3f5549e3f776d46642e94bb4675ab847f5fa3489ee3b7c65ce9c8d36e451989aada4f7042d4c078ea7dcf321b1920b97c6568d3262e234d8c7ed775f9ac70  dist/offline/ghippo-0.12.1.bundle.tar" | sha512sum -c
```

If the verification is successful, it will print:

```none
ghippo.tar: ok
```

## Install

Refer to [Global Management](../../ghippo/install/offlineInstall.md) installation process for installation.

If it is the first installation, please [apply for free trial](../../dce/license0.md) or [genuine authorization](https://qingflow.com/f/e3291647).
If you have any license key related questions, please contact DaoCloud delivery team.