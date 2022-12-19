# uninstall

!!! danger

    Please make sure to back up all data before uninstalling HwameiStor.

## Delete the Helm instance

```console
helm delete -n hwameistor hwameistor
```

## Cleanup

1. Remove the namespace

    ```console
    kubectl delete ns hwameistor
    ```

2. Delete the `LocalVolumeGroup` instance

    ```console
    kubectl delete localvolumegroups.hwameistor.io --all
    ```

    !!! note

        The `LocalVolumeGroup` object has a special finalizer, so its instance must be deleted before its definition.

3. Remove CRD, Hook and RBAC

    ```console
    kubectl get crd,mutating webhookconfiguration,clusterrolebinding,clusterrole -o name\
        | grep hwameistor \
        | xargs -t kubectl delete
    ```

4. Remove StorageClass

    ```console
    kubectl get sc -o name \
        | grep hwameistor-storage-lvm- \
        | xargs -t kubectl delete
    ```