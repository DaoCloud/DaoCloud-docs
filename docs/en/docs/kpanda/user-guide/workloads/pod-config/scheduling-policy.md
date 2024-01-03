# Scheduling strategy

In a Kubernetes cluster, like many other Kubernetes objects, nodes have [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/). You can [manually add labels](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/#add-a-label-to-a-node). Kubernetes also adds some standard labels to all nodes in the cluster. See [Common Labels, Annotations, and Taints](https://kubernetes.io/docs/reference/labels-annotations-taints/) for common node labels. By adding labels to nodes, you can have pods scheduled on specific nodes or groups of nodes. You can use this feature to ensure that specific Pods can only run on nodes with certain isolation, security or governance properties.

__nodeSelector__ is the simplest recommended form of a node selection constraint. You can add a __nodeSelector__ field to the Pod's spec to set the [node label](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#built -in-node-labels). Kubernetes will only schedule pods on nodes with each label specified. __nodeSelector__ provides one of the easiest ways to constrain Pods to nodes with specific labels. Affinity and anti-affinity expand the types of constraints you can define. Some benefits of using affinity and anti-affinity are:

- Affinity and anti-affinity languages are more expressive. __nodeSelector__ can only select nodes that have all the specified labels. Affinity, anti-affinity give you greater control over selection logic.

- You can mark a rule as "soft demand" or "preference", so that the scheduler will still schedule the Pod if no matching node can be found.

- You can use the labels of other Pods running on the node (or in other topological domains) to enforce scheduling constraints, instead of only using the labels of the node itself. This capability allows you to define rules which allow Pods to be placed together.

You can choose which node the Pod will deploy to by setting affinity and anti-affinity.

## Tolerance time

When the node where the workload instance is located is unavailable, the time window for the system to reschedule the instance to other available nodes. The default is 300 seconds.

## Node affinity (nodeAffinity)

Node affinity is conceptually similar to __nodeSelector__ , which allows you to constrain which nodes Pods can be scheduled on based on the labels on the nodes. There are two types of node affinity:

- **Must be satisfied: ( __requiredDuringSchedulingIgnoredDuringExecution__ )** The scheduler can only run scheduling when the rules are satisfied. This functionality is similar to __nodeSelector__ , but with a more expressive syntax. You can define multiple hard constraint rules, but only one of them must be satisfied.

- **Satisfy as much as possible: ( __preferredDuringSchedulingIgnoredDuringExecution__ )** The scheduler will try to find nodes that meet the corresponding rules. If no matching node is found, the scheduler will still schedule the Pod. You can also set weights for soft constraint rules. During specific scheduling, if there are multiple nodes that meet the conditions, the node with the highest weight will be scheduled first. At the same time, you can also define multiple hard constraint rules, but only one of them needs to be satisfied.

#### Tag name

The label corresponding to the node can use the default label or user-defined label.

#### Operators

- In: the label value needs to be in the list of values
- NotIn: the tag's value is not in a list
- Exists: To judge whether a certain label exists, no need to set the label value
- DoesNotExist: Determine if a tag does not exist, no need to set the tag value
- Gt: the value of the label is greater than a certain value (string comparison)
- Lt: the value of the label is less than a certain value (string comparison)

#### Weights

It can only be added in the "as far as possible" policy, which can be understood as the priority of scheduling, and those with the highest weight will be scheduled first. The value range is 1 to 100.

## Workload Affinity

Similar to node affinity, there are two types of workload affinity:

- **Must be satisfied: ( __requiredDuringSchedulingIgnoredDuringExecution__ )** The scheduler can only run scheduling when the rules are satisfied. This functionality is similar to __nodeSelector__ , but with a more expressive syntax. You can define multiple hard constraint rules, but only one of them must be satisfied.
- **Satisfy as much as possible: ( __preferredDuringSchedulingIgnoredDuringExecution__ )** The scheduler will try to find nodes that meet the corresponding rules. If no matching node is found, the scheduler will still schedule the Pod. You can also set weights for soft constraint rules. During specific scheduling, if there are multiple nodes that meet the conditions, the node with the highest weight will be scheduled first. At the same time, you can also define multiple hard constraint rules, but only one of them needs to be satisfied.

The affinity of the workload is mainly used to determine which Pods of the workload can be deployed in the same topology domain. For example, services that communicate with each other can be deployed in the same topology domain (such as the same availability zone) by applying affinity scheduling to reduce the network delay between them.

#### Tag name

The label corresponding to the node can use the default label or user-defined label.

#### Namespaces

Specifies the namespace in which the scheduling policy takes effect.

#### Operators

- In: the label value needs to be in the list of values
- NotIn: the tag's value is not in a list
- Exists: To judge whether a certain label exists, no need to set the label value
- DoesNotExist: Determine if a tag does not exist, no need to set the tag value

#### Topology domain

Specify the scope of influence during scheduling. If you specify kubernetes.io/Clustername, it will use the Node node as the distinguishing scope.

## Workload Anti-Affinity

Similar to node affinity, there are two types of anti-affinity for workloads:

- **Must be satisfied: ( __requiredDuringSchedulingIgnoredDuringExecution__ )** The scheduler can only run scheduling when the rules are satisfied. This functionality is similar to __nodeSelector__ , but with a more expressive syntax. You can define multiple hard constraint rules, but only one of them must be satisfied.
- **Satisfy as much as possible: ( __preferredDuringSchedulingIgnoredDuringExecution__ )** The scheduler will try to find nodes that meet the corresponding rules. If no matching node is found, the scheduler will still schedule the Pod. You can also set weights for soft constraint rules. During specific scheduling, if there are multiple nodes that meet the conditions, the node with the highest weight will be scheduled first. At the same time, you can also define multiple hard constraint rules, but only one of them needs to be satisfied.

The anti-affinity of the workload is mainly used to determine which Pods of the workload cannot be deployed in the same topology domain. For example, the same Pod of a load is distributed to different topological domains (such as different hosts) to improve the stability of the load itself.

#### Tag name

The label corresponding to the node can use the default label or user-defined label.

#### Namespaces

Specifies the namespace in which the scheduling policy takes effect.

#### Operators

- In: the label value needs to be in the list of values
- NotIn: the tag's value is not in a list
- Exists: To judge whether a certain label exists, no need to set the label value
- DoesNotExist: Determine if a tag does not exist, no need to set the tag value

#### Topology domain

Specify the scope of influence when scheduling, such as specifying kubernetes.io/Clustername, it will use the Node node as the distinguishing scope.