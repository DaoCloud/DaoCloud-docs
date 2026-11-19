# 安装简介

DCE 分为社区版和商业版。

- 社区版包括容器管理、全局管理、可观测性三大模块，可永久免费使用。[DCE 社区版安装手册 PDF](https://harbor-test2.cn-sh2.ufileos.com/docs/download/docs/dce5-community.pdf){ .md-button }
- 商业版在社区版的基础上可按需增加服务网格、微服务引擎、多云编排、数据服务中间件、镜像仓库、云边协同、容器化虚拟机等模块，
  功能更全面，更能适应各类生产环境需求。[DCE 商业版安装手册 PDF](https://harbor-test2.cn-sh2.ufileos.com/docs/download/docs/dce5.0-install.pdf){ .md-button }

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
          <li><a href="../ghippo/intro/">全局管理</a></li>
          <li><a href="../kpanda/intro/">容器管理</a></li>
          <li><a href="../insight/intro/">可观测性</a></li>
        </ul>
      </td>
      <td>
        <a href="../dce/license0/">永久免费授权</a>，3 个模块会保持持续更新，可随时
        <a href="https://docs.daocloud.io/download/#_3">下载子模块的离线包</a>
      </td>
    </tr>
    <tr>
      <td>商业版</td>
      <td><p>社区版上增加：</p>
        <ul>
          <li><a href="../amamba/intro/"><span style="white-space: nowrap;">应用工作台</span></a></li>
          <li><a href="../kairship/intro/">多云编排</a></li>
          <li><a href="../skoala/intro/"><span style="white-space: nowrap;">微服务引擎</span></a></li>
          <li><a href="../mspider/intro/">服务网格</a></li>
          <li><a href="../middleware/"><span style="white-space: nowrap;">精选中间件</span></a></li>
          <li><a href="../kangaroo/intro/">镜像仓库</a></li>
          <li><a href="../kant/intro/">云边协同</a></li>
          <li><a href="../virtnest/intro/">虚拟机</a></li>
          <li><a href="../topohub/intro/">设备管理</a></li>
          <li><a href="../network/intro/">云原生网络</a></li>
          <li><a href="../storage/hwameistor/intro/">云原生存储</a></li>
        </ul>
      </td>
      <td>
        联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898，各个模块可按需自由组合，
        可随时<a href="https://docs.daocloud.io/download/#_3">下载子模块的离线包</a>
      </td>
    </tr>
  </tbody>
</table>

## 社区版安装流程

DCE 社区版的安装流程如下图：

```mermaid
flowchart TB

subgraph second[使用说明]
    direction TB
    free[申请免费体验] --- kpanda[容器管理]
    kpanda --- ghippo[全局管理]
    ghippo --- insight[可观测性]
    insight -.- ask[提问!!!]
end

subgraph first[安装社区版]
    direction TB
    plan[资源规划] --> k8s[准备 K8s 集群]
    k8s --> tools[安装依赖项]
    tools -.-> kind[通过 kind 集群<br>在线安装]
    tools -.-> s1[通过标准 k8s 集群<br>在线安装]
    tools -.-> s2[通过标准 k8s 集群<br>离线安装]
end

start([fa:fa-user DCE 社区版<br>安装和使用流程]) --> first
start --> second


click plan "community/resources/"
click k8s "community/kind/online/#kind"
click tools "install-tools/"
click kind "community/kind/online/"
click s1 "community/k8s/online/"
click s2 "community/k8s/offline/"
click kpanda "../kpanda/intro/"
click ghippo "../ghippo/intro/"
click insight "../insight/intro/"
click free "../dce/license0/"
click ask "#_4"
```

## 商业版安装流程

DCE 商业版的安装流程如下图：

```mermaid
flowchart TB

    start([fa:fa-user DCE 商业版<br>安装流程]) -.- arch[了解部署架构]
    arch --> deploy[查阅部署要求]
    deploy --> prepare[准备工作]
    prepare --> download[下载离线包]
    download --> config[编辑<br>clusterConfig.yaml]
    
    config -.-> other-k8s[安装到<br>不同 K8s]
    config -.-> install[正常开始安装]
    config -.-> other-os[安装到<br>不同 Linux]

    other-k8s -.-> ocp[安装到<br>OpenShift OCP]
    other-k8s -.-> ali[安装到<br>阿里云 ECS]

    other-os -.-> uos[安装到<br>UOS]
    other-os -.-> oracle[安装到<br>Oracle Linux]
    other-os -.-> tencent[安装到<br>TencentOS Server]
    other-os -.-> other[安装到<br>更多 Linux]

click arch "commercial/deploy-arch/"
click deploy "commercial/deploy-requirements/"
click prepare "commercial/prepare/"
click download "commercial/start-install/#1"
click config "commercial/start-install/#2-clusterconfigyaml"
click install "commercial/start-install/#3"
click ocp "k8s-install/ocp-install-dce5.0/"
click ali "k8s-install/ecs-install-dce5.0/"
click uos "os-install/uos-v20-install-dce5.0/"
click oracle "os-install/oracleLinux-install-dce5.0/"
click tencent "os-install/TencentOS-install-dce5.0/"
click other "os-install/otherlinux/"
```

## 联系我们

DCE 的安装流程可能会有变更。请收藏此页，关注更新动态，更多操作文档也在制作之中。

- 若有任何安装或使用问题，请[提出反馈](https://github.com/DaoCloud/DaoCloud-docs/issues)。
- 欢迎扫描二维码，与开发者畅快交流：

    ![社区版交流群](https://docs.daocloud.io/daocloud-docs-images/docs/images/assist.png)

[下载中心](https://docs.daocloud.io/download/){ .md-button }
[了解 Token 工厂效能平台](https://docs.daocloud.io/tf/){ .md-button }
[了解 d.run AI 操作系统](https://docs.daocloud.io/drun/){ .md-button }
