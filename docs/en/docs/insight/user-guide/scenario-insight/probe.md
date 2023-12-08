# Probe

Probe refers to the use of black-box monitoring to regularly test the connectivity of targets through HTTP, TCP, and other methods, enabling quick detection of ongoing faults.

Insight uses the Prometheus Blackbox Exporter tool to probe the network using protocols such as HTTP, HTTPS, DNS, TCP, and ICMP, and returns the probe results to understand the network status.

## Prerequisites

The `insight-agent` has been successfully deployed in the target cluster and is in the `Running` state.

## View Probes

1. Go to the `Observability` product module.
2. Select `Infrastructure` -> `Probes` in the left navigation pane.

    - Click on the cluster or namespace dropdown in the table to switch between clusters and namespaces.
    - The list displays the name, probe method, probe target, connectivity status, and creation time of the probes by default.
    - The connectivity status can be:
        - Normal: The probe successfully connects to the target, and the target returns the expected response.
        - Abnormal: The probe fails to connect to the target, or the target does not return the expected response.
        - Pending: The probe is attempting to connect to the target.
    - Supports fuzzy search of probe names.


## Create a Probe

1. Click on `Create Probe`.
2. Fill in the basic information and click `Next`.

    - Name: The name can only contain lowercase letters, numbers, and hyphens (-), and must start and end with a lowercase letter or number, with a maximum length of 63 characters.
    - Cluster: Select the cluster for the probe task.
    - Namespace: The namespace where the probe task is located.


3. Configure the probe parameters.

    - Blackbox Instance: Select the blackbox instance responsible for the probe.
    - Probe Method:
        - HTTP: Sends HTTP or HTTPS requests to the target URL to check its connectivity and response time. This can be used to monitor the availability and performance of websites or web applications.
        - TCP: Establishes a TCP connection to the target host and port to check its connectivity and response time. This can be used to monitor TCP-based services such as web servers and database servers.
        - Other: Supports custom probe methods by configuring ConfigMap. For more information, refer to: [Custom Probe Methods](probe-module.md)
    - Probe Target: The target address of the probe, supports domain names or IP addresses, etc.
    - Labels: Custom labels that will be automatically added to Prometheus' labels.
    - Probe Interval: The interval between probes.
    - Probe Timeout: The maximum waiting time when probing the target.

4. After configuring, click confirm to complete the creation.

!!! warning

    After the probe task is created, it takes about 3 minutes to synchronize the configuration. During this period, no probes will be performed, and probe results cannot be viewed.

## View Monitoring Dashboards

Click `...` in the operations column and click `View Monitoring Dashboard`.

| Metric Name | Description |
| -- | -- |
| Current Status Response | Represents the response status code of the HTTP probe request. |
| Ping Status | Indicates whether the probe request was successful. 1 indicates a successful probe request, and 0 indicates a failed probe request. |
| IP Protocol | Indicates the IP protocol version used in the probe request. |
| SSL Expiry | Represents the earliest expiration time of the SSL/TLS certificate. |
| DNS Response (Latency) | Represents the duration of the entire probe process in seconds. |
| HTTP Duration | Represents the duration of the entire process from sending the request to receiving the complete response. |

## Edit a Probe

Click `...` in the operations column and click `Edit`.


## Delete a Probe

Click `...` in the operations column and click `Delete`.
