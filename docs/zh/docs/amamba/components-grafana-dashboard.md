# Amamba 组件可观测面板

本文提供了 `Amamba` 中相关组件如何开启grafana面板的方法,便于监控相关组件的关键指标。Amamba中的组件包括：

- Jenkins
- ArgoCD
- Argo-Rollouts
- Kubevela

默认情况下并不会开启这些组件的指标采集能力，需要手动开启，各个组件的开启方法如下。

## Jenkins

> jenkins 版本需要 >= v0.4.7

需要通过更新helm参数的方式开启,具体方式如下：

1. 前往 **容器管理** 模块，点击 **集群列表**，找到Jenkins安装的集群
2. 点击 **Helm 应用**，找到Jenkins安装的命名空间。找到Jenkins后，点击 **更新**
3. 选择通过yaml的形式更新，待修改的yaml值如下：

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

4. 点击保存，等待三分钟左右
5. 前往 **可观测性** 模块，点击 **仪表盘**, 在仪表盘中搜索关键字 `jenkins` 即可打开仪表盘

## ArgoCD

ArgoCD 也是通过更新helm参数的方式开启，通过helm更新的步骤与 jenkins 一致,关键字搜索argocd，此处不在赘述。
待修改的yaml值如下：

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

Argo-rollouts 也是通过更新helm参数的方式开启，通过helm更新的步骤与 jenkins 一致,关键字搜索argo-rollouts，此处不在赘述。
待修改的yaml值如下：

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

### kubevela

kubevela **不支持** 直接通过设置参数的方式开启可观测能力。目前需要手动部署以下资源：

1. 部署Service

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

2. 部署ServiceMonitor

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

注意需要对实际的namespace，labelSelector进行替换。打开面板的方式与其他组件一致。
