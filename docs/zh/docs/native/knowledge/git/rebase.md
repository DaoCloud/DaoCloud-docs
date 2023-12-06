# Git 常见问题

本地完成编辑 push 到 GitLab 后，会触发 pipeline 流水线，请确保 pipeline 成功后再合并 pr。

如果先前有 PR 无法合并，或无需合并，请先 close 掉。

对于 GitLab 的 pull、commit、push、rebase、squash 等操作，可以选用一些 Git 图形化工具。

## Rebase 问题

如果提交 PR 时提示需要 rebase，可以尝试以下方案。

### 方案 1

其他命令与 [GitLab 文档站上传流程](index.md)第 3 步相同，在第二次 commit 时运行以下命令：

```bash
git commit --amend --no-edit 
```

> 因为类似 kpanda 提倡 1 个 commit 对应 1 个 PR，这条命令将把修改追加到上一个 commit。

然后运行 `git push origin docsite -f` 强制推送到远程仓库。

### 方案 2

提交 PR 后提示 rebase，先按顺序运行以下命令：

```bash
git checkout main
git pull -r
git checkout yourbranch
git rebase main
```

屏幕上会提示有冲突的文件，手动解决所列文件内的所有冲突后，运行以下命令：

```shell
git add .
git rebase --continue
git push origin yourbranch -f
```

### 方案 3

这是 GitHub 官方的解决步骤，参见[合并和重设基线](https://deploy-preview-33648--kubernetes-io-main-staging.netlify.app/zh/docs/contribute/new-content/open-a-pr/#squashing-commits)：

1. 更新 fork 副本，重设本地分支的基线：

    ```bash
    git fetch origin
    git rebase origin/<your-branch-name>
    ```

2. 强制推送到你 fork 的副本仓库：

    ```bash
    git push --force-with-lease origin <your-branch-name>
    ```

### 方案 4

git rebase 之后把不相干的 commit 全部注释掉。

## Squash commits

很多项目要求每个 PR 只能包含 1 个 commit。但如果有很多次 git commit，可以按照以下步骤把多个 commit 压缩为一个。

1. 查看最近的 commit 日志。

    ```bash
    git log
    ```

    查看完后，按字母 `q` 退出。

2. 发起变基。

    ```bash
    git rebase -i HEAD~3
    ```
    
    `HEAD~3` 表示从头部开始追溯 3 条记录
    
3. 开始编辑文件。
    
    修改前：
    
    ```bash
    pick d875112ca Original commit
    pick 4fa167b80 Address feedback 1
    pick 7d54e15ee Address feedback 2
    ```
    
    修改后：
    
    ```bash
    pick d875112ca Original commit
    squash 4fa167b80 Address feedback 1
    squash 7d54e15ee Address feedback 2
    ```
    
    不能全部 squash，至少保留一个 pick。
    
4. 保存退出，重新 push 到所在分支。

## OpenSSL SSL_read 错误

如果运行 `git push origin xxx` 后提示以下错误：

```text
fatal: unable to access 'https://github.com/windsonsea/website-1.git/': OpenSSL SSL_read: Connection was reset, errno 10054
```

可以尝试运行以下命令，取消 SSL 验证：

```git
git config --global http.sslVerify "false"
```

> 如果还提示这个错误，可以切换一个 VPN 的入口。

然后重新运行 `git push origin xxx`，必要时可增加 `-f` 标记来强制推送。

## port 443 超时问题

有时候 git push 后，会提示超时错误：

```bash
Failed to connect to github.com port 443 after 21043 ms: Timed out
```

经查验，是代理的问题。运行以下 2 条命令取消全局代理，可以解决这个 error：

```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

> - 如果反复出现 errno 10054 和 timeout 问题，需要[设置代理](proxy.md)。
> - 实际操作中，可能还会遇到各种问题，所以关键还是要熟悉[常用 git 命令](http://www.360doc.com/content/22/0307/11/26794451_1020445861.shtml)，勤于笔记。

## 提交第二个 PR

正常每人只能提交一个 PR，想要同时提交第二个或更多 PR，需要依次执行以下操作：

```bash
git checkout main
git checkout -b branch1
git checkout main
git checkout -b branch2
```

> 每次切换 Branch 必须先切换回 main，不要直接从 branch1 切换到 branch2

## Spiderpool 检查机制

对于 spiderpool 和网络组的 PR，提交之前先本地运行以下 2 条命令检查语法：

```bash
make lint-markdown-format
make lint-markdown-spell-colour
```

对于 markdownlint 的错误，按提示逐条修改。

对于单词 spell 错误，按提示修改。如果你认为拼写无误，请将提示的单词添加到：

```bash
.github/.spelling
```
