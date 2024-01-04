# Modify system configuration

Observability will persist the data of metrics, logs, and traces by default. Users can modify the system configuration according to This page.

## How to modify the metric data retention period

Refer to the following steps to modify the metric data retention period.

1. run the following command:

    ```sh
    kubectl edit vmcluster insight-victoria-metrics-k8s-stack -n insight-system
    ```

2. In the Yaml file, the default value of __retentionPeriod__ is __14__ , and the unit is __day__ . You can modify the parameters according to your needs.

    ```Yaml
    apiVersion: operator.victoriametrics.com/v1beta1
    kind: VMCluster
    metadata:
      annotations:
        meta.helm.sh/release-name: insight
        meta.helm.sh/release-namespace: insight-system
      creationTimestamp: "2022-08-25T04:31:02Z"
      finalizers:
      - apps.victoriametrics.com/finalizer
      generation: 2
      labels:
        app.kubernetes.io/instance: insight
        app.kubernetes.io/managed-by: Helm
        app.kubernetes.io/name: victoria-metrics-k8s-stack
        app.kubernetes.io/version: 1.77.2
        helm.sh/chart: victoria-metrics-k8s-stack-0.9.3
      name: insight-victoria-metrics-k8s-stack
      namespace: insight-system
      resourceVersion: "123007381"
      uid: 55cee8d6-c651-404b-b2c9-50603b405b54
    spec:
      replicationFactor: 1
      retentionPeriod: "14"
      vminsert:
        extraArgs:
          maxLabelsPerTimeseries: "45"
        image:
          repository: docker.m.daocloud.io/victoriametrics/vminsert
          tag: v1.80.0-cluster
          replicaCount: 1
    ```

3. After saving the modification, the pod of the component responsible for storing the metrics will automatically restart, just wait for a while.

## How to modify the log data storage duration

Refer to the following steps to modify the log data retention period:

### Method 1: Modify the Json file

1. Modify the __max_age__ parameter in the __rollover__ field in the following files, and set the retention period. The default storage period is __7d__ . Change `http://localhost:9200` to the address of __elastic__ .

    ```json
    curl -X PUT "http://localhost:9200/_ilm/policy/insight-es-k8s-logs-policy?pretty" -H 'Content-Type: application/json' -d'
    {
    "policy": {
        "phases": {
            "hot": {
                "min_age": "0ms",
                "actions": {
                "set_priority": {
                    "priority": 100
                },
                "rollover": {
                    "max_age": "7d",
                    "max_size": "10gb"
                }
                }
            },
        "warm": {
            "min_age": "10d",
            "actions": {
            "forcemerge": {
                "max_num_segments": 1
            }
            }
        },
        "delete": {
            "min_age": "30d",
            "actions": {
            "delete": {}
            }
        }
        }
    }
    }
    ```

2. After modification, run the above command. It will print out the content as shown below, then the modification is successful.

    ```json
    {
    "acknowledged": true
    }
    ```

### Method 2: Modify from the UI

1. Log in __kibana__ , select __Stack Management__ in the left navigation bar.

    

2. Select the left navigation __Index Lifecycle Polices__ , and find the index __insight-es-k8s-logs-policy__ , click to enter the details.

    

3. Expand the __Hot phase__ configuration panel, modify the __Maximum age__ parameter, and set the retention period. The default storage period is __7d__ .

    

4. After modification, click __Save policy__ at the bottom of the page to complete the modification.

    

## How to modify the trace data storage duration

Refer to the following steps to modify the trace data retention period:

### Method 1: Modify the Json file

1. Modify the __max_age__ parameter in the __rollover__ field in the following files, and set the retention period. The default storage period is __7d__ . At the same time, modify `http://localhost:9200` to the access address of __elastic__ .

    ```json
    curl -X PUT "http://localhost:9200/_ilm/policy/jaeger-ilm-policy?pretty" -H 'Content-Type: application/json' -d'
    {
    "policy": {
        "phases": {
            "hot": {
                "min_age": "0ms",
                "actions": {
                "set_priority": {
                    "priority": 100
                },
                "rollover": {
                    "max_age": "7d",
                    "max_size": "10gb"
                }
                }
            },
        "warm": {
            "min_age": "10d",
            "actions": {
            "forcemerge": {
                "max_num_segments": 1
            }
            }
        },
        "delete": {
            "min_age": "30d",
            "actions": {
            "delete": {}
            }
        }
        }
    }
    }
    ```

2. After modification, run the above command on the console. It will print out the content as shown below, then the modification is successful.

    ```json
    {
    "acknowledged": true
    }
    ```

### Method 2: Modify from the UI

1. Log in __kibana__ , select __Stack Management__ in the left navigation bar.

    

2. Select the left navigation __Index Lifecycle Polices__ , and find the index __jaeger-ilm-policy__ , click to enter the details.

    

3. Expand the __Hot phase__ configuration panel, modify the __Maximum age__ parameter, and set the retention period. The default storage period is __7d__ .

    

4. After modification, click __Save policy__ at the bottom of the page to complete the modification.

    