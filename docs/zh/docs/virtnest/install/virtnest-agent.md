# 安装 virtnest-agent

本文将介绍如何在指定集群内安装 virtnest-agent。

## 前提条件

安装 virtnest-agent 之前，需要满足以下前提条件：

- 操作系统内核版本需要在 3.15 以上。

## 安装步骤

初始集群需要在 helm 中安装 virtnest-agent 组件后方可使用虚拟机的相关能力。

1. 点击左侧导航栏上的`容器管理`，然后点击`虚拟机`，若未安装 virtnest-agent 组件，则无法正常使用虚拟机能力。将提醒用户在所需集群内进行安装。

    ![安装提示](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/virtnest001.png)

2. 选择所需集群，点击左侧导航栏的 `Helm 应用`，然后点击 `Helm 模板`，查看模板列表。

    ![helm模板](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/virtnest002.png)

3. 搜索 `virtnest-agent` 组件，进入组件详情，选择合适版本，点击`安装`按钮，进行安装。

    ![virtnest-agent 组件](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/virtnest003.png)

    ![详情](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/virtnest004.png)

4. 进入安装表单页面，填写基本信息后，点击`确定`，安装完成。

    ![安装信息](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/virtnest005.png)

5. 重新点击`虚拟机`导航栏，成功出现虚拟机列表，可以正常使用虚拟机能力。

    ![虚拟机列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/virtnest006.png)
