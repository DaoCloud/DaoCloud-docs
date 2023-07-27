# Uninstall

!!! danger

    Please make sure to back up all data before uninstalling HwameiStor.

## Option 1: Uninstall and Preserve Existing Data

If you want to uninstall the system components of HwameiStor but keep the created data volumes to serve data applications, follow these steps:

```console
$ kubectl get cluster.hwameistor.io
NAME             AGE
cluster-sample   21m

$ kubectl delete clusters.hwameistor.io hwameistor-cluster
```

Ultimately, all HwameiStor system components (Pods) will be deleted. Use the following command to check, and the result should be empty.

```sh
kubectl -n hwameistor get pod
```

## Option 2: Complete Uninstallation

If you want to uninstall all components of HwameiStor and delete all data volumes
and data, follow these steps carefully.

1. Clean up stateful data applications

    1. Delete the applications.

    2. Delete the Persistent Volume Claims (PVCs).

        The related PVs, LVs, LVRs, LVGs will be deleted as well.

2. Clean up HwameiStor system components

    1. Delete the HwameiStor components.

        ```shell
        kubectl delete clusters.hwameistor.io hwameistor-cluster
        ```

    2. Delete the HwameiStor system namespace.

        ```shell
        kubectl delete ns hwameistor
        ```

    3. Delete CRDs, Hooks, and RBAC.

        ```shell
        kubectl get crd,mutatingwebhookconfiguration,clusterrolebinding,clusterrole -o name \
          | grep hwameistor \
          | xargs -t kubectl delete
        ```

    4. Delete StorageClasses.

        ```shell
        kubectl get sc -o name \
          | grep hwameistor-storage-lvm- \
          | xargs -t kubectl delete
        ```

    5. Uninstall the HwameiStor Operator.

        ```shell
        helm uninstall hwameistor-operator -n hwameistor
        ```

Finally, you still need to clean up the LVM configuration on each node and use
additional system tools (e.g., wipefs) to erase all data on the disks.
