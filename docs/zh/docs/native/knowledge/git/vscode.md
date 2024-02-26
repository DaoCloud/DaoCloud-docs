# VSCode 编辑技巧

[VSCode](https://code.visualstudio.com/) 目前是使用最广泛的 IDE 开发环境。

## 插件

安装一些插件，可以让你的工作事半功倍。
点击 **View** -> **Extentions** ，可以找到很多插件。
这里有几个推荐的插件：

- HTTP/s and relative link checker： 检查多语言文档中的 link
- Markdown Link Updater：当你修改了某个文件名，移动了文件夹，会自动修改相对路径，可以节省很多手动调整的时间
- i18n Ally：UI 多语言翻译必备工具
- Markdownlint：检查 markdown 语法，让你的文档编辑看起来更标准、更美观
- Markdown Preview Mermaid Support：可以实时预览 mermaid 流程图
- VS Code Counter：按文件夹统计代码行数

## 习惯

如果你要处理多语言文档，建议分屏操作，例如方便中英对照，底部终端直接敲命令。

![split screen](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/vscode01.png)

## 编辑 Repo

`git clone` 某个 repo 后，建议通过 **File** -> **Open Folder...** 进入 repo 工作空间。
随后就能在底部终端的 repo 根目录下运行各种 git 命令了。

![workspace](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/vscode02.png)

## 常用正则表达式

查找所有图片：

```text
!\[.*?\]\((?:https?:\/\/)?\S+\.(?:png|jpg|jpeg|gif|bmp)\)
```

查找所有前后带 /` 的字符，并替换为粗体：

```text
`([^`].*?)`
```
```text
**$1**
```

![search](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/vscode03.png)
