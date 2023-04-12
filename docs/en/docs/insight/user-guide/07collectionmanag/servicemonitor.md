# Configure service discovery rules

Observable Insight supports the way of creating CRD ServiceMonitor through `container management` to meet your collection requirements for custom service discovery.
Users can use ServiceMonitor to define the scope of the Namespace discovered by the Pod and select the monitored Service through `matchLabel`.

## Prerequisites

The cluster has the Helm application `insight-agent` installed and in the `running` state.

## Steps

1. Select `Acquisition Management` on the left navigation bar to view the status of all cluster collection plug-ins.

    

2. Click the list `cluster name` to enter the collection configuration details.

    

3. Click the link to jump to `Container Management` to create a Service Monitor.

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
name: micrometer-demo
namespace: insight-system
operator.insight.io/managed-by: insight
spec:
endpoints:
- honorLabels: true
interval: 15s
path: /actuator/prometheus
port: http
namespaceSelector:
matchNames:
-insight-system
selector:
matchLabels:
micrometer-prometheus-discovery: "true"
```

In the above YAML file, the meaning of each field is as follows:

- `name` and `namespace` under `metadata` will specify some key meta information required by ServiceMonitor.

- `endpoints` of `spec` is the service endpoint, which represents the address of the collected Metrics required by Prometheus. `endpoints` is an array, and multiple `endpoints` can be created at the same time. Each `endpoints` contains three fields, and the meaning of each field is as follows:

- `interval`: Specifies the period for Prometheus to collect the current `endpoints`. The unit is seconds, set to `15s` in this example.
- `path`: Specify the collection path of Prometheus. In this example, it is specified as `/actuator/prometheus`.
- `port`: Specify the port through which the collected data needs to pass, and the set port is the `name` set by the collected Service port.

- `namespaceSelector` of `spec` is the scope of the Service that needs to be discovered. `namespaceSelector` contains two mutually exclusive fields with the following meanings:

- `any`: There is one and only one value `true`, when this field is set, it will monitor the changes of all services that meet the filter conditions of the Selector.
- `matchNames`: an array value, specifying the range of `namespace` that needs to be monitored. For example, if you only want to listen to Services in the default and insight-system namespaces, then `matchNames` is set as follows:

         ```yaml
namespaceSelector:
matchNames:
- default
-insight-system
        ```

- The `selector` of `spec` is used to select the Service.