# Configure service discovery rules

Observable Insight supports the way of creating CRD ServiceMonitor through __container management__ to meet your collection requirements for custom service discovery.
Users can use ServiceMonitor to define the scope of the Namespace discovered by the Pod and select the monitored Service through __matchLabel__ .

## Prerequisites

The cluster has the Helm application __insight-agent__ installed and in the __running__ state.

## Steps

1. Select __Data Collection__ on the left navigation bar to view the status of all cluster collection plug-ins.

    ![Data Collection](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/collectmanage01.png)

2. Click a cluster name to enter the collection configuration details.

    ![Data Collection](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/collectmanage02.png)

3. Click the link to jump to __Container Management__ to create a Service Monitor.

    ```yaml
    apiVersion: monitoring.coreos.com/v1
    kind: ServiceMonitor
    metadata:
      name: micrometer-demo # (1)
      namespace: insight-system # (2)
        labels: 
         operator.insight.io/managed-by: insight
    spec:
      endpoints: # (3)
        - honorLabels: true
           interval: 15s
            path: /actuator/prometheus
            port: http
      namespaceSelector: # (4)
        matchNames:
          - insight-system  # (5)
      selector: # (6)
        matchLabels:
          micrometer-prometheus-discovery: "true"
    ```

    1. Specify the name of the ServiceMonitor.
    2. Specify the namespace of the ServiceMonitor.
    3. This is the service endpoint, which represents the address where Prometheus collects Metrics.
       __endpoints__ is an array, and multiple __endpoints__ can be created at the same time.
       Each __endpoint__ contains three fields, and the meaning of each field is as follows:

        - __interval__ : Specifies the collection cycle of Prometheus for the current __endpoint__ .
          The unit is seconds, set to __15s__ in this example.
        - __path__ : Specifies the collection path of Prometheus.
          In this example, it is specified as __/actuator/prometheus__ .
        - __port__ : Specifies the port through which the collected data needs to pass.
          The set port is the __name__ set by the port of the Service being collected.

    4. This is the scope of the Service that needs to be discovered.
       __namespaceSelector__ contains two mutually exclusive fields, and the meaning of the fields is as follows:

        - __any__ : Only one value __true__ , when this field is set, it will listen to changes
          of all Services that meet the Selector filtering conditions.
        - __matchNames__ : An array value that specifies the scope of __namespace__ to be monitored.
          For example, if you only want to monitor the Services in two namespaces, default and
          insight-system, the __matchNames__ are set as follows:

            ```yaml
            namespaceSelector:
              matchNames:
                - default
                - insight-system
            ```

    5. The namespace where the application that needs to expose metrics is located
    5. Used to select the Service
