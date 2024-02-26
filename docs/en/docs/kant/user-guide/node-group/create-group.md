# Create Edge Node Group

In edge computing scenarios, edge nodes are typically distributed in different geographical regions, each with its own differences in computing resources, network structures, and hardware platforms. Based on the geographical distribution of edge nodes, it is possible to group edge nodes from the same region together and organize them as a node group. Each node can only belong to one node group at a time.

Deploying edge applications to node groups improves operational efficiency for cross-regional application deployment.

The following steps explain how to create an edge node group.

1. Go to the edge unit details page and select the left-side menu __Edge Resources__ -> __Node Groups__ .

2. Click the __Create Node Group__ button at the top right of the node group list.

    ![Create Node Group](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kant/user-guide/images/create-group-01.png)

3. Fill in the relevant parameters.

    - Group Name: A combination of lowercase letters, numbers, hyphens (-), and dots (.), and it should not have consecutive separators. It should start and end with a letter or number. contains a maximum of 253 characters.
    - Description: Description information for the node group.
    - Node Selection Method: Nodes in the edge node group can be specified by selecting multiple nodes or matching with a label selector. Both methods can be used simultaneously.

    ![Fill Basic Info](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kant/user-guide/images/create-group-02.png)

4. Click the __OK__ button to successfully create the edge node group and return to the edge node group list.

Next step: [Manage Edge Node Groups](manage-group.md)
