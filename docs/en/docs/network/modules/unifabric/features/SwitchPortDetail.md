# Switch Node Access

## Feature Description

The Switch Port Detail feature displays detailed information about switch ports, including port
status and neighbor device information. This feature connects to the switch through the gNMI
protocol to obtain port status and neighbor device information, and stores the data in a
Kubernetes Custom Resource.

## Field Description

```yaml
apiVersion: unifabric.io/v1beta1
kind: SwitchEndpoint
metadata:
  name: gpu-leaf-switch-1
spec:
  connection:
    gnmi:
      port: 8080
    host: 10.193.77.201
  group: gpu
  manufacturer: cloudnix
status:
  conditions:
    - lastTransitionTime: "2025-08-19T00:05:57Z"
      message: Successfully connected to SwitchEndpoint
      reason: Connected
      status: "True"
      type: Connected
  ports:
    details:
      - name: Ethernet0
        neighbor:
          portID: Ethernet0
          portName: Ethernet0
          sysName: SPINE01
        status: up
      - name: Ethernet8
        neighbor:
          portID: Ethernet8
          portName: Ethernet8
          sysName: SPINE01
        status: up
```

- name: The port name, for example Ethernet0 or Ethernet8.
- neighbor: Describes the neighbor device connected to this port, making it easier to locate the
  physical topology.
  - portID: The port identifier of the neighbor device. If the peer is a host, this is the MAC
    address; if the peer is a switch, this is the peer port name.
  - portName: The neighbor device port name, which is the NIC name or port name.
  - sysName: The system name of the neighbor device, for example SPINE01.

## Troubleshooting

If you encounter problems when using the Switch Port Detail feature, troubleshoot them as
follows:

1. Check whether the SwitchEndpoint resource exists in Kubernetes and whether its status is
   Connected.

    ```bash
    kubectl get switchendpoint -n unifabric
    ```

2. Check whether the Unifabric Pods in Kubernetes are running properly.

    ```bash
    kubectl get pods -n unifabric -o wide
    ```

3. Log in to the switch and run the `show lldp summary` command to check whether the port status
   and neighbors are normal.
4. Log in to the switch and run the `show logging` command to check whether the switch log
   contains any abnormal information.
