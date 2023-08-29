# 安全漏洞

本页列出云原生社区近年来出现的一些重大安全漏洞。

- [回顾 2022 Kubernetes 安全漏洞，我们可以从中学到什么](https://www.armosec.io/blog/kubernetes-vulnerabilities-2022/)

    文章对 2022 年 Kubernetes 的主要安全漏洞和解决方法进行了总结，例如 CRI-O 运行时容器逃逸漏洞、ArgoCD 绕过认证等。
    介绍了一些防止漏洞的措施：实施安全配置文件，分配角色和权限时遵循最小权限原则，对 K8s 清单文件、代码库和集群进行持续扫描，定期更新集群上的软件包，使用容器沙盒项目等。

- [Istio 高风险漏洞：拥有 localhost 访问权限的用户可以冒充任何工作负载的身份](https://github.com/istio/istio/security/advisories/GHSA-6c6p-h79f-g6p4)

    如果用户拥有 Istiod 控制平面的 localhost 访问权，他们可以冒充服务网格内的任何工作负载身份。
    受影响的版本为 1.15.2。目前，已发布补丁版本 [1.15.3](https://github.com/istio/istio/releases/tag/1.15.3)。

- [Istio 高风险漏洞：Golang Regex 库导致 DoS 攻击](https://github.com/istio/istio/security/advisories/GHSA-86vr-4wcv-mm9w)

    Istiod 存在请求处理错误漏洞，攻击者会在 Kubernetes validating 或 mutating webhook 服务曝光时，发送自定义或超大消息，导致控制平面崩溃。
    目前，[Istio](https://github.com/istio/istio/releases) 已发布补丁版本 1.15.2、1.14.5 和 1.13.9。低于 1.14.4、1.13.8 或 1.12.9 的版本会受此影响。

- [CrowdStrike 发现针对 Docker 和Kubernetes 基础设施的新型挖矿攻击](https://www.crowdstrike.com/blog/new-kiss-a-dog-cryptojacking-campaign-targets-docker-and-kubernetes/)

    该攻击通过容器逃逸技术和匿名矿池，使用一个模糊的域名来传递其有效负载，以对 Docker 和 Kubernetes 基础设施开展加密货币挖掘活动。
    采用云安全保护平台能够有效保护云环境免受类似的挖矿活动的影响，防止错误配置和控制平面攻击。

- [Kube-apiserver CVE 漏洞: 聚合 API server 可能导致服务器请求伪造问题（SSRF）](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#cve-2022-3172-aggregated-api-server-can-cause-clients-to-be-redirected-ssrf)

    攻击者可能控制聚合 API Server，将客户端流量重定向到任何 URL。这可能导致客户端执行意外操作，或将客户端证书泄露给第三方。
    此问题没有缓解措施。集群管理员应注意保护聚合 API Server，不允许不受信任方访问 mutate API Services。
    受影响版本：kube-apiserver 1.25.0、1.24.0 - 1.24.4、1.23.0 - 1.23.10、1.22.0 - 1.22.14。已修复版本：1.25.1、1.24.5、1.23.11、1.22.14。

- [Aqua 发现新型非法加密挖矿方式，能够利用容器消耗网络带宽](https://blog.aquasec.com/cryptojacking-cloud-network-bandwidth)

    近日，Aqua Security 发布了一则关于新型挖矿攻击的警报。较传统的挖矿攻击会造成 CPU 消耗的急剧增加，新型攻击利用容器消耗网络带宽，而 CPU 消耗增加并不显著。
    因此，依靠 CPU 利用率来识别攻击的安全工具可能无法发现该威胁。
    Aqua 建议，运行能够静态和动态分析容器的安全工具是最有效的抵御攻击的方式。

- [Istio 漏洞：向 Envoy 发送格式不正确的头信息可能导致未知内存访问](https://istio.io/latest/news/security/istio-security-2022-006/)

    在受影响的版本（1.14.2 和 1.13.6）中，在某些配置中向 Envoy 发送的格式错误头信息可能导致未知行为或崩溃。该漏洞已在 1.12.8、1.13.5 和 1.14.1 版本中得到解决。此外，Istio 官方建议不要在生产环境中安装 1.14.2 或 1.13.6。

- [CRI-O 漏洞：Kube API 访问可能会导致节点上的内存耗尽](https://access.redhat.com/security/cve/cve-2022-1708)

    CRI-O 会读取 ExecSync 请求的输出结果。如果输出的数据量很大，有可能耗尽节点的内存或磁盘空间，对系统可用性造成威胁。目前，该文章尚未给出解决方案。

- [Istio 控制平面存在请求处理漏洞](https://istio.io/latest/news/security/istio-security-2022-004/)

    Istiod 存在请求处理漏洞，发送定制信息或超大信息的攻击者可能会导致控制平面进程崩溃。
    当Kubernetes 验证或变更 webhook 服务公开暴露时，受攻击的风险最大。此漏洞为 0day 漏洞。