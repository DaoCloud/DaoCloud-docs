# Manually Switch MySQL Primary/Standby Nodes

The manual primary/standby switchover feature of MySQL allows database administrators to manually promote a standby server to the new primary server when the primary server fails or requires maintenance.
By executing the appropriate commands and configuration, data consistency and service continuity are ensured, thereby achieving high availability.

## Notes

1. Ensure data consistency between the primary and standby nodes to avoid data loss or inconsistency during the switchover.
2. Before the switchover, confirm that the instance is in the __Running__ state.

## Steps

1. Click to enter the details page of the target MySQL instance.
2. In the upper right corner of the overview page, click **Switch Primary/Standby**.
3. Expand the drop-down list of standby nodes to specify the standby node to be promoted to the primary node.

![mysql-switch-role](../images/change-role.png){: width=1000px}
