---
hide:
  - toc
---

# 创建多分支流水线

应用工作台流水线支持基于代码仓库创建多分支流水线。

## 前提条件

- [创建工作空间](https://docs.daocloud.io/ghippo/user-guide/workspace/workspace/)、[创建用户](https://docs.daocloud.io/ghippo/user-guide/access-control/user/)。
- 将该用户添加至该工作空间，并赋予 **workspace editor** 或更高权限。
- 提供一个代码仓库，并且代码仓库的源码有多个分支，并且均有 Jenkinsfile 文本文件。
- 如果是私有仓库，需要事先[创建仓库访问凭证](https://docs.daocloud.io/amamba/user-guide/pipeline/credential/)。

## 操作步骤

1. 在流水线列表页点击**创建流水线**。

2. 选择**创建多分支流水线**，点击**确定**。

    ![mutilpipeline01](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/mutilpipeline01.png)

3. 参考下方说明填写基本信息和代码仓库信息。

    - 名称：流水线的名称。同一个工作空间下流水线名称必须唯一。
    - 描述信息：用户描述当前流水线的作用。
    - 代码仓库地址：填写远程代码仓库的地址。
    - 凭证：对于私有仓库，需要提前[创建仓库访问凭证](https://docs.daocloud.io/amamba/user-guide/pipeline/credential/)并在此处选择该凭证。
    - 脚本路径：Jenkinsfile 文件在代码仓库中的绝对路径。

    ![mutilpipeline02](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/mutilpipeline02.png)

4. 参考下方说明填写分支发现策略、扫描触发器、分支设置、克隆配置信息。

    - 开启发现分支：默认值为 **.*** ，通过正则表达式来过滤分支。
    - 开启多分支扫描：开启后，一旦代码仓库有分支变动，会进行同步。
    - 扫描间隔：根据预设的间隔来进行扫描代码仓库，来检查是否又更新。
    - 删除旧分支：开启后将根据策略删除旧分支及流水线
    - 保留天数：旧分支及旧分支的流水线保留的天数，到期后删除。
    - 保留数量：旧分支及旧分支的流水线保留的数量。
    - 浅克隆：开启后，拉取代码仓库的最新版本。支持设置克隆深度，一般默认为1用于加速拉取。
    - 克隆超时：拉取代码时的最长等待时间。

        ![mutilpipeline03](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/mutilpipeline03.png)

5. 完成创建。确认所有参数输入完成后，点击**确定**按钮，完成多分枝流水线创建，自动返回流水线列表。

    ![mutilpipeline04](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/mutilpipeline04.png)

6. 创建完成后，会自动触发执行符合条件的分支的对应的流水线。

    ![mutilpipeline05](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/mutilpipeline05.png)

## 其他操作

### 扫描仓库

**扫描仓库**的目的是通过手动的方式触发发现代码仓库的新分支。

![mutilpipeline06](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/mutilpipeline06.png)

### 查看扫描日志

展示最新一次扫描代码仓库时发现分支的日志。

![mutilpipeline07](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/mutilpipeline07.png)

### 查看分支

根据分支发现策略获取的分支信息，其中**禁用** 状态的分支代表，最新扫描结果中不符合分支发现的策略。

![mutilpipeline08](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/mutilpipeline08.png)
