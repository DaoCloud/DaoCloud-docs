
# DaoCloud Enterprise 5.0 文档站

本文档站采用 Mkdocs 编译而成，文档内容通过 Markdown 格式写作，并在 GitHub 上完成版本管理、协作开发等工作。

## 创建本地预览环境

1. [快速使用 Mkdocs 环境](https://www.mkdocs.org/getting-started/)
2. [下载项目](https://github.com/DaoCloud/daocloud-docs/archive/main.zip)并解压缩，或者直接[克隆](https://github.com/DaoCloud/DaoCloud-docs.git)
3. 安装基础依赖 `poetry install`
4. 启动项目 `poetry run mkdocs serve -f mkdocs.yml`
5. 访问本地 http://127.0.0.1:8000/

## 提交 PR 修改文档

请您通过 Pull Request (PR) 的方式提交文档修改或新内容。我们会仔细查验所有的 PR。如有必要，会与您沟通讨论，修订完善后合并到 main 分支并发布到文档站。

1. 点击 `Fork` 按钮创建一个 Fork
2. 运行 `git clone` 克隆自己的 Fork
3. 本地编辑文档，检查本地预览
4. 依次运行 `git add`, `git commit`, `git push` 提交文档
5. 进入本 repo 页面发起 PR
6. PR 评审后成功合并，谢谢。

在修改文档前，请仔细阅读 DaoCloud 的[文档书写规范](http://docs-static.daocloud.io/write-docs)。

## 基础写作规范

- 使用四个空格的缩进
- 中英文字符之间空格
- 每段的段前段后分别空一行，包括图片前后、嵌套列表下的段落前后均需空行
- 标题后不加标点符号
- 禁止使用空链接
- 标题层级依次增加，不要跳级


## 感谢

我们衷心感谢所有为 DaoCloud 添砖加瓦的用户。您提出的文档修改如被我们接受，我们会在对应页面的底部，列出您的 ID，以表谢意。

技术支持：[support@daocloud.io](mailto:support@daocloud.io?subject=FROM_DOCS_README)
