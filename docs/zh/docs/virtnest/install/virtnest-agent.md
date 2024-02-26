# 安装 virtnest-agent

本文将介绍如何在指定集群内安装 virtnest-agent。

## 前提条件

安装 virtnest-agent 之前，需要满足以下前提条件：

- 操作系统内核版本需要在 v3.15 以上。

## 安装步骤

初始集群需要在 Helm 中安装 virtnest-agent 组件后方可使用虚拟机的相关能力。

1. 点击左侧导航栏上的 __容器管理__ ，然后点击 __虚拟机__ ，若未安装 virtnest-agent 组件，则无法正常使用虚拟机能力。将提醒用户在所需集群内进行安装。

    ![安装提示](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/virtnest001.png)

2. 选择所需集群，点击左侧导航栏的 __Helm 应用__ ，然后点击 __Helm 模板__ ，查看模板列表。

    ![helm 模板](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/virtnest002.png)

3. 搜索 __virtnest-agent__ 组件，进入组件详情，选择合适版本，点击 __安装__ 按钮，进行安装。

    ![virtnest-agent 组件](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/virtnest003.png)

    ![详情](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/virtnest004.png)

4. 进入安装表单页面，填写基本信息后，点击 __确定__ ，安装完成。

    ![安装信息](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/virtnest005.png)

5. 重新点击 __虚拟机__ 导航栏，成功出现虚拟机列表，可以正常使用虚拟机能力。

    ![虚拟机列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/virtnest006.png)
