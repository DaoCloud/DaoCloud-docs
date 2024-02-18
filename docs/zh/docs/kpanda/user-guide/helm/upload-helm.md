# 上传 Helm 模版

本文介绍如何上传 Helm 模版，操作步骤见下文。

1. 引入 Helm 仓库，操作步骤参考：[引入第三方 Helm 仓库](./helm-repo.md)。

2. 上传 Helm chart 到 Helm 仓库。

    **客户端上传**

    !!! note

        此方式适用于 Harbor、ChartMuseum、JFrog 类型仓库。

    操作步骤：

    Step1：登陆一个可以访问到 Helm 仓库的节点，将 Helm 二进制文件上传到节点，并安装 cm-push 插件。

        安装插件流程参考：[安装 cm-push 插件](https://github.com/chartmuseum/helm-push)。

    Step2: 推送 Helm chart 到 helm 仓库，执行如下命令；

        ```shell
        helm cm-push ${charts-dir} ${HELM_REPO_URL} --username ${username} --password ${password}
        ```

        - charts-dir：Helm chart 的目录，这里也可以直接推送打包好的 chart（.tgz 文件）。
        - HELM_REPO_URL：Helm 仓库的 URL。
        - username/password：有推送权限的 Helm 仓库用户名密码。

    **页面上传**

    !!! note

        此方式仅适用于 Harbor 类型仓库。

    Step1: 登陆网页 harbor 仓库，请确保登陆用户有推送权限；

    Step2: 进入到对应项目，选择 Helm Charts tab，点击页面 `上传` 按钮，完成 helm chart 上传；

    ![上传 Helm chart](../../images/upload-helm-01.png)

3. 同步远端仓库数据

如果集群设置未开启 `Helm 仓库自动刷新` 设置，需要进行手动同步操作，步骤如下：

进入 `Helm 应用` -> `Helm 仓库`，点击对应仓库列表右侧操作按钮 `同步仓库`，完成仓库数据同步。

![上传 Helm chart](../../images/upload-helm-02.png)
