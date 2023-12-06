# 审计日志获取源 IP

审计日志源 IP 在系统和网络管理中扮演着关键角色，它有助于追踪活动、维护安全、解决问题并确保系统合规性。
但是获取源 IP 会带来一定的性能损耗，所以在 DCE5.0 中审计日志并不总是开启的，
在不同的安装模式下，审计日志源 IP 的默认开启情况不同，并且开启的方式不同。
下面会根据安装模式分别介绍审计日志源 IP 的默认开启情况以及如何开启。

## 判断安装模式的方法

```bash
kubectl get pod -n metallb-system
```

在集群中执行上面的命令，若返回结果如下，则表示该集群为非 metallb 安装模式

```console
No resources found in metallbs-system namespace.
```

## NodePort 安装模式

该模式安装下，审计日志源 IP 默认是关闭的，开启步骤如下：

1. 设置 `istio-ingressgateway` 的 HPA 的最大、最小副本数为节点数

    ```bash
    count=$(kubectl get node | wc -l)
    count=$((count-1))

    if [ $count -gt 5 ]; then
        kubectl patch hpa istio-ingressgateway -n istio-system -p '{"spec":{"maxReplicas":'$count',"minReplicas":'$count'}}'
    else
        kubectl patch hpa istio-ingressgateway -n istio-system -p '{"spec":{"minReplicas":'$count'}}'
    fi
    ```

2. 修改 `istio-ingressgateway` 的 service 的 `externalTrafficPolicy` 值为 Local

    ```bash
    kubectl patch svc istio-ingressgateway -n istio-system -p '{"spec":{"externalTrafficPolicy":"Local"}}'
    ```

## Metallb 安装模式

该模式下安装完成后，会默认获取审计日志源 IP，若需要了解更多，请参考
[Metallb 源 IP](../../../network/modules/metallb/source_ip.md)。
