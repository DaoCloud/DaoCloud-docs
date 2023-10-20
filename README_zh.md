# DaoCloud Enterprise 5.0 文档站

[![Contributors](https://img.shields.io/github/contributors/daocloud/daocloud-docs?color=purple)](CONTRIBUTING.md)
[![Build](https://github.com/DaoCloud/DaoCloud-docs/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/DaoCloud/DaoCloud-docs/actions/workflows/main.yml)

中文版 ｜ [English](README.md)

DaoCloud 是经认证的 K8s 服务提供商。目前 DCE 经 CNCF 认证可以完美支撑以下版本：

K8s 官方维护的当前 4 个版本：

[![1.25](../images/1.25.png)](https://github.com/cncf/k8s-conformance/pull/2240)
[![1.26](../images/1.26.png)](https://github.com/cncf/k8s-conformance/pull/2451)
[![1.27](../images/1.27.png)](https://github.com/cncf/k8s-conformance/pull/2666)
[![1.28](../images/1.28.png)](https://github.com/cncf/k8s-conformance/pull/2835)

K8s 官方不再维护（但 DaoCloud [KLTS](https://klts.io/) 会持续维护）的历史版本：

[![1.7](../images/1.7.png)](https://github.com/cncf/k8s-conformance/pull/68)
[![1.9](../images/1.9.png)](https://github.com/cncf/k8s-conformance/pull/210)
[![1.13](../images/1.13.png)](https://github.com/cncf/k8s-conformance/pull/418)
[![1.15](../images/1.15.png)](https://github.com/cncf/k8s-conformance/pull/794)
[![1.18](../images/1.18.png)](https://github.com/cncf/k8s-conformance/pull/1144)
[![1.20](../images/1.20.png)](https://github.com/cncf/k8s-conformance/pull/1463)
[![1.23](../images/1.23.png)](https://github.com/cncf/k8s-conformance/pull/2072)
[![1.24](../images/1.24.png)](https://github.com/cncf/k8s-conformance/pull/2239)

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
4. 访问本地 http://0.0.0.0:8000/

## 文档命名规范

此处列出一些文件、文件夹的命名规范，便于大家贡献和协作。

- 仅包含英文 **小写** 字母和连字符（`-`）
- 禁止包含除英文小写字母和连字符之外的其他符号，例如：
  - 中文字符
  - 空格
  - 特殊字符：`*`, `?`, `\`, `/`, `:`, `#`, `%`, `~`, `{`, `}`
- 单词之间用 **连字符 `-`** 连接
- 尽量简短：建议不超过 5 个英文单词，避免重复冗余信息，可使用常见的英文缩写
- 易于识别：文件名应能描述文档的主题和内容

| 不建议                             | 建议             | 原因                         |
| ---------------------------------- | ---------------- | ---------------------------- |
| ConfigName                         | config-name      | 应使用英文小写字母与连字符   |
| 创建 秘钥                          | create-secret    | 不要使用中文和空格、宏符号等 |
| quick-start-install-online-install | online-install   | 文档名应简短                 |
| c-ws                               | create-workspace | 文档名应清晰易懂             |
| update_config                      | update-config    | 用连字符连接单词             |

## 基础写作规范

- 使用 4 个空格的缩进（一个 tab 键）
- 中英字符之间 1 个空格
- 段前段后分别空一行，包括图片前后、嵌套列表前后
- 标题尾部不要加标点符号
- 请勿使用空链接、死链接
- 标题层级依次增加，不要跳级

在修改文档时，请参阅 DaoCloud 的[文档书写规范](./style.md)。

## 联系我们

技术支持：[support@daocloud.io](mailto:support@daocloud.io?subject=FROM_DOCS_README)

扫描二维码与开发者畅快交流：

![wechat](https://docs.daocloud.io/daocloud-docs-images/docs/images/assist.png)

## 参考链接

- [文档站发布说明 v1.0](docs/README.md)
- [DaoCloud 文档编写风格](./style.md)
- [社区贡献指南](./CONTRIBUTING.md)
- [社区行为准则](./CODE_OF_CONDUCT.md)
- [导出 Word 和 PDF](./scripts/generate_pdf_zh.md)
- [页面自动翻译](./scripts/README.md)；推荐使用质量更高的 ChatGPT 翻译

## 感谢所有贡献者 ❤

<a href="https://github.com/daocloud/daocloud-docs/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=daocloud/daocloud-docs" />
</a>
