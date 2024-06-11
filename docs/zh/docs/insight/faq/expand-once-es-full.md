# ElasticSearch 数据塞满如何操作？

当 ElasticSearch 内存占满时，可以选择[扩容](#_1)或者[删除数据](#_2)来解决：

你可以运行如下命令查看 ES 节点的资源占比。

```bash
kubectl get pod -n mcamel-system | grep common-es-cluster-masters-es | awk '{print $1}' | xargs -I {} kubectl exec {} -n mcamel-system -c elasticsearch -- df -h | grep /usr/share/elasticsearch/data
```

## 扩容

在主机节点还有资源的情况下， **扩容** 是一种常见的方案，也就是提高 PVC 的容量。

1. 先运行以下命令获取 es-data-0 节点的 PVC 配置，请以实际的环境的 PVC 为准。

    ```bash
    kubectl edit -n mcamel-system pvc elasticsearch-data-mcamel-common-es-cluster-masters-es-data-0
    ```

2. 然后修改以下 `storage` 字段（需要使用的存储类 SC 可以扩容）

    ```yaml
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 35Gi # (1)!
    ```

    1. 这个数值需调整

## 删除数据

当 ElasticSearch 内存占满时，你还可以删除 index 数据释放资源。

你可以参考以下步骤进入 Kibana 页面，手动执行删除操作。

1. 首先明确 Kibana Pod 是否存在并且正常运行：

    ```bash
    kubectl get po -n mcamel-system |grep mcamel-common-es-cluster-masters-kb
    ```

2. 若不存在，则手动设置 replica 为 1，并且等待服务正常运行；若存在，则跳过该步骤

    ```bash
    kubectl scale -n mcamel-system deployment mcamel-common-es-cluster-masters-kb --replicas 1
    ```

3. 修改 Kibana 的 Service 为 NodePort 暴露访问方式

    ```bash
    kubectl patch svc -n mcamel-system mcamel-common-es-cluster-masters-kb-http -p '{"spec":{"type":"NodePort"}}'

    # 修改完成后查看 NodePort。此例的端口为 30128，则访问方式为 https://{集群中的节点IP}:30128
    [root@insight-master1 ~]# kubectl get svc -n mcamel-system |grep mcamel-common-es-cluster-masters-kb-http
    mcamel-common-es-cluster-masters-kb-http   NodePort    10.233.51.174   <none>   5601:30128/TCP    108m
    ```

4. 获取 ElasticSearch 的 Secret，用于登录 Kibana（用户名为 elastic）

    ```bash
    kubectl get secrets -n mcamel-system mcamel-common-es-cluster-masters-es-elastic-user -o jsonpath="{.data.elastic}" |base64 -d
    ```

5. 进入 **Kibana** -> **Stack Management** -> **Index Management** ，打开 **Include hidden indices** 选项，即可见所有的 index。
   根据 index 的序号大小，保留序号大的 index，删除序号小的 index。
