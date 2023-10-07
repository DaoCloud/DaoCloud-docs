# deployment strategy

Multicloud Management supports viewing the deployment policy list of the current instance and its associated multicloud resources on the interface, supports creating and editing deployment policy information in the form of YAML and forms, and only provides a delete button for idle deployment policies.

Deployment policies define how resources are distributed across multicloud and multicluster. Deployment policy (PropagationPolicy) is divided into namespace level and cluster level.

- Namespace-level deployment policy (PropagationPolicy) represents a policy that propagates a set of resources to one or more member clusters, and can only propagate resources in its own namespace.
- A cluster-level deployment policy (ClusterPropagationPolicy) represents a cluster-wide policy for propagating a set of resources to one or more member clusters, capable of propagating cluster-level resources and resources in any namespace other than the system-reserved namespace.

## YAML creation

1. After entering a multicloud instance, in the left navigation bar, click `Policy Management` -> `Deployment Policy` -> `Namespace Level`, and click the `YAML Create` button in the upper right corner.

    <!--screenshot-->

2. On the `YAML Creation` page, after entering the correct YAML statement, click `OK`.

    <!--screenshot-->

3. Return to the deployment policy list, and the newly created one is the first one by default. Click `⋮` on the right side of the list to edit YAML and perform delete operations.

## YAML example

Here is an example YAML for a deployment policy that you can use with a little modification.

```yaml title="YAML example"
kind: PropagationPolicy
apiVersion: policy.karmada.io/v1alpha1
metadata:
  name: nginx-propagation
  namespace: default
  uid: 2190e122-a6b0-4994-80e6-5c03a9d1d3a4
  resourceVersion: '24258'
  generation: 1
  creationTimestamp: '2022-09-15T10:04:20Z'
  annotations:
    shadow.clusterpedia.io/cluster-name:k-kairshiptest
spec:
  resourceSelectors:
    - apiVersion: apps/v1
      kind: Deployment
      namespace: default
      name: nginx
  placement:
    clusterAffinity:
      clusterNames:
        -skoala-dev
    clusterTolerations:
      - key: cluster.karmada.io/not-ready
        operator: Exists
        effect: NoExecute
        tolerationSeconds: 300
      - key: cluster.karmada.io/unreachable
        operator: Exists
        effect: NoExecute
        tolerationSeconds: 300
```

## Form Creation

1. Follow the steps below to create a deployment policy.

    - Basic configuration: fill in the name, select the multicloud namespace, and add label annotations
    - Configure resources: select multicloud resources and target deployment clusters
    - Deployment strategy: Scheduling type, taint tolerance, you can choose whether to enable propagation constraints, support filling in priority (deployment strategy can also be created at the same time when creating resources, when the deployment strategy is also created on this page, you can choose according to the priority level to determine which deployment strategy the resource uses)

    <!--screenshot-->

    <!--screenshot-->

2. The form creates a cluster-level deployment strategy without selecting a namespace.

    <!--screenshot-->

    !!! note

        If you want to delete a deployment policy, you need to remove the workload related to the policy first. After the deletion, all the information related to the policy will be deleted. Please operate with caution.