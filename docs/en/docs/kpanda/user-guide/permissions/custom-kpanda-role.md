---
MTPE: ModetaNiu
Date: 2024-05-30
---

# Adding RBAC Rules to System Roles

*[kpanda]: A development codename for container management
   
In the past, the RBAC rules for those system roles in container management were pre-defined and could 
not be modified by users.
To support more flexible permission settings and to meet the customized needs for system roles,
now you can modify RBAC rules for system roles such as cluster admin, ns admin, ns editor, ns viewer.

The following example demonstrates how to add a new ns-view rule, granting the authority to delete 
workload deployments. Similar operations can be performed for other rules.

## Prerequisites

Before adding RBAC rules to system roles, the following prerequisites must be met:

- Container management version v0.27.0 and above.
- [Integrated Kubernetes cluster](../clusters/integrate-cluster.md) or
  [created Kubernetes cluster](../clusters/create-cluster.md), and able to access the cluster's UI interface.
- Completed creation of a [namespace](../namespaces/createns.md) and [user account](../../../ghippo/user-guide/access-control/user.md), 
  and the granting of [NS Viewer](./permission-brief.md#ns-viewer).
  For details, refer to [namespace authorization](./cluster-ns-auth.md).


!!! note

    - RBAC rules **only need to be added** in the Global Cluster, and the Kpanda controller will synchronize 
      those added rules to all integrated subclusters. Synchronization may take some time to complete.
    - RBAC rules **can only be added** in the Global Cluster. RBAC rules added in subclusters 
      will be overridden by the system role permissions of the Global Cluster.
    - Only ClusterRoles with fixed Label are supported for adding rules. Replacing or deleting rules 
      is not supported, nor is adding rules by using role. The correspondence between built-in roles and 
      ClusterRole Label created by users is as follows.

        ```output
        cluster-admin: rbac.kpanda.io/role-template-cluster-admin: "true"
        cluster-edit: rbac.kpanda.io/role-template-cluster-edit: "true"
        cluster-view: rbac.kpanda.io/role-template-cluster-view: "true"
        ns-admin: rbac.kpanda.io/role-template-ns-admin: "true"
        ns-edit: rbac.kpanda.io/role-template-ns-edit: "true"
        ns-view: rbac.kpanda.io/role-template-ns-view: "true"
        ```

## Steps

1. [Create a deployment](../workloads/create-deployment.md) by a user with `admin` or `cluster admin` permissions.

    ![image-20240514112742395](../images/create-depolyment.png)

1. Grant a user the `ns-viewer` role to provide them with the `ns-view` permission.
  
    ![image-20240514113009311](../images/permisson02.png)

1. Switch the login user to ns-viewer, open the console to get the token for the ns-viewer user, 
   and use `curl` to request and delete the nginx deployment mentioned above. However,
   a prompt appears as below, indicating the user doesn't have permission to delete it.
  
    ```bash
    [root@master-01 ~]# curl -k -X DELETE  'https://${URL}/apis/kpanda.io/v1alpha1/clusters/cluster-member/namespaces/default/deployments/nginx' -H 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJOU044MG9BclBRMzUwZ2VVU2ZyNy1xMEREVWY4MmEtZmJqR05uRE1sd1lFIn0.eyJleHAiOjE3MTU3NjY1NzksImlhdCI6MTcxNTY4MDE3OSwiYXV0aF90aW1lIjoxNzE1NjgwMTc3LCJqdGkiOiIxZjI3MzJlNC1jYjFhLTQ4OTktYjBiZC1iN2IxZWY1MzAxNDEiLCJpc3MiOiJodHRwczovLzEwLjYuMjAxLjIwMTozMDE0Ny9hdXRoL3JlYWxtcy9naGlwcG8iLCJhdWQiOiJfX2ludGVybmFsLWdoaXBwbyIsInN1YiI6ImMxZmMxM2ViLTAwZGUtNDFiYS05ZTllLWE5OGU2OGM0MmVmMCIsInR5cCI6IklEIiwiYXpwIjoiX19pbnRlcm5hbC1naGlwcG8iLCJzZXNzaW9uX3N0YXRlIjoiMGJjZWRjZTctMTliYS00NmU1LTkwYmUtOTliMWY2MWEyNzI0IiwiYXRfaGFzaCI6IlJhTHoyQjlKQ2FNc1RrbGVMR3V6blEiLCJhY3IiOiIwIiwic2lkIjoiMGJjZWRjZTctMTliYS00NmU1LTkwYmUtOTliMWY2MWEyNzI0IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJncm91cHMiOltdLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJucy12aWV3ZXIiLCJsb2NhbGUiOiIifQ.As2ipMjfvzvgONAGlc9RnqOd3zMwAj82VXlcqcR74ZK9tAq3Q4ruQ1a6WuIfqiq8Kq4F77ljwwzYUuunfBli2zhU2II8zyxVhLoCEBu4pBVBd_oJyUycXuNa6HfQGnl36E1M7-_QG8b-_T51wFxxVb5b7SEDE1AvIf54NAlAr-rhDmGRdOK1c9CohQcS00ab52MD3IPiFFZ8_Iljnii-RpXKZoTjdcULJVn_uZNk_SzSUK-7MVWmPBK15m6sNktOMSf0pCObKWRqHd15JSe-2aA2PKBo1jBH3tHbOgZyMPdsLI0QdmEnKB5FiiOeMpwn_oHnT6IjT-BZlB18VkW8rA'
    {"code":7,"message":"[RBAC] delete resources(deployments: nginx) is forbidden for user(ns-viewer) in cluster(cluster-member)","details":[]}[root@master-01 ~]#
    [root@master-01 ~]#
    ```

1. Create a ClusterRole on the global cluster, as shown in the yaml below.

    ```yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: append-ns-view # (1)!
      labels:
        rbac.kpanda.io/role-template-ns-view: "true" # (2)!
    rules:
      - apiGroups: [ "apps" ]
        resources: [ "deployments" ]
        verbs: [ "delete" ]
    ```

    1. This field value can be arbitrarily specified, as long as it is not duplicated and complies with 
       the Kubernetes resource naming conventions.
    2. When adding rules to different roles, make sure to apply different labels.

1. Wait for the kpanda controller to add a rule of user creation to the built-in role: ns-viewer,  
   then you can check if the rules added in the previous step are present for ns-viewer. 

    ```bash
    [root@master-01 ~]# kubectl get clusterrole role-template-ns-view -oyaml|grep deployments -C 10|tail -n 6
    ```
    ```yaml
    - apiGroups:
      - apps
      resources:
      - deployments
      verbs:
      - delete
    ```

1. When using curl again to request the deletion of the aforementioned nginx deployment, this time the deletion 
   was successful. This means that ns-viewer has successfully added the rule to delete deployments.

    ```bash
    [root@master-01 ~]# curl -k -X DELETE  'https://${URL}/apis/kpanda.io/v1alpha1/clusters/cluster-member/namespaces/default/deployments/nginx' -H 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJOU044MG9BclBRMzUwZ2VVU2ZyNy1xMEREVWY4MmEtZmJqR05uRE1sd1lFIn0.eyJleHAiOjE3MTU3NjY1NzksImlhdCI6MTcxNTY4MDE3OSwiYXV0aF90aW1lIjoxNzE1NjgwMTc3LCJqdGkiOiIxZjI3MzJlNC1jYjFhLTQ4OTktYjBiZC1iN2IxZWY1MzAxNDEiLCJpc3MiOiJodHRwczovLzEwLjYuMjAxLjIwMTozMDE0Ny9hdXRoL3JlYWxtcy9naGlwcG8iLCJhdWQiOiJfX2ludGVybmFsLWdoaXBwbyIsInN1YiI6ImMxZmMxM2ViLTAwZGUtNDFiYS05ZTllLWE5OGU2OGM0MmVmMCIsInR5cCI6IklEIiwiYXpwIjoiX19pbnRlcm5hbC1naGlwcG8iLCJzZXNzaW9uX3N0YXRlIjoiMGJjZWRjZTctMTliYS00NmU1LTkwYmUtOTliMWY2MWEyNzI0IiwiYXRfaGFzaCI6IlJhTHoyQjlKQ2FNc1RrbGVMR3V6blEiLCJhY3IiOiIwIiwic2lkIjoiMGJjZWRjZTctMTliYS00NmU1LTkwYmUtOTliMWY2MWEyNzI0IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJncm91cHMiOltdLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJucy12aWV3ZXIiLCJsb2NhbGUiOiIifQ.As2ipMjfvzvgONAGlc9RnqOd3zMwAj82VXlcqcR74ZK9tAq3Q4ruQ1a6WuIfqiq8Kq4F77ljwwzYUuunfBli2zhU2II8zyxVhLoCEBu4pBVBd_oJyUycXuNa6HfQGnl36E1M7-_QG8b-_T51wFxxVb5b7SEDE1AvIf54NAlAr-rhDmGRdOK1c9CohQcS00ab52MD3IPiFFZ8_Iljnii-RpXKZoTjdcULJVn_uZNk_SzSUK-7MVWmPBK15m6sNktOMSf0pCObKWRqHd15JSe-2aA2PKBo1jBH3tHbOgZyMPdsLI0QdmEnKB5FiiOeMpwn_oHnT6IjT-BZlB18VkW8rA'
    ```
