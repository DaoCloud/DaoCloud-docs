
# DaoCloud Enterprise 5.0 文档站

[![Contributors](https://img.shields.io/github/contributors/daocloud/daocloud-docs?color=purple)](CONTRIBUTING.md)
[![Build](https://github.com/DaoCloud/DaoCloud-docs/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/DaoCloud/DaoCloud-docs/actions/workflows/main.yml)

中文版 ｜ [English](README.md)

本文档站采用 Mkdocs 编译而成，文档内容通过 Markdown 格式写作，并在 GitHub 上完成版本管理、协作开发等工作。

## 提交 PR 修改文档

通过 Pull Request (PR) 的方式提交文档修改、译文或新编内容。

1. 点击 `Fork` 按钮创建一个 Fork
2. 运行 `git clone` 克隆这个 Fork
3. 本地编辑文档，本地预览
4. 依次运行 `git add`, `git commit`, `git push` 提交文档
5. 进入本 repo 页面发起 PR
6. PR 评审后成功合并，谢谢。

在修改文档前，请仔细阅读 DaoCloud 的[文档书写规范](http://docs-static.daocloud.io/write-docs)。

## 创建本地预览环境

### 使用 Docker 预览

1. 需要本地安装好 Docker，启动 Docker
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
- 请勿使用空链接
- 标题层级依次增加，不要跳级

## 感谢

我们衷心感谢所有为 DaoCloud 添砖加瓦的贡献者。您提出的文档修改成功合并后，您的 ID 将出现对应页面的底部，以表谢意。

技术支持：[support@daocloud.io](mailto:support@daocloud.io?subject=FROM_DOCS_README)
