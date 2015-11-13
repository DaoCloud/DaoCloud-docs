---
title: 提交内容并集成发布
taxonomy:
    category:
        - docs
process:
    twig: true
---

#### DaoCloud 文档后台

DaoCloud 文档采用 Grav CMS，内容通过 Markdown 格式写作，并在 GitHub 上完成版本管理、协作开发等工作。

#### 创建本地环境

1. [下载 Grav 主程序](http://getgrav.org/downloads)
2. 把 ZIP 包解压缩到您的 weboot 目录， (例如 `~/www/grav-core/`)
3. [下载](https://github.com/getgrav/grav-learn/archive/develop.zip) 并解压缩，或者直接[克隆](https://github.com/getgrav/grav-learn.git), 把 daocloud-docs 覆盖 grav-core 的 user 目录（ `~/www/grav-core/user/`）
4. 在 grav－core 根目录运行 `bin/grav install`  (e.g. `~/www/grav-core/`)完成以来安装
5. 如需运行，请先安装 PHP，然后使用 `php -S localhost:8000`，启动程序

注意：确保 dalcoud-docs 文件夹下有 .dependencies 隐藏文件，否则无法完成 grav 插件的依赖安装
如无此文件，可根据以下内容创建

````yaml
git:
    anchors:
        url: https://github.com/getgrav/grav-plugin-anchors
        path: user/plugins/anchors
        branch: master
    simplesearch:
        url: https://github.com/getgrav/grav-plugin-simplesearch
        path: user/plugins/simplesearch
        branch: master
    error:
        url: https://github.com/getgrav/grav-plugin-error
        path: user/plugins/error
        branch: master
    github:
        url: https://github.com/getgrav/grav-plugin-github
        path: user/plugins/github
        branch: master
    highlight:
        url: https://github.com/getgrav/grav-plugin-highlight
        path: user/plugins/highlight
        branch: master
    gravui:
        url: https://bitbucket.org/rockettheme/grav-plugin-gravui
        path: user/plugins/gravui
        branch: master
    learn2:
        url: https://github.com/getgrav/grav-theme-learn2
        path: user/themes/learn2
        branch: master
links:
    anchors:
        src: grav-plugin-anchors
        path: user/plugins/anchors
        scm: github
    simplesearch:
        src: grav-plugin-simplesearch
        path: user/plugins/simplesearch
        scm: github
    error:
        src: grav-plugin-error
        path: user/plugins/error
        scm: github
    github:
        src: grav-plugin-github
        path: user/plugins/github
        scm: github
    highlight:
        src: grav-plugin-highlight
        path: user/plugins/highlight
        scm: github
    gravui:
        src: grav-plugin-gravui
        path: user/plugins/gravui
        scm: bitbucket
    learn2:
        src: grav-theme-learn2
        path: user/themes/learn2
        scm: github
```

