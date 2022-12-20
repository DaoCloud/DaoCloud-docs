---
hide:
  - toc
---

# 安装简介

DCE 5.0 有两个版本：社区版和商业版。

| 版本   | 包含的模块                                                   | 描述                                               |
| ------ | ------------------------------------------------------------ | -------------------------------------------------- |
| 社区版 | [全局管理](../ghippo/01ProductBrief/WhatisGhippo.md)<br />[容器管理](../kpanda/03ProductBrief/WhatisKPanda.md)<br />[可观测性](../insight/03ProductBrief/WhatisInsight.md)                         | [永久免费授权](../dce/license0.md)，3 个模块会保持持续更新，可随时[下载子模块的离线包](../download/dce5.md) |
| 商业版 | [全局管理](../ghippo/01ProductBrief/WhatisGhippo.md)<br />[容器管理](../kpanda/03ProductBrief/WhatisKPanda.md)<br />[可观测性](../insight/03ProductBrief/WhatisInsight.md)<br />[应用工作台](../amamba/01ProductBrief/WhatisAmamba.md)<br />[多云编排](../kairship/01product/whatiskairship.md)<br />[微服务引擎](../skoala/intro/features.md)<br />[服务网格](../mspider/01Intro/WhatismSpider.md)<br />[精选中间件](../middleware/midware.md)<br />[云原生网络](../network/intro/what-is-net.md)<br />[云原生存储](../hwameistor/intro/what.md)<br />[镜像仓库](../kangaroo/intro.md) | [正版授权](https://qingflow.com/f/e3291647)，各个模块可按需自由组合，可随时[下载子模块的离线包](../download/dce5.md)   |

## 社区版安装流程

DCE 5.0 社区版的安装流程如下图：

```mermaid
flowchart TB

subgraph second[使用说明]
    direction TB
    U[ ] -.-
    free[申请免费体验] --- kpanda[容器管理]
    kpanda --- ghippo[全局管理]
    ghippo --- insight[可观测性]
    insight -.- ask[提问!!!]
end

subgraph first[安装社区版]
    direction TB
    S[ ] -.-
    plan[资源规划] --> k8s[准备 K8s 集群] 
    k8s --> tools[安装依赖项]
    tools -.-> kind[通过 kind 集群<br>在线安装]
    tools -.-> s1[通过标准 k8s 集群<br>在线安装]
    tools -.-> s2[通过标准 k8s 集群<br>离线安装]
end

start([fa:fa-user DCE 5.0 社区版<br>安装和使用流程]) --> first
start --> second

classDef grey fill:#dddddd,stroke:#ffffff,stroke-width:px,color:#000000, font-size:15px;
classDef white fill:#ffffff,stroke:#000,stroke-width:px,color:#000,font-weight:bold
classDef spacewhite fill:#ffffff,stroke:#fff,stroke-width:0px,color:#000
classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class plan,k8s,tools,kind,s1,s2,kpanda,ghippo,insight,free,ask cluster;
class start plain
class S,U spacewhite

click plan "https://docs.daocloud.io/install/community/resources/"
click k8s "https://docs.daocloud.io/install/community/kind/online/#kind"
click tools "https://docs.daocloud.io/install/install-tools/"
click kind "https://docs.daocloud.io/install/community/kind/online/"
click s1 "https://docs.daocloud.io/install/community/k8s/online/"
click s2 "https://docs.daocloud.io/install/community/k8s/offline/"

click kpanda "https://docs.daocloud.io/kpanda/03ProductBrief/WhatisKPanda/"
click ghippo "https://docs.daocloud.io/ghippo/01ProductBrief/WhatisGhippo/"
click insight "https://docs.daocloud.io/insight/03ProductBrief/WhatisInsight/"
click free "https://docs.daocloud.io/dce/license0/"
click ask "https://docs.daocloud.io/install/intro/#_4"
```

!!! tip

    - 上图中的蓝色文字可点击跳转
    - 可参考[保姆式安装 DCE 5.0](../blogs/dce5-install1209.md)

## 商业版安装流程

DCE 5.0 商业版的安装流程如下图：

```mermaid
flowchart TB

    start([fa:fa-user DCE 5.0 商业版<br>安装流程]) -.- deploy[部署规划]
    deploy --> tools[在火种节点上安装依赖项]
    tools --> download[下载离线包]
    download --> config[编辑并配置<br>clusterConfig.yaml]

    config -.compactClusterMode: false.-> typical[经典模式<br>多数据中心]
    typical --> mng2[自动创建 K8s 管理集群<br>安装 Kubean Operator]
    typical --> gsc2[自动创建<br>K8s 全局服务集群<br>安装 DCE 常规组件]

    config -.compactClusterMode: true.-> simple[简约模式<br>单数据中心]
    simple --> k8s1[自动创建<br>一个 K8s 管理集群]
    simple --> gsc1[自动在此集群<br>安装所有 DCE 组件]

classDef grey fill:#dddddd,stroke:#ffffff,stroke-width:1px,color:#000000, font-size:15px;
classDef white fill:#ffffff,stroke:#000,stroke-width:1px,color:#000,font-weight:bold
classDef spacewhite fill:#ffffff,stroke:#fff,stroke-width:0px,color:#000
classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class deploy,tools,download,config cluster
class typical,k8s,mng2,gsc2,k8s2 k8s
class simple,start plain
class gsc1,k8s1 grey

click deploy "https://docs.daocloud.io/install/commercial/deploy-plan/"
click tools "https://docs.daocloud.io/install/install-tools/"
click download "https://docs.daocloud.io/install/commercial/download-file/"
click config "https://docs.daocloud.io/install/commercial/clusterconfig/"
click typical,simple "https://docs.daocloud.io/install/commercial/start-install/"
```

### 联系我们

DaoCloud Enterprise 5.0 还处于发布初期，安装流程可能会有变更。请收藏此页，关注更新动态，更多操作文档也在制作之中。

- 若有任何安装或使用问题，请[提出反馈](https://github.com/DaoCloud/DaoCloud-docs/issues)。

- 欢迎扫描二维码，与开发者畅快交流：

    ![社区版交流群](../images/assist.png)

[下载 DCE 5.0](../download/dce5.md){ .md-button .md-button--primary }
[申请社区免费体验](../dce/license0.md){ .md-button .md-button--primary }
