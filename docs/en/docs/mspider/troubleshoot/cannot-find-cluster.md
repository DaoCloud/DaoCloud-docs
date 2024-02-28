# Could not find the owning cluster when creating the mesh

## Cause Analysis

The main reason is that the __MeshCluster__ status of the cluster to which it belongs is not "CLUSTER_RUNNING". You can log in to the global cluster to view the status of the MeshCluster CRD of the cluster to which it belongs.

```bash
kubectl get meshcluster -n mspider-system
```

There are several situations that can cause this problem:

### Case 1

If the mesh has not been created with the cluster before, the meshcluster CRD of the cluster cannot be found by executing the above command.
Probably because of gsc-controller syncing cluster exception from container management (kpanda).

### Case 2

To remove the cluster from the created mesh, run the above command. The state of the __meshcluster__ found for this cluster may be in one of the following states:

- MANAGED_RECONCILING
- MANAGED_SUCCEED
- MANAGED_EVICTING
- MANAGED_FAILED

The reason may be that resources are being cleaned up or there is a meshconfig that is not cleaned up.

## Solution

1. For case 1, you only need to restart the gsc-controller of the global cluster.

     ```bash
     kubectl -n mspider-system delete pod $(kubectl -n mspider-system get pod -l app=mspider-gsc-controller -o 'jsonpath={.items.metadata.name}')
     ```

2. For case 2, the environment may not be cleaned up. Please ensure that the control plane components of the cluster to which it belongs (control plane cluster) are cleaned up, otherwise it will affect the next mesh creation.

     1. Delete the meshconfig that has not been cleaned up and caused abnormal installation status

         ```bash
         kubectl delete meshcluster -n mspider-system ${clustername}
         ```

     1. Restart gsc-controller to resync the cluster

         ```bash
         kubectl delete po -n mspider-system ${gsc-coontroller-xxxxxxxxxx}
         ```
