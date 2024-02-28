# Multicloud Network Interconnection

Multicloud Network Interconnection is a set of solutions provided in the multicluster mode when the networks between the multiclusters are not connected to each other (Pods cannot directly establish communication). It can quickly connect the networks of multiple clusters to realize cross-cluster Pods visit each other.

## Use cases

If your environment meets the following conditions, you can try to use the Multicloud Network Interconnection function:

1. Multiple clusters on the same mesh
2. Pod networks in multiple clusters cannot be directly connected (including Pod CIDR conflicts, etc.)

!!! note

     Multicloud networking is only available for hosted meshs.

## Glossary

- Network grouping:
     - Used to identify network topology relationships of clusters within the mesh.
     - If the networks of some clusters can directly communicate with each other (the Pod IPs across clusters do not conflict and can be directly connected), then these clusters should be placed in one network group, otherwise they will belong to different network groups.
     - Network CNI implementation types for network grouping and clustering are not explicitly related.
- East-West Gateway:
     - It is used for communication and interconnection between different network groups, and multiple network groups can be created in one network group.
     - Users can create east-west gateways in any cluster under the network group. When the cluster is moved to another network group, the east-west gateway will also be migrated.
     - The load balancing IP used by the east-west gateway is usually automatically assigned by the cloud platform where the cluster is located, or it can be configured by the user.
- Basic settings: Create a __Gateway Rule__ configuration for the east-west gateway, which will open port 15443 for communication between network groups. Users can view the detailed content of the CRD file in the __Gateway Rule__ list, but it is not recommended to modify it. May cause network communication failure.
- List of network groups:
     - Display the currently created network group and the information of clusters and east-west gateways under the group;
     - Under this list, users can add and delete network groups, clusters under groups, and east-west gateways, and migrate clusters between network groups.
- Interconnect list:
     - A network group that contains at least one east-west gateway can be added to the interconnection list, and the network group that joins the interconnection can communicate with other network groups.
     - The load balancing IP can be modified for network groups that have joined the interconnection, but if you need to modify other configurations (such as adding or deleting clusters, east-west gateways), you need to remove the __Network Group Interconnection__ list first.
     - Adding and removing interconnections will cause the restart of the mesh control plane, so it is recommended to proceed with caution.

## Operating procedures

The recommended operation process is shown in the figure below


## Steps

1. Enter a certain mesh, click the enable switch, and a __gateway rule__ for the east-west gateway will be automatically created. Click the __Create Network Group__ button to add at least one cluster to the network group.


1. Fill in a name for the network group and add at least one cluster.

     !!! note

         The network group name cannot be modified after it is created.

1. Add and delete clusters.

     After creating a network group, you can add more clusters to the group. The clusters in the same group must be of the same network type and can communicate with each other, otherwise the interconnection may fail.


     After the addition is complete, you can see multiple clusters under the network group.


     !!! note

         At least one cluster must be kept in the network group. To remove all clusters, please delete the network group.

1. Create/delete east-west gateway.

     The east-west gateway is used for communication between network groups, and one or more gateways can be created on any cluster in the group. Click __⋮__ to the right of a cluster and select __Edit East-West Gateway__ :


     Create configuration items as follows:

     - __Load balancing comment__ is an optional setting, and some cloud platforms will provide load balancing IP allocation in the form of comments, please refer to the technical documentation provided by the cloud platform;
     - __Number of East-West Gateway Replicas__ defaults to 1, if you need to improve the availability of the gateway, you can create multiple copies; click __OK__ ;


         Select an east-west gateway and click __Delete East-West Gateway__ in the operation to delete the gateway, as shown in the figure:


     !!! note

         Each network group needs to create at least one east-west gateway, otherwise it cannot join the interconnection.

1. Network packet interconnection

     1. If you want to add a network group to the interconnection, click the __Join interconnection__ button.

     1. Check a network group and click __Next__ .

     1. Select an available __East-West Gateway Address__ and click __OK__ .

     1. You can see the newly added network group in the interconnection list, and the groups in the list have established communication with each other.

     !!! note

         - A network group without an east-west gateway cannot join the interconnection
         - Joining the group interconnection operation will cause the mesh control plane to restart. It is recommended to ensure that the network group configuration is correct before joining the interconnection

## Other operations

1. Update the east-west gateway address.

     Users can add or delete east-west gateway addresses for network groups in the interconnected state. Check a group in the interconnection list, and click __Update East-West Gateway Address__ .

     Click __OK__ after updating the address.

1. Remove the Internet

     If the network group no longer needs to establish interconnection with other network groups, or needs to adjust the cluster and east-west gateway settings in the group, the interconnection can be removed.
     Select the network group to be removed, click the __Remove Interconnection__ button, and the following dialog box will appear.

     After the second confirmation, the network group can be removed from the interconnection list.

1. Delete network group

     Click __Delete Network Group__ in the operation drop-down box of the network group to be deleted to delete the selected network group.

1. Disable __Multicloud Network Interconnection__ function

     In the "Basic Settings" area at the top, click the slider of the "Enabled" state, and the prerequisites for disabling multicloud interconnection will pop up:


     First remove the network group:

     Enter __Close Basic Settings__ in the text box to confirm, and you can turn off the multicloud interconnection function:
