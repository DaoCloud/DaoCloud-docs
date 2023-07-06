# Third-party workloads use IP pools

This page focuses on configuring IP pools for custom workloads (taking the workload CloneSet created by the [OpenKruise](https://github.com/openkruise/kruise) controller as an example here)  and using Spiderpool to assign and fix the IPs in the Underlay network.

## Prerequisites

1. [SpiderPool has been successfully deployed](install.md). 
2. [Multus with Macvlan/SR-IOV has been successfully deployed](../multus-underlay/install.md).
3. If you choose manual selection of IP pool, please complete [Create IP subnet and IP pool](../spiderpool/createpool.md) in advance. To use a fixed IP pool in this example, please complete [Create a fixed IP pool](../spiderpool/createpool.md) in advance.

## Steps

### Using created fixed IP pools

Deploy the CR `CloneSet` and specify the default network type, VLAN ID, subnet interface, and IP pool information in `Annotation`.

    ```
    v1.multus-cni.io/default-network: kube-system/calico
    k8s.v1.cni.cncf.io/networks: kube-system/vlan6
    ipam.spidernet.io/ippools: '[{"interface":"net1","ipv4":["ippool01"]}]'
    ```

    ```
    apiVersion: apps.kruise.io/v1alpha1
    kind: CloneSet
    metadata:
      name: custom-kruise-cloneset
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: custom-kruise-cloneset
      template:
        metadata:
          annotations:
            v1.multus-cni.io/default-network: "kube-system/calico"
            k8s.v1.cni.cncf.io/networks: "kube-system/vlan6"
            ipam.spidernet.io/ippool: |-
              {
                "interface":"net1", "ipv4":["ippool01"]
              }
          labels:
            app: custom-kruise-cloneset
        spec:
          containers:
          - name: custom-kruise-cloneset
            image: busybox
            imagePullPolicy: IfNotPresent
            command: ["/bin/sh", "-c", "trap : TERM INT; sleep infinity & wait"]
    ```

1. Check the status of CloneSet after `CloneSet` is deployed.

    ```
    kubectl get pods -A|grep kruise-clone
    default            custom-kruise-cloneset-jkqtx                                      1/1     Running             0                  44h
    default            custom-kruise-cloneset-v5qz7                                      1/1     Running        0                  44h
    default            custom-kruise-cloneset-xhtq6                                      1/1     Running
    0                  44h
    ```

2.  Go to `Container Platform`-->Select the corresponding cluster`-->Click `Container Network`, then find the corresponding subnet-->Go to the subnet details and check the IP usage.

### Automatic creation of fixed IP pools

1. To automatically create a fixed IP pool using a subnet, add the following Annotation when creating a custom workload.

    ```
    apiVersion: apps.kruise.io/v1alpha1
    kind: CloneSet
    metadata:
      name: custom-kruise-cloneset03
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: custom-kruise-cloneset03
      template:
        metadata:
          annotations:
            v1.multus-cni.io/default-network: "kube-system/calico" # Specify the default container NIC
            k8s.v1.cni.cncf.io/networks: "kube-system/vlan6" #Specify the Multus CRD instance（NetworkAttachmentDefinition）
            ipam.spidernet.io/subnet: |-   # Specify the NIC and the subnet to be used with the fixed IP pool
              {"interface":"net1","ipv4": ["subnet124"]}
            ipam.spidernet.io/ippool-ip-number: "1" # Specify the number of resilient IPs, the number of available IPs = the number of resilient IPs + the number of Replicas
          labels:
            app: custom-kruise-cloneset03
        spec:
          containers:
          - name: custom-kruise-cloneset03
            image: busybox
            imagePullPolicy: IfNotPresent
            command: ["/bin/sh", "-c", "trap : TERM INT; sleep infinity & wait"]
    ```

2. Check the status of Clonset:

    ```
    kubectl get pods -A|grep kruise-clone03
    ```

3. Check the status of the IP Pool IP:

    ```
    kubectl get sp -oyaml | grep kruise
          ipam.spidernet.io/application: apps.kruise.io/v1alpha1:CloneSet:default:custom-kruise-cloneset03
        name: auto-custom-kruise-cloneset03-v4-net1-f3114156804d
        allocatedIPs: '{"10.6.124.200":{"interface":"net1","pod":"default/custom-kruise-cloneset-r7xjd","podUid":"43942169-3c43-4a81-aaae-60ba1dc9d07e"},"10.6.124.201":{"interface":"net1","pod":"default/custom-kruise-cloneset-sp5t6","podUid":"4980a045-7ee9-467a-a6a3-b259411963cb"},"10.6.124.202":{"interface":"net1","pod":"default/custom-kruise-cloneset-j94tl","podUid":"72b13a85-5275-44b1-8491-323f9fff3571"}}'
   
    ```

