# Deploy Harbor through LoadBalancer mode

Currently, DCE 5.0 image repository does not support deploying Harbor using LoadBalancer mode.
It only supports Ingress and NodePort modes.
This document briefly explains how to manually change the access type to LB.

## 1. Create a NodePort Harbor service

First, [create a managed Harbor](../managed/harbor.md) and create a Harbor service with
the access mode set to NodePort.

<!-- ![nodeport](../images/nodeport.png) -->

## 2. Create a LoadBalancer SVC resource

In the **Container Network** -> **Services** of the cluster where Harbor is located,
create an LB-type SVC resource.

!!! note

    When creating an LB-type SVC resource, the labels need to match the labels of the
    nginx SVC and be created in the same namespace.

After creating the Harbor service, an nginx SVC resource will automatically appear in the
**Container Network** -> **Services** of the cluster where Harbor is located.
In the service list, click the **⋮** button on the right side, and select **Update** in
the dropdown menu to view the label information of nginx.

<!-- ![nginx](../images/nginx.png)

![nginxlabel](../images/nginxlabel.png) -->

## 3. Modify the harborclusters.goharbor.io CR

Modify the externalUrl field in the harborclusters.goharbor.io CR to the IP address of the LB.

### Modify with UI

1. Search for harborclusters.goharbor.io in the Custom Resource List.

    <!-- ![crdlist](../images/crdlist.png) -->

2. Click the name to enter the details, select API version **v1beta1**, and save after modifying the API version.

   <!-- ![crddetail](../images/crddetail.png) -->

### Modify with CLI

Run the following command in the proper cluster:

```bash
kubectl edit harborclusters.goharbor.io
```
