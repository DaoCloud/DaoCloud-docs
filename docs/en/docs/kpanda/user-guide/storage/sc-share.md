# shared StorageClass

The DCE 5.0 container management module supports sharing a StorageClass with multiple namespaces to improve resource utilization efficiency.

1. Find the StorageClass that needs to be shared in the StorageClass list, and click `Authorize Namespace` under the operation bar on the right.

    

2. Click `Custom Namespace` to select which namespaces this StorageClass needs to be shared to one by one.

    - Click `Authorize All Namespaces` to share this StorageClass to all namespaces under the current cluster at one time.
    - Click `Remove Authorization` under the operation bar on the right side of the list to deauthorize and stop sharing this StorageClass to this namespace.

        