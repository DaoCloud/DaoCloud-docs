---
hide:
   - toc
---

# Create the external mesh

External mesh means that the existing mesh of the enterprise can be connected to the DCE 5.0 service mesh for unified management.

1. In the upper right corner of the service mesh list page, click `Create mesh`.

1. Select `External mesh`, fill in the basic information of the mesh and click `Next`.

     - mesh name: start with a lowercase letter, consist of lowercase letters, numbers, dashes (-), and cannot end with a dash (-)
     - Cluster: The cluster used to run the mesh management plane, the list contains the clusters that the current mesh platform can access and are in normal state.
       Click `Create Cluster` to jump to `Container Management` to create a new cluster. After the creation is complete, return to this page and click the refresh icon to update the list.
     - Istio root namespace: The Istio root namespace where the mesh resides.
     - mesh component repository: Enter the URL address of the mirror repository.
  

1. System settings. After setting observability and mesh size, click `Next`.


1. Governance settings. Set outbound traffic policies, location-aware load balancing, request retries, and more.


1. Sidecar setup. After setting the global sidecar, resource limit, and log, click `OK`.


1. Automatically return to the mesh list, the newly created mesh is at the first place by default, and the status will change from `creating` to `running` after a period of time. Click `...` on the right to perform operations such as editing and deleting.


Next step: [Service Management](../service-list/README.md)