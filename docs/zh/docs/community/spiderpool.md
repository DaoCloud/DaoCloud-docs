---
hide:
  - toc
---

# Spiderpool

Spiderpool 是一个免费开源的 IPAM 管理软件，已加入 CNCF 全景图。

Spiderpool 专门设计用于 Underlay 底层网络，解决在集群内外通信时的复杂 IP 分配问题，网络管理员可以利用 Spiderpool 划分 ippool（IP 资源池）准确管理集群内外的每个 IP。

目前社区已经有一些 IPAM 插件，比如 whereabout、kube-ipam、static、dhcp、host-local，但是无法解决复杂的 Underlay 网络问题，这就是我们决定开发 Spiderpool IPAM 管理软件的原因。

Spiderpool 适用于任何能够对接第三方 IPAM 的 CNI 插件，尤其适合于一些缺失 IPAM 的 CNI，例如 SRIOV、MacVLAN、IPVLAN、OVS-CNI 等。
而一些 Overlay CNI 自带了 IPAM 组件，对这款 Spiderpool IPAM 管理软件的需求相对较低。

## 如何让传统应用上云后仍通过固定 IP 对外通信？

<div class="responsive-video-container">
<video controls src="https://harbor-test2.cn-sh2.ufileos.com/docs/videos/underlay-ip.mp4" preload="metadata" poster="../images/underlay-ip.png"></video>
</div>

[了解 Spiderpool 社区](https://github.com/spidernet-io){ .md-button }

[查阅 Spiderpool 官网](https://spidernet-io.github.io/spiderpool/){ .md-button }

<p align="center">
<img src="https://landscape.cncf.io/images/left-logo.svg" width="150"/>&nbsp;&nbsp;<img src="https://landscape.cncf.io/images/right-logo.svg" width="200"/>
<br/><br/>
Spiderpool 已入选 <a href="https://landscape.cncf.io/?selected=spiderpool">CNCF 云原生全景图。</a>
</p>
