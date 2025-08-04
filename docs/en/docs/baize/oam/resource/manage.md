# Manage Resource Pools

AI Lab allows you to **update** or **delete** resource pools.

## Update

!!! note

    If a resource pool is configured with node topology, it cannot be updated.
    To modify such a resource pool, please create a new one instead.

Steps:

1. In the resource pool list, click the **┇** menu on the right side of the target pool, then select **Update** from the dropdown.

    <!-- ![Update](../../images/udpdate-resource-01.png) -->

2. On the update page, modify the configuration parameters as needed. When finished, click **Confirm**. The system will automatically return to the resource pool list.

    <!-- ![Confirm](./../images/udpdate-resource-02.png) -->

## Delete

!!! caution

    If the resource pool is currently bound to a queue that has running workloads, proceed with caution before deleting.

Steps:

1. In the resource pool list, click the **┇** menu on the right side of the target pool, then select **Delete** from the dropdown.

    <!-- ![Delete](../../images/deleate-resource-01.png) -->

2. In the confirmation dialog, click **Delete** to confirm.

    <!-- ![Confirm Deletion](../../images/deleate-resource-02.png) -->

3. Once the deletion is successful, a confirmation message appears and the resource pool is removed from the list.
