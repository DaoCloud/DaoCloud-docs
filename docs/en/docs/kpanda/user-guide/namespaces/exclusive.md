# namespace exclusive node

Namespace exclusive node refers to the exclusive use of CPU, memory and other resources of one or more nodes in a specific namespace through taint and taint tolerance in the kubernetes cluster. After configuring an exclusive node for a specific namespace, other applications and services not in this namespace cannot run on the exclusive node. The use of dedicated nodes allows important applications to exclusively share a portion of computing resources, thereby achieving physical isolation from other applications.

!!! note

    Applications and services that have been running on this node before the node is set as an exclusive node will not be affected, and will still run normally on this node. Only when these Pods are deleted or rebuilt, will they be scheduled to other non- Exclusive node.

## Preconditions:

Using the namespace exclusive node feature requires the user to enable the __PodNodeSelector__ and __PodTolerationRestriction__ two feature admission controllers (Admission Controllers) on the cluster API server. For more information about admission controllers, refer to [kubernetes Admission Controllers Reference](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/).

1. Check if the API server of the current cluster has the __PodNodeSelector__ and __PodTolerationRestriction__ admission controllers enabled. You can go to any Master node in the current cluster to check whether these two features are enabled in the __kube-apiserver.yaml__ file, or run the following command on the Master node for a quick check:

    ```bash
    [root@g-master1 ~]# cat /etc/kubernetes/manifests/kube-apiserver.yaml | grep enable-admission-plugins

    # The expected output is as follows:
    - --enable-admission-plugins=NodeRestriction, PodNodeSelector, PodTolerationRestriction
    ```

2. Enable the __PodNodeSelector__ and __PodTolerationRestriction__ features for clusters that do not have __PodNodeSelector__ and __PodTolerationRestriction__ admission controllers enabled.

!!! note

    If the result output in the previous step contains two parameters __PodNodeSelector__ and __PodTolerationRestriction__ , please skip this step and go directly to the user interface to set exclusive nodes for the namespace.

Go to any Master node in the current cluster to modify the __kube-apiserver.yaml__ configuration file, or run the following command on the Master node to configure:

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

Find the __--enable-admission-plugins__ parameter and add (comma-separated) __PodNodeSelector__ and __PodTolerationRestriction__ admission controllers. The reference is as follows:

    ```bash
    # Add __, PodNodeSelector, PodTolerationRestriction__ 
    - --enable-admission-plugins=NodeRestriction, PodNodeSelector, PodTolerationRestriction
    ```

## Use the interface to set exclusive nodes for namespaces

After you confirm that the __PodNodeSelector__ and __PodTolerationRestriction__ feature admission controllers on the cluster API server have been enabled, refer to the following steps to use the UI management interface of DCE 5.0 to set exclusive nodes for the namespace.

1. Click the cluster name on the cluster list page, and then click Namespace in the left navigation bar.

    

2. Click the namespace name, then click the __Exclusive Node__ tab, and click __Add Node__ on the bottom right.

    

3. On the left side of the page, select which nodes are exclusive to this namespace, on the right side you can clear or delete a selected node, and finally click __OK__ at the bottom.

    

4. You can view the existing exclusive nodes of this namespace in the list, and you can select __Cancel Exclusive__ on the right side of the node.

    > After canceling exclusive access, Pods under other namespaces can also be scheduled on this node.

    