# DCE 5.0 的 Istio 从 v1.16.1 升级到 1.22.3

Istio 升级涉及这几个部分：

- Istio 控制面升级
- istio 数据面升级

社区推荐 Istio 升级[使用金丝雀方式升级](https://istio.io/latest/docs/setup/upgrade/canary/)，目前 GProduct
不支持金丝雀升级，在升级过程中[全局服务集群](../../kpanda/user-guide/clusters/cluster-role.md#_2)的应用会因
Istio 控制面更新而无法访问，可能需要人工干预。

## 通过安装器升级 DCE 5.0 时涉及到的 Istio 升级

安装器升级到 v0.24.0 及更高版本时，由于安装器自动处理了相关逻辑，只需要重启未更新 GProduct 的 Pod。

举例：容器管理在安装器升级到 v0.24.0 时版本并没有变化，需要重启容器管理的所有 Pod。

### 重启 GP ro du c t pod

由于 Istio 升级包括两个部分：数据面和控制面。，刚刚我们升级了安装器已经升级了控制面，下面需要升级数据面

重启没有更新版本的 GProduct 命名空间下的 Pod，让数据面的可以升级到 v1.22.3

参考步骤：

1. 直接删除 Pod

    ```shell
    kubectl delete pods --all -n $NAMESPACE
    ```

1. 滚动升级 Deployment、StatefulSet

    ```shell
    kubectl -n $NAMESPACE get deployment -o name | xargs kubectl -n $NAMESPACE rollout restart
    kubectl -n $NAMESPACE get statefulset -o name | xargs kubectl -n $NAMESPACE rollout restart
    ```

## 单独升级全局管理时涉及到的 Istio 升级（通过 Helm）

当全局管理升级到 v0.33.0 及更高版本时，需要将全局服务集群中的 Istio 升级到 v1.22.3。

升级步骤（以 helm 升级为例）如下：

### 获取宿主机内核版本

确定宿主机的操作系统的内核版本，确定内核版本是否小于 v4.11

### 获取 istio helm values 配置

通过 Helm 安装的 Istio 有 3 个 Chart，分别是 base、istiod、gateway，获取它们的 values

```shell
helm -n istio-system get values istio-base > istio-base.yaml
helm -n istio-system get values istiod > istiod.yaml
helm -n istio-system get values istio-ingressgateway > istio-ingressgateway.yaml
```

这样就获取到 3 个 YAML 文件，需要修改其中的 istiod.yaml 和 istio-ingressgateway.yaml

```yaml title="istiod.yaml 示例"
USER-SUPPLIED VALUES:
global:
  hub: docker.m.daocloud.io/istio
  imagePullPolicy: IfNotPresent
  meshID: global-service
  multiCluster:
    clusterName: kpanda-global-cluster
  proxy:
    resources:
      limits:
        cpu: 0m
        memory: 0Mi
      requests:
        cpu: 0m
        memory: 0Mi
meshConfig:
  defaultConfig:
    extraStatTags:
    - destination_mesh_id
    - source_mesh_id
    gatewayTopology:
      numTrustedProxies: 2
    proxyMetadata:
      ISTIO_META_DNS_AUTO_ALLOCATE: "true"
      ISTIO_META_DNS_CAPTURE: "true"
pilot:
  autoscaleMin: 1
  replicaCount: 1
  resources:
    requests:
      cpu: 256m
      memory: 256Mi
telemetry:   # 下一步，这个结构就要删除
  v2:
    prometheus:
      configOverride:
        gateway:
          debug: "false"
          disable_host_header_fallback: true
          metrics:
          - dimensions:
              destination_cluster: node.metadata['CLUSTER_ID']
              destination_mesh_id: node.metadata['MESH_ID']
              source_cluster: downstream_peer.cluster_id
              source_mesh_id: downstream_peer.mesh_id
          stat_prefix: istio
        inboundSidecar:
          debug: "false"
          disable_host_header_fallback: true
          metrics:
          - dimensions:
              destination_cluster: node.metadata['CLUSTER_ID']
              destination_mesh_id: node.metadata['MESH_ID']
              source_cluster: downstream_peer.cluster_id
              source_mesh_id: downstream_peer.mesh_id
          stat_prefix: istio
        outboundSidecar:
          debug: "false"
          metrics:
          - dimensions:
              destination_cluster: node.metadata['CLUSTER_ID']
              destination_mesh_id: node.metadata['MESH_ID']
              source_cluster: downstream_peer.cluster_id
              source_mesh_id: downstream_peer.mesh_id
          stat_prefix: istio
```

```yaml title="istio-ingressgateway.yaml 示例"
USER-SUPPLIED VALUES:
autoscaling:
  minReplicas: 1
global:
  hub: docker.m.daocloud.io/istio
replicaCount: 1
securityContext:
  fsGroup: 1337
  runAsGroup: 1337
  runAsNonRoot: true
  runAsUser: 1337
service:
  ports:
  - name: status-port
    port: 15021
    protocol: TCP
    targetPort: 15021
  - name: http2
    port: 80
    protocol: TCP
    targetPort: 8080
  - name: https
    port: 443
    protocol: TCP
    targetPort: 8443
  type: NodePort
topologySpreadConstraints:
- labelSelector:
    matchLabels:
      app: istio-ingressgateway
  maxSkew: 1
  topologyKey: kubernetes.io/hostname
  whenUnsatisfiable: ScheduleAnyway
```

### 修改 Istio 配置

将 telemetry 结构都删除。如果宿主机的操作系统内核低于 v4.11，需要添加 YAML 配置。

#### 修改 istiod.yaml

```yaml title="修改后的 istiod.yaml"
USER-SUPPLIED VALUES:
global:
  hub: docker.m.daocloud.io/istio
  imagePullPolicy: IfNotPresent
  meshID: global-service
  multiCluster:
    clusterName: kpanda-global-cluster
  proxy:
    resources:
      limits:
        cpu: 0m
        memory: 0Mi
      requests:
        cpu: 0m
        memory: 0Mi
meshConfig:
  defaultConfig:
    extraStatTags:
    - destination_mesh_id
    - source_mesh_id
    gatewayTopology:
      numTrustedProxies: 2
    proxyMetadata:
      ISTIO_META_DNS_AUTO_ALLOCATE: "true"
      ISTIO_META_DNS_CAPTURE: "true"
pilot:
  autoscaleMin: 1
  replicaCount: 1
  resources:
    requests:
      cpu: 256m
      memory: 256Mi
gateways: # 这部分配置是新添加的
  securityContext:
    fsGroup: 1337
    runAsGroup: 1337
    runAsNonRoot: true
    runAsUser: 1337
    sysctls: ~
```

#### 修改 istio-ingressgateway.yaml

如果 YAML 中 Service 和上面示例形式一致，则不用修改。

如果是下面的形式：

```yaml title="istio-ingressgateway.yaml"
USER-SUPPLIED VALUES:
global:
  hub: docker.m.daocloud.io/istio
securityContext:
  runAsUser: 0
service:
  type: NodePort
```

需要修改成：

```yaml title="修改后的 istio-ingressgateway.yaml"
global:
  hub: docker.m.daocloud.io/istio
securityContext:
  runAsUser: 0
service:
  type: NodePort
  ports:
  - name: status-port
    port: 15021
    protocol: TCP
    targetPort: 15021
  - name: config-port
    protocol: TCP
    port: 15000
    targetPort: 15000
  - name: http2
    port: 80
    protocol: TCP
    targetPort: 8080
  - name: https
    port: 443
    protocol: TCP
    targetPort: 8443
```

### 升级 Istio

```shell
helm install istio-base istio/base -n istio-system -f istio-base.yaml
helm install istiod istio/istiod -n istio-system -f istiod.yaml
helm install istio-ingrassgateway istio/gateway -n istio-system -f istio-ingressgateway.yaml
```

Helm 升级可能并不会更新 CRD，你需要手动更新：

```shell
kubectl apply -f ``https://raw.githubusercontent.com/istio/istio/refs/tags/1.22.3/manifests/charts/base/crds/crd-all.gen.yaml
```

### 升级全局管理并重启所有命名空间下的 Pod

#### 升级全局管理

参见[全局管理离线升级步骤](../../ghippo/install/offline-install.md#_3)。

#### 重启 Pod

重启所有命名空间下的 Pod，让数据面可以升级到 v1.22.3

参考步骤：

1. 直接删除 Pod

    ```shell
    kubectl delete pods --all -n $NAMESPACE
    ```

1. 滚动升级 Deployment、StatefulSet

    ```shell
    kubectl -n $NAMESPACE get deployment -o name | xargs kubectl -n $NAMESPACE rollout restart
    kubectl -n $NAMESPACE get statefulset -o name | xargs kubectl -n $NAMESPACE rollout restart
    ```

## 参考

- [Istio 金丝雀升级](https://istio.io/latest/docs/setup/upgrade/canary/)
- [Istio Helm 升级](https://istio.io/latest/docs/setup/upgrade/helm/)
