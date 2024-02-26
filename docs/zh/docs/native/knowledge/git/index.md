# Git 文档流程

本页简要说明一些通用的 Git 文档编写、评审、翻译流程和技巧。

## 准备

良好的网络环境，嗯，这是必须的 O(∩_∩)O

## Git 云端编写 (For Author)

如今云无处不在，只要能连通互联网，就可以在线编辑，无需构建环境和安装工具。

### 网页直接修改

这种方式仅适合改 1 个文件的小幅修改。

1. 在任何一个网页上点击编辑图标。

    !!! tip

        K8s 和 Istio 网站都有类似的按钮，比如 __Edit this page__ 、 __Edit this page on GitHub__ 。

    ![点击图标按钮](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/local01.png)

1. 完成编辑操作后，点击右上角的 __Commit changes__ 按钮。

    ![commit change](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/local02.png)

1. 修改 __Commit message__ ，填写 __Extended description__ 后，点击 __Propose changes__ 按钮。

    ![propose change](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/local03.png)

1. 点击 __Create pull request__ 按钮就完成了提交 PR 的操作。

    ![create PR](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/local04.png)

1. 提交 PR 后，Reviewer 会给出一些 comments，你也可以在网页上修改。

    点击 __Files changed__ 页签，点击右侧的 __...__ ，选择 __Edit file__ ，就能开始编辑修改文件了。

    ![Edit file](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/local05.png)

    !!! caution

        在看到 comment 后，不要关闭 PR！
        社区法则第一条：尊重彼此及其劳动成果。
        要努力按 suggestions 去解决问题！这个很重要！

### 通过 Codespace 编辑

如果你修改的文件不止 1 个，那可以试试 Codespace。Codespace 是一个云端的 VSCode 环境。
这种云端的 VSCode 好处是随时随地，缺点是免费版本只能保留几小时的环境，只有 VIP 才能长期留存数据。

1. 进入你的 Fork，点击 __Code__ -> __Codespaces__ -> __Create Codespace on main__ 。

    ![Create Codespace](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/cloud01.png)

1. 稍待片刻完成环境的创建，

    ![online vscode](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/cloud02.png)

1. 你可以在底部 TERMINAL 中运行各种命令，从左侧目录树中找到要修改的文件。

    ![online edit](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/cloud03.png)

1. 编辑完成后，跟在本地一样，运行 git 命令提交修改。

!!! tip

    - 目前免费的 Codespace 貌似只能留存 1 小时的数据。
    - 提了 PR 只是一个开始，Reviewer 可能会给出许多 comment，要记得及时去修改。

## Git 本地编写 (For Author)

这是 Git 老兵们常用的编辑方式。在本地编辑之前，需要预先安装几个工具：

- [Git](https://git-scm.com/downloads)，必需，装完才能支持各种 Git 命令
- [VScode](https://code.visualstudio.com/)，推荐，常用的 Markdown 编辑器
- [Typora](https://macwk.com/soft/typora)，可选，可以粘贴网页的图表文字，转换成 markdown 格式

准备好上述工具后，参照以下步骤从本地提 PR：

1. Fork 后克隆 GitHub 仓库。

    ```bash
    git clone https://github.com/windsonsea/daodocs.git
    ```

1. 在本地创建分支。

    ```bash
    git checkout -b yourbranch
    ```

1. 在本地完成编辑工作后，推荐在本地运行 __mkdocs serve__ 进行预览，以免把错误带到线上。
   
    ![本地预览](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/make-serve.png)

    !!! tip
    
        - 每天开始前，切到 main 分支，运行 __git pull__ 更新本地数据，与服务器的文件保持同步，以免跟别人的修改发生冲突。
        - 每天结束前，要将当天的修改提交上去。Git 是一种小步快走的开发模式，只需保证每一步正确，那天长日久将成就伟业。

1. 本地预览正常后，依次运行以下命令提交修改的内容。
   参见更多 [GitHub 命令](https://education.github.com/git-cheat-sheet-education.pdf)。

    ```bash
    git add .
    git commit -m "fix a typo in chapter 1" 
    git push origin yourbranch
    ```

1. 从网页上进入 GitHub 仓库，提交 PR。
   
    ![提 PR](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/pr.png)

    > - 有些项目要求 1 个 commit 提交 1 次 PR，如遇到 rebase 提示可参考 [GitHub rebase 问题](rebase.md)
    > - 对于 Scrum 开发组，若改动较大，请在 main/release-notes/notes 目录仿照其他文件创建一个 yaml，填写必要的信息
    > - 有关 GitHub 基础知识，参阅 [B 站教程](https://www.bilibili.com/video/BV18y4y1S7VC?p=9&spm_id_from=pageDriver)

## Git 评审流程 (For Reviewer)

这是代码、文档和任何修改都通用的评审流程。

1. 作者提交 PR 后，相关 Reviewer 会收到一封邮件。

    ![请求 review](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/review1.png)

1. 点击 __Files changed__ 查看改了什么内容。

    ![review 列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/review2.png)

1. 如果对某句话有不同想法，可以直接添加 comment。

    ![添加注释](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/review3.png)

    - 建议点击 __Add a suggestion__ 图标后进行修改，这样 PR 作者可以清晰看到评审建议。
    - 写好 comment 后，点击 __Start a review__ 按钮，继续看其他字句，全部看完以后统一 __Submit review__ 

1. PR 作者收到 comment 后，要及时去修复，最后运行以下命令覆盖原来的提交。

    ```git
    git add .
    git commit --amend --no-edit
    git push origin yourbranch -f
    ```

1. 经作者反复修改后，若没有其他问题，Reviewer 会给出以下标记，批准合并 PR：

    ![审批通过](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/review4.png)

    ```git
    /lgtm
    /approve
    ```
  
> 对于 Spiderpool、Spidernet 这几个网络项目，push 之前需要运行以下命令校验 markdownlint、拼写和 YAML 语法：

```shell
make lint-markdown-format
make lint-markdown-spell-colour
make lint-yaml
```

## 前端 UI 翻译 (For Translator)

对于前端 UI 文字翻译，除了 Weblate 翻译外，还可以用 i18n 插件。以 VScode 为例：

1. 安装 __i18n Ally__ 插件。

    ![安装插件](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/i18n01.png)

1. 运行以下命令安装所有依赖项：

    ```shell
    npm i
    ```

1. 点击左侧的 __i18n Ally__ 页签，找到 __No Translation__ 内容，点击 __Open in editor__ 图标。

    ![开始翻译](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/i18n02.png)

1. 翻好一个字段后，点击下一个字段。可以在 Source Control 部分查看完成的译文。

    ![翻译中](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/i18n03.png)

1. 译文检查无误后，依次运行以下命令提交。

    ```shell
    git add .
    npm run commit
    git push origin branch-name
    ```

## 长句高效折行 (Make Prettier)

过长的语句不方便以 Git 方式更新，因为更新长句时很难从 PR 中一眼找出变化，所以需要将长句折行。

推荐使用 [prettier](https://prettier.io/)。如果有很长的句子，可以在 col 100 - 120
左右的（中英、标点、数字之间）折行。也可以尝试运行以下命令：

```shell
npx prettier -w filename
```

然后手动修改对应的文件，实现折行。

## PR 和 Issue 筛选

只需修改 URL 就能筛选出不同的内容：

- 查看某个月份 Closed Issue：

    ```
    https://github.com/DaoCloud/DaoCloud-docs/issues?page=1&q=is%3Aclosed+is%3Aissue+closed%3A2024-01
    ```

- 查看某个月份创建的 Issue 并增加搜索：

    ```
    https://github.com/DaoCloud/DaoCloud-docs/issues?q=is%3Aissue+%E6%9C%8D%E5%8A%A1%E7%BD%91%E6%A0%BC+created%3A2024-01+is%3Aopen
    ```

- 查看某个月份 Merged PR：

    ```
    https://github.com/DaoCloud/DaoCloud-docs/pulls?q=is%3Apr+label%3Akpanda+is%3Aclosed+merged%3A%3E%3D2024-01
    ```

!!! tip

    有什么问题，多问问 GPT，会给你很多提示。

## 参考资料

- [Markdown 语法](https://www.markdownguide.org/cheat-sheet/)
- [Git 命令查询表](https://education.github.com/git-cheat-sheet-education.pdf)
- [Issues](https://github.com/DaoCloud/DaoCloud-docs/issues)：目前文档站存在的一些问题
- [Discussions](https://github.com/DaoCloud/DaoCloud-docs/discussions)：
  类似于 Issue 频道，也列出了一些文档站的问题
- [Material for MkDocs 帮助](https://squidfunk.github.io/mkdocs-material/reference/)：
  这是 DCE 5.0 文档站的编译器帮助手册