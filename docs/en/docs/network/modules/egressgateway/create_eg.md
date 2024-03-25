# Create EgressGateway Instance

This page describes the steps to create an EgressGateway instance.

## Prerequisites

1. Currently, EgressGateway supports the following CNIs:

    ===  "Calico"

        If your cluster is using [Calico](https://www.tigera.io/project-calico/) CNI, execute the following command to ensure that the iptables rules of EgressGateway are not overridden by Calico rules, otherwise EgressGateway will not work.

        ```shell
        # set chainInsertMode
        $ kubectl patch felixconfigurations default --type='merge' -p '{"spec":{"chainInsertMode":"Append"}}'
        
        # check status
        $ kubectl get FelixConfiguration default -o yaml
        apiVersion: crd.projectcalico.org/v1
        kind: FelixConfiguration
        metadata:
          generation: 2
          name: default
          resourceVersion: "873"
          uid: 0548a2a5-f771-455b-86f7-27e07fb8223d
        spec:
          chainInsertMode: Append
        ......

        ```

        !!! tip

            The meaning of __spec.chainInsertMode__ can be referred to in the [Calico documentation](https://projectcalico.docs.tigera.io/reference/resources/felixconfig).

    ===  "Flannel"

        [Flannel](https://github.com/flannel-io/flannel) CNI does not require any configuration, you can skip this step.

    ===  "Weave"

        [Weave](https://github.com/flannel-io/flannel) CNI does not require any configuration, you can skip this step.

    ===  "Spiderpool"

        If your cluster is using [Spiderpool](https://github.com/spidernet-io/spiderpool) with another CNI, follow these steps.

        Add the addresses of external services to the 'hijackCIDR' of the 'default' object in 'spiderpool.spidercoordinators' outside the cluster. This ensures that when Pods access these external services, the traffic first goes through the host where the Pod is located, and is matched by the EgressGateway rules.

        If "1.1.1.1/32", "2.2.2.2/32" are external service addresses. For Pods that are already running, you need to restart the Pods for these routing rules to take effect in the Pods.

        ```shell
        kubectl patch spidercoordinators default  --type='merge' -p '{"spec": {"hijackCIDR": ["1.1.1.1/32", "2.2.2.2/32"]}}'
        ```

2. Confirm that all EgressGateway Pods are running normally.

    ```shell
    $ kubectl get pod -n kube-system | grep egressgateway
    egressgateway-agent-29lt5                  1/1     Running   0          9h
    egressgateway-agent-94n8k                  1/1     Running   0          9h
    egressgateway-agent-klkhf                  1/1     Running   0          9h
    egressgateway-controller-5754f6658-7pn4z   1/1     Running   0          9h
    ```

## Create EgressGateway Instance

1. Go to the corresponding cluster, click the __Cluster Name__ to enter the details, select __Network__ -> __Network Configuration__ -> __Egress Gateway__ , click __Create Egress Gateway__ , and enter the following parameters. Click confirm to complete the creation.

    <!-- ![egress-create01](../../images/egress-create-1.jpg) -->

    * __Name__: EgressGateway instance name.
    * __Description__: Description of the EgressGateway instance, optional.
    * __Node Selector__: Select the egress gateway exit node based on node labels. Selecting multiple nodes can achieve high availability. Plan ahead for exit nodes and assign the corresponding label to the nodes. In this chapter, label 2 nodes with __egressgateway: true__.
    * __Egress IP Range__: A group of EgressGateway exit IP ranges, the subnet must be the same as the exit network card (usually the default route network card) on the gateway node, otherwise, it is highly likely that egress access will not work. The setting supports IP range/IP address/CIDR.
        * __IP Range__ Example: 172.22.0.100-172.22.0.110, used in this chapter.
        * __IP Address__ Example: 172.22.0.100
        * __CIDR__ Example: 172.22.0.0/16
    * __IPv4 Default Egress IP__: The default exit IP address of the gateway after creation. Select an IP address from the Egress IP Range as the default VIP for this group of EgressGateway. Its purpose is that when creating EgressPolicy objects for applications, if the VIP address is not specified, it will default to using this default VIP.

2. Once created, you can view the status of the EgressGateway instance on the interface.

    <!-- ![egress-create01](../../images/egress-create-2.jpg) -->

    You can also check the status using the following command.

    ```shell
    $ kubectl get EgressGateway default -o yaml
    apiVersion: egressgateway.spidernet.io/v1beta1
    kind: EgressGateway
    metadata:
      name: default
      uid: 7ce835e2-2075-4d26-ba63-eacd841aadfe
    spec:
      ippools:
      ipv4:
      - 172.22.0.100-172.22.0.110
      ipv4DefaultEIP: 172.22.0.110
      nodeSelector:
        selector:
          matchLabels:
          egressgateway: "true"
    status:
      nodeList:
      - name: egressgateway-worker1
        status: Ready
      - name: egressgateway-worker2
        status: Ready
    ```

    In the output above, the __status.nodeList__ field has identified the nodes that match the __spec.nodeSelector__ and the status of the EgressTunnel objects corresponding to those nodes.

After creating the EgressGateway instance, please proceed to [create gateway policies](create-egpolicy.md).
