
## DaoCloud 文档

DaoCloud 文档采用 Mkdocs，内容通过 Markdown 格式写作，并在 GitHub 上完成版本管理、协作开发等工作。

## 创建本地环境

1. [快速使用 Mkdocs 环境](https://www.mkdocs.org/getting-started/)
2. [下载项目](https://github.com/DaoCloud/daocloud-docs/archive/master.zip) 并解压缩，或者直接[克隆](git@github.com:DaoCloud/daocloud-docs.git)， 用 daocloud-docs 项目内的内容替换 grav-core 的 user 目录（ `~/www/grav-core/user/`）
3. 安装基础依赖 `poetry install`
4. 启动项目 `poetry run mkdocs serve -f mkdocs.yml`
5. 访问本地 http://127.0.0.1:8000/

## 提交文档修改

请您通过 pull reqesut 的方式提交您的文档修改，或新的内容。我们会仔细阅读所有的 PR，如果需要，会与您沟通讨论，修订完善后合并到我们的 master 分支并上线。

在开始工作前，请您仔细阅读 DaoCloud 的[文档书写规范和提交流程](http://docs-static.daocloud.io/write-docs)。

## 感谢

我们衷心感谢所有为 DaoCloud 添砖加瓦的用户。您提出的文档修改如被我们接受，我们会在对应页面的底部，列出您的 ID，以表谢意。

技术支持： [support@daocloud.io](mailto:support@daocloud.io?subject=FROM_DOCS_README)

## 以下用户为本页内容做出了贡献

* [imcaffrey](https://github.com/imcaffrey) 修复了标点符号半角全角不一致的错误
