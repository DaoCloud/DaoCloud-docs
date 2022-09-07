# 安装

Spiderpool 需要 kube-apiserver webhook，所以也需要 TLS（Transparent Layer Security，传输层安全性）证书。

有两种安装方法：一种是通过自签名证书，一种是使用 cert-manager。

## 通过自签名证书进行安装

这种安装方法比较简单，不需要安装任何依赖项。我们提供了一个脚本来生成这个证书。

以下是针对 IPv4 单栈的示例。

```shell
helm repo add spiderpool https://spidernet-io.github.io/spiderpool

git clone https://github.com/spidernet-io/spiderpool.git
cd spiderpool

# 生成证书
tools/cert/generateCert.sh "/tmp/tls"
CA=`cat /tmp/tls/ca.crt  | base64 -w0 | tr -d '\n' `
SERVER_CERT=` cat /tmp/tls/server.crt | base64 -w0 | tr -d '\n' `
SERVER_KEY=` cat /tmp/tls/server.key | base64 -w0 | tr -d '\n' `

# 针对默认的 ipv4 ippool
# CIDR
Ipv4Subnet="172.20.0.0/16"
# 可用的 IP 资源
Ipv4Range="172.20.0.10-172.20.0.200"
Ipv4Gateway="172.20.0.1"

# 部署 spiderpool
helm install spiderpool spiderpool/spiderpool --wait --namespace kube-system \
  --set spiderpoolController.tls.method=provided \
  --set spiderpoolController.tls.provided.tlsCert="${SERVER_CERT}" \
  --set spiderpoolController.tls.provided.tlsKey="${SERVER_KEY}" \
  --set spiderpoolController.tls.provided.tlsCa="${CA}" \
  --set feature.enableIPv4=true --set feature.enableIPv6=false \
  --set clusterDefaultPool.installIPv4IPPool=true  \
  --set clusterDefaultPool.ipv4Subnet=${Ipv4Subnet} \
  --set clusterDefaultPool.ipv4IPRanges={${Ipv4Range}} \
  --set clusterDefaultPool.ipv4Gateway=${Ipv4Gateway}
```

以下是一个同时支持 IPv4 和 IPv6 双栈的示例。

```shell
helm repo add spiderpool https://spidernet-io.github.io/spiderpool

# 生成证书
tools/cert/generateCert.sh "/tmp/tls"
CA=`cat /tmp/tls/ca.crt  | base64 -w0 | tr -d '\n' `
SERVER_CERT=` cat /tmp/tls/server.crt | base64 -w0 | tr -d '\n' `
SERVER_KEY=` cat /tmp/tls/server.key | base64 -w0 | tr -d '\n' `

# 针对默认的 ipv4 ippool
# CIDR
Ipv4Subnet="172.20.0.0/16"
# 可用的 IP 资源
Ipv4Range="172.20.0.10-172.20.0.200"
Ipv4Gateway="172.20.0.1"

# 针对默认的 ipv6 ippool
# CIDR
Ipv6Subnet="fd00::/112"
# 可用的 IP 资源
Ipv6Range="fd00::10-fd00::200"
Ipv6Gateway="fd00::1"

# 部署 spiderpool
helm install spiderpool spiderpool/spiderpool --wait --namespace kube-system \
  --set spiderpoolController.tls.method=provided \
  --set spiderpoolController.tls.provided.tlsCert="${SERVER_CERT}" \
  --set spiderpoolController.tls.provided.tlsKey="${SERVER_KEY}" \
  --set spiderpoolController.tls.provided.tlsCa="${CA}" \
  --set feature.enableIPv4=true --set feature.enableIPv6=true \
  --set clusterDefaultPool.installIPv4IPPool=true  \
  --set clusterDefaultPool.installIPv6IPPool=true  \
  --set clusterDefaultPool.ipv4Subnet=${Ipv4Subnet} \
  --set clusterDefaultPool.ipv4IPRanges={${Ipv4Range}} \
  --set clusterDefaultPool.ipv4Gateway=${Ipv4Gateway} \
  --set clusterDefaultPool.ipv6Subnet=${Ipv6Subnet} \
  --set clusterDefaultPool.ipv6IPRanges={${Ipv6Range}} \
  --set clusterDefaultPool.ipv6Gateway=${Ipv6Gateway}
```

> 注意：spiderpool-controller Pod 以 hostNetwork 模式运行，它需要占用 host 端口，所以使用 `podAntiAffinity` 来设置亲和性，
> 这可以确保某个节点仅运行一个 spiderpool-controller Pod。因此如果你将 spiderpool-controller 的副本数设置为大于 2，则需要先确保有足够的节点。

## 通过 cert-manager 进行安装

这种安装方法不通用，因为 cert-manager 需要 CNI 创建一个 Pod，但作为 IPAM，Spiderpool 还未安装提供 IP 资源。这意味着 cert-manager 和 Spiderpool 需要先自己独立走完安装步骤。

这种安装方式适用于以下场景：

- 通过自签名证书安装 Spiderpool 之后，且已部署 cert-manager，采用这种安装方式来变更 cert-manager 方案。

- 在带有 [Multus CNI](https://github.com/k8snetworkplumbingwg/multus-cni) 的集群上，通过其他 CNI 部署 cert-manager Pod，然后通过 cert-manager 可以部署 Spiderpool。

部署示例如下：

```shell
helm repo add spiderpool https://spidernet-io.github.io/spiderpool

# 针对默认的 ipv4 ippool
# CIDR
ipv4_subnet="172.20.0.0/16"
# 可用的 IP 资源
ipv4_range="172.20.0.10-172.20.0.200"
Ipv4Gateway="172.20.0.1"

helm install spiderpool spiderpool/spiderpool --wait --namespace kube-system \
  --set spiderpoolController.tls.method=certmanager \
  --set spiderpoolController.tls.certmanager.issuerName=${CERT_MANAGER_ISSUER_NAME} \
  --set feature.enableIPv4=true --set feature.enableIPv6=false \
  --set clusterDefaultPool.installIPv4IPPool=true --set clusterDefaultPool.installIPv6IPPool=false \
  --set clusterDefaultPool.ipv4Subnet=${ipv4_subnet} \
  --set clusterDefaultPool.ipv4IPRanges={${ipv4_ip_range}} \
  --set clusterDefaultPool.ipv4Gateway=${Ipv4Gateway}
```
