# 集成 DeepFlow

DeepFlow 是一款基于 eBPF 的可观测性产品。它的社区版已经被集成进 Insight 中，以下是集成方式。

## 前提条件

- 全局服务集群已经安装 Insight
- Insight 最低版本要求为 v0.23.0
- [DeepFlow 运行权限及内核要求](https://deepflow.io/docs/zh/ce-install/overview/#%E8%BF%90%E8%A1%8C%E6%9D%83%E9%99%90%E5%8F%8A%E5%86%85%E6%A0%B8%E8%A6%81%E6%B1%82)
- 存储卷就绪

## 安装 DeepFlow

安装 DeepFlow 组件需要用到两个 chart `deepflow`,`deepflow-agent`：

- `deepflow`: 包含 `deepflow-app`,`deepflow-server`,`deepflow-clickhouse`，`deepflow-agent` 等组件。一般`deepflow` 会部署在
- 全局服务集群中，所以它也一并安装了 `deepflow-agent`
- `deepflow-agent`： 只包含了 `deepflow-agent` 组件，用于采集 eBPF 数据并发送给 `deepflow-server`

1. 安装 DeepFlow

    它需要安装在全局服务集群中。进入 kpanda-global-cluster 集群，在左侧导航栏内点击
    __Helm 应用__ -> __Helm 模板__ ，仓库选择 __community__ ，搜索框查询 `deepflow`:
    
    ![img.png](./images/deepflow_chart.png)
    
    点击 deepflow 卡片进入详情：
    
    ![img.png](./images/deepflow_chart_readme.png)
    
    点击安装，进入安装界面：
    
    ![img.png](./images/deepflow_chart_config.png)
    
    大部分 values 都有默认值。其中 Clickhouse 和 Mysql 都需要申请存储卷，他们的默认大小都是 __10Gi__ ，可以通过 __persistence__ 
    关键字搜索到相关配置并修改它们。
    
    配置好后就可以点击确定，执行安装了。

2. 修改 insight 配置

    在安装 `deepflow` 后，还需要在 Insight 中开启相关的功能开关。在左侧导航栏内点击 __配置与密钥__ -> __配置项__ ， 搜索框查询
    insight-server-config 并编辑它:
    
    ![img.png](./images/deepflow_integ_insight_cm.png)
    
    在配置中找到 __eBPF Flow feature__ 这个功能开关并将它开启:
    
    ![img.png](./images/deepflow_integ_insight_cm_edit.png)
    
    保存更改，重启 insight-server 后，Insight 主界面就会出现 __网络观测__ :
    
    ![img.png](./images/deepflow_ui.png)

## 安装 DeepFlow Agent

DeepFlow Agent 通过 `deepflow-agent` chart 安装，它被安装在子集群中，用于采集子集群的 eBPF 观测数据并上报到全局服务集群中。类似于安装 `deepflow`，
通过 __Helm 应用__ -> __Helm 模板__ ，仓库选择 __community__ ，搜索框查询 `deepflow-agent`，按流程进入安装界面，在 __参数配置__ 配置部分需要注意：

![img.png](./images/deepflow_agent_chart_config.png)

 __DeepflowServerNodeIPS__ 对应 deepflow server 安装集群的节点地址。配置好后点击确认，完成安装。

## 使用

在正确安装 DeepFlow 后，点击 __网络观测__ 就可以进入 DeepFlow Grafana UI。它内置了大量的 Dashboard 可供查看与帮助分析问题，
点击 __DeepFlow Templates__ ，可以浏览所有可以查看的 Dashboard:

![img.png](./images/deepflow_ui_templates.png)

![img.png](./images/deepflow_ui_template_list.png)
