# Manually Switch Redis Primary/Standby

In the Redis cache service, manually switching the primary/standby roles ensures continuous system operation when the primary node fails or requires maintenance.
This article describes how to manually switch the primary/standby roles of Redis through the UI, and discusses the use cases and limitations.

## Use Cases

1. **Failure recovery:** When the primary node fails, the standby node can be promoted to the new primary node to ensure service continuity.
2. **Load balancing:** Under high load, switching the primary/standby roles can distribute requests and improve the response capability of the system.
3. **Test environment:** In development and test environments, manually switching the primary/standby roles helps developers verify the fault tolerance and data consistency of the system.

## Cluster Mode

1. Click the name of the target Redis instance to enter its details page.
2. In the Pod list of the instance that requires a primary/standby switchover, click the icon in front of the shard name to expand all nodes under the current shard.
3. To switch the primary/standby roles of the nodes in a shard, click the **Switch Primary/Standby** icon after the shard to promote the standby node to the primary node.

    ![switch-role](../images/switch-role.png){: width=}

4. Expand the drop-down list of standby nodes to specify the standby node to be promoted to the primary node.

    ![switch-role](../images/switch-role-1.png)

## Sentinel Mode

1. Click the name of the target Redis instance to enter its details page.
2. In the upper right corner of the overview page, click **Switch Primary/Standby**.

    ![switch-role](../images/switch-role-2.png)

3. Expand the drop-down list of standby nodes to specify the standby node to be promoted to the primary node.

    ![switch-role](../images/switch-role-3.png)
