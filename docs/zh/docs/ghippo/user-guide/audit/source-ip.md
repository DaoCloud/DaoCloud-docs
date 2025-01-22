# 审计日志获取源 IP

审计日志源 IP 在系统和网络管理中扮演着关键角色，它有助于追踪活动、维护安全、解决问题并确保系统合规性。
但是获取源 IP 会带来一定的性能损耗，所以在 DCE 5.0 中审计日志并不总是开启的，
在不同的安装模式下，审计日志源 IP 的默认开启情况不同，并且开启的方式不同。
下面会根据安装模式分别介绍审计日志源 IP 的默认开启情况以及如何开启。

!!! note

    开启审计日志会修改 istio-ingressgateway 的副本数，带来一定的性能损耗。
    开启审计日志需要关闭 kube-proxy 的负载均衡以及拓扑感知路由，会对集群性能产生一定的影响。
    开启审计日志后，访问IP所对应的节点上必须保证存在 istio-ingressgateway ，若因为节点健康或其他问题导致 istio-ingressgateway 发生漂移，需要手动调度回该节点，否则会影响 DCE 5.0 的正常使用。

## 判断安装模式的方法

```bash
kubectl get pod -n metallb-system
```

在集群中执行上面的命令，若返回结果如下，则表示该集群为非 MetalLB 安装模式

```console
No resources found in metallbs-system namespace.
```

## NodePort 安装模式

该模式安装下，审计日志源 IP 默认是关闭的，开启步骤如下：

1. 设置 __istio-ingressgateway__ 的 HPA 的最小副本数为控制面节点数

    ```bash
    count=$(kubectl get nodes --selector=node-role.kubernetes.io/control-plane | wc -l)
    count=$((count-1))

    kubectl patch hpa istio-ingressgateway -n istio-system -p '{"spec":{"minReplicas":'$count'}}'
    ```

2. 修改 __istio-ingressgateway__ 的 service 的 __externalTrafficPolicy__ 和 __internalTrafficPolicy__ 值为 "Local"

    ```bash
    kubectl patch svc istio-ingressgateway -n istio-system -p '{"spec":{"externalTrafficPolicy":"Local","internalTrafficPolicy":"Local"}}'
    ```

## MetalLB 安装模式

该模式下安装完成后，会默认获取审计日志源 IP，若需要了解更多，请参考
[MetalLB 源 IP](../../../network/modules/metallb/source_ip.md)。
