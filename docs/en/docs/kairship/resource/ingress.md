---
hide:
  - toc
---

# multicloud routing

Multicloud routing is a unified abstraction of the standard Kubernetes Ingress multicloud. By creating an Ingress and associating it with several multicloud services, it can be distributed to multiple clusters at the same time.

Currently, two creation methods are provided: form creation and YAML creation. This article takes form creation as an example, and follows the steps below.

1. After entering a multicloud instance, in the left navigation bar, click `Resource Management` -> `Multicloud Routing`, and click the `Create` button in the upper right corner.

    <!--screenshot-->

2. On the `Create multicloud Route` page, after configuring the deployment location, setting routing rules, Ingress Class, whether to enable session persistence, etc., click `OK`. For details, please refer to [Create Route](../../kpanda/user-guide/services-routes/create-ingress.md)

    <!--screenshot-->

3. The new function is an early adopter. It supports one-click conversion of sub-cluster services to multicloud routing. Click `Experience Now` on the list page, select the routing under the specified working cluster and namespace, and click OK to convert successfully.

    <!--screenshot-->

4. Click `⋮` on the right side of the list to update and delete the route.

    <!--screenshot-->

    !!! note

        If a route is deleted, the service-related information will also disappear, so please proceed with caution.

## YAML example

Here is an example YAML for multicloud routing that you can use with a little modification.

```yaml
kind: Ingress
apiVersion: networking.k8s.io/v1
metadata:
  name: ingress-test
  namespace: default
  uid: 49a45f23-2e5a-4a23-9f21-77418c1b9bbb
  resourceVersion: '1979660'
  generation: 1
  creationTimestamp: '2023-04-27T00:07:43Z'
  labels:
    propagationpolicy.karmada.io/name: ingress-ingress-test-ygddx
    propagationpolicy.karmada.io/namespace: default
  annotations:
    shadow.clusterpedia.io/cluster-name: k-kairship-jxy
spec:
  rules:
    - host: testing.daocloud.io
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: test-service
                port:
                  number: 123
status:
  loadBalancer: {}
```