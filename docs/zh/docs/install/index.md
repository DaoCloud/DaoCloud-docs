# 安装简介

DCE 5.0 大体分为两个版本：社区版和商业版。

社区版可包括容器管理、全局管理、可观测性三大模块，可永久免费使用。

商业版在社区版的基础上可按需购买服务网格、微服务引擎、多云编排、数据服务中间件、镜像仓库等高级模块，功能更全面，更能适应生产环境需求。

<table>
  <thead>
    <tr>
      <th>版本</th>
      <th>包含的模块</th>
      <th>描述</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>社区版</td>
      <td>
        <ul>
          <li><a href="https://docs.daocloud.io/ghippo/intro/index.html">全局管理</a></li>
          <li><a href="https://docs.daocloud.io/kpanda/intro/index.html">容器管理</a></li>
          <li><a href="https://docs.daocloud.io/insight/intro/index.html">可观测性</a></li>
        </ul>
      </td>
      <td>
        <a href="https://docs.daocloud.io/dce/license0.html">永久免费授权</a>，3 个模块会保持持续更新，可随时
        <a href="https://docs.daocloud.io/download/index.html#_3">下载子模块的离线包</a>
      </td>
    </tr>
    <tr>
      <td>商业版</td>
      <td>
        <ul>
          <li><a href="https://docs.daocloud.io/ghippo/intro/index.html">全局管理</a></li>
          <li><a href="https://docs.daocloud.io/kpanda/intro/index.html">容器管理</a></li>
          <li><a href="https://docs.daocloud.io/insight/intro/index.html">可观测性</a></li>
          <li><a href="https://docs.daocloud.io/amamba/intro/index.html"><span style="white-space: nowrap;">应用工作台</span></a></li>
          <li><a href="https://docs.daocloud.io/kairship/intro/index.html">多云编排</a></li>
          <li><a href="https://docs.daocloud.io/skoala/intro/index.html"><span style="white-space: nowrap;">微服务引擎</span></a></li>
          <li><a href="https://docs.daocloud.io/mspider/intro/index.html">服务网格</a></li>
          <li><a href="https://docs.daocloud.io/middleware/index.html"><span style="white-space: nowrap;">精选中间件</span></a></li>
          <li><a href="https://docs.daocloud.io/kangaroo/intro/index.html">镜像仓库</a></li>
        </ul>
      </td>
      <td>
        联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898，各个模块可按需自由组合，可随时
        <a href="https://docs.daocloud.io/download/index.html#_3">下载子模块的离线包</a>
      </td>
    </tr>
  </tbody>
</table>

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

click kpanda "https://docs.daocloud.io/kpanda/intro/"
click ghippo "https://docs.daocloud.io/ghippo/intro/"
click insight "https://docs.daocloud.io/insight/intro/"
click free "https://docs.daocloud.io/dce/license0/"
click ask "https://docs.daocloud.io/install/intro/#_4"
```

!!! tip

    上图中的蓝色文字可点击跳转

## 商业版安装流程

DCE 5.0 商业版的安装流程如下图：

```mermaid
flowchart TB

    start([fa:fa-user DCE 5.0 商业版<br>安装流程]) -.- arch[部署架构]
    arch --> deploy[部署要求]
    deploy --> prepare[准备工作]
    prepare --> download[下载离线包]
    download --> config[编辑并配置<br>clusterConfig.yaml]
    config --> install[开始安装]

classDef grey fill:#dddddd,stroke:#ffffff,stroke-width:1px,color:#000000, font-size:15px;
classDef white fill:#ffffff,stroke:#000,stroke-width:1px,color:#000,font-weight:bold
classDef spacewhite fill:#ffffff,stroke:#fff,stroke-width:0px,color:#000
classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class arch,deploy,prepare,download,config,install cluster
class start plain

click arch "https://docs.daocloud.io/install/commercial/deploy-arch/"
click deploy "https://docs.daocloud.io/install/commercial/deploy-requirements/"
click prepare "https://docs.daocloud.io/install/commercial/prepare/"
click download "https://docs.daocloud.io/install/commercial/start-install/#1"
click config "https://docs.daocloud.io/install/commercial/start-install/#2"
click install "https://docs.daocloud.io/install/commercial/start-install/#3"
```

## 联系我们

DaoCloud Enterprise 5.0 还处于发布初期，安装流程可能会有变更。请收藏此页，关注更新动态，更多操作文档也在制作之中。

- 若有任何安装或使用问题，请[提出反馈](https://github.com/DaoCloud/DaoCloud-docs/issues)。

- 欢迎扫描二维码，与开发者畅快交流：

    ![社区版交流群](https://docs.daocloud.io/daocloud-docs-images/docs/images/assist.png)

[下载 DCE 5.0](../download/index.md){ .md-button .md-button--primary }
[申请社区免费体验](../dce/license0.md){ .md-button .md-button--primary }
