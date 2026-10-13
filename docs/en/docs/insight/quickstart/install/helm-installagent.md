# Deploy Insight Agent via Helm

This article describes the steps to install the Community Edition of Insight Agent
by running Helm commands on the command line.

## Install Insight Agent

1. Use the following command to add the address of the image repository.

    ```shell
    helm repo add insight https://release.daocloud.io/chartrepo/insight
    helm repo update
    helm search repo  insight/insight-agent --versions
    ```

2. Installing __Insight Agent__ requires that __Insight Server__ in the global service cluster is running properly.
   Run the following command to install the Community Edition of __Insight Agent__. This configuration does not enable the Tracing feature:

    First set the deployment version, service address and port, and the username and password for Elasticsearch.
    For the service address, refer to __How to Get the Connection Address__ below. Replace the following placeholders with your actual configuration:

    ```shell
    version="<deployment version>"
    es_host="<Elasticsearch address>"
    es_port="<Elasticsearch port>"
    es_user="<Elasticsearch username>"
    es_password="<Elasticsearch password>"
    vminsert_host="<vminsert address>"
    vminsert_port="<vminsert port>"
    otel_col_host="<opentelemetry-collector address>"
    otel_col_auditlog_port="<opentelemetry-collector audit log port>"

    helm upgrade --install --create-namespace --cleanup-on-fail \
        --version "${version}" \
        insight-agent  insight/insight-agent \
        --set global.exporters.logging.elasticsearch.host="${es_host}" \
        --set global.exporters.logging.elasticsearch.port="${es_port}" \
        --set global.exporters.logging.elasticsearch.user="${es_user}" \
        --set global.exporters.logging.elasticsearch.password="${es_password}" \
        --set global.exporters.metric.host="${vminsert_host}" \
        --set global.exporters.metric.port="${vminsert_port}" \
        --set global.exporters.auditLog.host="${otel_col_host}" \
        --set global.exporters.auditLog.port="${otel_col_auditlog_port}" \
        -n insight-system
    ```

    !!! info

        You can refer to __How to Get the Connection Address__ for the address information.

3. Run the following command to check the installation status:

    ```shell
    helm list -A
    kubectl get pods -n insight-system
    ```

### How to Get the Connection Address

#### Install Insight Agent in the Global Service Cluster

If the Agent is installed in the management cluster, it is recommended to access the cluster through a domain name:

```shell
export vminsert_host="vminsert-insight-victoria-metrics-k8s-stack.insight-system.svc.cluster.local" # metrics
export es_host="insight-es-master.insight-system.svc.cluster.local" # logs
export otel_col_host="insight-opentelemetry-collector.insight-system.svc.cluster.local" # traces
```

#### Install Insight Agent in the Worker Cluster

=== "Global Service Cluster Uses the Default LoadBalancer"

    When the global service cluster exposes services through the default LoadBalancer, log in to the console of the global service cluster and run the following commands:

    ```shell
    export INSIGHT_SERVER_IP=$(kubectl get service insight-server -n insight-system --output=jsonpath={.spec.clusterIP})
    curl --location --request POST 'http://'"${INSIGHT_SERVER_IP}"'/apis/insight.io/v1alpha1/agentinstallparam'
    ```

    The following return value will be obtained:

    ```shell
    {"global":{"exporters":{"logging":{"output":"elasticsearch","elasticsearch":{"host":"10.6.182.32"},"kafka":{},"host":"10.6.182.32"},"metric":{"host":"10.6.182.32"},"auditLog":    {"host":"10.6.182.32"}}},"opentelemetry-operator":{"enabled":true},"opentelemetry-collector":{"enabled":true}}
    ```

    Among them:

    - __global.exporters.logging.elasticsearch.host__ is the log service address [there is no need to set the port of the corresponding service, the default values will be used];
    - __global.exporters.metric.host__ is the metric service address;
    - __global.exporters.trace.host__ is the trace service address;
    - __global.exporters.auditLog.host__ is the audit log service address (the same service as traces but with a different port);

=== "Operations in the Console of the Global Service Cluster"

    Log in to the console of the global service cluster and run the following commands:

    ```shell
    kubectl get service -n insight-system | grep lb
    kubectl get service -n mcamel-system | grep es
    ```

    Among them:

    - __lb-vminsert-insight-victoria-metrics-k8s-stack__ is the metric service address;
    - __lb-insight-opentelemetry-collector__ is the trace service address;
    - __mcamel-common-es-cluster-masters-es-http__ is the log service address;

=== "Global Service Cluster Uses Nodeport"

    When the global service cluster exposes services through Nodeport, log in to the console of the global service cluster and run the following commands:

    ```shell
    kubectl get service -n insight-system
    kubectl get service -n mcamel-system
    ```

    Among them:

    - __vminsert-insight-victoria-metrics-k8s-stack__ is the metric service address;
    - __insight-opentelemetry-collector__ is the trace service address;
    - __mcamel-common-es-cluster-masters-es-http__ is the log service address;

## Upgrade Insight Agent

1. Log in to the console of the target cluster and run the following command to back up the `--set` parameters.

    ```shell
    helm get values insight-agent -n insight-system -o yaml > insight-agent.yaml
    ```

2. Run the following command to update the repository.

    ```shell
    helm repo update
    ```

3. Run the following command to upgrade.

    ```shell
    helm upgrade insight-agent insight/insight-agent \
    -n insight-system \
    -f ./insight-agent.yaml \
    --version "${version}"   # specify the version to upgrade to
    ```

4. Run the following command to check the installation status:

    ```shell
    kubectl get pods -n insight-system
    ```

## Uninstall Insight Agent

```shell
helm uninstall insight-agent -n insight-system --timeout 10m
```
