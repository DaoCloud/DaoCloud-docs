# Tenant-Level Default EgressGateway

Setting a default `EgressGateway` for a tenant simplifies `EgressPolicy` configuration by eliminating the need to specify the `EgressGateway` name in each policy. The tenant-level default `EgressGateway` takes precedence over the cluster-wide default `EgressGateway`. In other words, if a tenant has a default `EgressGateway`, it will be used first. If the tenant does not have a default `EgressGateway`, the cluster default will be used.

## Prerequisites

- The `EgressGateway` component is installed.
- An `EgressGateway` CR has been created.

## Steps

1. Assign a default `EgressGateway` for the tenant (namespace):

    ```bash
    kubectl label ns default spidernet.io/egressgateway-default=egressgateway
    ```

2. Create an `EgressPolicy` without specifying `spec.egressGatewayName`:

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

3. Verify that the `EgressPolicy` is automatically assigned to the tenant’s default `EgressGateway`:

    ```shell
    $ kubectl get egresspolicies mock-app -o yaml
    ```

    Expected output:

    ```yaml
    apiVersion: egressgateway.spidernet.io/v1beta1
    kind: EgressPolicy
    metadata:
      creationTimestamp: "2023-08-09T10:54:34Z"
      generation: 1
      name: mock-app
      namespace: default
      resourceVersion: "6233341"
      uid: 5692c5e6-a71b-41bd-a611-1106abd41ba3
    spec:
      appliedTo:
        podSelector:
          matchLabels:
            app: mock-app
      destSubnet:
        - 10.6.1.92/32
        - fd00::92/128
        - 172.30.40.0/21
      egressGatewayName: egressgateway
    ```

Now, `mock-app` traffic will be routed through the tenant's default `EgressGateway`.
