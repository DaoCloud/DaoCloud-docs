# Cluster-Wide Default EgressGateway

Setting a default EgressGateway for the entire cluster simplifies the process of defining EgressPolicies for tenants or using EgressClusterPolicy at the cluster level, eliminating the need to specify an `EgressGateway` name each time. Note that only one default EgressGateway can be set per cluster.

## Prerequisites

- EgressGateway components must be installed.

## Steps

1. When creating an `EgressGateway`, set `spec.clusterDefault` to `true` to designate it as the cluster-wide default. If an `EgressClusterPolicy` does not specify `spec.egressGatewayName`, or if an `EgressPolicy` does not specify `spec.egressGatewayName` and the tenant has not configured a default EgressGateway, the cluster default will be used automatically.

    ```yaml
    apiVersion: egressgateway.spidernet.io/v1beta1
    kind: EgressGateway
    metadata:
      name: default
    spec:
      clusterDefault: true
      ippools:
        ipv4:
          - 10.6.1.55
          - 10.6.1.56
        ipv4DefaultEIP: 10.6.1.55
        ipv6:
          - fd00::55
          - fd00::56
        ipv6DefaultEIP: fd00::56
      nodeSelector:
        selector:
          matchLabels:
            egress: "true"    
    ```

2. Create an `EgressPolicy` without specifying the `spec.egressGatewayName` field:

    ```yaml
    apiVersion: egressgateway.spidernet.io/v1beta1
    kind: EgressPolicy
    metadata:
      name: mock-app
    spec:
      appliedTo:
        podSelector:
          matchLabels:
            app: mock-app
      destSubnet:
        - 10.6.1.92/32
    ```

3. Run the following command to verify that the `EgressPolicy` is using the default EgressGateway:

    ```shell
    $ kubectl get egresspolicies mock-app -o yaml
    apiVersion: egressgateway.spidernet.io/v1beta1
    kind: EgressPolicy
    metadata:
      creationTimestamp: "2023-08-09T11:54:34Z"
      generation: 1
      name: mock-app
      namespace: default
      resourceVersion: "6233341"
      uid: 5692c5e6-a72b-41bd-a611-1106abd41bc2
    spec:
      appliedTo:
        podSelector:
          matchLabels:
            app: mock-app
      destSubnet:
      - 10.6.1.92/32
      - fd00::92/128
      - 172.30.40.0/21
      egressGatewayName: default
    ```
