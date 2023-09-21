# DCE 4.0 接入问题追踪

本页列出一些服务网格接入 DCE 4.0 时常见的问题。

## LimitRange 问题

### 问题描述

1. 接入 DCE 4.0 时报错。

    ```console
    message: 'unable to retrieve Pods: Unauthorized'
    ```

1. 控制面集群。

    提示以下报错：

    ```console
    mspider-mcpc-mcpc-controller-5bd6d54c4-df6kg  CrashLoopBackOff
    ```

    查看控制面的日志：

    ```shell
    kubectl logs -n istio-system mspider-mcpc-mcpc-controller-5bd6d54c4-df6kg
    ```

    ```console
    time="2022-10-19T06:35:49Z" level=error msg="Unable to get kube configs of multi clusters: Get \"http://mspider-mcpc-ckube-remote/api/v1/namespaces/istio-system/configmaps/mspider-mcpc-remote-kube-api-server?resourceVersion=dsm-cluster-dce4-mspider\": dial tcp: lookup mspider-mcpc-ckube-remote: i/o timeout" func="cmholder.NewConfigHolder()" file="holder.go:52"
    panic: unable to get kube configs of multi clusters: Get "http://mspider-mcpc-ckube-remote/api/v1/namespaces/istio-system/configmaps/mspider-mcpc-remote-kube-api-server?resourceVersion=dsm-cluster-dce4-mspider": dial tcp: lookup mspider-mcpc-ckube-remote: i/o timeout

    goroutine 1 [running]:
    main.main()
        /app/cmd/control-plane/mcpc/main.go:62 +0x694
    ```

1. rs: istio-operator-*** 报错：

    ```console
    message: 'pods "istio-operator-5fbbf5bbd-hf2q2" is forbidden: memory max limit
        to request ratio per Container is 1, but provided ratio is 2.000000'
    ```

### 解决办法

需要手动在 istio-operator 和 isito-system 中设置 limit range，将超配比例设置成 0。

执行以下命令查看 istio-operator 命令空间的 limit range：

```shell
kubectl describe limits -n istio-operator dce-default-limit-range
```

执行以下命令查看 istio-system 命令空间的 limit range：

```shell
kubectl describe limits -n istio-system dce-default-limit-range
```

## istiod 和 ingressgateway 一直处于 ContainerRuning 状态

原因分析：DCE 4.0 所使用的 Kubernetes 版本为 1.18，相对新版服务网格，其版本太低了。

表现形式 01： `istio-managed-istio-hosted` 一直无法启动，提示 `istio-token` 的 Configmap 不存在。

需要手动为网格实例的 CR 中 `GlobalMesh` 添加对应的参数： `istio.custom_params.values.global.jwtPolicy: first-party-jwt`。

![params](./images/dce4-01.png)

!!! tip

    1. DCE 4.0 在接入新版服务网格之前，需提前部署 coreDNS。

    2. `GlobalMesh` 配置是在 DCE5 的全局管理集群，而不是在接入集群。
