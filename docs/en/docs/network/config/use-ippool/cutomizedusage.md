---
MTPE: WANG0608GitHub
Date: 2024-08-12
---

# Third-Party Workloads Use IPPools

This section primarily discusses the integration of Spiderpool and Multus CR for managing custom workload
(Specifically, workloads created by the [OpenKruise](https://github.com/openkruise/kruise) controller, such as CloneSet) pods.
It covers the configuration of IPPools for pods and explains how to allocate and fix IP addresses in the underlay network using Spiderpool.

## Prerequisites

1. [Spiderpool has been successfully deployed](../../modules/spiderpool/install/install.md).

2. If you choose manual selection of IPPool, please [Create IP subnet and IPPool](../ippool/createpool.md) in advance.
   To use a fixed IPPool in this example, please complete [Create a fixed IPPool](../ippool/createpool.md) in advance.

## Steps

### Using created fixed IPPools

1. Deploy the CR CloneSet and specify the default network type, VLAN ID, subnet interface, and IPPool information in `Annotation`.

    ```yaml
    v1.multus-cni.io/default-network: kube-system/calico
    k8s.v1.cni.cncf.io/networks: kube-system/vlan6
    ipam.spidernet.io/ippools: '[{"interface":"net1","ipv4":["ippool01"]}]'
    ```

    ```yaml
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

1. Check the CloneSet status after deployment.

    ```shell
    $ kubectl get pods -A|grep kruise-clone
    default            custom-kruise-cloneset-jkqtx                                      1/1     Running             0                  44h
    default            custom-kruise-cloneset-v5qz7                                      1/1     Running        0                  44h
    default            custom-kruise-cloneset-xhtq6                                      1/1     Running
    0                  44h
    ```

1. Go to __Container Management__  -> Select the proper cluster -> Click __Container Network__ , then find the proper subnet -> Go to the subnet details and check the IP usage.

    <!-- add image later -->

### Automatically creating fixed IPPools

1. To automatically create a fixed IPPool using a subnet, add the following `Annotation` when creating a custom workload.

    ```yaml
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
            v1.multus-cni.io/default-network: "kube-system/calico" # (1)!
            k8s.v1.cni.cncf.io/networks: "kube-system/vlan6" # (2)!
            ipam.spidernet.io/subnet: |-   # (3)!
              {"interface":"net1","ipv4": ["subnet124"]}
            ipam.spidernet.io/ippool-ip-number: "1" # (4)!
          labels:
            app: custom-kruise-cloneset03
        spec:
          containers:
          - name: custom-kruise-cloneset03
            image: busybox
            imagePullPolicy: IfNotPresent
            command: ["/bin/sh", "-c", "trap : TERM INT; sleep infinity & wait"]
    ```
    
    1. Specify the default container NIC
    2. Specify the Multus CRD instance（NetworkAttachmentDefinition）
    3. Specify the NIC and the subnet to be used with the fixed IPPool
    4. Specify the number of resilient IPs, the number of available IPs = the number of resilient IPs + the number of Replicas

2. Check the CloneSet status after deployment:

    ```shell
    kubectl get pods -A|grep kruise-clone03
    ```

3. Check the IPPool IP status:

    ```shell
    kubectl get sp -oyaml | grep kruise
          ipam.spidernet.io/application: apps.kruise.io/v1alpha1:CloneSet:default:custom-kruise-cloneset03
        name: auto-custom-kruise-cloneset03-v4-net1-f3114156804d
        allocatedIPs: '{"10.6.124.200":{"interface":"net1","pod":"default/custom-kruise-cloneset-r7xjd","podUid":"43942169-3c43-4a81-aaae-60ba1dc9d07e"},"10.6.124.201":{"interface":"net1","pod":"default/custom-kruise-cloneset-sp5t6","podUid":"4980a045-7ee9-467a-a6a3-b259411963cb"},"10.6.124.202":{"interface":"net1","pod":"default/custom-kruise-cloneset-j94tl","podUid":"72b13a85-5275-44b1-8491-323f9fff3571"}}'   
    ```
