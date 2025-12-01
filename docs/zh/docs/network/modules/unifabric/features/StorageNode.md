# 存储节点接入指南

## 功能概述

Unifabric 支持将外部裸金属存储节点接入到 Kubernetes 集群中进行统一管理和监控。通过部署 unifabric agent 到存储节点上，agent 会采集存储节点的 RDMA 网络状态、LLDP 邻居信息等，并将数据上报到 k8s 集群中的 unifabric 控制平面。也可以在集群的 grafana 面板中查看存储节点的监控数据。

## 基本要求

1. 存储节点需要安装 Docker（要求支持 docker compose）
2. 存储节点需要能够访问 Kubernetes 集群的 API Server
3. 存储节点是具备 RDMA 网卡的裸金属服务器
4. 待接入的 Kubernetes 集群中已经部署并运行 unifabric 组件

## 创建 kubeconfig 文件

在需要接入存储节点的 k8s 集群的控制节点上，执行以下命令生成 kubeconfig 文件：

```shell
# 指定 unifabric 安装的命名空间
UNIFABRIC_NAMESPACE="unifabric"

cat > cluster1-kubeconfig.yaml <<EOF
apiVersion: v1
kind: Config
clusters:
- cluster:
    certificate-authority-data: $(kubectl config view --raw -o jsonpath="{.clusters[0].cluster.certificate-authority-data}")
    server: $(kubectl config view --raw -o jsonpath="{.clusters[0].cluster.server}")
  name: $(kubectl config view --raw -o jsonpath="{.clusters[0].name}")
contexts:
- context:
    cluster: $(kubectl config view --raw -o jsonpath="{.clusters[0].name}")
    user: unifabric-sa-token
    namespace: ${UNIFABRIC_NAMESPACE}
  name: unifabric-sa-token@$(kubectl config view --raw -o jsonpath="{.clusters[0].name}")
current-context: unifabric-sa-token@$(kubectl config view --raw -o jsonpath="{.clusters[0].name}")
users:
- name: unifabric-sa-token
  user:
    token: $(kubectl get secret unifabric-sa-token -n ${UNIFABRIC_NAMESPACE} -o jsonpath='{.data.token}' | base64 -d)
EOF
```

该 kubeconfig 文件基于 unifabric 安装命名空间下的 ServiceAccount `unifabric-sa-token` 生成，仅包含访问 unifabric 所需要的最小权限。

在本地临时验证，确保 kubeconfig 文件内容正确：

```shell
kubectl --kubeconfig=cluster1-kubeconfig.yaml version
kubectl --kubeconfig=cluster1-kubeconfig.yaml get pods -A
```

将 kubeconfig 文件复制到存储节点服务器的 `/etc/unifabric/cluster1-kubeconfig.yaml` 路径下，方便下面步骤使用。

## 部署 lldp 和 unifabric agent（使用 Docker Compose）

本章节介绍如何使用 Docker Compose 在存储节点上部署 lldp 和 unifabric agent 服务。在每个逻辑金属存储节点上执行以下步骤。

### 1. 运行 lldp 服务

在每一个存储主机上执行部署 unifabric-lldp 服务，每个主机即使接入多个 k8s 集群，也只需部署一个实例即可。首先创建 `/etc/unifabric/lldp.yaml` 文件：

```shell
sudo mkdir -p /etc/unifabric
cat <<'EOF' | sudo tee /etc/unifabric/lldp.yaml > /dev/null
services:
  unifabric-lldp:
    image: ${UNIFABRIC_AGENT_IMAGE}
    container_name: unifabric-lldp
    command: ["/usr/bin/unifabric/entrypoint.sh"]
    network_mode: host
    restart: always
    privileged: true
    environment:
      # 节点 IP 信息（选填）
      NODE_IPADDRESS: ${NODE_IPADDRESS}
      # LLDP 发送间隔，单位秒（选填）
      LLDPD_TX_INTERVAL: 30
      # 要启用 LLDP 的接口，逗号分隔的列表
      # LLDPD_INTERFACE_PATTERN: ""
    volumes:
      - /var/run:/var/run
      - /etc/hostname:/etc/hostname:ro
    healthcheck:
      test: CMD-SHELL lldpcli -v || exit 1
      interval: 5s
      timeout: 3s
      retries: 5
EOF
```

通过下面命令启动 lldp 服务：

- 设置 `UNIFABRIC_AGENT_IMAGE` 环境变量指定 Agent 镜像版本，使用和 k8s 集群匹配的版本。
- 可选设置 `NODE_IPADDRESS` 环境变量指定节点 IP 地址，该 IP 地址将用于 LLDP 广播。

```shell
UNIFABRIC_AGENT_IMAGE="release.daocloud.io/unifabric/unifabric-agent:latest" \
  sudo -E docker compose -f /etc/unifabric/lldp.yaml up -d
```

### 2. 启动 unifabric-agent 服务

确保上节创建的 kubeconfig 在 `/etc/unifabric/cluster1-kubeconfig.yaml` 路径存在。

创建 unifabric agent 配置文件 `/etc/unifabric/cluster1-agent-config.yaml`：

```shell
export METRICS_PORT=5025
export STORAGE_RDMA_NIC_FILTER="interface=*"

cat <<EOF | sudo tee /etc/unifabric/cluster1-agent-config.yaml > /dev/null
inStorageNode: true
metrics:
  port: ${METRICS_PORT}
rdmaNeighbor:
  # 匹配存储 RDMA 网卡，支持通配符
  storageRdmaNicFilter: "${STORAGE_RDMA_NIC_FILTER}"
EOF
```

- `inStorageNode` 是指示 Agent 运行在外部存储节点的方式，必须设置为 `true`。
- `metrics.port` 参数指定存储节点上用于暴露 metrics 的端口，默认是 `5025`，可以根据需要修改，如果接入不同集群，修改使用不同端口以避免冲突。
- `storageRdmaNicFilter` 参数用于匹配存储节点的 RDMA 网卡接口名称，支持通配符，例如 `ens*` 可以匹配所有以 `ens` 开头的接口名称。根据实际存储节点的网卡命名规则进行调整。

创建 Docker Compose 文件 `/etc/unifabric/cluster1-agent-compose.yaml`：

```shell
cat <<'EOF' | sudo tee /etc/unifabric/cluster1-agent-compose.yaml > /dev/null
services:
  unifabric-agent:
    image: ${UNIFABRIC_AGENT_IMAGE}
    container_name: unifabric-agent
    network_mode: host
    restart: always
    privileged: true
    volumes:
      - /etc/unifabric/cluster1-kubeconfig.yaml:/root/.kube/config
      - /etc/unifabric/cluster1-agent-config.yaml:/etc/config/config.yaml
      - /var/run:/var/run
      - /etc/hostname:/etc/hostname:ro
      - /proc:/host/proc:ro
    command:
      - /usr/bin/unifabric/agent
      - -config
      - /etc/config/config.yaml
EOF


UNIFABRIC_AGENT_IMAGE="release.daocloud.io/unifabric/unifabric-agent:latest" \
  sudo -E docker compose -f /etc/unifabric/cluster1-agent-compose.yaml up -d
```

- 注意替换 `UNIFABRIC_AGENT_TAG` 为 k8s 集群匹配的 image 版本，不同的集群可能需要使用不同版本的 Agent 镜像。
- 如果需要接入多个集群，可以复制该文件并修改服务名称和配置文件路径，例如 `cluster1-agent-compose.yaml`，并使用对应的 kubeconfig 和配置文件。

## 集群内配置存储节点 metrics 抓取

在要 k8s 集群控制节点，生成存储节点 metrics 抓取配置文件 `unifabric-metrics-external.yaml`：

```shell
# 设置存储节点 IP 列表，逗号分隔
export STORAGE_NODE_IPS="1.1.1.1,2.2.2.2"
# 设置存储节点 RDMA Agent metrics 端口
export AGENT_PORT_METRICS="5025"
# 设置存储节点 RDMA 延迟 metrics 端口
export RDMA_LATENCY_PORT_METRICS="5027"

# 生成配置文件内容
cat > unifabric-metrics-external.yaml << EOF
apiVersion: v1
kind: Service
metadata:
  name: unifabric-metrics-external
  namespace: unifabric
  labels:
    app: unifabric-metrics-external
spec:
  clusterIP: None
  ports:
    - name: metrics-agent
      port: ${AGENT_PORT_METRICS}
      targetPort: ${AGENT_PORT_METRICS}
    - name: metrics-rdma-latency-cluster1
      port: ${RDMA_LATENCY_PORT_METRICS}
      targetPort: ${RDMA_LATENCY_PORT_METRICS}
---
apiVersion: v1
kind: Endpoints
metadata:
  name: unifabric-metrics-external
  namespace: unifabric
subsets:
  - addresses:
$(IFS=',' read -ra IPS <<< "$STORAGE_NODE_IPS"; for ip in "${IPS[@]}"; do echo "      - ip: $ip"; done)
    ports:
      - name: metrics-agent
        port: ${AGENT_PORT_METRICS}
      - name: metrics-rdma-latency
        port: ${RDMA_LATENCY_PORT_METRICS}
---
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: unifabric-metrics-external
  namespace: unifabric
  labels:
    operator.insight.io/managed-by: insight
    release: kube-prometheus-stack
spec:
  selector:
    matchLabels:
      app: unifabric-metrics-external
  namespaceSelector:
    matchNames:
      - unifabric
  endpoints:
    - port: metrics-agent
      interval: 30s
      path: /metrics
    - port: metrics-rdma-latency
      interval: 30s
      path: /metrics
EOF
```

部署配置文件：

```shell
kubectl apply -f unifabric-metrics-external.yaml
```

## 验证存储节点接入状态

1. 通过下面命令可以看到新接入的节点：

    ```shell
    kubectl get fabricnode
    ```

    然后查看存储节点 fabricnode YAML 信息，确认 RDMA 网卡和 LLDP 邻居信息已经采集：

    ```yaml
    apiVersion: unifabric.io/v1beta1
    kind: FabricNode
    metadata:
      name: l-oss-2
    status:
      rdmaHealthy: true
      scaleUp:
        scaleUpHealthy: false
      storageNics:
        - ipv4: 172.16.1.41/24
          ipv6: ""
          lldpNeighbor:
            description:
              "SONiC Software Version: SONiC.CuOS_4.0-0.R_X86_64_ztp - HwSku:
              ds730-32d - Distribution: 10.13 - Kernel: 4.19.0-12-2-amd64"
            hostname: StorageSW
            mac: 70:06:92:6e:32:64
            mgmtIP: 10.193.77.211
            port: Ethernet200
          name: ens2np0
          rdma: true
          state: up
        - ipv4: ""
          ipv6: ""
          lldpNeighbor:
            description:
              "SONiC Software Version: SONiC.CuOS_4.0-0.R_X86_64_ztp - HwSku:
              ds730-32d - Distribution: 10.13 - Kernel: 4.19.0-12-2-amd64"
            hostname: StorageSW
            mac: 70:06:92:6e:32:64
            mgmtIP: 10.193.77.211
            port: Ethernet192
          name: ens1np0
          rdma: true
          state: up
    ```

2. 在交换机查看 lldp 邻居信息，确认存储节点已经通过 LLDP 广播：

    ```shell
    lldpcli show neighbors
    ```

3. 查看存储节点的 metrics 数据：

    ```shell
    curl http://localhost:5025/metrics
    ```

4. 在 kube-prometheus-stack 的 Grafana 中查看存储节点相关的监控面板，确保可以查看到存储节点的指标数据。

## 接入多个集群

如果需要将存储节点接入多个 Kubernetes 集群，可以为每个集群创建单独的 kubeconfig 和 agent 配置文件，然后创建对应的 Docker Compose 文件启动多个 unifabric agent 实例。
例如，可以创建 `cluster2-kubeconfig.yaml`、`cluster2-agent-config.yaml` 和 `cluster2-agent-compose.yaml`，并使用不同的 metrics 端口以避免冲突。

## 卸载存储节点 Agent

通过下面命令可以卸载存储节点上的 unifabric 服务：

```shell
# 卸载 unifabric agent 服务
# 如果接入了多个集群，需要分别卸载对应的 agent 服务，例如 cluster2-agent-compose.yaml
docker compose down -f /etc/unifabric/cluster1-agent-compose.yaml

# 如果需要卸载 lldp 服务，可以执行：
docker compose down -f /etc/unifabric/lldp.yaml

# 如果需要删除所有配置文件，可以执行：
sudo rm -rf /etc/unifabric
```

## 问题排查

如果存储节点没有正常接入，可以通过查看 Agent 日志进行排查：

```shell
docker compose logs -f /etc/unifabric/cluster1-agent-compose.yaml
docker compose logs -f /etc/unifabric/lldp.yaml
```

如果日志中提示无法连接 Kubernetes 集群，请检查 `/etc/unifabric/cluster1-kubeconfig.yaml` 文件内容是否正确。
可以使用 kubectl 命令测试连接：

```shell
KUBECONFIG=/etc/unifabric/cluster1-kubeconfig.yaml kubectl get pods
```

如果没有 metrics 数据，可以检查存储节点的防火墙设置，确保 5025 端口开放。
并 curl 测试 metrics 抓取：

```shell
curl http://localhost:5025/metrics
```
