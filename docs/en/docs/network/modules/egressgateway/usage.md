# Using Egress Policy

## Currently supported CNIs for EgressGateway

=== "Calico"

    If your cluster uses [Calico](https://www.tigera.io/project-calico/) CNI, run the following command
    to ensure that EgressGateway's iptables rules are not overridden by Calico rules. Otherwise,
    EgressGateway will not work.

    ```shell
    # set chainInsertMode
    $ kubectl patch felixconfigurations  default --type='merge' -p '{"spec":{"chainInsertMode":"Append"}}'
    
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

    > For details about `spec.chainInsertMode`, refer to [Calico documentation](https://projectcalico.docs.tigera.io/reference/resources/felixconfig).

===  "Flannel"

    [Flannel](https://github.com/flannel-io/flannel) CNI does not require any configuration, you can skip this step.

===  "Weave"

    [Weave](https://github.com/flannel-io/flannel) CNI does not require any configuration, you can skip this step.

===  "Spiderpool"

    If your cluster uses [Spiderpool](https://github.com/spidernet-io/spiderpool) in conjunction with other CNIs, you need to perform the following steps.

    Add the addresses of external services outside the cluster to the 'hijackCIDR' field of the 'default'
    object in spiderpool.spidercoordinators. This ensures that when Pods access these external services,
    the traffic goes through the host where the Pod is located, allowing it to match the EgressGateway rules.

    Assuming "1.1.1.1/32" and "2.2.2.2/32" are the addresses of the external services.
    For already running Pods, you need to restart them for these routing rules to take effect within the Pods.

    ```shell
    kubectl patch spidercoordinators default  --type='merge' -p '{"spec": {"hijackCIDR": ["1.1.1.1/32", "2.2.2.2/32"]}}'
    ```

## Verify EgressGateway is running properly

Confirm that all EgressGateway Pods are running correctly.

```shell
$ kubectl get pod -n kube-system | grep egressgateway
egressgateway-agent-29lt5                  1/1     Running   0          9h
egressgateway-agent-94n8k                  1/1     Running   0          9h
egressgateway-agent-klkhf                  1/1     Running   0          9h
egressgateway-controller-5754f6658-7pn4z   1/1     Running   0          9h
```

## Create EgressGateway instances

1. EgressGateway defines a set of nodes as the cluster's egress gateway, and egress traffic from
   within the cluster will be forwarded through this set of nodes to exit the cluster. Therefore,
   we need to define a set of EgressGateway instances in advance. Here is an example:

    ```shell
    cat <<EOF | kubectl apply -f -
    apiVersion: egressgateway.spidernet.io/v1beta1
    kind: EgressGateway
    metadata:
      name: default
    spec:
      ippools:
        ipv4:
        - "172.22.0.100-172.22.0.110"
      nodeSelector:
        selector:
          matchLabels:
            egressgateway: "true"
    EOF
    ```

    In the creation command:

    - In the above YAML example, `spec.ippools.ipv4` defines a set of egress egress IP addresses,
      which need to be adjusted according to the specific environment.
    - The CIDR of `spec.ippools.ipv4` should be the same as the subnet of the egress network interface
      on the gateway nodes (usually the default route interface), otherwise, it may cause egress access issues.
    - Use the `spec.nodeSelector` of EgressGateway to select a set of nodes as the egress gateway.
      It supports selecting multiple nodes for high availability.

2. Label the egress gateway nodes. You can label multiple nodes, but for production environments,
   it is recommended to have at least 2 nodes, while for POC environments, 1 node is sufficient.

    ```shell
    kubectl get node
    kubectl label node $NodeName egressgateway="true"
    ```

3. Check status.

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

    In the above output:

    - The `status.nodeList` field has identified the nodes that match the `spec.nodeSelector`
      and the status of the corresponding EgressTunnel objects for each node.
    - The `spec.ippools.ipv4DefaultEIP` field randomly selects an IP address from `spec.ippools.ipv4`
      as the default VIP for this group of EgressGateway. Its purpose is to be used as the default
      allocation when creating an EgressPolicy object for an application if no VIP address is specified.

## Create an application and egress policy

1. Create an application that will be used to test Pod access to external services and label it.

    ```shell
    kubectl create deployment visitor --image nginx
    ```

1. Create an EgressPolicy CR object for the application.

    The EgressPolicy instance is used to define which Pods' egress traffic should be forwarded through
    the EgressGateway nodes, as well as other configuration details. You can create an example like
    the following, where any Pod matching the criteria that accesses any external address
    (not the Node IP, CNI Pod CIDR, or ClusterIP) will be forwarded by the EgressGateway nodes.
    Note that the EgressPolicy object is tenant-level, so it must be created under the selected
    application's tenant.

    ```shell
    cat <<EOF | kubectl apply -f -
    apiVersion: egressgateway.spidernet.io/v1beta1
    kind: EgressPolicy
    metadata:
     name: test
     namespace: default
    spec:
     egressGatewayName: default
     appliedTo:
      podSelector:
       matchLabels:
        app: "visitor"
    EOF
    ```

    In the above creation command:

    - `spec.egressGatewayName` specifies which group of EgressGateway to use.
    - `spec.appliedTo.podSelector` specifies which Pods within the cluster this policy applies to.
    - There are two options for the source IP address of egress traffic from the cluster:
        - You can use the IP address of the gateway nodes. This option is suitable for public cloud
          and traditional network environments. The downside is that the egress source IP may change
          if there are failures with the gateway nodes. You can set `spec.egressIP.useNodeIP=true`
          to enable this option.
        - You can use a dedicated VIP. Since EgressGateway works based on ARP, this option is suitable for
          traditional network environments but not for public cloud environments. The advantage is that
          the egress source IP is permanently fixed. If no settings are made in the EgressPolicy, it will
          use the default VIP of the egressGatewayName, or you can manually specify `spec.egressIP.ipv4`
          with an IP value that matches the IP pool in EgressGateway.

1. Check the status of the EgressPolicy.

    ```shell
    $ kubectl get EgressPolicy -A
    NAMESPACE   NAME   GATEWAY   IPV4           IPV6   EGRESSTUNNEL
    default     test   default   172.22.0.110          egressgateway-worker2
     
    $ kubectl get EgressPolicy test -o yaml
    apiVersion: egressgateway.spidernet.io/v1beta1
    kind: EgressPolicy
    metadata:
      name: test
      namespace: default
    spec:
      appliedTo:
        podSelector:
          matchLabels:
            app: visitor
      egressIP:
        allocatorPolicy: default
        useNodeIP: false
    status:
      eip:
        ipv4: 172.22.0.110
      node: egressgateway-worker2
    ```

    In the above output:

    - `status.eip` displays the egress IP address used by the group of applications when exiting the cluster.
    - `status.node` shows which EgressGateway node is currently responsible for forwarding egress traffic
      in real-time. Note: EgressGateway nodes support high availability. When multiple EgressGateway nodes
      exist, all EgressPolicies will be evenly distributed to different EgressGateway nodes for implementation.

4. Check the status of EgressEndpointSlices.

   For each EgressPolicy object, there is a corresponding EgressEndpointSlices object that stores
   the collection of IP addresses for the Pods selected by the EgressPolicy. If an application
   cannot egress, you can check if the IP addresses in this object are functioning properly.

    ```shell
    $ kubectl get egressendpointslices -A
    NAMESPACE   NAME         AGE
    default     test-kvlp6   18s
    
    $ kubectl get egressendpointslices test-kvlp6 -o yaml
    apiVersion: egressgateway.spidernet.io/v1beta1
    endpoints:
    - ipv4:
      - 172.40.14.195
      node: egressgateway-worker
      ns: default
      pod: visitor-6764bb48cc-29vq9
    kind: EgressEndpointSlice
    metadata:
      name: test-kvlp6
      namespace: default
    ```

## Test the effect

1. Deploy the nettools application outside the cluster to simulate an external service.
   The nettools application will return the source IP address of the requester in the HTTP response.

    ```shell
    docker run -d --net=host ghcr.io/spidernet-io/egressgateway-nettools:latest /usr/bin/nettools-server -protocol web -webPort 8080
    ```

2. In the visitor Pod within the cluster, verify the effect of egress traffic. You will see that
   when the visitor accesses the external service, the source IP returned by nettools matches the
   effect of the EgressPolicy `.status.eip`.

    ```shell
    $ kubectl get pod
    NAME                       READY   STATUS    RESTARTS   AGE
    visitor-6764bb48cc-29vq9   1/1     Running   0          15m

    $ kubectl exec -it visitor-6764bb48cc-29vq9 bash
    $ curl 10.6.1.92:8080
    Remote IP: 172.22.0.110
    ```
