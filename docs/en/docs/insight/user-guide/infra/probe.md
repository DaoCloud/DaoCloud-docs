# Probe

Probe refers to the use of black-box monitoring to regularly test the connectivity of targets through HTTP, TCP, and other methods, enabling quick detection of ongoing faults.

Insight uses the Prometheus Blackbox Exporter tool to probe the network using protocols such as HTTP, HTTPS, DNS, TCP, and ICMP, and returns the probe results to understand the network status.

## Prerequisites

The __insight-agent__ has been successfully deployed in the target cluster and is in the __Running__ state.

## View Probes

1. Go to the __Insight__ product module.
2. Select __Infrastructure__ -> __Probes__ in the left navigation bar.

    - Click the cluster or namespace dropdown in the table to switch between clusters and namespaces.
    - The list displays the name, probe method, probe target, connectivity status, and creation time of the probes by default.
    - The connectivity status can be:
        - Normal: The probe successfully connects to the target, and the target returns the expected response.
        - Abnormal: The probe fails to connect to the target, or the target does not return the expected response.
        - Pending: The probe is attempting to connect to the target.
    - Supports fuzzy search of probe names.


## Create a Probe

1. Click __Create Probe__ .
2. Fill in the basic information and click __Next__ .

    - Name: The name can only contain lowercase letters, numbers, and hyphens (-), and must start and end with a lowercase letter or number, with a maximum length of 63 characters.
    - Cluster: Select the cluster for the probe task.
    - Namespace: The namespace where the probe task is located.


3. Configure the probe parameters.

    - Blackbox Instance: Select the blackbox instance responsible for the probe.
    - Probe Method:
        - HTTP: Sends HTTP or HTTPS requests to the target URL to check its connectivity and response time. This can be used to monitor the availability and performance of websites or web applications.
        - TCP: Establishes a TCP connection to the target host and port to check its connectivity and response time. This can be used to monitor TCP-based services such as web servers and database servers.
        - Other: Supports custom probe methods by configuring ConfigMap. For more information, refer to: [Custom Probe Methods](../collection-manag/probe-module.md)
    - Probe Target: The target address of the probe, supports domain names or IP addresses.
    - Labels: Custom labels that will be automatically added to Prometheus' labels.
    - Probe Interval: The interval between probes.
    - Probe Timeout: The maximum waiting time when probing the target.

4. After configuring, click **OK** to complete the creation.

!!! warning

    After the probe task is created, it takes about 3 minutes to synchronize the configuration. During this period, no probes will be performed, and probe results cannot be viewed.

## View Monitoring Dashboards

Click __ ...__ in the operations column and click __View Monitoring Dashboard__ .

| Metric Name | Description |
| -- | -- |
| Current Status Response | Represents the response status code of the HTTP probe request. |
| Ping Status | Indicates whether the probe request was successful. 1 indicates a successful probe request, and 0 indicates a failed probe request. |
| IP Protocol | Indicates the IP protocol version used in the probe request. |
| SSL Expiry | Represents the earliest expiration time of the SSL/TLS certificate. |
| DNS Response (Latency) | Represents the duration of the entire probe process in seconds. |
| HTTP Duration | Represents the duration of the entire process from sending the request to receiving the complete response. |

## Custom Metrics Alert

After creating a blackbox probing task, besides checking the health status of the probe target via the monitoring 
dashboard, you can also create corresponding alert rules based on the metrics related to the probing. Specifically, 
Prometheus Blackbox Exporter generates a series of metrics from the probing results, with the most commonly used ones 
listed as follows:


| Metric | Description |
| ------ | ------ |
| probe_success | Ping status |
| probe_http_ssl | SSL verification result |
| probe_ssl_earliest_cert_expiry | Earliest SSL certificate expiration date|
| probe_ip_protocol | IP protocol being used |
| probe_http_status_code | HTTP status code returned |
| probe_http_duration_seconds | HTTP request duration |
| probe_http_version | HTTP version|

Commonly used alert rules are configured as below:

```yaml
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMRule
metadata:
  labels:
    operator.insight.io/managed-by: insight
  name: probe-alert-rule
  namespace: test1
spec:
  groups:
    - name: probe
      rules:
        - alert: ProbeFailed
          annotations:
            description: Probe job {{ .labels.job }} access {{ .labels.instance }} in namespace {{ .labels.namespace }} target down for 15s
            value: '{{$value}}'
          expr: probe_success == 0
          for: 15s
          labels:
            severity: critical
        - alert: SlowProbe
          annotations:
            description: Probe job {{ .labels.job }} access {{ .labels.instance }} in namespace {{ .labels.namespace }} took more than 1s to complete
            value: '{{$value}}'
          expr: avg_over_time(probe_duration_seconds[1m]) > 1
          for: 1m
          labels:
            severity: warning
```

## Edit a Probe

Click __ ...__ in the operations column and click __Edit__ .


## Delete a Probe

Click __ ...__ in the operations column and click __Delete__ .
