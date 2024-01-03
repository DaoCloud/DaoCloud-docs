# 修改系统配置

可观测性会默认持久化保存指标、日志、链路的数据，您可参阅本文修改系统配置。该文档仅适用于内置部署的 Elasticsearch，若使用外部 Elasticsearch 可自行调整。

## 如何修改指标数据保留期限

先 ssh 登录到对应的节点，参考以下步骤修改指标数据保留期限。

1. 执行以下命令：

    ```sh
    kubectl edit vmcluster insight-victoria-metrics-k8s-stack -n insight-system
    ```

2. 在 Yaml 文件中， __retentionPeriod__ 的默认值为 __14__ ，单位为 __天__ 。您可根据需求修改参数。

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

3. 保存修改后，负责存储指标的组件的容器组会自动重启，稍等片刻即可。

## 如何修改日志数据存储时长

先 ssh 登录到对应的节点，参考以下步骤修改日志数据保留期限：

### 方法一：修改 Json 文件

1. 修改以下文件中 __rollover__ 字段中的 __max_age__ 参数，并设置保留期限，默认存储时长为 __7d__ 。注意需要修改第一行中的 Elastic 用户名和密码、IP 地址和索引。

    ```json
    curl  --insecure --location -u"elastic:amyVt4o826e322TUVi13Ezw6" -X PUT "https://172.30.47.112:30468/_ilm/policy/insight-es-k8s-logs-policy?pretty" -H 'Content-Type: application/json' -d'
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
                            "max_age": "8d",
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
    }'
    ```

2. 修改完后，执行以上命令。它会打印出如下所示内容，则修改成功。

    ```json
    {
    "acknowledged" : true
    }
    ```

### 方法二：从 UI 修改

1. 登录 __kibana__ ，选择左侧导航栏 __Stack Management__ 。

    ![Stack Management](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/logsys01.png)

2. 选择左侧导航 __Index Lifecycle Polices__ ，并找到索引 __insight-es-k8s-logs-policy__ ，点击进入详情。

    ![索引](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/logsys02.png)

3. 展开 __Hot phase__ 配置面板，修改 __Maximum age__ 参数，并设置保留期限，默认存储时长为 __7d__ 。

    ![保留期限](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/logsys03.png)

4. 修改完后，点击页面底部的 __Save policy__ 即修改成功。

    ![保存](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/logsys04.png)

## 如何修改链路数据存储时长

先 ssh 登录到对应的节点，参考以下步骤修改链路数据保留期限：

### 方法一：修改 Json 文件

1. 修改以下文件中 __rollover__ 字段中的 __max_age__ 参数，并设置保留期限，默认存储时长为 __7d__ 。注意需要修改第一行中的 Elastic 用户名和密码、IP 地址和索引。

    ```json
    curl --insecure --location -u"elastic:amyVt4o826e322TUVi13Ezw6" -X PUT "https://172.30.47.112:30468/_ilm/policy/jaeger-ilm-policy?pretty" -H 'Content-Type: application/json' -d'
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
                            "max_age": "6d",
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
    }'
    ```

2. 修改完后，在控制台执行以上命令。它会打印出如下所示内容，则修改成功。

    ```json
    {
    "acknowledged" : true
    }
    ```

### 方法二：从 UI 修改

1. 登录 __kibana__ ，选择左侧导航栏 __Stack Management__ 。

    ![Stack Management](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/logsys01.png)

2. 选择左侧导航 __Index Lifecycle Polices__ ，并找到索引 __jaeger-ilm-policy__ ，点击进入详情。

    ![索引](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/trace02.png)

3. 展开 __Hot phase__ 配置面板，修改 __Maximum age__ 参数，并设置保留期限，默认存储时长为 __7d__ 。

    ![保留期限](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/trace03.png)

4. 修改完后，点击页面底部的 __Save policy__ 即修改成功。

    ![保存](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/trace04.png)
