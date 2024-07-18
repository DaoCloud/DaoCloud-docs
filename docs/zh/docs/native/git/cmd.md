# 常用 Git 命令

本页列出一些常用的 Git 命令。

| 类型    | 命令描述                            | Git 命令                                               |
| ------ | ---------------------------------- | ------------------------------------------------------ |
| 创建    | 创建一个分支                         | git checkout -b branch-name                            |
|        | 切换到某个分支                        | git checkout branch2                                   |
| 查看    | 列出本地所有分支                      | git branch                                             |
|        | 查看分支的状态                        | git status                                             |
|        | 查看 git 提交记录                     | git log                                                |
|        | 查看本地运行过的命令                   | history                                                |
| 提交    | 提交某个文件到缓存区                   | git add /docs/en/test.md                               |
|        | 提交当前所有修改到缓存区                | git add .                                              |
|        | 提交本地修改                         | git commit -m "change a text for chapter 1"             |
|        | 首次推送到 GitHub 仓库                | git push origin branch-name                             |
|        | 修改后再次推送到 GitHub 仓库           | git push origin branch-name -f                          |
| 删除    | 删除一个分支                         | git branch -D branchName                                 |
|        | 删除当前分支外的所有分支               | git branch &#124; xargs git branch -d                     |
|        | 删除分支名包含指定 'dev' 的分支        | git branch &#124; grep 'dev\*' &#124; xargs git branch -d |
| Rebase | 将当前分支与 main 保持同步             | git rebase main                                           |
|        | 对最近的 3 个提交进行 rebase 或 squash | git rebase -i HEAD~3                                      |

更多 Git 命令，请查阅 [Git 命令查询表](https://education.github.com/git-cheat-sheet-education.pdf)。
