# Differentiation strategy

Multicloud orchestration supports differentiated strategies, supports viewing the differentiated strategy list of the current instance and its associated multicloud resources on the interface, maintains, creates and edits differentiated strategy information in the form of YAML, and supports viewing the differentiated strategies of the current instance on the interface A list of policies and the multicloud resources associated with the current differentiated policy.

Differentiation policies define different configurations in multicloud and multi-cluster, which facilitates the management of deployment policies (Propagation Policy) and differentiation policies (Override Policy).

Follow the steps below to create a differentiation strategy.

1. After entering a multicloud instance, in the left navigation bar, click `Policy Management` -> `Differential Policy`, and click the `YAML Create` button in the upper right corner.

    ![image](../images/deploy01.png)

2. On the `YAML Creation` page, after entering the correct YAML statement, click `OK`.

    ![image](../images/deploy02.png)

3. Return to the differentiated policy list, the newly created one is the first one by default. Click `⋮` on the right side of the list to edit YAML and perform delete operations.

    ![image](../images/deploy03.png)

    !!! note

        If you want to delete a differentiated policy, you need to remove the workload related to the policy first. After the deletion, all the information related to the policy will be deleted. Please proceed with caution.

## YAML example

Here is an example YAML for a diff policy that you can use with a little modification.

```yaml
kind: OverridePolicy
apiVersion: policy.karmada.io/v1alpha1
metadata:
  name: nginx-op
  namespace: default
  uid: 09f89bc4-c6bf-47b3-81bf-9e494b831aac
  resourceVersion: '856977'
  generation: 1
  creationTimestamp: '2022-09-21T10:30:40Z'
  labels:
    a:b
  annotations:
    shadow.clusterpedia.io/cluster-name:k-kairshiptest
spec:
  resourceSelectors:
    - apiVersion: apps/v1
      kind: Deployment
      namespace: default
      name: nginx
  overriders: {}
```