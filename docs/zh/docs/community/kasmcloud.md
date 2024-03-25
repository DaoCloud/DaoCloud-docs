<div align="center">
  <h1><code>KasmCloud</code></h1>

<strong>在 Kubernetes 中管理和运行 Actors、Providers 和 Links</strong>

</div>

## :warning:警告

**这是一个由贡献者领导的实验性项目，目前不建议在生产环境中运行。**

每个标签都可以正常工作，但在标签之间可能存在不兼容的更改。

## 设计

[将 WasmCloud 与 Kubernetes 结合](https://docs.google.com/document/d/16p-9czZ6GT_layiabGE6HTyVpbYSALjoyxXhgIfYW0s/edit#heading=h.ymjg4q1g3smk)

<div align="center"><img src="./arch.png" style="width:500px;" /></div>

## 快速开始

1. 部署 Nats

    ```bash
    helm repo add nats https://nats-io.github.io/k8s/helm/charts/
    helm repo update
    helm upgrade --install kasmcloud-nats nats/nats
    ```

2. 部署 KasmCloud CRDs 和 Webhook 服务器

    ```bash
    kubectl apply -f ./deploy/crds
    kubectl apply -f ./deploy/webhook
    ```

3. 部署 KasmCloud Host

    ```bash
    kubectl apply -f ./deploy/kasmcloud_host_rbac.yaml

    # 部署默认的 KasmCloud Host
    kubectl apply -f ./deploy/kasmcloud_host_default.yaml

    # [可选] 您也可以在每个 Kubernetes 节点上部署 KasmCloud Host
    kubectl apply -f ./deploy/kasmcloud_host_daemonset.yaml

    # [可选] 您还可以部署任意数量的临时主机，并通过扩展 Deployment 来更改临时主机的数量
    kubectl apply -f ./deploy/kasmcloud_host_deployment.yaml
    ```

4. 部署 Actor、Link 和 Provider 示例

    ```bash
    kubectl apply -f ./sample.yaml
    kubectl get kasmcloud
    ```
    
    输出为：

    ```console
    NAME                              DESC   PUBLICKEY                                                  REPLICAS   AVAILABLEREPLICAS   CAPS                                                   IMAGE
    actor.kasmcloud.io/echo-default   Echo   MBCFOPM6JW2APJLXJD3Z5O4CN7CPYJ2B4FTKLJUR5YR5MITIU7HD3WD5   10         10                  ["wasmcloud:httpserver","wasmcloud:builtin:logging"]   wasmcloud.azurecr.io/echo:0.3.8

    NAME                                CONTRACTID             LINK   ACTORYKEY                                                  PROVIDERKEY
    link.kasmcloud.io/httpserver-echo   wasmcloud:httpserver   test   MBCFOPM6JW2APJLXJD3Z5O4CN7CPYJ2B4FTKLJUR5YR5MITIU7HD3WD5   VAG3QITQQ2ODAOWB5TTQSDJ53XK3SHBEIFNK4AYJ5RKAX2UNSCAPHA5M

    NAME                                       DESC          PUBLICKEY                                                  LINK   CONTRACTID             IMAGE
    provider.kasmcloud.io/httpserver-default   HTTP Server   VAG3QITQQ2ODAOWB5TTQSDJ53XK3SHBEIFNK4AYJ5RKAX2UNSCAPHA5M   test   wasmcloud:httpserver   ghcr.io/iceber/wasmcloud/httpserver:0.17.0-index
    ```

5. 使用 curl 访问 echo 服务器

    ```bash
    # 在另一个终端中
    kubectl port-forward pod/kasmcloud-host-default 8080:8080

    curl 127.0.0.1:8080
    {"body":[],"method":"GET","path":"/","query_string":""}
    ```

## 路线图

- 添加 KasmCloudHost 资源
- 为资源添加状态信息
- 添加 Kasmcloud Repeater 模块
- 为 Actor 添加滚动更新
- 为 Actor 添加 DaemonSet 部署
- Actors 和 Providers 的蓝/绿部署

## 参考链接

- [kasmcloud 仓库](https://github.com/wasmCloud/kasmcloud)
