# Metallb 升级及调试

- [Metallb 升级问题](#metallb_1)
- [Metallb Debug](#metallb_2)

## Metallb 升级问题

如果您在安装 Metallb 时未启用 Metallb ARP Mode, 请务必 **不要通过在页面点击升级按钮** 来进行 Metallb 升级，否则会导致 Metallb 无法正常工作。

您需要通过以下的步骤来手动开启 Metallb ARP Mode:

- 前往自定义资源模块创建 L2Advertisement 资源:

![metallb_l2advertisement](../../images/metallb_l2avertisement.png)

点击 `YAML 创建`:

```yaml
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
  metadata:
    name: default
    namespace: metallb-system
```

以上 YAML 表示所有 Metallb IP 池都会通过该 L2Advertisement 资源宣告，如果您的集群同时运行 BGP 和 ARP 两种模式。可以通过以下方式指定特定池进行 ARP 宣告：

```yaml
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: default
  namespace: metallb-system
spec:
  ipAddressPools:
  - default-pool
```

以上配置表示只有 `default-pool` 的 IP 池会通过该 L2Advertisement 资源宣告 ARP。

- 前往自定义资源模块创建 L2Advertisement 资源:

![metallb_ipaddresspool](../../images/metallb-ipaddresspool.png)

点击 `YAML 创建`，创建以下内容:

```yaml
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: default
  namespace: metallb-system
spec:
  addresses:
  - 192.168.10.0/24
```

以上 YAML 表示创建一个名为 `default` 的 IP 池，IP 地址为 `192.168.10.0/24`。

## Metallb 调试

如果您使用 Metallb 遇到网络连通性问题，按照以下步骤排查：

- 检查 L2Advertisement 资源是否存在，如果 L2Advertisement 资源配置了 NodeSelector，请确认有集群是否有节点配置该 Label。

    ```bash
    kubectl get l2advertisement -n metallb-system
    ```

- 请确认该 LoadBalancer 是否存在正常运行的 Endpoint。

- 检查 LoadBalaner Service 的注解是否正确

- 检查 LoadBalaner Service 所用的 IP 池是否有充足的 IP

- 获取您的 LoadBalancer Service 的事件，获取关键错误信息:

    ```bash
    kubectl describe svc -n <lb_service_ns> <lb_service_name>
    ```

    > 如果未获取到任何事件，请重建服务然后获取。

- 请确认您是否单集群节点或所有节点都是 Controller Plane 节点，如果是请清理 Controller Plane 节点上的 Labels: `node.kubernetes.io/exclude-from-external-load-balancers`。

    ```bash
    kubectl label nodes <Your_Controller_Plane_Node> node.kubernetes.io/exclude-from-external-load-balancers-
    ```

- 通过服务名称过滤 Metallb 组件日志，查看是否有相关错误信息。如果未有明显日志请编辑 metallb-speaker DaemonSet 的日志登记为 Debug。

    ```bash
    kubectl logs -n metallb-system controller-xxxx | grep <lb_service_name>

    kubectl logs -n metallb-system speaker-xxxx | grep <lb_service_name>
    ```

