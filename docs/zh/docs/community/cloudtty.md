# CloudTTY：一款专用于 Kubernetes 的 Cloud Shell Operator

CloudTTY 是专为 Kubernetes 云原生环境打造的 Web 终端和 Cloud Shell Operator。
通过 CloudTTY，您可以轻松用浏览器打开一个终端窗口，操控多云资源。

CloudTTY 意指云原生虚拟控制台，也称为 Cloud Shell（云壳）。
想象一下，在复杂多变的多云环境中，嵌入这样一层 Shell 来操纵整个云资源。
而这就是 CloudTTY 的设计初衷，我们希望在日趋复杂的 Kubernetes 容器云环境中，能够为开发者提供一个简单的 Shell 入口。

!!! info "TTY 的由来"

    TTY 全称为 TeleTYpe，即电传打字机、电报机。
    没错，就是那种很古老会发出滴滴答答声响、用线缆相连的有线电报机，那是一种只负责显示和打字的纯 IO 设备。
    近些年随着虚拟化技术的飞速发展，TTY 常指虚拟控制台或虚拟终端。

## 为什么需要 CloudTTY?

目前，社区的 [ttyd](https://github.com/tsl0922/ttyd) 等项目对 TTY 技术的探索已经达到了一定的深度，可以提供浏览器之上的终端能力。

但是在 Kubernetes 的场景下，这些 TTY 项目还需要更加云原生的能力拓展。
如何让 ttyd 在容器内运行，如何通过 NodePort\Ingress 等方式访问，如何用 CRD 的方式创建多个实例？

CloudTTY 提供了这些问题的解决方案，欢迎试用 CloudTTY 🎉！
CloudTTY 已入选 CNCF 全景图：

![landscape](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/community/images/cloudtty.png)

## 适用场景

CloudTTY 适用于以下几个场景。

1. 如果企业正使用容器云平台来管理 Kubernetes，但由于安全原因，无法随意 SSH 到主机上执行 kubectl 命令，这就需要一种 Cloud Shell 能力。

2. 在浏览器网页上进入运行中的容器(`kubectl exec`)的场景。

3. 在浏览器网页上能够滚动展示容器日志的场景。

CloudTTY 的网页终端使用效果如下：

![screenshot_gif](https://github.com/cloudtty/cloudtty/raw/main/docs/snapshot.gif)

如果将 CloudTTY 集成到您自己的 UI 里面，最终效果 demo 如下:

![demo_png](https://github.com/cloudtty/cloudtty/raw/main/docs/demo.png)

[了解 CloudTTY 社区](https://github.com/cloudtty/cloudtty){ .md-button }

![cncf logo](./images/cncf.png)

<p align="center">
CloudTTY 已入选 <a href="https://landscape.cncf.io/?selected=cloud-tty">CNCF 云原生全景图。</a>
</p>
