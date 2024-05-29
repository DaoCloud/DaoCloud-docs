# Monitoring Edge Resource

This document explains how to enable monitoring capabilities in edge units
to view the status and resource usage of edge nodes and workloads in real time.

Edge monitoring relies on the `insight-agent` component and the edge monitoring component.
The following sections describe how to install the proper components.

!!! note

    Install the `insight-agent` component first, as the edge monitoring component depends on Insight-related plugins.

## Check if Monitoring Components are Installed

Select __Cloud Edge Collaboration__ from the left navigation bar to enter the edge unit page.
Check the Insight and edge component information in the edge unit entries:

- If a version number is displayed, the monitoring component is installed.
- If **Install Now** is displayed, the monitoring component is not installed.
  Click the **Install Now** button to navigate to the proper Helm app details page.

<!-- add screenshot later -->

## Install `insight-agent`

The `insight-agent` is a plugin for cluster observation data collection, supporting unified monitoring
of metrics, traces, and logging. The installation process can be referenced from
[Online Installation of insight-agent](../../../insight/quickstart/install/install-agent.md).

To prevent the `insight` DaemonSet component from being scheduled to edge nodes, add the following
affinity settings to each DaemonSet component under the **insight-system** namespace of the **Global Service Cluster**.

```yaml
nodeAffinity:
  requiredDuringSchedulingIgnoredDuringExecution:
    nodeSelectorTerms:
      - matchExpressions:
        - key: node-role.kubernetes.io/edge
          operator: DoesNotExist
```

<!-- add screenshot later -->

## Install Edge Monitoring Component

1. Select **Container Management** -> **Clusters** from the left navigation bar to enter
   the clusters page. Click the cluster name to enter the cluster details page.

    <!-- add screenshot later -->

2. Select **Helm Apps** -> **Helm Charts** from the left menu.
   Find the `insight-edge-agent` plugin under the addon repository and click to enter the chart details page.

    <!-- add screenshot later -->

3. In the top right corner of the page, select the `insight-edge-agent` version and click
   the **Install** button to enter the `insight-edge-agent` installation page.

    <!-- add screenshot later -->

4. Fill in the addresses of the proper data storage components in the global management cluster
   and the edge worker cluster in the form. After confirming that the information is correct, click **OK** .

    To achieve unified storage and querying of observation data across multiple clusters, the edge cluster needs to report the collected observation data to the global management cluster for unified storage.

    - Obtain the Prometheus service address and port in the **Edge Worker Cluster** . Currently,
      only NodePort is supported, so the address corresponds to that of the worker cluster control node.

        Enter the following command in the `insight-system` namespace to find the service port mapped to port 9090:

        ```shell
        kubectl get svc -n insight-system | grep prometheus
        ```

        !!! note

            If the default access method for the Prometheus service is ClusterIP,
            please change it to NodePort.

        <!-- add screenshot later -->

    - Obtain the ElasticSearch service address and port in the **Global Service Cluster**. Currently,
      only NodePort is supported, so the address corresponds to that of the cluster controller node.

        Enter the following command in the `insight-system` or `mcamel-system` namespace to find
        the service port mapped to port 9200:

        ```shell
        kubectl get service -n mcamel-system | grep es
        ```

        <!-- add screenshot later -->

        !!! note

            Other parameters do not need to be modified by default.

        <!-- add screenshot later -->

5. The system will automatically return to the Helm app list. When the status of **insight-edge-agent**
   changes from **Pending** to **Deployed** , and all component statuses are **Running** ,
   the installation is successful.

## View Edge Monitoring Data

After the edge components are successfully installed and deployed, wait for a while, and then
you can enter the **Insight** module from the left navigation bar to view the data of edge resources.

<!-- add screenshot later -->
