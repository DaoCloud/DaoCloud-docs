# Insight-agent component status

Insight is a multicluster observation product in DCE 5.0. In order to realize the unified collection of multicluster observation data, users need to install the Helm application __insight-agent__ 
(Installed in insight-system namespace by default). See [How to install __insight-agent__ ](install/install-agent.md).

## Status description

In __Insight__ -> __Data Collection__ section, you can view the status of __insight-agent__ installed in each cluster.

- __not installed__ : __insight-agent__ is not installed under the insight-system namespace in this cluster
- __Running__ : __insight-agent__ is successfully installed in the cluster, and all deployed components are running
- __Exception__ : If insight-agent is in this state, it means that the helm deployment failed or the deployed components are not running

Can be checked by:

1. Run the following command, if the status is __deployed__ , go to the next step.
   If it is __failed__ , since it will affect the upgrade of the application,
   it is recommended to reinstall after uninstalling __Container Management__ -> __Helm Apps__ :

     ```bash
     helm list -n insight-system
     ```

2. run the following command or check the status of the components deployed in the cluster in
   __Insight__ -> __Data Collection__ . If there is a pod that is not in the __Running__ state, please restart the abnormal pod.

     ```bash
     kubectl get pods -n insight-system
     ```

## Supplementary instructions

1. The resource consumption of the metric collection component Prometheus in __insight-agent__ is directly proportional
   to the number of pods running in the cluster. Adjust Prometheus resources according to the cluster size,
   please refer to [Prometheus Resource Planning](./res-plan/prometheus-res.md).

2. Since the storage capacity of the metric storage component vmstorage in the global service cluster
   is directly proportional to the sum of the number of pods in each cluster.

    - Please contact the platform administrator to adjust the disk capacity of vmstorage according to the cluster size,
      see [vmstorage disk capacity planning](./res-plan/vms-res-plan.md).
    - Adjust vmstorage disk according to multicluster size, see [vmstorge disk expansion](./res-plan/modify-vms-disk.md).
