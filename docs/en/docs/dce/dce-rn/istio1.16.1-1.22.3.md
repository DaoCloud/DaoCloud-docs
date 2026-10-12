---
hide:
  - navigation
---

# Upgrade DCE's Istio from v1.16.1 to v1.22.3

The Istio upgrade involves the following parts:

- Istio control plane upgrade
- Istio data plane upgrade

The community recommends [upgrading Istio using the canary approach](https://istio.io/latest/docs/setup/upgrade/canary/). Currently, GProduct does not support canary upgrades. During the upgrade process, applications in the [global service cluster](../../kpanda/user-guide/clusters/cluster-role.md#global-service-cluster) may become inaccessible due to the Istio control plane update, which may require manual intervention.

## Istio upgrade involved when upgrading DCE via the installer

When the installer is upgraded to v0.24.0 or higher, the installer automatically handles the related logic, so you only need to restart the Pods of GProducts that have not been updated.

For example, when the installer is upgraded to v0.24.0, the version of Container Management does not change, but all Pods of Container Management need to be restarted.

### Restart GProduct Pods

The Istio upgrade consists of two parts: the data plane and the control plane. The installer has just upgraded the control plane, and now the data plane needs to be upgraded.

Restart the Pods in the namespace of the GProduct that has not been updated, so that the data plane is upgraded to v1.22.3.

Reference steps:

1. Delete Pods directly

    ```shell
    kubectl delete pods --all -n $NAMESPACE
    ```

1. Rolling upgrade Deployments and StatefulSets

    ```shell
    kubectl -n $NAMESPACE get deployment -o name | xargs kubectl -n $NAMESPACE rollout restart
    kubectl -n $NAMESPACE get statefulset -o name | xargs kubectl -n $NAMESPACE rollout restart
    ```

## Istio upgrade involved when upgrading Global Management separately (via Helm)

When Global Management is upgraded to v0.33.0 or higher, Istio in the global service cluster needs to be upgraded to v1.22.3.

The upgrade steps (taking a Helm upgrade as an example) are as follows:

### Get the host kernel version

Determine the kernel version of the host operating system and check whether it is lower than v4.11.

### Get the Istio Helm values configuration

An Istio installed via Helm has 3 charts: base, istiod, and gateway. Get their values:

```shell
helm -n istio-system get values istio-base > istio-base.yaml
helm -n istio-system get values istiod > istiod.yaml
helm -n istio-system get values istio-ingressgateway > istio-ingressgateway.yaml
```

This gives you 3 YAML files. You need to modify istiod.yaml and istio-ingressgateway.yaml.

```yaml title="istiod.yaml example"
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
telemetry:   # In the next step, this structure should be deleted
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

```yaml title="istio-ingressgateway.yaml example"
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

### Modify the Istio configuration

Delete the entire telemetry structure. If the host operating system kernel is lower than v4.11, you need to add YAML configuration.

#### Modify istiod.yaml

```yaml title="Modified istiod.yaml"
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
gateways: # This part of the configuration is newly added
  securityContext:
    fsGroup: 1337
    runAsGroup: 1337
    runAsNonRoot: true
    runAsUser: 1337
    sysctls: ~
```

#### Modify istio-ingressgateway.yaml

If the Service in the YAML is in the same form as the example above, no modification is needed.

If it is in the following form:

```yaml title="istio-ingressgateway.yaml"
USER-SUPPLIED VALUES:
global:
  hub: docker.m.daocloud.io/istio
securityContext:
  runAsUser: 0
service:
  type: NodePort
```

Modify it to:

```yaml title="Modified istio-ingressgateway.yaml"
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

### Upgrade Istio

```shell
helm install istio-base istio/base -n istio-system -f istio-base.yaml
helm install istiod istio/istiod -n istio-system -f istiod.yaml
helm install istio-ingrassgateway istio/gateway -n istio-system -f istio-ingressgateway.yaml
```

A Helm upgrade may not update CRDs; you need to update them manually:

```shell
kubectl apply -f https://raw.githubusercontent.com/istio/istio/refs/tags/1.22.3/manifests/charts/base/crds/crd-all.gen.yaml
```

### Upgrade Global Management and restart all Pods in all namespaces

#### Upgrade Global Management

See [Global Management offline upgrade steps](../../ghippo/install/offline-install.md#upgrade).

#### Restart Pods

Restart all Pods in all namespaces so that the data plane can be upgraded to v1.22.3.

Reference steps:

1. Delete Pods directly

    ```shell
    kubectl delete pods --all -n $NAMESPACE
    ```

1. Rolling upgrade Deployments and StatefulSets

    ```shell
    kubectl -n $NAMESPACE get deployment -o name | xargs kubectl -n $NAMESPACE rollout restart
    kubectl -n $NAMESPACE get statefulset -o name | xargs kubectl -n $NAMESPACE rollout restart
    ```

## Reference

- [Istio canary upgrade](https://istio.io/latest/docs/setup/upgrade/canary/)
- [Istio Helm upgrade](https://istio.io/latest/docs/setup/upgrade/helm/)