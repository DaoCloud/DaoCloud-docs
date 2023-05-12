# index capture method

Prometheus mainly captures the monitoring interface exposed by the target service through Pull, so it is necessary to configure the corresponding capture task to request monitoring data and write it into the storage provided by Prometheus. Currently, the Prometheus service provides the configuration of the following tasks :

- Native Job configuration: Provides the configuration of Prometheus's native grab job.
- Pod Monitor: In the K8S ecosystem, capture the corresponding monitoring data on the Pod based on the Prometheus Operator.
- Service Monitor: In the K8S ecosystem, based on the Prometheus Operator, the monitoring data on the corresponding Endpoints of the Service is captured.

!!! note

     ConfigMaps in [] are optional.

## Native Job configuration

The corresponding ConfigMaps are described as follows:

```yaml
# Grab the task name, and add a label(job=job_name) to the index corresponding to the grab
job_name: <job_name>

# Fetching task time interval
[ scrape_interval: <duration> | default = <global_config. scrape_interval> ]

# Fetch request timeout
[ scrape_timeout: <duration> | default = <global_config. scrape_timeout> ]

# fetch task request URI path
[ metrics_path: <path> | default = /metrics ]

# Solve the processing when the captured label conflicts with the label added by the backend Prometheus.
# true: Keep the captured label, ignore the label that conflicts with the backend Prometheus;
# false: For conflicting labels, add exported_<original-label> before the captured label, and add the label added by the backend Prometheus;
[ honor_labels: <boolean> | default = false ]

# Whether to use the time generated on the target.
# true: If there is a time in the target, use the time on the target;
# false: directly ignore the time on the target;
[ honor_timestamps: <boolean> | default = true ]

# Capture protocol: http or https
[ scheme: <scheme> | default = http ]

# Crawl request corresponding URL parameters
params:
   [ <string>: [<string>, ...] ]

# Set the value of `Authorization` in the crawl request header through basic auth, password/password_file are mutually exclusive, and the value in password_file is preferred.
basic_auth:
   [ username: <string> ]
   [ password: <secret> ]
   [ password_file: <string> ]

# Set the `Authorization` bearer_token/bearer_token_file mutual exclusion in the crawl request header through the bearer token, and the value in the bearer_token is preferred.
[ bearer_token: <secret> ]

# Set the `Authorization` bearer_token/bearer_token_file mutual exclusion in the crawl request header through the bearer token, and the value in the bearer_token is preferred.
[ bearer_token_file: <filename> ]

# Grab whether the connection passes through the TLS secure channel, and configure the corresponding TLS parameters
tls_config:
   [<tls_config>]

# Use the proxy service to capture the metrics on the target, and fill in the corresponding proxy service address.
[ proxy_url: <string> ]

# Specify the target through static configuration, see the description below for details.
static_configs:
   [ - <static_config> ... ]

# CVM service discovery configuration, see the description below for details.
cvm_sd_configs:
   [ - <cvm_sd_config> ... ]

# After capturing the data, rewrite the corresponding label on the target through the relabel mechanism, and execute multiple relabel rules in sequence.
# relabel_config See below for details.
relabel_configs:
   [ - <relabel_config> ... ]

# Before the data is captured and written, rewrite the value corresponding to the label through the relabel mechanism, and execute multiple relabel rules in sequence.
# relabel_config See below for details.
metric_relabel_configs:
   [ - <relabel_config> ... ]

# One-time capture data point limit, 0: no limit, the default is 0
[ sample_limit: <int> | default = 0 ]

# One-time capture Target limit, 0: no limit, default is 0
[ target_limit: <int> | default = 0 ]
```

## Pod Monitor

The corresponding ConfigMaps are described as follows:

```yaml
# Prometheus Operator CRD version
apiVersion: monitoring.coreos.com/v1
# Corresponding to the resource type of K8S, here Pod Monitor
kind: PodMonitor
# Corresponding to the Metadata of K8S, here only care about the name, if no jobLabel is specified, the value of the job in the label corresponding to the capture index is <namespace>/<name>
metadata:
   name: redis-exporter # fill in a unique name
   namespace: cm-prometheus # The namespace is fixed and does not need to be modified
# Describe the selection of the capture target Pod and the configuration of the capture task
spec:
   # Fill in the label of the corresponding Pod, and the pod monitor will take the corresponding value as the value of the job label.
   # If viewing Pod Yaml, take the value in pod.metadata.labels.
   # If viewing Deployment/Daemonset/Statefulset, take spec.template.metadata.labels.
   [ jobLabel: string ]
   # Add the Label on the corresponding Pod to the Label of Target
   [ podTargetLabels: []string ]
   # One-time capture data point limit, 0: no limit, the default is 0
   [ sampleLimit: uint64 ]
   # One-time capture Target limit, 0: no limit, default is 0
   [ targetLimit: uint64 ]
   # Configure the exposed Prometheus HTTP interface that needs to be crawled, and multiple Endpoints can be configured
   podMetricsEndpoints:
   [ - <endpoint_config> ... ] # See the endpoint description below for details
   # Select the namespace where the Pod is to be monitored, if not filled, select all namespaces
   [ namespaceSelector: ]
     # Whether to select all namespaces
     [ any: bool ]
     # Need to select the namespace list
     [ matchNames: []string ]
   # Fill in the Label value of the Pod to be monitored to locate the target Pod [K8S metav1.LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#labelselector-v1-meta)
   selector:
     [ matchExpressions: array ]
       [ example: - {key: tier, operator: In, values: [cache]} ]
     [ matchLabels: object ]
       [ example: k8s-app: redis-exporter ]
```

### Examples

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PodMonitor
metadata:
   name: redis-exporter # fill in a unique name
   namespace: cm-prometheus # namespace fixed, do not modify
spec:
   podMetricsEndpoints:
     - interval: 30s
       port: metric-port # Fill in the name of the Port corresponding to Prometheus Exporter in pod yaml
       path: /metrics # Fill in the value of the Path corresponding to the Prometheus Exporter, if not fill in the default /metrics
       relabelings:
         - action: replace
           sourceLabels:
             - instance
           regex: (.*)
           targetLabel: instance
           replacement: "crs-xxxxxx" # Adjust to the corresponding Redis instance ID
         - action: replace
           sourceLabels:
             - instance
           regex: (.*)
           targetLabel: ip
           replacement: "1.x.x.x" # Adjust to the corresponding Redis instance IP
   namespaceSelector: # Select the namespace where the pod is to be monitored
     matchNames:
       -redis-test
   selector: # Fill in the Label value of the pod to be monitored to locate the target pod
     matchLabels:
       k8s-app: redis-exporter
```

## Service Monitor

The corresponding ConfigMaps are described as follows:

```yaml
# Prometheus Operator CRD version
apiVersion: monitoring.coreos.com/v1
# Corresponding to the resource type of K8S, here Service Monitor
kind: ServiceMonitor
# Corresponding to the K8S Metadata, only the name is concerned here. If no jobLabel is specified, the value of the job in the label of the corresponding capture index is the name of the Service.
metadata:
   name: redis-exporter # fill in a unique name
   namespace: cm-prometheus # The namespace is fixed and does not need to be modified
# Describe the selection of the capture target Pod and the configuration of the capture task
spec:
   # Fill in the label (metadata/labels) of the corresponding Pod, and the service monitor willTake the corresponding value as the value of the job label
   [ jobLabel: string ]
   # Add the Label on the corresponding service to the Label of Target
   [ targetLabels: []string ]
   # Add the Label on the corresponding Pod to the Label of Target
   [ podTargetLabels: []string ]
   # One-time capture data point limit, 0: no limit, the default is 0
   [ sampleLimit: uint64 ]
   # One-time capture Target limit, 0: no limit, default is 0
   [ targetLimit: uint64 ]
   # Configure the exposed Prometheus HTTP interface that needs to be crawled, and multiple Endpoints can be configured
   endpoints:
   [ - <endpoint_config> ... ] # See the endpoint description below for details
   # Select the namespace where the Pod is to be monitored, if not filled, select all namespaces
   [ namespaceSelector: ]
     # Whether to select all namespaces
     [ any: bool ]
     # Need to select the namespace list
     [ matchNames: []string ]
   # Fill in the Label value of the Pod to be monitored to locate the target Pod [K8S metav1.LabelSelector](https://v1-17.docs.kubernetes.io/docs/reference/generated/kubernetes-api/v1.17/#labelselector -v1-meta)
   selector:
     [ matchExpressions: array ]
       [ example: - {key: tier, operator: In, values: [cache]} ]
     [ matchLabels: object ]
       [ example: k8s-app: redis-exporter ]
```

### Examples

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
   name: go-demo # fill in a unique name
   namespace: cm-prometheus # namespace fixed, do not modify
spec:
   endpoints:
     - interval: 30s
       # Fill in the Name of the Port corresponding to the Prometheus Exporter in the service yaml
       port: 8080-8080-tcp
       # Fill in the value of Path corresponding to Prometheus Exporter, do not fill in the default /metrics
       path: /metrics
       relabelings:
         # ** There must be a label for application, here it is assumed that k8s has a label for app,
         # We replaced it with application through the replace action of relabel
         - action: replace
           sourceLabels: [__meta_kubernetes_pod_label_app]
           targetLabel: application
   # Select the namespace where the service is to be monitored
   namespaceSelector:
     matchNames:
       -golang-demo
   # Fill in the Label value of the service to be monitored to locate the target service
   selector:
     matchLabels:
       app: golang-app-demo
```

### endpoint_config

The corresponding ConfigMaps are described as follows:

```yaml
# Corresponding to the name of the port, here you need to pay attention that it is not the corresponding port, default: 80, the corresponding value is as follows:
# ServiceMonitor: corresponding to Service>spec/ports/name;
# PodMonitor: The description is as follows:
# If viewing Pod Yaml, take the value in pod.spec.containers.ports.name.
# If you are looking at Deployment/Daemonset/Statefulset, take the value spec.template.spec.containers.ports.name
[port: string | default = 80]
# fetch task request URI path
[ path: string | default = /metrics ]
# Capture protocol: http or https
[ scheme: string | default = http]
# Crawl request corresponding URL parameters
[params: map[string][]string]
# fetch task interval time
[ interval: string | default = 30s ]
# Fetch task timed out
[ scrapeTimeout: string | default = 30s]
# Grab whether the connection passes through the TLS secure channel, and configure the corresponding TLS parameters
[ tlsConfig: TLSConfig ]
# Read the value corresponding to the bearer token through the corresponding file, and put it in the header of the capture task
[ bearerTokenFile: string ]
# Read the corresponding bearer token through the corresponding K8S secret key, note that the secret namespace needs to be the same as PodMonitor/ServiceMonitor
[ bearerTokenSecret: string ]
# Solve the processing when the captured label conflicts with the label added by the backend Prometheus.
# true: Keep the captured label, ignore the label that conflicts with the backend Prometheus;
# false: For conflicting labels, add exported_<original-label> before the captured label, and add the label added by the backend Prometheus;
[ honorLabels: bool | default = false ]
# Whether to use the time generated on the target.
# true: If there is a time in the target, use the time on the target;
# false: directly ignore the time on the target;
[ honorTimestamps: bool | default = true ]
# Basic auth authentication information, username/password fill in the corresponding K8S secret key value, note that the secret namespace needs to be the same as PodMonitor/ServiceMonitor.
[ basicAuth: BasicAuth ]
# Use the proxy service to capture the metrics on the target, and fill in the corresponding proxy service address
[ proxyUrl: string ]
# After capturing the data, rewrite the corresponding label on the target through the relabel mechanism, and execute multiple relabel rules in order.
# relabel_config See below for details
relabelings:
[-<relabel_config>...]
# Before the data is captured and written, rewrite the value corresponding to the label through the relabel mechanism, and execute multiple relabel rules in order.
# relabel_config See below for details
metricRelabelings:
[-<relabel_config>...]
```

### relabel_config

The corresponding ConfigMaps are described as follows:

```yaml
# Which label values are taken from the original labels for relabeling, and the extracted values are concatenated according to the definition in the separator.
# If it is PodMonitor/ServiceMonitor, the corresponding ConfigMap is sourceLabels
[ source_labels: '[' <labelname> [, ...] ']' ]
# Define the character that needs to be concatenated in the label value of relabel, the default is ';'.
[ separator: <string> | default = ; ]

# When the action is replace/hashmod, use target_label to specify the corresponding label name.
# If it is PodMonitor/ServiceMonitor, the corresponding ConfigMap is targetLabel
[ target_label: <labelname> ]

# An expression that needs to perform regular matching on the corresponding value of source labels
[ regex: <regex> | default = (.*) ]

# Action is used when hashmod is used, and the modulus value is taken according to the corresponding value md5 of the source label
[ modulus: <int> ]

# When the action is replace, use replacement to define the expression that needs to be replaced after the regex matches, which can be replaced with regex regular expressions
[ replacement: <string> | default = $1 ]

# Perform related operations based on the value matched by regex, the corresponding action is as follows, the default is replace:
# replace: If the regex matches, replace the corresponding value with the value defined in replacement, set the value through target_label and add the corresponding label
# keep: If the regex does not match, discard
# drop: if the regex matches, drop it
# hashmod: Take the modulus of the md5 value corresponding to the source label through the value specified by moduels
# And add a new label, the label name is specified by target_label
# labelmap: If the regex matches, use replacement to replace the corresponding label name
# labeldrop: If the regex matches, delete the corresponding label
# labelkeep: If the regex does not match, delete the corresponding label
[ action: <relabel_action> | default = replace ]
```