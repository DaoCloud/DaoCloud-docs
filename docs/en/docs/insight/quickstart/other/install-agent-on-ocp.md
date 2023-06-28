# OpenShift Install Insight Agent

Although the OpenShift system comes with a monitoring system, we will still install Insight Agent because of some rules in the data collection agreement.

Among them, in addition to the basic installation configuration, the following parameters need to be added during helm install:

```bash
## Parameters related to fluentbit;
--set fluent-bit.ocp.enabled=true \
--set fluent-bit.serviceAccount.create=false \
--set fluent-bit.securityContext.runAsUser=0 \
--set fluent-bit.securityContext.seLinuxOptions.type=spc_t \
--set fluent-bit.securityContext.readOnlyRootFilesystem=false \
--set fluent-bit.securityContext.allowPrivilegeEscalation=false \

## Enable Prometheus(CR) for OpenShift4.x
--set compatibility.openshift.prometheus.enabled=true \

## Close the Prometheus instance of the higher version
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

## Limit the namespace processed by PrometheusOperator to avoid competition with OpenShift's own PrometheusOperator
--set kube-prometheus-stack.prometheusOperator.kubeletService.namespace="insight-system" \
--set kube-prometheus-stack.prometheusOperator.prometheusInstanceNamespaces="insight-system" \
--set kube-prometheus-stack.prometheusOperator.denyNamespaces[0]="openshift-monitoring" \
--set kube-prometheus-stack.prometheusOperator.denyNamespaces[1]="openshift-user-workload-monitoring" \
--set kube-prometheus-stack.prometheusOperator.denyNamespaces[2]="openshift-customer-monitoring" \
--set kube-prometheus-stack.prometheusOperator.denyNamespaces[3]="openshift-route-monitor-operator" \
```

### Write system monitoring data into Prometheus through OpenShift's own mechanism

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
