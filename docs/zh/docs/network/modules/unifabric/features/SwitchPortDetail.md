# 交换机节点接入

## 功能描述

Switch Port Detail 功能用于展示交换机端口的详细信息，包括端口状态、邻居设备信息等。该功能通过 gNMI 协议连接到交换机，获取端口状态和邻居设备信息，并将其存储在 Kubernetes 的 Custom Resource 中。

## 字段说明

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

- name: 端口名称，例如 Ethernet0、Ethernet8。
- neighbor: 描述该端口所连接的邻居设备信息，便于定位物理拓扑。
  - portID: 邻居设备的端口标识符，如果对端为主机则为 mac 地址，如果是交换机则为 peer port 名称。
  - portName: 邻居设备端口名称，为网卡名称或端口名称。
  - sysName: 邻居设备的系统名称，例如 SPINE01

## 问题排查

如果在使用 Switch Port Detail 功能时遇到问题，可以按照以下步骤进行排查：

1. 检查 Kubernetes 中的 SwitchEndpoint 资源是否存在，并且状态为 Connected。

    ```bash
    kubectl get switchendpoint -n unifabric
    ```

2. 检查 Kubernetes 中的 Unifabric Pod 是否正常运行。

    ```bash
    kubectl get pods -n unifabric -o wide
    ```

3. 登录交换机执行 `show lldp summary` 命令，检查端口状态是否正常，邻居是否正常。
4. 登录交换机执行 `show logging` 命令，检查交换机日志是否有异常信息。
