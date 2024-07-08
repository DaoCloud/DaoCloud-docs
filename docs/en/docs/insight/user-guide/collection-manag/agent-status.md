# insight-agent Component Status Explanation

In DCE 5.0, Insight acts as a multi-cluster observability product.
To achieve unified data collection across multiple clusters, users need to install
the Helm application __insight-agent__ (installed by default in the __insight-system__ namespace).
Refer to [How to Install __insight-agent__ ](../../quickstart/install/install-agent.md).

## Status Explanation

In the "Observability" -> "Collection Management" section, you can view the installation status
of __insight-agent__ in each cluster.

- __Not Installed__ : __insight-agent__ is not installed in the __insight-system__ namespace of the cluster.
- __Running__ : __insight-agent__ is successfully installed in the cluster, and all deployed components are running.
- __Error__ : If __insight-agent__ is in this state, it indicates that the helm deployment failed or
  there are components deployed that are not in a running state.

You can troubleshoot using the following steps:

1. Run the following command. If the status is __deployed__ , proceed to the next step.
   If it is __failed__ , it is recommended to uninstall and reinstall it from
   __Container Management__ -> __Helm Apps__ as it may affect application upgrades:

    ```bash
    helm list -n insight-system
    ```

2. Run the following command or check the status of the deployed components in
   __Insight__ -> __Data Collection__ . If there are container groups not in the __Running__ state,
   restart the containers in an abnormal state.

    ```bash
    kubectl get pods -n insight-system
    ```

## Additional Notes

1. The resource consumption of the Prometheus metric collection component in __insight-agent__ 
   is directly proportional to the number of container groups running in the cluster.
   Please adjust the resources for Prometheus according to the cluster size.
   Refer to [Prometheus Resource Planning](../../quickstart/res-plan/prometheus-res.md).

2. The storage capacity of the vmstorage metric storage component in the global service cluster
   is directly proportional to the total number of container groups in the clusters.

    - Please contact the platform administrator to adjust the disk capacity of vmstorage
      based on the cluster size. Refer to [vmstorage Disk Capacity Planning](../../quickstart/res-plan/vms-res-plan.md).
    - Adjust vmstorage disk based on multi-cluster scale.
      Refer to [vmstorge Disk Expansion](../../quickstart/res-plan/modify-vms-disk.md).
