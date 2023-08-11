# Install Contour

This page describes how to install Contour.

Please confirm that your cluster has successfully connected to the `Container Management` platform, and then perform the following steps to install Contour.

1. Click `Container Management`->`Cluster List` in the left navigation bar, and then find the cluster name where you want to install Contour.

    ![contour-cluster](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/contour-install-1.png)

2. In the left navigation bar, select `Helm Applications` -> `Helm charts`, find and click `contour`.

    ![contour-helm](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/contour-install-2.png)

3. Select the version you want to install in the `Version selection` and click `Install`.

    ![contour-version](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/contour-install-3.png)

4. In the installation page, fill in the required installation parameters.

    ![contour-install-1](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/contour-install-4.png)

    In the screen as above, fill in the `Name`, `Namespace`, `Version`, etc.

    ![contour-install-2](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/contour-install-5.png)

    In the screen as above, fill in the following parameters:

    - `contour` -> `Global Settings` -> `Global Container Registry`: the container registry address.
    - `contour` -> `Contour Settings` -> `Contour Controller` -> `Manage CRDs`: CRDs for Contour.
    - `contour` -> `Contour Settings` -> `Contour Controller` -> `Controller Replica Count`: the number of replicas for the Contour control plane.
    - `contour` -> `Contour Settings` -> `IngressClass` -> `IngressClass Name`: the Ingress Class name. If the cluster deploys multiple Ingresses, this class can be used to differentiate them, and this field will be set when creating the Ingres CR.
    - `contour` -> `Contour Settings` -> `IngressClass` -> `Default IngressClass`: the default Ingress.
    - `contour` -> `Contour Settings` -> `IngressClass` -> `Enable Debug Log`: debug-level log output at the control plane .

    ![contour-install-3](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/contour-install-6.png)

    In the screen as above, fill in the following parameters:

    - `contour` -> `Contour Settings` -> `Envoy Settings` -> `Envoy Replica Count`: the number of replicas of the data plane Envoy.
    - `contour` -> `Contour Settings` -> `Envoy Settings` -> `Envoy Deploy Kind`: the application type of Envoy, including Deployment or DaemonSet.
    - `contour` -> `Contour Settings` -> `Envoy Settings` -> `Enable HostNetwork`: enables Host network, and the default is off. It is not recommended to enable this option if you have no special needs.
    - `contour` -> `Contour Settings` -> `Envoy Settings` -> `Envoy Access Log Level`: Envoy access log level.
    - `contour` -> `Contour Settings` -> `Envoy Settings` -> `Envoy Service` -> `Service Type`: the Service type.
    - `contour` -> `Contour Settings` -> `Envoy Settings` -> `Envoy Service` -> `IP Family Policy`: IP single and dual stack setting. You can turn it on according to your requirement.

    ![contour-install-4](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/contour-install-7.png)

    In the screen as above, fill in the following parameters:

    - `contour` -> `Contour Settings` -> `Envoy Settings` -> `Envoy Node Affinity` -> `Match Expressions`: scheduling rules by soft affinity.
    - `contour` -> `Contour Settings` -> `Envoy Settings` -> `Envoy Node Affinity` -> `Match Expressions` -> `Weight`: the weight of the soft affinity scheduling rule.
    - `contour` -> `Contour Settings` -> `Metrics` -> `ServiceMonitor`: it requires that the cluster has Prometheus Operator deployed in your cluster.
    - `contour` -> `Contour Settings` -> `Alert Configurations` -> `Prometheus Rule`: ff enabled, create a Prometheus Rule CR with alert rules. It requires that the cluster has Prometheus Operator installed or that the Insight component is deployed.

5. Click the tab `YAML` to perform advanced configuration via YAML. Then, click the `OK` button in the bottom right corner to complete the creation.

    ![contour-yaml](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/contour-install-8.png)

Once created, create the Ingress route and select the Contour instance via `Platform Load Balancing`. For details, refer to: [Create Route](../../../kpanda/user-guide/services-routes/create-ingress.md)
