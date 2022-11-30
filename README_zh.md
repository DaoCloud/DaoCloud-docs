# DaoCloud Enterprise 5.0 文档站

[![Contributors](https://img.shields.io/github/contributors/daocloud/daocloud-docs?color=purple)](CONTRIBUTING.md)
[![Build](https://github.com/DaoCloud/DaoCloud-docs/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/DaoCloud/DaoCloud-docs/actions/workflows/main.yml)

中文版 ｜ [English](README.md)

DaoCloud 是经认证的 K8s 服务提供商。目前 DCE 经 CNCF 认证可以完美支撑以下版本：

当前版本：

[![1.23](./docs/zh/docs/images/1.23.png)](https://github.com/cncf/k8s-conformance/pull/2072)
[![1.24](./docs/zh/docs/images/1.24.png)](https://github.com/cncf/k8s-conformance/pull/2239)
[![1.25](./docs/zh/docs/images/1.25.png)](https://github.com/cncf/k8s-conformance/pull/2240)

历史版本：

[![1.7](./docs/zh/docs/images/1.7.png)](https://github.com/cncf/k8s-conformance/pull/68)
[![1.9](./docs/zh/docs/images/1.9.png)](https://github.com/cncf/k8s-conformance/pull/210)
[![1.13](./docs/zh/docs/images/1.13.png)](https://github.com/cncf/k8s-conformance/pull/418)
[![1.15](./docs/zh/docs/images/1.15.png)](https://github.com/cncf/k8s-conformance/pull/794)
[![1.18](./docs/zh/docs/images/1.18.png)](https://github.com/cncf/k8s-conformance/pull/1144)
[![1.20](./docs/zh/docs/images/1.20.png)](https://github.com/cncf/k8s-conformance/pull/1463)

本文档站采用 MkDocs 编译而成，文档内容通过 Markdown 格式写作，并在 GitHub 上完成版本管理、协作开发等工作。

## 提交 PR 修改文档

通过 Pull Request (PR) 的方式提交文档修改、译文或新编内容。

1. 点击 `Fork` 按钮创建一个 Fork
2. 运行 `git clone` 克隆这个 Fork
3. 本地编辑文档，本地预览
4. 依次运行 `git add`, `git commit`, `git push` 提交文档
5. 进入本 repo 页面发起 PR
6. PR 评审后成功合并，谢谢。

## 创建本地预览环境

本节说明如何在你的本机上预览修改效果。

### 使用 Docker 预览

1. 需要本地安装好 Docker，启动 [Docker](https://www.docker.com/)
2. 运行 `make serve`

### 使用 Git repo 预览

参阅 [MkDocs 官方安装文档](https://squidfunk.github.io/mkdocs-material/getting-started/)。

1. 安装开发环境： Poetry 和 Python 3.9 以上
   1. 配置 poetry: `poetry config virtualenvs.in-project true`
   2. 开启 venv: `poetry env use 3.9`
2. 安装基础依赖：`poetry install`
3. 启动项目 `poetry run mkdocs serve -f mkdocs.yml`
4. 访问本地 http://127.0.0.1:8000/

## 基础写作规范

- 使用 4 个空格的缩进（一个 tab 键）
- 中英字符之间 1 个空格
- 段前段后分别空一行，包括图片前后、嵌套列表前后
- 标题尾部不要加标点符号
- 请勿使用空链接、死链接
- 标题层级依次增加，不要跳级

在修改文档时，请参阅 DaoCloud 的[文档书写规范](./style.md)。

## 感谢

特别感谢 [SAMZONG](https://github.com/SAMZONG) 对文档站后台技术的强劲支撑。

衷心感谢所有为 DaoCloud 文档站添砖加瓦的所有贡献者们，感谢数百位 DCE 开发者日以继夜的辛勤付出，愿云原生社区进一步发展壮大。技术无国界，欢迎你我他 🤝

## 联系我们

技术支持：[support@daocloud.io](mailto:support@daocloud.io?subject=FROM_DOCS_README)

扫描二维码与开发者畅快交流：

![](./docs/zh/docs/images/assist.png)