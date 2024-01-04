# Manage Edge Units

## View Edge Unit Status

**Edge Units Status List:**

- Creating: The edge unit is being created, and the edit and delete buttons are disabled.
- Running: The edge unit has been successfully created and is running normally.
- Failed: The edge unit failed to create or encountered an error during runtime. Hover over the icon on the right to view the error information.
- Updating: The edge unit is being edited and updated, and the edit and delete buttons are disabled.
- Deleting: The edge unit is being deleted, and the edit and delete buttons are disabled.

**Edge Unit Resource Statistics:**

- Normal/Total Nodes: The number of nodes in a normal state out of the total number of nodes.
- Normal/Total Instances: The number of running instances out of the total number of instances in the workload.

![Edge Unit List](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kant/user-guide/images/manage-unit-01.png)

## Edit Edge Units

On the right side of the edge unit list, click the `⋮` button and select `Edit` from the pop-up menu. This allows you to edit the basic information, component repo and network config of the edge unit.

![Edit Edge Unit](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kant/user-guide/images/manage-unit-02.png)

## Delete Edge Units

On the right side of the edge unit list, click the `⋮` button and select `Delete` from the pop-up menu.

!!! note

    - When deleting an edge unit, the system will automatically delete the end device, message endpoints, and message routes under the edge unit.
    - If there are created edge nodes and workloads under the edge unit, you need to manually delete them first.
    - By clicking on the edge nodes and workloads, you can quickly navigate to the edge node list and workload list pages.

![Delete Edge Unit](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kant/user-guide/images/manage-unit-03.png)

## Edge Unit Overview

Click the Edge Unit name in the list to go to the overview page, where you can view basic information and resource status. For more management operations, click the corresponding menu in the left sidebar.

![Edge Unit Overview](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kant/user-guide/images/manage-unit-04.png)
