# 安装

Knative 是一个面向无服务器部署的跨平台解决方案。

## 步骤

1. 登录集群，点击侧边栏 __Helm 应用__ -> __Helm 模板__ ，在右侧上方搜索框输入 __knative__ ，然后按回车键搜索。

    ![Install-1](../../../images/knative-install-1.png)

2. 点击搜索出的 __knative-operator__ ，进入安装配置界面。你可以在该界面查看可用版本以及 Helm values 的 Parameters 可选项。

    ![Install-2](../../../images/knative-install-2.png)

3. 点击安装按钮后，进入安装配置界面。

    ![Install-3](../../../images/knative-install-3.png)

4. 输入名称，安装租户，建议勾选 __就绪等待__ 和 __详细日志__ 。

5. 在下方设置，可以勾选 __Serving__ ，并输入 Knative Serving 组件的安装租户，会在安装后部署 Knative Serving 组件，该组件由 Knative Operator 管理。
