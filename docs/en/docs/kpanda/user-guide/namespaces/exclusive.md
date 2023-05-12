# namespace exclusive node

Namespace exclusive node refers to the exclusive use of CPU, memory and other resources of one or more nodes in a specific namespace through taint and taint tolerance in the kubernetes cluster. After configuring an exclusive node for a specific namespace, other applications and services not in this namespace cannot run on the exclusive node. The use of dedicated nodes allows important applications to exclusively share a portion of computing resources, thereby achieving physical isolation from other applications.

!!! note

    Applications and services that have been running on this node before the node is set as an exclusive node will not be affected, and will still run normally on this node. Only when these Pods are deleted or rebuilt, will they be scheduled to other non- Exclusive node.

## Preconditions:

Using the namespace exclusive node function requires the user to enable the `PodNodeSelector` and `PodTolerationRestriction` two feature admission controllers (Admission Controllers) on the cluster API server. For more information about admission controllers, please refer to [kubernetes Admission Controllers Reference](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/).

1. Check if the API server of the current cluster has the `PodNodeSelector` and `PodTolerationRestriction` admission controllers enabled. You can go to any Master node in the current cluster to check whether these two features are enabled in the `kube-apiserver.yaml` file, or run the following command on the Master node for a quick check:

    ```bash
    [root@g-master1 ~]# cat /etc/kubernetes/manifests/kube-apiserver.yaml | grep enable-admission-plugins

    # The expected output is as follows:
    - --enable-admission-plugins=NodeRestriction, PodNodeSelector, PodTolerationRestriction
    ```

2. Enable the `PodNodeSelector` and `PodTolerationRestriction` features for clusters that do not have `PodNodeSelector` and `PodTolerationRestriction` admission controllers enabled.

!!! note

    If the result output in the previous step contains two parameters `PodNodeSelector` and `PodTolerationRestriction`, please skip this step and go directly to the user interface to set exclusive nodes for the namespace.

Go to any Master node in the current cluster to modify the `kube-apiserver.yaml` configuration file, or run the following command on the Master node to configure:

    ```bash
    [root@g-master1 ~]# vi /etc/kubernetes/manifests/kube-apiserver.yaml

    # The expected output is as follows:
    apiVersion: v1
    kind: Pod
    metadata:
         …
    spec:
    containers:
    - command:
        -kube-apiserver
         …
        - --default-not-ready-toleration-seconds=300
        - --default-unreachable-toleration-seconds=300
        - --enable-admission-plugins=NodeRestriction #List of enabled admission controllers
        - --enable-aggregator-routing=False
        - --enable-bootstrap-token-auth=true
        - --endpoint-reconciler-type=lease
        - --etcd-cafile=/etc/kubernetes/ssl/etcd/ca.crt
         …
    ```

Find the `--enable-admission-plugins` parameter and add (comma-separated) `PodNodeSelector` and `PodTolerationRestriction` admission controllers. The reference is as follows:

    ```bash
    # Add `, PodNodeSelector, PodTolerationRestriction`
    - --enable-admission-plugins=NodeRestriction, PodNodeSelector, PodTolerationRestriction
    ```

## Use the interface to set exclusive nodes for namespaces

After you confirm that the `PodNodeSelector` and `PodTolerationRestriction` feature admission controllers on the cluster API server have been enabled, please refer to the following steps to use the UI management interface of DCE 5.0 to set exclusive nodes for the namespace.

1. Click the cluster name on the cluster list page, and then click Namespace in the left navigation bar.

    

2. Click the namespace name, then click the `Exclusive Node` tab, and click `Add Node` on the bottom right.

    

3. On the left side of the page, select which nodes are exclusive to this namespace, on the right side you can clear or delete a selected node, and finally click `OK` at the bottom.

    

4. You can view the existing exclusive nodes of this namespace in the list, and you can select `Cancel Exclusive` on the right side of the node.

    > After canceling exclusive access, Pods under other namespaces can also be scheduled on this node.

    