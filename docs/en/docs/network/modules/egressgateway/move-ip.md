# Migrating Egress IP Between Egress Gateway Nodes

## Use Cases

- When multiple nodes are designated as `EgressNode` via `EgressGateway`, and a node requires maintenance, you can manually migrate its VIP (Egress IP) to another node using a CLI command.
- If there is any other need to manually move a node’s VIP to a different node.

## Steps

First, check the `EgressGateway` definition by running:

```shell
kubectl get egw egressgateway -o yaml
```

Example output:

```yaml
apiVersion: egressgateway.spidernet.io/v1beta1
kind: EgressGateway
metadata:
  finalizers:
  - egressgateway.spidernet.io/egressgateway
  name: egressgateway
spec:
  ippools:
    ipv4:
    - 10.6.91.1-10.6.93.125
    ipv4DefaultEIP: 10.6.92.222
  nodeSelector:
    selector:
      matchLabels:
        egress: "true"
status:
  ipUsage:
    ipv4Free: 37
    ipv4Total: 637
    ipv6Free: 0
    ipv6Total: 0
  nodeList:
  - name: workstation2
    status: Ready
  - name: workstation3
    status: Ready
    eips:
    - ipv4: 10.6.92.209
      policies:
      - name: policy-1
        namespace: default
```

Before migration, the Egress IP is assigned to `workstation3`:

```shell
node@workstation:~$ kubectl get egp
NAME       GATEWAY          IPW4          IPV6       EGRESSNODE
policy-1   egressgateway    10.6.92.209              workstation3
```

Now, migrate the Egress IP from `workstation3` to `workstation2` by running:

```shell
kubectl exec -it egressgateway-controller-86c84f4858-b6dz4 bash
egctl vip move --egressGatewayName egressgateway --vip 10.6.92.209 --targetNode workstation2
```

Expected output:

```log
Moving VIP 10.6.92.209 to node workstation2...
Successfully moved VIP 10.6.92.209 to node workstation2
```

After migration, verify that the Egress IP has been moved to `workstation2`:

```shell
node@workstation:~$ kubectl get egp
NAME       GATEWAY          IPW4          IPV6       EGRESSNODE
policy-1   egressgateway    10.6.92.209              workstation2
```

Now, `10.6.92.209` is assigned to `workstation2`, ensuring that traffic is routed through the updated node.
