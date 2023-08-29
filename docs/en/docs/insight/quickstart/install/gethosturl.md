# How to get the address of data upload?

When [installing insight-agent](./install-agent.md), you need to configure the service address to upload the cluster metrics, logs, and trace data to `global service cluster`.
This page outlines the steps on how to obtain the address for data uploads.

## Parameter Description

| parameter | description |
| -------------------------- | ----------------------- -------------------------------------------------- ------------- |
| ${vminsert_host} | metric data upload address, the default is the externally accessible address of the global service cluster vminsert service |
| ${es_host} | Log data upload address, consistent with the elasticsearch service configuration used by the global service cluster |
| ${otel_col_auditlog_port} | audit log data upload address, the default is the externally accessible address of the global service cluster opentelemetry-collector service |
| ${otel_col_host} | trace data upload address, the default is the externally accessible address of the global service cluster opentelemetry-collector service |

!!! note

    If you use an external ElasticSearch cluster, please fill in the address, username and password of the corresponding cluster.

## Install insight-agent in `global service cluster`

When installing `Global Service Cluster`, it is recommended to access the cluster through a domain name:

```go
export vminsert_host="vminsert-insight-victoria-metrics-k8s-stack.insight-system.svc.cluster.local" // metrics
export es_host="insight-es-master.insight-system.svc.cluster.local" // log
export otel_col_host="insight-opentelemetry-collector.insight-system.svc.cluster.local" // link
```

## Install insight-agent on `worker cluster`

The `Working Cluster` needs to upload the data of metrics, logs, and traces to the `Global Service Cluster`. Please ensure that the Insight in the `global service cluster` is running and has exposed the address that the working cluster can access.

### Obtain insight-agent through the interface

Refer to the following steps to obtain insight-agent through the interface.

1. Log in to the console of `Global Service Cluster` and run the following command:

   ```sh
   export INSIGHT_SERVER_IP=$(kubectl get service insight-server -n insight-system --output=jsonpath={.spec.clusterIP})
   curl --location --request POST 'http://'"${INSIGHT_SERVER_IP}"'/apis/insight.io/v1alpha1/agentinstallparam'
   ```

1. After executing the above command, the following return value is obtained:

    ```json
    {"values":"{\"global\":{\"exporters\":{\"logging\":{\"scheme\":\"https\",\"host\":\"mcamel- common-es-cluster-es-http.mcamel-system.svc.cluster.local\",\"port\":9200,\"user\":\"elastic\",\"password\":\" XAlJ948ZY0leE320SQ6hfv17\"},\"metric\":{\"host\":\"10.6.229.181\"},\"auditLog\":{\"host\":\"10.6.229.181\"}}} }"}
    ```

### Connect insight-agent via LoadBalancer

Please confirm that your cluster has installed a load balancer, and follow the steps below to connect insight-agent through LoadBalancer:

1. Log in to the console of the global management cluster and run the following command:

    ```sh
    kubectl get service -n insight-system | grep lb
    kubectl get service -n mcamel-system
    ```

1. Obtain the address information of the corresponding service after execution:

    ```sh
    $ kubectl get service -n insight-system | grep lb
    lb-insight-opentelemetry-collector LoadBalancer 10.233.0.48 10.6.229.181 4317:32608/TCP,8006:30039/TCP 46d
    lb-vminsert-insight-victoria-metrics-k8s-stack LoadBalancer 10.233.3.151 10.6.229.181 8480:31718/TCP 46d

    $ kubectl get service -n mcamel-system | grep common-es-cluster
    mcamel-common-es-cluster-es-http NodePort 10.233.50.159 <none> 9200:31450/TCP 57d
    mcamel-common-es-cluster-es-internal-http ClusterIP 10.233.42.246 <none> 9200/TCP 57d
    mcamel-common-es-cluster-es-transport ClusterIP None <none> 9300/TCP 57d
    mcamel-common-es-cluster-kb-http NodePort 10.233.62.189 <none> 5601:31424/TCP 57d
    mcamel-common-es-cluster-prometheus-exporter ClusterIP 10.233.20.175 <none> 9114/TCP 57d
    ```

	in,

- `lb-vminsert-insight-victoria-metrics-k8s-stack`: URL for uploading metrics data
- `lb-insight-opentelemetry-collector`: trace data upload address
- `mcamel-es-cluster-masters-es-http`: log data upload address

### Connect insight-agent via NodePort

#### Obtain NodePort address through UI page

1. Click `Container Management` from the left navigation bar to enter `Cluster List`.

    

2. Select the cluster `kpanda-global-cluster`, select `Container Application` -> `Service` in the left navigation bar, select `insight-system` namespace, and view the ports exposed by the corresponding service.

    

- `vminsert-insight-victoria-metrics-k8s-stack`: index data upload address, set the NodePort corresponding to port 8480
- `insight-opentelemetry-collector`: trace data upload address, set the NodePort corresponding to port 8006
- `insight-opentelemetry-collector`: Audit log data upload address, set the NodePort corresponding to port 4317
- `mcamel-es-cluster-masters-es-http`: log data upload address, set the NodePort corresponding to port 9200

#### Obtain the service address through the console

Connect insight-agent via NodePort.

1. Log in to the console of the global management cluster and run the following command:

    ```shell
    kubectl get service -n insight-system
    kubectl get service -n mcamel-system
    ```

2. Obtain the address information of the corresponding service:

    ```shell
    $ kubectl get service -n insight-system | grep -E "opentelemetry|vminsert"
    insight-agent-opentelemetry-collector NodePort 10.233.9.24 <none> 6831:32621/UDP,14250:31181/TCP,14268:30523/TCP,8888:32415/TCP,4317:32106/TCP,4318:31221/TCP, 8889:32558/TCP,9411:30911/TCP 42d
    vminsert-insight-victoria-metrics-k8s-stack NodePort 10.233.33.39 <none> 8480:32638/TCP 8d

    $ kubectl get service -n mcamel-system | grep common-es-cluster
    mcamel-common-es-cluster-es-http NodePort 10.233.50.159 <none> 9200:31450/TCP 57d
    ```