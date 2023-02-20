---
date: 2022-11-17
hide:
  - toc
---

# 安装组件 insight-agent

请确认您的集群已成功接入`容器管理`平台，然后执行以下步骤安装 insight-agent 来采集数据。

1. 从左侧导航栏进入`容器管理`，进入`集群列表`。

    ![进入集群列表](../../images/login01.png)

1. 点击要安装 insight-agent 的集群名称。

    ![点击集群名称](../../images/login02.png)

1. 在左侧导航栏中选择 `Helm 应用` -> `Helm 模板`，找到 `insight-agent`，点击该磁贴卡片。

    ![找到 insight-agent](../../images/installagent01.png)

1. 选择合适的版本，点击`安装`。

    ![安装](../../images/installagent02.png)

1. 填入名称，选择命名空间和版本后，在 yaml 文件中分别填写 logging、metric、audit、trace 上报数据的地址。

    系统默认已填写数据上报的组件的地址，仍请您检查无误后再点击`确定` 进行安装。
    如需修改数据上报地址，请参考[获取数据上报地址](gethosturl.md)。

    ![填表](../../images/installagent03.png)

1. 系统将自动返回 `Helm 应用`，当应用状态从 `未就绪`变为`已部署` 时，表示 insight-agent 安装成功。

    ![成功](../../images/login03.png)

    !!! note

        - 点击最右侧的 `⋮`，在弹出菜单中可以执行`更新`、`查看 YAML` 和`删除`等更多操作。
        - 有关实际安装演示，请观看[安装 insight-agent 的视频演示](../../../videos/insight.md#_6)
