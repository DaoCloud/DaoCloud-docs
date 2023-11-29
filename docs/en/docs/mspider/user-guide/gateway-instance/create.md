---
hide:
  - toc
---

# Managing Mesh Gateways

The Mesh Gateway module provides lifecycle management for Mesh Gateway instances, including creation, update, and deletion. Users can use this page to manage all the managed Gateway instances within the current mesh.

Mesh Gateways are divided into two categories: Ingress and Egress.

* Ingress Gateways are used to define the traffic entry points for applications within the service mesh. All incoming traffic to applications within the service mesh should go through the Ingress Gateway.
* Egress Gateways are used to define the traffic exit points for applications within the mesh. They allow traffic from external services to flow through the Egress Gateway, enabling more precise traffic control.

Gateway instances run Envoy, similar to sidecars, but gateways run as separate instances.

## Create a Mesh Gateway

The steps to create a Mesh Gateway are as follows.

1. Click `mesh Gateway` in the left navigation bar to enter the gateway list, and click the `Create` button in the upper right corner.

    

2. In the `Create mesh Gateway` window, follow the prompts to configure parameters, which are basically required. After checking the configuration information is correct, click `OK`.

    

3. Return to the mesh gateway list, and the upper right corner of the screen will prompt that the creation is successful. The status of the newly created mesh gateway is `creating`.

    

4. Refresh the page after a few seconds, and the status will change to `Running`, indicating that the gateway is successfully configured. Click `...` on the right side of the list to perform edit and delete operations.

    

!!! info

    For a more intuitive operation demonstration, please refer to [Video Tutorial](../../../videos/mspider.md).
