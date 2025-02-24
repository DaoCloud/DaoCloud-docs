# EgressGateway Failover

## Controller Failover

EgressGateway control plane failover is managed by specifying the `controller.replicas` parameter during installation. If one of the multiple controller replicas fails, the system automatically selects another replica as the primary controller to ensure continuous service availability.

## Datapath Failover

For datapath failover, you can designate a set of nodes as Egress Nodes when creating an `EgressGateway` by using `nodeSelector`. The Egress IP will be bound to one of these nodes. If a node fails or its Egress Agent encounters an issue, the Egress IP will automatically transfer to another available node, ensuring service continuity and reliability.

```yaml
apiVersion: egressgateway.spidernet.io/v1beta1
kind: EgressGateway
metadata:
  name: egw1
spec:
  clusterDefault: true
  ippools:
    ipv4:
      - 10.6.1.55
      - 10.6.1.56
    ipv4DefaultEIP: 10.6.1.56
    ipv6:
      - fd00::55
      - fd00::56
    ipv6DefaultEIP: fd00::55
  nodeSelector:
    selector:
      matchLabels:
        egress: "true"
status:
  nodeList:
    - name: node1
      status: Ready
      eips:
        - ipv4: 10.6.1.56
          ipv6: fd00::55
          policies:
            - name: policy1
              namespace: default
    - name: node2
      status: Ready
```

In the above `EgressGateway` definition, by setting `egress: "true"`, both `node1` and `node2` are designated as Egress Nodes. `node1` is the active node, and its assigned Egress IPs can be viewed in the `status` field. If `node1` fails, `node2` will take over as the failover node.

![primary-backup](./primary-backup.svg)

### Configuring Failover Timing

You can fine-tune the status check and Egress IP failover timing using Helm values:

- `feature.tunnelMonitorPeriod`: The interval (in seconds) at which the Egress Controller checks the last update status of the `EgressTunnel`. Default: `5`.
- `feature.tunnelUpdatePeriod`: The interval (in seconds) at which the Egress Agent updates the `EgressTunnel` status. Default: `5`.
- `feature.eipEvictionTimeout`: If the last update time of an `EgressTunnel` exceeds this timeout, the Egress IP will be moved to another available node. Default: `5` seconds.

```yaml
apiVersion: egressgateway.spidernet.io/v1beta1
kind: EgressTunnel
metadata:
  name: workstation1
spec: {}
status:
  lastHeartbeatTime: "2023-11-27T12:04:56Z"
  mark: "0x26d9b723"
  phase: Ready
```

The `EgressGateway` Agent periodically updates the `status.lastHeartbeatTime` field based on `feature.tunnelUpdatePeriod`, while the `EgressGateway` Controller periodically checks all `EgressTunnel` instances based on `feature.tunnelMonitorPeriod`. If the sum of `status.lastHeartbeatTime` and `feature.eipEvictionTimeout` exceeds the current time, the Egress IP will be reassigned to another available node.

![egress-check](../../images/egress-check.svg)

## Troubleshooting Datapath Failover Issues

If issues arise with failover, follow these steps:

1. Review the `values.yaml` file used for deploying EgressGateway to ensure that failover-related parameters are correctly set. Specifically, make sure that the `eipEvictionTimeout` value is greater than the sum of `tunnelMonitorPeriod` and `tunnelUpdatePeriod`.

2. Run the following command to monitor the status of `EgressTunnel` instances. Check whether the selected node is in a `HeartbeatTimeout` state and verify if other nodes are in a `Ready` state.

    ```shell
    kubectl get egt -w
    ```
    ```
    NAME    TUNNELMAC           TUNNELIPV4        TUNNELIPV6   MARK         PHASE
    node1   66:50:85:cb:b2:bf   192.200.229.11    fd01::c486   0x26d9b723   Ready
    node2   66:d4:65:85:e2:c7   192.200.128.75    fd01::6676   0x26abf380   HeartbeatTimeout
    node3   66:c4:da:a7:58:25   192.200.101.153   fd01::edb5   0x26c4ce84   Ready
    ```

3. To check if there was an IP switch due to `HeartbeatTimeout`, search for logs containing `update tunnel status to HeartbeatTimeout` in the controller container.
