# 安装

1. 登录集群，点击侧边栏「Helm 应用」→「Helm 模版」，在右侧上方搜索框输入「knative」，然后按回车键搜索。

    ![Install-1](../../../images/knative-install-1.png)

2. 点击搜索出的 knative-operator，进入安装配置界面。你可以在该界面查看可用版本以及 Helm values 的 Parameters 可选项。

    ![Install-2](../../../images/knative-install-2.png)

3. 点击安装按钮后，进入安装配置界面。

    ![Install-3](../../../images/knative-install-3.png)

4. 输入名称，安装租户，建议勾选「就绪等待」和「详细日志」。

5. 在下方设置，可以勾选 Serving，并输入 Knative Serving 组件的安装租户，会在安装后部署 Knative Serving 组件，该组件由 Knative Operator 管理。

