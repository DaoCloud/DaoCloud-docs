# Create EgressPolicy

EgressPolicy is used to define which Pod's outbound traffic needs to be forwarded through the EgressGateway node, and to define other configuration details.
When a matching Pod accesses any address outside the cluster (any address that is not a Node IP, CNI Pod CIDR, or ClusterIP), it will be forwarded by the EgressGateway Node.
Currently, EgressPolicy is divided into two categories: namespace-level policies and cluster-level policies.

- __Namespace-level__ : The scope of the created policy is at the namespace level.
- __Cluster-level__ : The scope of the created policy is at the cluster level.

## Create Namespace EgressPolicy

1. Click on __Gateway Policy__ -> __Create Namespace Policy__ , and fill in the following parameters:

    <!-- ![egresspolicy-create-1](../../images/egresspolicy-create-1.jpg) -->

    **Basic Information**:
    
    * __Policy Name__ : Enter the name of the policy to be created.
    * __Description__ : Define the description of the policy to be created.
    * __Namespace__ : The namespace where the policy will take effect, in this example, select __default__ .
    * __Gateway Selection__ : Specify which already created [Egress Gateway instance](../egressgateway/create_eg.md) to use.

    **Outbound Address**:

    * __Outbound IP Address__ : Use a separate VIP as the outbound IP. Since EgressGateway operates on the basis of ARP, it is suitable for traditional networks where the source IP is always fixed. If not set, the default VIP will be used, and the IP value must be within the IP pool range of the EgressGateway. You can choose the IP in two ways:
        * __Specify Outbound IP Address__ : Specify a specific IP address as the outbound IP.
        * __Specify Allocation Policy__ : Use the default outbound IP or select an IP from the pool as the outbound IP through round-robin allocation.
      
    * __Node IP Address__ : Use the node's IP address as the outbound IP. This is suitable for public cloud and traditional network environments, but the disadvantage is that the outbound source IP may change with node failures. The corresponding field information is __spec.egressIP.useNodeIP=true__ .

    **Source Address Pods** :

    __Select Pods__ : Support selecting source address Pods through __label selectors__ or __source addresses__ , specifying the range of Pods where this policy will take effect. When a matching Pod accesses any address outside the cluster (any address that is not a Node IP, CNI Pod CIDR, or ClusterIP), it will be forwarded by the EgressGateway Node.
    * __Label Selectors__ : Specify the source address Pods using labels.
    * __Source Address__ : Add whitelist by adding source address CIDR address segments, locking the Pods that will be affected by this policy.

    **Advanced Settings** :

    __Destination Address__ : Specify a whitelist of destination addresses. When specified, this policy will only apply to the defined destination addresses. Supports input in various formats such as single IP address, IP range, CIDR, etc. Default is to apply to all destination addresses.

2. Click **OK** after inputting the details to complete the creation.

## Create Cluster EgressPolicy

1. Click on __Gateway Policy__ -> __Create Cluster Policy__ , and refer to the parameters for basic information, outbound address, and Pod selection as described in [Create Namespace EgressPolicy](#create-namespace-egresspolicy).

    **Advanced Settings** :
    
    * __Namespace Selector__ : Select namespaces using labels, and the policy will apply to the selected namespaces.
    * __Destination Address__ : Similar to creating namespace Egress Gateway policies.

2. Click **OK** after inputting the details to complete the creation.

## Create EgressPolicy Using YAML

1. Create the EgressPolicy YAML

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

    * __spec.egressGatewayName__ specifies which EgressGateway group to use.
    * __spec.appliedTo.podSelector__ specifies which Pods within the cluster this policy will apply to.
    * There are two options for the source IP address of egress traffic:
        * You can use the IP of the gateway node. This is suitable for public cloud and traditional network environments, but the drawback is that the outbound source IP may change with node failures. You can set __spec.egressIP.useNodeIP=true__ to make it effective.
        * You can use a separate VIP. Since EgressGateway operates on the basis of ARP, it is suitable for traditional networks, but not suitable for public cloud environments. The advantage is that the outbound source IP is always fixed. If no settings are made in EgressPolicy, the default VIP of `egressGatewayName` will be used, or you can manually specify __spec.egressIP.ipv4__, and the IP value must be within the IP pool of the EgressGateway.

2. Check the status of the EgressPolicy

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

    * __status.eip__ shows the outbound IP address used when the Pods in this group exit the cluster.
    * __status.node__ shows which EgressGateway node is currently responsible for forwarding outbound traffic.

    !!! note
    
        EgressGateway nodes support high availability. When there are multiple EgressGateway nodes, all EgressPolicies will be evenly distributed among different EgressGateway nodes.

3. Check the status of EgressEndpointSlices

    Each EgressPolicy object has a corresponding EgressEndpointSlices object, which stores the set of IP addresses of Pods selected by the EgressPolicy. If an application cannot access the outside, you can check if the IP addresses in this object are correct.

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

## Egress Gateway Test

1. Deploy the nettools application outside the cluster to simulate an external service. nettools will return the requester's source IP address in the HTTP response.

    ```shell
    docker run -d --net=host ghcr.io/spidernet-io/egressgateway-nettools:latest /usr/bin/nettools-server -protocol web -webPort 8080
    ```

2. In the visitor Pod within the cluster, verify the effect of outbound traffic. When the visitor accesses the external service, the source IP returned by nettools should match the effect of EgressPolicy `.status.eip`.

    ```shell
    $ kubectl get pod
    NAME                       READY   STATUS    RESTARTS   AGE
    visitor-6764bb48cc-29vq9   1/1     Running   0          15m
    
    $ kubectl exec -it visitor-6764bb48cc-29vq9 bash
    $ curl 10.6.1.92:8080
    Remote IP: 172.22.0.110
    ```
