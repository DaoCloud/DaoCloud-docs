# 从 AWS Marketplace 安装 EgressGateway

EgressGateway 提供了一种高性价比、可扩展的出口流量管理解决方案，满足企业对公网原 IP 固定功能的需求，是 NAT Gateway 的理想替代选择，以实现更低成本、更细力度的出口连接控制。

本文介绍了如何从 AWS Marketplace 安装 EgressGateway。

## 前提条件

在开始安装之前，需要满足以下前提条件：

- 订阅 EgressGateway。
- 创建一个 Kubernetes 集群。

## Helm 安装

订阅 EgressGateway 后，使用 Helm Chart 在您的 Kubernetes 集群上安装 EgressGateway。

!!! note

    “username”、“password-stdin” 对应的是您登录 AWS 的用户名和密码。

```shell
export HELM_EXPERIMENTAL_OCI=1
aws ecr get-login-password --region us-east-1 | helm registry login --username AWS --password-stdin 709825985650.dkr.ecr.us-east-1.amazonaws.com
mkdir awsmp-chart && cd awsmp-chart
helm pull oci://709825985650.dkr.ecr.us-east-1.amazonaws.com/daocloud-hong-kong/egressgateway --version 0.6.2
tar xf $(pwd)/* && find $(pwd) -maxdepth 1 -type f -delete
helm install --generate-name --namespace <ENTER_NAMESPACE_HERE> ./*
```

## 开始使用

安装成功后，您可以参考以下操作流程，开始体验。

### 创建网关实例

1. 选择网关节点，给节点设置标签。

    ```shell
    ~ kubectl get nodes -A -owide
    NAME                             STATUS   ROLES    AGE   VERSION               INTERNAL-IP      EXTERNAL-IP                         
    ip-172-16-103-117.ec2.internal   Ready    <none>   25m   v1.30.0-eks-036c24b   172.16.103.117   34.239.162.85  
    ip-172-16-61-234.ec2.internal    Ready    <none>   25m   v1.30.0-eks-036c24b   172.16.61.234    54.147.15.230
    ip-172-16-62-200.ec2.internal    Ready    <none>   25m   v1.30.0-eks-036c24b   172.16.62.200    54.147.16.130  
    ```

    此 demo 中我们选择 `ip-172-16-103-117.ec2.internal` 和 `ip-172-16-62-200.ec2.internal` 作为网关节点。给节点设置 `role: gateway` 标签。

    ```shell
    kubectl label node ip-172-16-103-117.ec2.internal role=gateway
    kubectl label node ip-172-16-62-200.ec2.internal role=gateway
    ```

2. 创建网关实例，通过标签来匹配网关节点。YAML 示例如下：

    ```yaml
    apiVersion: egressgateway.spidernet.io/v1beta1
    kind: EgressGateway
    metadata:
    name: "egressgateway"
    spec:
    nodeSelector:
        selector:
        matchLabels:
            role: gateway
    ```

### 创建测试 Pod

在完成网关实例创建后，您可以部署一个 Pod 来验证测试。此 demo 中我们选择 `ip-172-16-61-234.ec2.internal ` 节点运行 Pod，YAML 示例如下。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mock-app
  labels:
    app: mock-app
spec:
  nodeName: ip-172-16-61-234.ec2.internal
  containers:
  - name: nginx
    image: nginx
```

查看确保 Pods 处于 Running 状态。

```shell
~ kubectl get pods -o wide
NAME                                        READY   STATUS    RESTARTS   AGE   IP               NODE                             NOMINATED NODE   READINESS GATES
egressgateway-agent-zw426                   1/1     Running   0          15m   172.16.103.117   ip-172-16-103-117.ec2.internal   <none>           <none>
egressgateway-agent-zw728                   1/1     Running   0          15m   172.16.61.234    ip-172-16-61-234.ec2.internal    <none>           <none>
egressgateway-controller-6cc84c6985-9gbgd   1/1     Running   0          15m   172.16.51.178    ip-172-16-61-234.ec2.internal    <none>           <none>
mock-app                                    1/1     Running   0          12m   172.16.51.74     ip-172-16-61-234.ec2.internal    <none>           <none>
```

### 给 Pod 设置网关策略

Egress 网关策略用于定义哪些 Pod 的出口流量要经过 EgressGateway 节点转发，以及其它的配置细节。 当匹配的 Pod 访问任意集群外部的地址（任意非 Node IP、CNI Pod CIDR、ClusterIP 的地址）时，都会被 EgressGateway Node 转发。 

YAML 示例如下：

```yaml
apiVersion: egressgateway.spidernet.io/v1beta1
kind: EgressPolicy
metadata:
  name: test-egw-policy
  namespace: default
spec:
  egressIP:
    useNodeIP: true
  appliedTo:
    podSelector:
      matchLabels:
        app: mock-app
  egressGatewayName: egressgateway
```

### 测试出口 IP 地址

使用 exec 进入容器，运行 `curl ipinfo.io`，您可以看到当前节点的 Pod 已经使用网关节点访问互联网，`ipinfo.io` 会回显主机 IP。

!!! note

    由于 EgressGateway 使用主备实现 HA，当 EIP 节点发生切换时，Pod 会自动切换到匹配的备用节点，同时出口 IP 也会发生变化。

```shell
kubectl exec -it -n default mock-app bash
curl ipinfo.io
{
  "ip": "34.239.162.85",
  "hostname": "ec2-34-239-162-85.compute-1.amazonaws.com",
  "city": "Ashburn",
  "region": "Virginia",
  "country": "US",
  "loc": "39.0437,-77.4875",
  "org": "AS14618 Amazon.com, Inc.",
  "postal": "20147",
  "timezone": "America/New_York",
  "readme": "https://ipinfo.io/missingauth"
}
```

## 获取帮助

有关更多信息，请参阅 EgressGateway 详细[介绍文档](../index.md)。