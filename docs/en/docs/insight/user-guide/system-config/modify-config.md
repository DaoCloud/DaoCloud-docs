# Modify system configuration

Observability will persist the data of metrics, logs, and traces by default. Users can modify the system configuration according to This page. This document only applies to the built-in Elasticsearch deployment; if you use an external Elasticsearch, you can adjust it by yourself.

## How to modify the metric data retention period

Refer to the following steps to modify the metric data retention period.

1. Run the following command:

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

Please modify the following Elasticsearch ILM policy configuration file, and adjust the `min_age` parameter of the `delete` phase to set the data retention period. The default retention period is 3d. Fill in the Elasticsearch username and password after `-u`, and change http://localhost:9200 to the address of elastic. Since the data lifecycle passes through the `hot > warm > cold > delete` phases in sequence, but each phase is calculated from the index creation date rather than the end time of the previous phase, the final `retention period = delete.min_age`. Please adjust the `min_age` settings of each phase according to your actual needs. Please note the protocol used by Elasticsearch (for example, HTTPS), and modify the access address according to the actual situation. For example, the Elasticsearch cluster of a default Insight deployment has only the `hot` and `delete` phases, and if you want to retain data for 1 day, you can set `hot.min_age` to 1d and `delete.min_age` to 0.

Refer to the following steps to modify the log data retention period:

### Method 1: Modify the Json file

1. Modify the __min_age__ parameter in the __delete__ field in the following file, and set the retention period. The default storage period is __7d__ . Note that you need to modify the Elastic username and password, IP address, and index in the first line.

    ```json
    curl --insecure --location -u"elastic:amyVt4o826e322TUVi13Ezw6" -X PUT "https://localhost:9200/_ilm/policy/insight-es-k8s-logs-policy?pretty" -H 'Content-Type: application/json' -d'
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
            "min_age": "3d",
            "actions": {
            "delete": {}
            }
        }
        }
    }
    }'
    ```

2. After modification, run the above command. It will print out the content as shown below, then the modification is successful.

    ```json
    {
    "acknowledged" : true
    }
    ```

### Method 2: Modify from the UI

1. Log in __kibana__ , select __Stack Management__ in the left navigation bar.

    ![Stack Management](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/logsys01.png)

2. Select the left navigation __Index Lifecycle Polices__ , and find the index __insight-es-k8s-logs-policy__ , click to enter the details.

    ![Index](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/logsys02.png)

3. Expand the __Hot phase__ configuration panel, modify the __Maximum age__ parameter, and set the retention period. The default storage period is __7d__ .

    ![Retention period](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/logsys03.png)

4. After modification, click __Save policy__ at the bottom of the page to complete the modification.

    ![Save](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/logsys04.png)

## How to modify the trace data storage duration

Same as modifying the log data storage duration above, please modify the following Elasticsearch ILM policy configuration file, and adjust the `min_age` parameter of the `delete` phase to set the data retention period. The default retention period is 3d. Fill in the Elasticsearch username and password after `-u`, and change http://localhost:9200 to the address of elastic. Since the data lifecycle passes through the `hot > warm > cold > delete` phases in sequence, but each phase is calculated from the index creation date rather than the end time of the previous phase, the final `retention period = delete.min_age`. Please adjust the `min_age` settings of each phase according to your actual needs. Please note the protocol used by Elasticsearch (for example, HTTPS), and modify the access address according to the actual situation. For example, the Elasticsearch cluster of a default Insight deployment has only the `hot` and `delete` phases, and if you want to retain data for 1 day, you can set `hot.min_age` to 1d and `delete.min_age` to 0.

Refer to the following steps to modify the trace data retention period:

### Method 1: Modify the Json file

1. Modify the __min_age__ parameter in the __delete__ field in the following file, and set the retention period. The default storage period is __7d__ . Note that you need to modify the Elastic username and password, IP address, and index in the first line.

    ```json
    curl --insecure --location -u"elastic:amyVt4o826e322TUVi13Ezw6" -X PUT "https://localhost:9200/_ilm/policy/jaeger-ilm-policy?pretty" -H 'Content-Type: application/json' -d'
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
            "min_age": "3d",
            "actions": {
            "delete": {}
            }
        }
        }
    }
    }'
    ```

2. After modification, run the above command on the console. It will print out the content as shown below, then the modification is successful.

    ```json
    {
    "acknowledged" : true
    }
    ```

### Method 2: Modify from the UI

1. Log in __kibana__ , select __Stack Management__ in the left navigation bar.

    ![Stack Management](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/logsys01.png)

2. Select the left navigation __Index Lifecycle Polices__ , and find the index __jaeger-ilm-policy__ , click to enter the details.

    ![Index](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/trace02.png)

3. Expand the __Hot phase__ configuration panel, modify the __Maximum age__ parameter, and set the retention period. The default storage period is __7d__ .

    ![Retention period](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/trace03.png)

4. After modification, click __Save policy__ at the bottom of the page to complete the modification.

    ![Save](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/trace04.png)
