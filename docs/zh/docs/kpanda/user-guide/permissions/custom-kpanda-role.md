# 增加 kpanda 内置角色权限点

*[kpanda]: 容器管理的开发代号

kpanda 内置角色的权限点（rbac rules）都是提前预定义好的且用户无法修改，因为修改内置角色的权限点之后也被 kpanda 控制器还原成预定义权限点。
为了支持更加灵活的权限配置，满足对系统角色的自定义需求，kpanda 支持为内置系统角色（cluster admin、ns admin、ns edit、ns view）修改权限点。
以下示例演示如何新增 ns-view 权限点，增加可以删除工作负载 deployment 的权限。其他权限点操作类似。

## 前提条件

- 容器管理模块[已接入 Kubernetes 集群](https://docs.daocloud.io/kpanda/user-guide/clusters/integrate-cluster.html)或者[已创建 Kubernetes 集群](https://docs.daocloud.io/kpanda/user-guide/clusters/create-cluster.html)，且能够访问集群的 UI 界面。
- 已完成一个[命名空间的创建](https://docs.daocloud.io/kpanda/user-guide/namespaces/createns.html)、[用户的创建](https://docs.daocloud.io/ghippo/user-guide/access-control/user.html)，并为用户授予 [NS View](https://docs.daocloud.io/kpanda/user-guide/permissions/permission-brief.html#ns-admin) ，详情可参考[命名空间授权](https://docs.daocloud.io/kpanda/user-guide/permissions/cluster-ns-auth.html)。

### 说明

- 只需在 Global Cluster 增加权限点即可，kpanda 控制器会把 Global Cluster 增加的权限点同步到所有接入子集群中，同步需一段时间才能完成

- 只能在 Global Cluster 增加权限点，在子集群新增的权限点会被 Global Cluster 内置角色权限点覆盖

- 只支持使用固定 labels 的 ClusterRoles 追加权限，不支持替换或者删除权限，也不能使用 role 追加权限，内置角色跟用户创建的 clusterrole labels 对应关系如下

    ```output
    cluster-admin: rbac.kpanda.io/role-template-cluster-admin: "true"
    cluster-edit: rbac.kpanda.io/role-template-cluster-edit: "true"
    cluster-view: rbac.kpanda.io/role-template-cluster-view: "true"
    ns-admin: rbac.kpanda.io/role-template-ns-admin: "true"
    ns-edit: rbac.kpanda.io/role-template-ns-edit: "true"
    ns-view: rbac.kpanda.io/role-template-ns-view: "true"
    ```

## 操作步骤

1. 使用 admin 或者 cluster admin 权限的用户[创建无状态负载](https://docs.daocloud.io/kpanda/user-guide/workloads/create-deployment.html)

    ![image-20240514112742395](../images/create-depolyment.png)

1. 授权 ns-viewer，用户有该 namespace ns-view 权限
  
    ![image-20240514113009311](../images/permisson02.png)

1. 切换登陆用户为 ns-viewer，打开控制太获取 ns-viewer 用户对应的 token，使用 curl 请求去删除上述的 deployment nginx，发现无删除权限
  
    ```bash
    [root@master-01 ~]# curl -k -X DELETE  'https://${URL}/apis/kpanda.io/v1alpha1/clusters/cluster-member/namespaces/default/deployments/nginx' -H 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJOU044MG9BclBRMzUwZ2VVU2ZyNy1xMEREVWY4MmEtZmJqR05uRE1sd1lFIn0.eyJleHAiOjE3MTU3NjY1NzksImlhdCI6MTcxNTY4MDE3OSwiYXV0aF90aW1lIjoxNzE1NjgwMTc3LCJqdGkiOiIxZjI3MzJlNC1jYjFhLTQ4OTktYjBiZC1iN2IxZWY1MzAxNDEiLCJpc3MiOiJodHRwczovLzEwLjYuMjAxLjIwMTozMDE0Ny9hdXRoL3JlYWxtcy9naGlwcG8iLCJhdWQiOiJfX2ludGVybmFsLWdoaXBwbyIsInN1YiI6ImMxZmMxM2ViLTAwZGUtNDFiYS05ZTllLWE5OGU2OGM0MmVmMCIsInR5cCI6IklEIiwiYXpwIjoiX19pbnRlcm5hbC1naGlwcG8iLCJzZXNzaW9uX3N0YXRlIjoiMGJjZWRjZTctMTliYS00NmU1LTkwYmUtOTliMWY2MWEyNzI0IiwiYXRfaGFzaCI6IlJhTHoyQjlKQ2FNc1RrbGVMR3V6blEiLCJhY3IiOiIwIiwic2lkIjoiMGJjZWRjZTctMTliYS00NmU1LTkwYmUtOTliMWY2MWEyNzI0IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJncm91cHMiOltdLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJucy12aWV3ZXIiLCJsb2NhbGUiOiIifQ.As2ipMjfvzvgONAGlc9RnqOd3zMwAj82VXlcqcR74ZK9tAq3Q4ruQ1a6WuIfqiq8Kq4F77ljwwzYUuunfBli2zhU2II8zyxVhLoCEBu4pBVBd_oJyUycXuNa6HfQGnl36E1M7-_QG8b-_T51wFxxVb5b7SEDE1AvIf54NAlAr-rhDmGRdOK1c9CohQcS00ab52MD3IPiFFZ8_Iljnii-RpXKZoTjdcULJVn_uZNk_SzSUK-7MVWmPBK15m6sNktOMSf0pCObKWRqHd15JSe-2aA2PKBo1jBH3tHbOgZyMPdsLI0QdmEnKB5FiiOeMpwn_oHnT6IjT-BZlB18VkW8rA'
    {"code":7,"message":"[RBAC] delete resources(deployments: nginx) is forbidden for user(ns-viewer) in cluster(cluster-member)","details":[]}[root@master-01 ~]#
    [root@master-01 ~]#
    ```

1. 在 global 集群上创建如下 cluster role，yaml 如下所示

    ```yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: append-ns-view # name 可任意指定，不重复且符合 kubernetes 资源名称规则要求即可
      labels:
        rbac.kpanda.io/role-template-ns-view: "true" # 注意给不同的角色添加权限时 label 不同,不同角色跟label 对应关系如下 
    rules:
      - apiGroups: [ "apps" ]
        resources: [ "deployments" ]
        verbs: [ "delete" ]
    ```

1. 等待 kpanda 控制器添加用户创建权限到内置角色中 ns-view 中，可查看对应内置角色如是否有上一步新增的 rules

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

1. 再次使用 curl 请求删除上诉的 deployment nginx，可成功删除

    ```bash
    [root@master-01 ~]# curl -k -X DELETE  'https://${URL}/apis/kpanda.io/v1alpha1/clusters/cluster-member/namespaces/default/deployments/nginx' -H 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJOU044MG9BclBRMzUwZ2VVU2ZyNy1xMEREVWY4MmEtZmJqR05uRE1sd1lFIn0.eyJleHAiOjE3MTU3NjY1NzksImlhdCI6MTcxNTY4MDE3OSwiYXV0aF90aW1lIjoxNzE1NjgwMTc3LCJqdGkiOiIxZjI3MzJlNC1jYjFhLTQ4OTktYjBiZC1iN2IxZWY1MzAxNDEiLCJpc3MiOiJodHRwczovLzEwLjYuMjAxLjIwMTozMDE0Ny9hdXRoL3JlYWxtcy9naGlwcG8iLCJhdWQiOiJfX2ludGVybmFsLWdoaXBwbyIsInN1YiI6ImMxZmMxM2ViLTAwZGUtNDFiYS05ZTllLWE5OGU2OGM0MmVmMCIsInR5cCI6IklEIiwiYXpwIjoiX19pbnRlcm5hbC1naGlwcG8iLCJzZXNzaW9uX3N0YXRlIjoiMGJjZWRjZTctMTliYS00NmU1LTkwYmUtOTliMWY2MWEyNzI0IiwiYXRfaGFzaCI6IlJhTHoyQjlKQ2FNc1RrbGVMR3V6blEiLCJhY3IiOiIwIiwic2lkIjoiMGJjZWRjZTctMTliYS00NmU1LTkwYmUtOTliMWY2MWEyNzI0IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJncm91cHMiOltdLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJucy12aWV3ZXIiLCJsb2NhbGUiOiIifQ.As2ipMjfvzvgONAGlc9RnqOd3zMwAj82VXlcqcR74ZK9tAq3Q4ruQ1a6WuIfqiq8Kq4F77ljwwzYUuunfBli2zhU2II8zyxVhLoCEBu4pBVBd_oJyUycXuNa6HfQGnl36E1M7-_QG8b-_T51wFxxVb5b7SEDE1AvIf54NAlAr-rhDmGRdOK1c9CohQcS00ab52MD3IPiFFZ8_Iljnii-RpXKZoTjdcULJVn_uZNk_SzSUK-7MVWmPBK15m6sNktOMSf0pCObKWRqHd15JSe-2aA2PKBo1jBH3tHbOgZyMPdsLI0QdmEnKB5FiiOeMpwn_oHnT6IjT-BZlB18VkW8rA'
    ```
