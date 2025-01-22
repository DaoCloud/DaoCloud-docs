---
MTPE: WANG0608GitHub
Date: 2024-08-27
---

# Manage Edge Units

## View Edge Unit Status

**Edge Units Status List:**

- Executing: The edge unit is being created or the edge unit information is being updated. During this time, the edge unit name cannot be clicked, and edge unit operations cannot be accessed.
- Running: The edge unit is running normally.
- Failed: The edge unit creation has failed or there is an abnormality in the operation. Hover over the icon on the right to view the error information.
- Deleting: The edge unit is being deleted. During this process, the edge unit name, edit, and delete buttons cannot be clicked.
- Pending: The edge unit is waiting to be created or updated.

**Edge Unit Resource Statistics:**

- Normal/Total Nodes: Number of nodes with a healthy status / Total number of nodes.
- Normal/Total Instances: Number of workloads running normally / Total number of workloads.

![Edge Unit List](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kant/user-guide/images/manage-unit-01.png)

## Edit Edge Units

On the right side of the edge unit list, click the __┇__ button and select __Edit__ from the pop-up menu. This allows you to edit the basic information, component repo and network config of the edge unit.

![Edit Edge Unit](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kant/user-guide/images/manage-unit-02.png)

## Delete Edge Units

On the right side of the edge unit list, click the __┇__ button and select __Delete__ from the pop-up menu.

!!! note

    - When deleting an edge unit, the system will automatically delete the end device, message endpoints, and message routes under the edge unit.
    - If there are created edge nodes and workloads under the edge unit, you need to manually delete them first.
    - By clicking the edge nodes and workloads, you can quickly navigate to the edge node list and workload list pages.

![Delete Edge Unit](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kant/user-guide/images/manage-unit-03.png)

## Edge Unit Overview

Click the Edge Unit name in the list to go to the overview page, where you can view basic information
and resource status. For more management operations, click the corresponding menu in the left sidebar.

![Edge Unit Overview](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kant/user-guide/images/manage-unit-04.png)
