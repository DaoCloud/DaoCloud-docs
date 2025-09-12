# 部署 Cilium

本文以 Cilium v1.17.6 为例，讲述如何将 Cilium 部署到你的 Kubernetes 集群中。

1. 准备

    1. 如果是通过 kubespray 安装新集群，建议配置 `kube_network_plugin=cni` 参数。对于已安装
       Calico 的集群，请在 Cilium 安装成功后，参考[卸载 Calico](#calico) 步骤卸载 Calico。

    1. 把整个工程拷贝到 master 节点上, 确保机器上有如下 CLI：helm、kubectl、jq。

        注意：Helm 版本最好高于 v3.17.3（经测试 v3.9.4 会出现与 Cilium Chart 的语法兼容问题）

    1. 确保已经安装了 Kubernetes 集群
        
        如果使用 Kubespray 安装集群，可以指定 kube_network_plugin=cni 和 kube_proxy_remove=true 选项。

    1. 留意 Cilium 官方的[系统要求](https://docs.cilium.io/en/stable/operations/system_requirements/#admin-system-reqs)

1. 安装 Cilium

    进入工程的 Cilium 子目录下，运行如下命令，它会完成 CLI 的安装，以及 Chart 的安装。

    使用该方式安装的 Cilium，默认工作在 vxlan 模式隧道下，且打开了能够兼容的所有其它功能。

    默认从 DaoCloud 在线仓库拉取镜像。

    安装单栈集群：

    ```bash
    export POD_v4CIDR="172.16.0.0/16"
    export POD_v4Block="24"
    export CLUSTER_NAME="cluster1"
    export CLUSTER_ID="10"
    export CLUSTERMESH_APISERVER_NODEPORT="31001"
    export K8S_API_IP="10.0.1.11"
    export K8S_API_PORT="6443"
    export HUBBLE_WEBUI_NODEPORT_PORT="31000"
    export INTEGRATE_ISTIO="false"
    ./setup.sh
    ```

    安装双栈集群：

    ```bash
    export POD_v4CIDR="172.16.0.0/16"
    export POD_v4Block="24"
    export ENABLE_IPV6="true"
    export POD_v6CIDR="fd00::/48"
    export POD_v6Block="64"
    export CLUSTER_NAME="cluster1"
    export CLUSTER_ID="10"
    export CLUSTERMESH_APISERVER_NODEPORT="31001"
    export K8S_API_IP="10.0.1.11"
    export K8S_API_PORT="6443"
    export HUBBLE_WEBUI_NODEPORT_PORT="31000"
    export INTEGRATE_ISTIO="false"
    ./setup.sh
    ```

    | 参数 | 说明 |
    |------|------|
    | `POD_v4CIDR` | 本集群的 Pod IPv4 CIDR。注意，如果后续步骤需要实现多集群网络互联，请确保每个集群的 `POD_v4CIDR` 不重叠。 |
    | `POD_v4Block` | 每个 Node 分割的 Pod 小子网大小。 |
    | `ENABLE_IPV6` | 表示是否启用 IPv6。如果集群主机网卡没有配置 IPv6 地址，Kubernetes 集群没有开启双栈，请不要打开双栈。 |
    | `CLUSTER_NAME` | 表示本集群的名称。请确保唯一，以便未来多集群联通时不会冲突。 |
    | `CLUSTER_ID` | 表示本集群的 ID（取值范围 1–255）。同样必须唯一。 |
    | `CLUSTERMESH_APISERVER_NODEPORT` | Cilium 多集群互联的 nodePort 号，可手动指定一个在合法 nodePort 范围（30000–32767）内的值。注意，每个集群设置的该参数必须唯一，否则多集群互联会出问题。 |
    | `K8S_API_IP` | 本集群 Kubernetes API 服务器的地址。不能是 clusterIP，必须是单个主机的物理地址，或者通过 keepalived 等工具实现的高可用地址。 |
    | `K8S_API_PORT` | 本集群 Kubernetes API 服务器的端口。用于在没有 kube-proxy 时，Cilium 也能访问 API 服务器，为集群提供 Service 能力。 |
    | `HUBBLE_WEBUI_NODEPORT_PORT` | Cilium 可观测性 GUI 的 nodePort 号，可手动指定一个在合法 nodePort 范围（30000–32767）内的值。Cilium 遵循 Kubernetes 集群的 clusterIP CIDR 设置，并允许不同集群的 clusterIP CIDR 重叠。 |
    | `INTEGRATE_ISTIO` | 表示 Istio 是否工作在 Cilium 网络中。如果值为 `true`，会针对 Istio 调优 Cilium 的工作参数。 |

1. 完成 Cilium 安装后，可运行如下命令，查看本集群 Cilium 的状态：

    ```bash
    chmod +x ./showStatus.sh
    ./showStatus.sh
    ```

    完成安装后，可通过 `CLUSTERMESH_APISERVER_NODEPORT` 的 nodePort 访问 Cilium 的报文可观测性 GUI。

1. (可选) 卸载 Calico

    如果您的集群已经安装 Calico，参考[卸载 Calico](#calico) 步骤卸载 Calico。

1. (可选) 卸载 kube-proxy

    Cilium 按照 kube-proxy replacement 方式在工作，因此如果集群中还在运行 kube-proxy，其已经无任何作用了，可卸载。

    ```bash
    # 替换 kube proxy 启动命令，使其清理各种主机规则
    kubectl patch daemonset kube-proxy -n kube-system --type='json' -p='[
      {
        "op": "replace",
        "path": "/spec/template/spec/containers/0/command",
        "value": [
          "/usr/local/bin/kube-proxy",
          "--cleanup"
        ]
      }
    ]'

    # 等待 kube proxy 的所有pod 重启 运行退出后，即可卸载 
    kubectl delete daemonset kube-proxy -n kube-system
    
    # 或者修改 nodename，使其不运行在任何节点上
    # kubectl patch daemonset kube-proxy -n kube-system --type='json' -p='[{"op": "add", "path": "/spec/template/spec/nodeName", "value": "notexsitednode"}]'
    ```

1. (可选) 开启 Cilium 的指标和 Grafana 面板

    1. 确保安装 Grafana 和 Prometheus（需要依赖集群中已经安装了 Grafana 和 Prometheus 的 CRD）

    1. 进入工程的 Cilium 子目录下，运行如下命令，此命令会开启指标和观测面板：

        ```bash
        chmod +x ./setupMetrics.sh
        ./setupMetrics.sh
        ```

    1. 开启指标和观测面板后，即可以在 Grafana 上看到 Cilium 相关的面板。可安装 DCE 定义的告警规则和精选指标面板：

        ```bash
        kubectl apply -n <Insight 租户> -f ./cilium/yamls/ciliumPrometheusRules.yaml
        ```

        ```bash
        kubectl apply -n <Insight 租户> -f ./cilium/yamls/ciliumGrafana.yaml

        # 重启 Grafana Pod
        ```

1. (可选) 实现多集群互联

    注：当多个 Cilium 集群之间的应用需要通过 nodePort 相互访问，会因为 nodePort 端口冲突，导致客户端集群把
    Service 解析到本地集群上，出现访问错误。因此，请务必使用该功能互联集群，并使用 Service 来进行东西向访问，解决该问题。
   
    1. 创建 /root/clustermesh 目录，把所有希望互联的集群的 `/root/.kube/config` 拷贝到该目录下，命名为
       `/root/clustermesh/cluster1`、 `/root/clustermesh/cluster2`、`/root/clustermesh/cluster3` ..... 

    1. 进入本工程的 Cilium 子目录，运行如下命令，完成多集群互联的配置

        ```bash
        chmod +x ./showClusterMesh.sh
        ./setupClusterMesh.sh  /root/clustermesh/cluster1  /root/clustermesh/cluster2 [/root/clustermesh/cluster3 ... ]
        ```

    1. 检查多集群互联状态

        进入工程的 Cilium 子目录下，运行如下命令检查多集群互联状态：

        ```bash
        ./showClusterMesh.sh
        ```

## 卸载 Cilium

```bash
chmod +x ./uninstall.sh
./uninstall.sh
```

## 卸载 Calico

1. 首先在 **具有 kubectl 的 Controller 节点** 执行以下命令，卸载 Calico Kubernetes 资源：

    ```bash
    kubectl get crd | grep projectcalico | awk '{print $1}' | xargs kubectl delete crd || true
    kubectl delete deploy -n kube-system calico-kube-controllers || true
    kubectl delete ds -n kube-system calico-node || true
    kubectl delete sa -n kube-system calico-kube-controllers calico-cni-plugin calico-node || true
    kubectl delete clusterrolebinding calico-cni-plugin calico-kube-controllers calico-node || true
    ```

1. 进入到 Cilium 子目录，在 **每个节点** 上执行 `uninstall_calico.sh`，用于清理每个节点上残留的
   Calico 网络资源。包括其 CNI 配置文件、iptables 规则等。

    ```bash
    chmod +x ./uninstall_calico.sh
    ./uninstall_calico.sh
    ```

1. 为了快速让存量业务 Pod 接入到 Cilium 网络中，有以下两种方式：

    * 依次重启主机，彻底清除 Calico 的残留网络规则（优先推荐）。
    * 如果无法重启主机，可以在每个节点上执行 `restartAllPods.sh`，这将重启所有 Pod 的
      Sandbox 容器，让 Cilium 重新设置 Pod 网络。这不会重启业务容器，不会影响到业务容器的日志等。

    ```bash
    chmod +x ./restartAllPods.sh
    ./restartAllPods.sh
    ```
 
## Cilium 和 Istio 一起工作

当 Istio 和 Cilium 一起工作时，参阅
[Cilium 官方文档](https://docs.cilium.io/en/latest/network/servicemesh/istio/)说明需要进行双方的参数适配

- 在 Cilium 安装过程中，打开 export INTEGRATE_ISTIO="true" 参数，会调整 Cilium 的工作参数
- 在使用中，不要同时使用  Cilium 和 Istio 的 L7 HTTP policy
- 在 Istio 使用带有自动边车注入功能的边车模式时，如果和 Cilium 的隧道模式（VXLAN 或 GENEVE）一起工作，需要让
  istiod Pod 运行在 `hostNetwork=true` 模式，以便能够被 API 服务器访问。

## 运维排障

- 运行命令 `./cilium/showStatus.sh` 查看集群中 Cilium 的状态
- 运行命令 `cilium sysdump` 会导出一个压缩包，包括集群中所有 Cilium 的状态信息
- 抓包

    1. 监控节点本地的实时流量，它最完整，最底层，但是没法看到流量记录：

        ```bash
        kubectl -n kube-system exec ds/cilium -- cilium-dbg monitor -vv
        ```

    1. 查看实时流量和历史记录，它是通过 hubble 过滤了一道：

        ```bash
        kubectl -n kube-system exec ds/cilium -- hubble observe -f
        ```

    1. 主机上使用 hubble，

        查看整个集群的流量事件：

        ```bash
        cilium hubble port-forward &
        ```

        查看所有流量：

        ```bash
        hubble observe -f
        ```

        查看被拒绝的流量：

        ```bash
        hubble observe --verdict DROPPED --verdict ERROR  -f
        ```

        查看某个 Pod 的流量：

        ```bash
        hubble observe --since 3m --pod default/tiefighter -f
        ```
