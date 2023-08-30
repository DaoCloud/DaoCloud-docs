# Store NIC configuration

HwameiStor supports the use of a separate network card for data volume synchronization, which can avoid traffic congestion caused by using a communication network card.

!!! note

    -【🔥Advance configuration】: The configuration of the storage network card belongs to the pre-configuration of the storage system. It is recommended to **configure in advance** before installing the HwameiStor system.
    - [Configuration during operation]: If HwameiStor has been deployed, and the above configuration modification is performed later, then **will not take effect on the previously created data volume**, that is, the previous network card will be used for data volume synchronization.
    - If you need to modify the storage network cards of multiple nodes, please configure them one by one. Currently, batch configuration is not possible

## Prerequisites

The storage NIC planning has been completed in advance, please refer to [Network Card Planning](../../../network/plans/ethplan.md).

## Steps

You can use two methods to configure it:

1. Configuration via LocalStorage CR
2. Mark by node annotation

### Modify LocalStorage CR configuration

1. On the left navigation bar, click `Container Management` —> `Cluster List`, find the `Cluster whose NIC configuration needs to be modified`, and enter the cluster details.

2. Select `Custom Resources` in the left navigation bar, find `localdisknodes.hwameistor.io`, and click to enter the details.


3. Find the `node to be modified` and click `Edit YAML` to modify `storage-ipv4=172.30.40.12` parameter in `spec`,
    Specify the IP address as the planned network card IP [network card plan](../../../network/plans/ethplan.md).
    

4. Click `Save` when finished, and select the next node to modify.

### via node comment markup

1. View the value of ENV: **NODE_ANNOTATION_KEY_STORAGE_IPV4** of local-storage, the default is
    **[localstorage.hwameistor.io/storage-ipv4](http://localstorage.hwameistor.io/storage-ipv4)**

2. Mark the **storage network card address on the node by comment**

    ```sh
    kubectl annotate node <your_storage_node> localstorage.hwameistor.io``/storage-ipv4``=172.30.46.12
    ```

3. **Restart** the local-storage service on the node

4. **Verify** whether the configuration is effective

    ```sh
    kubectl get lsn <your_storage_node> -o yaml |``grep`` -i storageIP
    ```

5. After the modification is successful, proceed to the next node modification.