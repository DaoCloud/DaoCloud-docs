# Managing Edge Units

## Viewing Edge Unit Status

**Edge units have the following statuses:**

- Creating: The edge unit is being created, and the edit and delete buttons are disabled.
- Running: The edge unit has been successfully created and is running normally.
- Failed: The edge unit failed to create or encountered an error during runtime. Hover over the icon on the right to view the error information.
- Updating: The edge unit is being edited and updated, and the edit and delete buttons are disabled.
- Deleting: The edge unit is being deleted, and the edit and delete buttons are disabled.

**Edge Unit Resource Statistics:**

- Healthy Nodes/Total Nodes: The number of nodes in a healthy state out of the total number of nodes.
- Normal Application Instances/Total Instances: The number of running application instances out of the total number of instances in the workload.

## Editing Edge Units

On the right side of the edge unit list, click the `⋮` button and select `Edit` from the pop-up menu. This allows you to edit the basic information, component repository settings, and access settings of the edge unit.

## Deleting Edge Units

On the right side of the edge unit list, click the `⋮` button and select `Delete` from the pop-up menu.

!!! note

    - When deleting an edge unit, the system will automatically delete the end device, message endpoints, and message routes under the edge unit.
    - If there are created edge nodes and workloads under the edge unit, you need to manually delete them first.
    - By clicking on the edge nodes and workloads, you can quickly navigate to the edge node list and workload list pages.

## Edge Unit Overview

Click the `Edge Unit Name` in the list to go to the edge unit overview page, where you can view basic information and resource status information. For more management operations, click the corresponding menu in the left sidebar.
