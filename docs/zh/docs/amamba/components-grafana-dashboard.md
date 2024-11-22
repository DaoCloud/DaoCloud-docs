# 应用工作台组件的可观测面板

本文提供了应用工作台中相关组件如何开启 Grafana 面板的方法，便于监控相关组件的关键指标。应用工作台中的组件包括：

- Jenkins
- ArgoCD
- Argo Rollouts
- KubeVela

默认情况下并不会开启这些组件的指标采集能力，需要手动开启，各个组件的开启方法如下。

## Jenkins

!!! note

    Jenkins 版本需要 >= v0.4.7

需要通过更新 Helm 参数的方式开启，具体方式如下：

1. 前往 **容器管理** ，点击 **集群列表** ，找到 Jenkins 所在的集群
2. 点击 **Helm 应用** ，找到 Jenkins 所在的命名空间。找到 Jenkins 后，点击 **更新**
3. 选择通过 YAML 的形式更新，待修改的 YAML 字段如下：

    ```yaml
    jenkins:
      Master:
        metrics:
          enabled: true
          serviceMonitor:
            enabled: true
            additionalLabels:
              operator.insight.io/managed-by: insight
    ```

4. 点击**保存** ，等待 3 分钟左右
5. 前往 **可观测性** ，点击 **仪表盘** ，在仪表盘中搜索关键字 `jenkins` 即可打开仪表盘

## ArgoCD

ArgoCD 也是通过更新 Helm 参数的方式开启，通过 Helm 更新的步骤与[上述 Jenkins 的步骤](#jenkins)一致，关键字搜索 `argocd`。
待修改的 YAML 字段如下：

```yaml
argo-cd:
  controller:
    metrics:
      enabled: true
      serviceMonitor:
        enabled: true
        additionalLabels:
          operator.insight.io/managed-by: insight
  dex:
    metrics:
      enabled: true
      serviceMonitor:
        enabled: true
        additionalLabels:
          operator.insight.io/managed-by: insight
  redis:
    metrics:
      enabled: true
      serviceMonitor:
        enabled: true
        additionalLabels:
          operator.insight.io/managed-by: insight
  server:
    metrics:
      enabled: true
      serviceMonitor:
        enabled: true
        additionalLabels:
          operator.insight.io/managed-by: insight
  repoServer:
    metrics:
      enabled: true
      serviceMonitor:
        enabled: true
        additionalLabels:
          operator.insight.io/managed-by: insight
  notifications:
    metrics:
      enabled: true
      serviceMonitor:
        enabled: true
        additionalLabels:
          operator.insight.io/managed-by: insight
  applicationSet:
    metrics:
      enabled: true
      serviceMonitor:
        enabled: true
        additionalLabels:
          operator.insight.io/managed-by: insight
```

### argo-rollouts

argo-rollouts 也是通过更新 Helm 参数的方式开启，通过 Helm 更新的步骤与[上述 Jenkins 的步骤](#jenkins)一致，关键字搜索argo-rollouts。
待修改的 YAML 字段如下：

```yaml
argo-rollouts:
  controller:
    metrics:
      enabled: true
      serviceMonitor:
        enabled: true
        additionalLabels:
          operator.insight.io/managed-by: insight
```

### KubeVela

KubeVela **不支持** 直接通过设置参数的方式开启可观测能力。目前需要手动部署以下资源：

1. 部署 Service

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: kubevela-controller-service
      namespace: < your kubevela namespace > # 需要替换
      labels:
        component: kubevela-controller
    spec:
      ports:
        - name: http
          protocol: TCP
          port: 9443
          targetPort: 9443
        - name: metrics
          protocol: TCP
          port: 8080
          targetPort: 8080
      selector: < kubevela core pod label selector> # 需要替换
    ```

2. 部署 ServiceMonitor

    ```yaml
    apiVersion: monitoring.coreos.com/v1
    kind: ServiceMonitor
    metadata:
      name: amamba-kubevela
      namespace: < your kubevela namespace > # 需要替换
      labels:
        operator.insight.io/managed-by: insight
    spec:
      endpoints:
        - honorLabels: true
          interval: 10s
          path: /metrics
          port: metrics
          scheme: http
      namespaceSelector:
        matchNames:
          - < your kubevela namespace > # 需要替换
      selector:
        matchLabels:
          component: kubevela-controller
    ```

注意需要替换成实际的 namespace、labelSelector。打开仪表板的方式与上述 Jenkins、ArgoCD 等其他组件一致。
