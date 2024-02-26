# Manage Edge Nodes

After successfully connecting and managing edge nodes, the platform provides the ability to perform scheduling pause and node removal operations on these nodes.

## Scheduling Pause

Use case: When maintenance operations need to be performed on a node, you can choose to pause the scheduling of the node. During the scheduling pause, workloads will not be deployed to this node.

> Note: Workloads that have already been deployed on the node will not be affected and will continue to run normally.

The steps to pause scheduling are as follows:

1. Go to the details page of the edge unit and select the left-side menu __Edge Resources__ -> __Edge Nodes__ .

2. Click the __Pause Scheduling__ button on the right side of the node list. A prompt will appear indicating the successful issuance of the scheduling pause task. Click the refresh icon later, and the node status will change to "Healthy/Scheduling Paused".

    ![Pause Scheduling](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kant/images/node-manage-01.png)

3. If you need to resume scheduling, click the __Resume Scheduling__ button on the right side of the list. A prompt will appear indicating the successful issuance of the scheduling resume task. Click the refresh icon later, and the node status will change to "Healthy/Schedulable".

## Node Removal

The steps to remove a node are as follows:

1. Go to the details page of the edge unit and select the left-side menu __Edge Resources__ -> __Edge Nodes__ .

2. Click the __Remove__ button on the right side of the node list, and a confirmation dialog box will appear.

    ![Remove Node](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kant/images/node-manage-02.png)

3. Manually unbind the workloads and end device resources. If the resources on the node have already been cleared, you can skip this step.

    1. Click the __Workloads__ button in the dialog box to go to the workloads list page.

    2. Find the workloads on the node and delete them one by one.

    3. Click the __End Device__ button in the dialog box to go to the end device list page.

    4. Find the end device bound to the node and unbind them.

4. Enter the node name in the input box and click the __Delete__ button to complete the node removal process.
