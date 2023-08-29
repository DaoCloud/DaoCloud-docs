# Cilium 对于 Pod 访问 Service 的加速

Cilium 在 Pod 的网络命名空间内，提前做了 Service 目的地址的 NAT 解析，而无需流量经过宿主机的 iptables 规则进行解析，因此提升了访问的性能。

![cilium](../../images/cilium-service.png)

在官方的[测试报告](https://cilium.io/blog/2019/08/20/cilium-16/#hostservices)中提到，在 Pod 间基于 HTTP 访问 Service 时，随着 Service 数量的增强，传统的 iptables 解析模式会使得访问延时越来越慢，而使用基于 Cilium 提供的加速方案，应用间的访问延时稳定不变。
