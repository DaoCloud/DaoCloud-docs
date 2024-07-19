# Get Data Storage Address of Global Service Cluster

Insight is a product for unified observation of multiple clusters. To achieve unified storage and
querying of observation data from multiple clusters, sub-clusters need to report the collected observation data to the
[global service cluster](../../../kpanda/user-guide/clusters/cluster-role.md#global-service-cluster)
for unified storage. This document provides the necessary address of the storage component when
installing the collection component insight-agent.

## Install insight-agent in Global Service Cluster

If installing insight-agent in the global service cluster, it is recommended to access the cluster via domain name:

```shell
export vminsert_host="vminsert-insight-victoria-metrics-k8s-stack.insight-system.svc.cluster.local" # (1)!
export es_host="insight-es-master.insight-system.svc.cluster.local" # (2)!
export otel_col_host="insight-opentelemetry-collector.insight-system.svc.cluster.local" # (3)!
```

1. Metrics
2. Logs
3. Traces

## Install insight-agent in Other Clusters

### Get Address via Interface Provided by Insight Server

1. The [management cluster](../../../kpanda/user-guide/clusters/cluster-role.md#management-clusters)
   uses the default LoadBalancer mode for exposure.

    Log in to the console of the global service cluster and run the following command:

    !!! note

        Please replace the `${INSIGHT_SERVER_IP}` parameter in the command.

    ```bash
    export INSIGHT_SERVER_IP=$(kubectl get service insight-server -n insight-system --output=jsonpath={.spec.clusterIP})
    curl --location --request POST 'http://'"${INSIGHT_SERVER_IP}"'/apis/insight.io/v1alpha1/agentinstallparam'
    ```

    You will get the following response:

    ```json
    {
      "values": {
        "global": {
          "exporters": {
            "logging": {
              "host": "10.6.182.32"
            },
            "metric": {
              "host": "10.6.182.32"
            },
            "auditLog": {
              "host": "10.6.182.32"
            },
            "trace": {
              "host": "10.6.182.32"
            }
          }
        },
        "opentelemetry-operator": {
          "enabled": true
        },
        "opentelemetry-collector": {
          "enabled": true
        }
      }
    }
    ```

    - `global.exporters.logging.host` is the log service address, no need to set the proper service port,
      the default value will be used.
    - `global.exporters.metric.host` is the metrics service address.
    - `global.exporters.trace.host` is the trace service address.
    - `global.exporters.auditLog.host` is the audit log service address (same service as trace but different port).

1. Management cluster disables LoadBalancer

    When calling the interface, you need to additionally pass an externally accessible node IP from the cluster,
    which will be used to construct the complete access address of the proper service.

    ```bash
    export INSIGHT_SERVER_IP=$(kubectl get service insight-server -n insight-system --output=jsonpath={.spec.clusterIP})
    curl --location --request POST 'http://'"${INSIGHT_SERVER_IP}"'/apis/insight.io/v1alpha1/agentinstallparam' --data '{"extra": {"EXPORTER_EXTERNAL_IP": "10.5.14.51"}}'
    ```

    You will get the following response:

    ```json
    {
      "values": {
        "global": {
          "exporters": {
            "logging": {
              "scheme": "https",
              "host": "10.5.14.51",
              "port": 32007,
              "user": "elastic",
              "password": "j8V1oVoM1184HvQ1F3C8Pom2"
            },
            "metric": {
              "host": "10.5.14.51",
              "port": 30683
            },
            "auditLog": {
              "host": "10.5.14.51",
              "port": 30884
            },
            "trace": {
              "host": "10.5.14.51",
              "port": 30274
            }
          }
        },
        "opentelemetry-operator": {
          "enabled": true
        },
        "opentelemetry-collector": {
          "enabled": true
        }
      }
    }
    ```

    - `global.exporters.logging.host` is the log service address.
    - `global.exporters.logging.port` is the NodePort exposed by the log service.
    - `global.exporters.metric.host` is the metrics service address.
    - `global.exporters.metric.port` is the NodePort exposed by the metrics service.
    - `global.exporters.trace.host` is the trace service address.
    - `global.exporters.trace.port` is the NodePort exposed by the trace service.
    - `global.exporters.auditLog.host` is the audit log service address (same service as trace but different port).
    - `global.exporters.auditLog.port` is the NodePort exposed by the audit log service.

### Connect via LoadBalancer

The above [getting address via interface provided by Insight Server](#get-address-via-interface-provided-by-insight-server) is done by
querying the cluster's LoadBalancer to get the connection address.
Additionally, you can manually run the following command to get the address information of the proper services:

```shell
$ kubectl get service -n insight-system | grep lb
lb-insight-es-master                             LoadBalancer   10.233.35.17    <pending>     9200:31529/TCP                 24d
lb-insight-opentelemetry-collector               LoadBalancer   10.233.23.12    <pending>     4317:31286/TCP,8006:31351/TCP  24d
lb-vminsert-insight-victoria-metrics-k8s-stack   LoadBalancer   10.233.63.67    <pending>     8480:31629/TCP                 24d
```

- `lb-insight-es-master` is the address of the log service.
- `lb-vminsert-insight-victoria-metrics-k8s-stack` is the address of the metrics service.
- `lb-insight-opentelemetry-collector` is the address of the trace service.

### Connect via NodePort

1. Global service cluster enables LB feature [enabled by default]

    Manually run the command `kubectl get service -n insight-system | grep lb` to
    get the NodePort port information of the corresponding services,
    refer to [Connect via LoadBalancer](#connect-via-loadbalancer).
    
1. Global service cluster disables LB feature

    In this case, the above LoadBalancer resources will not be created by default, and the corresponding service names are:

    - vminsert-insight-victoria-metrics-k8s-stack (metrics service)
    - insight-es-master (log service)
    - insight-opentelemetry-collector (trace service)

    After getting the proper port information of the respective services in the above two cases, set as follows:

    ```shell
    --set global.exporters.logging.host=  # (1)!
    --set global.exporters.logging.port=  # (2)!
    --set global.exporters.metric.host=   # (3)!
    --set global.exporters.metric.port=   # (4)!
    --set global.exporters.trace.host=    # (5)!
    --set global.exporters.trace.port=    # (6)!
    --set global.exporters.auditLog.host= # (7)!
    --set global.exporters.auditLog.port= # (8)!
    ```

    1. Externally accessible management cluster NodeIP
    2. NodePort corresponding to log service port 9200
    3. Externally accessible management cluster NodeIP
    4. NodePort corresponding to metrics service port 8480
    5. Externally accessible management cluster NodeIP
    6. NodePort corresponding to trace service port 4317
    7. Externally accessible management cluster NodeIP
    8. NodePort corresponding to trace service port 8006
