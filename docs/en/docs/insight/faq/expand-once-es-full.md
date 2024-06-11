---
MTPE: windsonsea
date: 2024-06-11
---

# What to Do When ElasticSearch is Full?

When ElasticSearch memory is full, you can choose to either [scale up](#scale-up) or [delete data](#delete-data) to resolve the issue:

You can run the following command to check the resource usage of ES nodes.

```bash
kubectl get pod -n mcamel-system | grep common-es-cluster-masters-es | awk '{print $1}' | xargs -I {} kubectl exec {} -n mcamel-system -c elasticsearch -- df -h | grep /usr/share/elasticsearch/data
```

## Scale Up

If the host still has available resources, **scaling up** is a common solution, which involves increasing the PVC capacity.

1. First, run the following command to get the PVC configuration of the `es-data-0` node.
   Use the actual environment's PVC as a reference.

    ```bash
    kubectl edit -n mcamel-system pvc elasticsearch-data-mcamel-common-es-cluster-masters-es-data-0
    ```

2. Then modify the following `storage` field (the storage class SC you are using should be scalable):

    ```yaml
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 35Gi # (1)!
    ```

    1. Adjust this value as needed.

## Delete Data

When ElasticSearch memory is full, you can also delete index data to free up resources.

You can follow the steps below to access the Kibana page and manually delete data.

1. First, ensure that the Kibana Pod exists and is running normally:

    ```bash
    kubectl get po -n mcamel-system | grep mcamel-common-es-cluster-masters-kb
    ```

2. If it does not exist, manually set the replica to 1 and wait for the service to run normally. If it exists, skip this step.

    ```bash
    kubectl scale -n mcamel-system deployment mcamel-common-es-cluster-masters-kb --replicas 1
    ```

3. Modify the Kibana Service to be exposed as a NodePort for access:

    ```bash
    kubectl patch svc -n mcamel-system mcamel-common-es-cluster-masters-kb-http -p '{"spec":{"type":"NodePort"}}'

    # After modification, check the NodePort. For example, if the port is 30128, the access URL will be https://{NodeIP in the cluster}:30128
    [root@insight-master1 ~]# kubectl get svc -n mcamel-system | grep mcamel-common-es-cluster-masters-kb-http
    mcamel-common-es-cluster-masters-kb-http   NodePort    10.233.51.174   <none>   5601:30128/TCP    108m
    ```

4. Retrieve the ElasticSearch Secret to log in to Kibana (username is `elastic`):

    ```bash
    kubectl get secrets -n mcamel-system mcamel-common-es-cluster-masters-es-elastic-user -o jsonpath="{.data.elastic}" | base64 -d
    ```

5. Go to **Kibana** -> **Stack Management** -> **Index Management** and enable the **Include hidden indices** option to see all indexes.
   Based on the index sequence numbers, keep the indexes with larger numbers and delete the ones with smaller numbers.
