# Realize one-click conversion of DCE4 to DCE5 applications

This section will take the stateless load nginx as an example to introduce how to implement one-click conversion of DCE4 to DCE5 applications through the Multicloud Management interface.

## prerequisites

- The container management module is connected to the cluster whose cluster manufacturer is DaoCloud DCE, please refer to [Connected to Kubernetes cluster](../cluster.md), and can access the UI interface of the cluster.
- The workload in the DCE4 cluster can run normally.

## One-click transfer

1. Go to `multicloud Instance - Workload Management`, click `Connect to Cluster` and choose to connect the DCE4 cluster to the multicloud instance.

    <!--screenshot-->

2. Enter `multicloud Workload - Stateless Load`, click Experience Now, select the target application, and its associated service will be automatically selected, and the associated configuration items and keys will also be converted synchronously.

    <!--screenshot-->

    <!--screenshot-->

3. After the conversion is successful, click Update, select the target deployment cluster, and enable automatic propagation (by default, resources such as ConfigMap and Secret relied on in the multicloud workload configuration will be automatically detected and automatic propagation will be realized).

    <!--screenshot-->

4. Update the deployment policy of the service, and select the deployment cluster.

    <!--screenshot-->

5. Verify that multicloud nginx is running successfully: Pods in both clusters are running successfully and can be accessed normally.

    <!--screenshot-->

6. The workload nginx in the DCE4 cluster will not be affected, and the application will continue to be served.

    <!--screenshot-->