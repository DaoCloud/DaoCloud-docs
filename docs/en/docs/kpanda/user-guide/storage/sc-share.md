# shared storage pool

The DCE 5.0 container management module supports sharing a storage pool with multiple namespaces to improve resource utilization efficiency.

1. Find the storage pool that needs to be shared in the storage pool list, and click `Authorize Namespace` under the operation bar on the right.

    

2. Click `Custom Namespace` to select which namespaces this storage pool needs to be shared to one by one.

    - Click `Authorize All Namespaces` to share this storage pool to all namespaces under the current cluster at one time.
    - Click `Remove Authorization` under the operation bar on the right side of the list to deauthorize and stop sharing this storage pool to this namespace.

        