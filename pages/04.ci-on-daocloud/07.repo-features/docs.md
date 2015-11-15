---
title: 各个代码托管商的功能支持
taxonomy:
    category:
        - docs
---

<!-- 
这篇不需要修改了
-->

#### 功能矩阵

|remote   |commit_push|pull_request|private_repo|set_commit_status|tag_build|
|---------|-----------|------------|------------|-----------------|---------|
|GitHub   |true       | true       |true        |true             |true     |
|Bitbucket|true       | false      |true        |false            |false    |
|Coding   |true       | false      |true        |false            |true     |
|GitCafe  |true       | false      |true        |false            |true     |
|GitLab   |true       | false      |true        |false            |true     |

##### 说明：

0. true：支持 false：不支持
1. commit_push：push 时自动持续集成。
2. pull_request：创建、更新 pull request 时自动持续集成。不能支持这个主要是因为没有 git 接口获得代码。
3. private_repo：获得私有项目代码。
4. set_commit_status：设置 remote 上 commit 的状态，如 failed， success， error 等，只有 github 支持。
5. tag_build：push 一个 tag 时触发 build image。

#### Coding
由于受到 Coding 系统设置的限制，DaoCloud 保存的用于访问 Coding 的 Token（Deploye Key）会不定期失效，如您遇到无法访问 Coding 代码库的情况，可以尝试重新绑定，这是会重新创建 Token。

#### GitCafe
如您在 GitCafe 以 Fork 的方式建立了新项目，这个项目不会在 DaoCloud 显示，您需要等待 15 分钟左右，这是 GitCafe 系统的一个限制，DaoCloud 无法调整改变。

#### BitBucket
如您在 BitBucket 以 Fork 的方式建立了新项目，这个项目不会在 DaoCloud 显示，您需要等待 15 分钟左右，这是 BitBucket 系统的一个限制，DaoCloud 无法调整改变。


