# OpenShift 安装 Insight Agent

虽然 OpenShift 系统自带了一套监控系统，因为数据采集约定的一些规则，我们还是会安装 Insight Agent。

其中，安除了基础的安装配置之外，helm install 的时候还需要增加如下的参数：

```bash
## 针对 fluentbit 相关的参数；
--set fluent-bit.ocp.enabled=true \
--set fluent-bit.serviceAccount.create=false \
--set fluent-bit.securityContext.runAsUser=0 \
--set fluent-bit.securityContext.seLinuxOptions.type=spc_t \
--set fluent-bit.securityContext.readOnlyRootFilesystem=false \
--set fluent-bit.securityContext.allowPrivilegeEscalation=false \

## 启用适配 OpenShift4.x 的 Prometheus(CR)
--set compatibility.openshift.prometheus.enabled=true \

## 关闭高版本的 Prometheus 实例
--set kube-prometheus-stack.prometheus.enabled=false \
--set kube-prometheus-stack.kubeApiServer.enabled=false \
--set kube-prometheus-stack.kubelet.enabled=false \
--set kube-prometheus-stack.kubeControllerManager.enabled=false \
--set kube-prometheus-stack.coreDns.enabled=false \
--set kube-prometheus-stack.kubeDns.enabled=false \
--set kube-prometheus-stack.kubeEtcd.enabled=false \
--set kube-prometheus-stack.kubeEtcd.enabled=false \
--set kube-prometheus-stack.kubeScheduler.enabled=false \
--set kube-prometheus-stack.kubeStateMetrics.enabled=false \
--set kube-prometheus-stack.nodeExporter.enabled=false \

## 限制 PrometheusOperator 处理的 namespace，避免与 OpenShift 自带的 PrometheusOperator 相互竞争
--set kube-prometheus-stack.prometheusOperator.kubeletService.namespace="insight-system" \
--set kube-prometheus-stack.prometheusOperator.prometheusInstanceNamespaces="insight-system" \
--set kube-prometheus-stack.prometheusOperator.denyNamespaces[0]="openshift-monitoring" \
--set kube-prometheus-stack.prometheusOperator.denyNamespaces[1]="openshift-user-workload-monitoring" \
--set kube-prometheus-stack.prometheusOperator.denyNamespaces[2]="openshift-customer-monitoring" \
--set kube-prometheus-stack.prometheusOperator.denyNamespaces[3]="openshift-route-monitor-operator" \
```

### 通过 OpenShift  自身机制，将系统监控数据写入 Prometheus 中

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-monitoring-config
  namespace: openshift-monitoring
data:
  config.yaml: |
    prometheusK8s:
      remoteWrite:
        - queueConfig:
            batchSendDeadline: 60s
            maxBackoff: 5s
            minBackoff: 30ms
            minShards: 1
            capacity: 5000
            maxSamplesPerSend: 1000
            maxShards: 100
          remoteTimeout: 30s
          url: http://insight-agent-prometheus.insight-system.svc.cluster.local:9090/api/v1/write
          writeRelabelConfigs:
            - action: keep
              regex: etcd|kubelet|node-exporter|apiserver|kube-state-metrics
              sourceLabels:
                - job
```
