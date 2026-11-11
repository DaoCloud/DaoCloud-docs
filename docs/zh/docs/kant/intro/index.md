---
hide:
  - toc
---

# 什么是云边协同

物联网接入节点呈爆发式增长，集中式云计算已难以满足海量数据的实时传输与处理需求；云边协同（Kant）将云原生能力延伸至边缘，采用「端-边-云」一体化协同架构，把数据处理、业务应用与 AI 模型下沉到边缘执行。云端统一管理边缘节点、应用与设备，边缘侧在弱网 / 离线环境下仍可自治运行，设备侧支持多协议终端接入，从而解决响应实时性、数据隐私性与维护便利性问题，广泛适用于工业互联网、智慧工厂、智慧园区、智慧零售等场景。

## 产品架构

![云边协同产品架构](../images/kant-arch.svg)

架构自上而下分为云、边、端三层：

| 层面 | 组件 | 职责 | 图中标识 |
| --- | --- | --- | --- |
| **云** | 管理平面 | 统一纳管边缘节点、下发应用与模型、管理设备孪生、配置消息端点与路由 | 蓝色区域 |
| **云** | Kubernetes 集群 / 操作系统 | 承载云端控制面，向边缘下发应用、配置与模型，接收数据与状态上报 | 蓝色横条、橙色虚线 |
| **边** | 应用 / 模型、边缘控制 | 运行容器化应用与模型，提供资源控制、边缘运维、设备数据采集与协议转换、数据通道 | 绿色区域 |
| **边** | 容器引擎、操作系统、基础设施 | 基于 x86、ARM 与网络、计算、存储资源，在弱网或离线时保持业务连续 | 绿色底座 |
| **端** | 多协议终端与智能物联设备 | 通过 Modbus 等协议及 DMI 标准接口接入边缘节点，就近采集并上报数据 | 橙色区域、灰色箭头 |

## 核心能力

云边协同围绕边缘节点、应用模型、终端设备与数据协同提供完整能力：

<div class="grid cards" markdown>

-   :material-server-network:{ .lg .middle } __边缘节点管理__

    ---

    支持海量边缘节点接入，提供 Token 与证书两种纳管方式，可在云端统一管理、监控和运维节点及节点组。

    [:arrow_forward: 边缘节点概述](../user-guide/node/index.md)

-   :material-cube-outline:{ .lg .middle } __边缘应用与模型__

    ---

    将应用或模型打包为容器镜像，快速部署到边缘节点运行，支持查看运行数据、事件与日志，以及 CPU / GPU 调度。

    [:arrow_forward: 边缘应用概述](../user-guide/edge-app/index.md)

-   :material-developer-board:{ .lg .middle } __终端设备接入__

    ---

    支持 Modbus 等多种协议终端接入，通过 DMI 标准接口对接设备能力，接入后可在云端统一管理设备与设备孪生。

    [:arrow_forward: 终端设备概述](../user-guide/device/index.md)

-   :material-transit-connection-variant:{ .lg .middle } __边云消息路由__

    ---

    配置消息路由规则，将边缘消息按路径转发至 rest、eventbus、servicebus 等端点；支持图片、视频等非结构化数据云边双向传输。

    [:arrow_forward: 边云消息概述](../user-guide/route/index.md)

-   :material-lan:{ .lg .middle } __应用网格__

    ---

    通过服务发现与流量代理实现边缘业务流量闭环，解决边缘场景下边缘业务之间的通信问题。

    [:arrow_forward: 应用网格概述](../user-guide/edge-network/index.md)

-   :material-shield-check-outline:{ .lg .middle } __边缘自治与安全__

    ---

    弱网 / 无网环境下边缘节点仍具备自我管理能力；提供平台、文件夹、工作空间多级权限、云边双向 TLS 加密与审计日志。

    [:arrow_forward: 产品优势](benefits.md)

</div>

## 学习路径

按下面的顺序依次完成，即可从创建边缘单元到打通云边数据通道：

<style>
.kant-path{display:flex;gap:0.75rem;margin:1.25rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.kant-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.kant-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.kant-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.kant-path-step:last-child::after{display:none}
.kant-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.kant-path-title{font-weight:700;font-size:0.95rem}
.kant-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.kant-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.kant-path-step{flex:1 1 100%}.kant-path-step::after{display:none}}
</style>

<div class="kant-path">
  <a class="kant-path-step" style="--path-c:#2196f3" href="../user-guide/edge-unit/create-internal-unit/">
    <span class="kant-path-num">1</span>
    <span class="kant-path-title">创建边缘单元</span>
    <span class="kant-path-desc">创建专有边缘单元，为边缘业务准备运行环境</span>
    <span class="kant-path-go">前往 →</span>
  </a>
  <a class="kant-path-step" style="--path-c:#00acc1" href="../user-guide/node/access-guide/">
    <span class="kant-path-num">2</span>
    <span class="kant-path-title">接入边缘节点</span>
    <span class="kant-path-desc">用 Token 或证书把边缘节点纳管到云端</span>
    <span class="kant-path-go">前往 →</span>
  </a>
  <a class="kant-path-step" style="--path-c:#43a047" href="../user-guide/edge-app/create-app/">
    <span class="kant-path-num">3</span>
    <span class="kant-path-title">创建工作负载</span>
    <span class="kant-path-desc">将应用或模型部署到边缘节点运行</span>
    <span class="kant-path-go">前往 →</span>
  </a>
  <a class="kant-path-step" style="--path-c:#fb8c00" href="../user-guide/device/create-device-model/">
    <span class="kant-path-num">4</span>
    <span class="kant-path-title">接入终端与数据</span>
    <span class="kant-path-desc">创建设备模型与设备实例，再配置云边消息路由</span>
    <span class="kant-path-go">前往 →</span>
  </a>
</div>

[下载中心](https://docs.daocloud.io/download/){ .md-button }
[了解 Token 工厂效能平台](https://docs.daocloud.io/tf/){ .md-button }
[了解 d.run AI 操作系统](https://docs.daocloud.io/drun/){ .md-button }
[查阅《云边协同用户手册》PDF](https://harbor-test2.cn-sh2.ufileos.com/docs/download/docs/kant.pdf){ .md-button }
