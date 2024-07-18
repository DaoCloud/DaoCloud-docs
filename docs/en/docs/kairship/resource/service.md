---
MTPE: ModetaNiu
Date: 2024-07-18
hide:
  - toc
---

# Multicloud Services

Multicloud services are applications running on a group of Pods, which are exposed as network services one by one.
Using the DCE multicloud management module, you can use unfamiliar service discovery mechanisms without modifying your applications.
DCE provides the IP address for the Pod running the service and provides the same DNS name for a group of Pods, which can be load balanced among these Pods.

Follow the steps below to manage multicloud services.

1. After entering a multicloud instance, in the left navigation bar, click __Resource Management__ -> __Multicloud Services__ , 
   and click the __Create Service__ button in the upper right corner.

    ![Create](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/service01.png)

2. On the __Create Multicloud Service__ page, after configuring the Access Mode, Deploy Position, Ports Configuration 
   and other information, click __OK__ . The position is divided into several deploying methods: Specify Clusters/Specify Regions/Specify Labels. 
   Please refer to the detailed introduction in Workloads.

    ![Deploy](../images/service.png)

3. It supports one-click conversion of single-cloud service to multicloud service. Click __Convert Now__ on the list page, 
   select the service under the specified worker cluster and namespace, and click __OK__.

    ![Convert](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/service03.png)

4. Check the multicloud service list at this time, and find that the single-cluster service has been upgraded successfully.

    ![Upgrade](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/service04.png)

5. Click __⋮__ on the right side of the list to update and delete the service.

    ![Update/Delete](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/service05.png)

    !!! note

        If a service is deleted, the information related to the service will also disappear, please operate with caution.

## YAML example

Here is an example YAML for a multicloud service that you can use with a little modification.

```yaml
kind: Service
apiVersion: v1
metadata:
  name: kubernetes
  namespace: default
  uid: a23a0616-789e-469f-88f5-07eb67d460dc
  resourceVersion: '190'
  creationTimestamp: '2023-04-13T10:11:19Z'
  labels:
    component: apiserver
    provider: kubernetes
  annotations:
    shadow.clusterpedia.io/cluster-name: k-kairship-jxy
spec:
  ports:
    - name: https
      protocol: TCP
      port: 443
      targetPort: 5443
  clusterIP: 10.96.0.1
  clusterIPs:
    - 10.96.0.1
  type: ClusterIP
  sessionAffinity: None
  ipFamilies:
    - IPv4
  ipFamilyPolicy: SingleStack
  internalTrafficPolicy: Cluster
status:
  loadBalancer: {}
```