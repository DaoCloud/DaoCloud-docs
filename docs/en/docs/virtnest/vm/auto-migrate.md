# Automatic VM Drifting

This article will explain how to seamlessly migrate running virtual machines to other nodes
when a node in the cluster becomes inaccessible due to power outages or network failures,
ensuring business continuity and data security.

Compared to automatic drifting, live migration requires you to manually initiate
the migration process through the interface, rather than having the system automatically trigger it.

## Prerequisites

Before implementing automatic drifting, the following prerequisites must be met:

- The virtual machine has not performed disk commit operations, or is using rook-ceph as the storage system.
- The node has been unreachable for more than five minutes.
- Ensure there are at least two available nodes in the cluster.
- The virtual machine's launcher pod has been deleted.

## Steps

1. Check the status of the virtual machine launcher pod:

    ```sh
    kubectl get pod
    ```

    Check if the launcher pod is in a Terminating state.

2. Force delete the launcher pod:

    If the launcher pod is in a Terminating state, you can force delete it with the following command:

    ```sh
    kubectl delete <launcher pod> --force
    ```

    Replace `<launcher pod>` with the name of your launcher pod.

3. Wait for recreation and check the status:

    After deletion, the system will automatically recreate the launcher pod.
    Wait for its status to become running, then refresh the virtual machine list to see if the VM has successfully migrated to the new node.

## Notes

If using rook-ceph as storage, it needs to be configured in ReadWriteOnce mode:

1. After force deleting the pod, you need to wait approximately six minutes for the launcher pod
   to start, or you can immediately start the pod using the following commands:

    ```sh
    kubectl get pv | grep <vm name>
    kubectl get VolumeAttachment | grep <pv name>
    ```

    Replace `<vm name>` and `<pv name>` with your virtual machine name and persistent volume name.

2. Then delete the corresponding VolumeAttachment with the following command:

    ```sh
    kubectl delete VolumeAttachment <vm>
    ```

    Replace `<vm>` with your virtual machine name.
