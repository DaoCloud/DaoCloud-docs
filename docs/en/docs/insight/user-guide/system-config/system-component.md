# System Components

On the system component page, you can quickly view the running status of the system components in the observability module. When a system component fails, some features in the observability module will be unavailable.

1. Go to __Insight__ product module,
2. In the left navigation bar, select __System Management -> System Components__ .
  
     

## Component description

|Module| Component Name | Description |
| ----- | --------------- | --------------------------- -------------------- |
|Metrics| vminsert-insight-victoria-metrics-k8s-stack | Responsible for writing the metric data collected by Prometheus in each cluster to the storage component. If this component is abnormal, the metric data of the working cluster cannot be written. |
|Metrics| vmalert-insight-victoria-metrics-k8s-stack | Responsible for taking effect of the recording and alert rules configured in the VM Rule, and sending the triggered alert rules to alertmanager. |
|Metrics| vmalertmanager-insight-victoria-metrics-k8s-stack| is responsible for sending messages when alerts are triggered. If this component is abnormal, the alert information cannot be sent. |
|Metrics| vmselect-insight-victoria-metrics-k8s-stack | Responsible for querying metrics data. If this component is abnormal, the metric cannot be queried. |
|Metrics| vmstorage-insight-victoria-metrics-k8s-stack | Responsible for storing multicluster metrics data. |
| Dashboard | grafana-deployment | Provide monitoring panel capability. The exception of this component will make it impossible to view the built-in dashboard. |
|Link| insight-jaeger-collector | Responsible for receiving trace data in opentelemetry-collector and storing it. |
|Link| insight-jaeger-query | Responsible for querying the trace data collected in each cluster. |
|Link| insight-opentelemetry-collector | Responsible for receiving trace data forwarded by each sub-cluster |
|Log| elasticsearch | Responsible for storing the log data of each cluster. |