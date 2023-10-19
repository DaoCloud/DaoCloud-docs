# 安装 Multus-underlay

本页介绍如何安装 Multus-underlay 组件。

!!! warning

    1. 目前 Multus-underlay 已经被标记为 deprecated 状态，可能在未来被移除，目前已经不再更新
    2. Spiderpool > v0.7.0 后支持安装 Multus，所以不需要再安装 Multus-underlay，并且 Multus-underlay
       大部分功能已经迁移到 [Spiderpool v0.7.0](https://github.com/spidernet-io/spiderpool/releases/tag/v0.7.0)，
       请使用 Spiderpool v0.7.0。
    3. 现在不再通过 Multus-underlay 安装 Sriov-CNI，而是通过 [sriov-network-operator](../sriov-network-operator/install.md)
       安装，请使用 [sriov-network-operator](../sriov-network-operator/index.md)

## 注意事项

- 默认 CNI：安装 Multus-underlay 之前，需要确认当前集群是否存在默认 CNI，比如 Calico 或者 Cilium，否则 Multus 可能会无法工作。
- Spiderpool：Multus-underlay 依赖 [Spiderpool](https://github.com/spidernet-io/spiderpool) 作为 `ipam`。
  安装 `Spiderpool` 请参考 [Install Spiderpool](../spiderpool/install.md)。
- 如需安装 SRIOV-CNI，需要确认节点是否为物理主机且节点拥有支持 SRIOV 的物理网卡。
  如果节点为 VM 虚拟机或者没有支持 SR-IOV 的网卡，那么 SR-IOV 将无法工作。
  详情参考 [sriov-device-plugin](https://github.com/k8snetworkplumbingwg/sriov-network-device-plugin)。
- 不建议同时安装 MacVLAN 和 SR-IOV。

## 安装步骤

请确认您的集群已成功接入`容器管理`平台，然后执行以下步骤安装 Multus-underlay。

1. 在左侧导航栏点击`容器管理`—>`集群列表`，然后找到准备安装 Multus-underlay 的集群名称。
   然后，在左侧导航栏中选择 `Helm 应用` -> `Helm 模板`，找到并点击 `multus-underlay`。

    ![helm repo](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/repo.png)

2. 进入安装界面，填写基础配置信息。命名空间选择 `kube-system`，并开启`就绪等待`:

    ![helm install-1](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/install1.png)

3. 为 Multus 配置默认 CNI：

    安装 Multus 之前，必须要先安装一种 CNI 作为默认CNI。注意: 保证选择的 Value 必须与集群目前安装的默认 CNI 保持一致。

    !!! note

        如果当前是通过 kubean 安装的集群，那么 value 为 calico 或者 cilium 中二选一。
        或通过查看主机 `/etc/cni/net.d/` 路径，按照字典顺序第一个 CNI 配置文件的 `name` key 所对应的 Value 值就为默认 CNI。比如：
        
        ```shell
        root@master:~# ls /etc/cni/net.d/
        10-calico.conflist  calico-kubeconfig
        root@master:~# cat /etc/cni/net.d/10-calico.conflist
        {
          "name": "k8s-pod-network",
          "cniVersion": "0.3.1",
        ...
        ```
        `name` 的值如果为 `k8s-pod-network`，那么这里就应该选中 `k8s-pod-network`。

        ![Default CNI](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/install2.png)

        如果当前集群是接入的第三方、calico 为 CNI 的集群，那么这里应该选择为 `k8s-pod-network`。
        同样，也可以通过查看主机上 `/etc/cni/net.d` 文件确认。

4. 配置目前集群 Service 和 Pod 的 CIDR:

    此步骤的目的是告知 [Meta-Plugins](https://github.com/spidernet-io/cni-plugins)
    集群的 CIDR，Meta-Plugins 会创建对应的路由规则，解决 Underlay CNI 的集群东西向通信问题。

    ![Cluster CIDR](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/install3.png)

    可通过查看 `configMap`: `kube-system/kubeadm-config` 获取目前集群中 Service 和 Pod 的 CIDR：

    ![kubeadm-config](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/kubeadm-config.png)

    !!! note

        如果为双栈集群，也需要填写 IPv6 的地址。
        如果 CNI 为 Calico 且 有多个 IP 池，Pod CIDR 可配置多个。

5. 安装 MacVLAN（可选，默认安装）：

    此步骤会根据配置创建 MacVLAN 对应的 Multus CRD 实例:

    ![macvlan](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/macvlan.png)

    - `Install Macvlan CNI`：true/false，是否创建 MacVLAN 的 Multus CRD 实例。
    - `Macvlan Type`：macvlan-overlay/macvlan-standalone，安装 MacVLAN CRD 实例的类型。

        - `macvlan-overlay`：此类型下，MacVLAN 会与默认 CNI 搭配使用（比如 Calico），这样会在 Pod 中插入两张网卡。
           分别是默认 CNI 和 MacVLAN 的网卡，前者用于解决 Pod 与集群东西向通信问题；后者用于 Pod 集群南北向通信。
        - `macvlan-standalone`：此类型下，Pod 中只会插入一张 MacVLAN 的网卡，只由其完成与集群东西向和南北向的通信问题。
      
    - `Multus CR Name`：Multus CRD 实例的名称。
    - `Master Interface`：MacVLAN 主接口的名称。注意：配置的主接口必须存在于主机上，否则 MacVLAN 无法工作。
    - `Vlan ID`：可选，MacVLAN 主接口的 Vlan tag。

6. 安装 SR-IOV（可选，默认不安装）：

    配置 SR-IOV Multus CRD：

    ![sriov_install](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/sriov_install.png)

    - `Install SRIOV CNI`：是否安装 SR-IOV，默认不安装。
    - `SRIOV Type`：安装 SR-IOV 的 Multus CRD 实例的类型，有以下几种：
      - `sriov-overlay`：此类型下，SR-IOV 会与默认 CNI 搭配使用（比如 Calico），这样会在 Pod 中插入两张网卡。
          分别是默认 CNI 和 SR-IOV 的网卡，前者用于解决 Pod 与集群东西向通信问题；后者用于 Pod 集群南北向通信。
      - `sriov-standalone`：此类型下，Pod 中只会插入一张 SR-IOV 的网卡，只由其完成与集群东西向和南北向的通信问题。
    - `SRIOV CR Name`：Multus CRD 实例的名称。
    - `Vlan ID`：可选，SR-IOV PF 的 Vlan tag。
    - `SRIOV Device Plugin Configuration`：用于发现主机上的 SR-IOV PF 和 VF device，筛选方式可以为：`vendors`、`devices`、`drivers`、`pfNames`。
        具体参考 [sriov-device-plugin-readme.md](https://github.com/k8snetworkplumbingwg/sriov-network-device-plugin/blob/master/README.md)。

    配置 SR-IOV Net-Device Plugin：

    - `vendors`：PCI 设备厂商号，如 '8086' 代表 Intel
    - `devices`：PCI 设备型号，如 '154c'
    - `drivers`：PCI 设备驱动，如 'mlx5_core'
    - `pfNames`：PF 设备的名称列表

    ![sriov-net-device](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/sriov-net-device.png)

    !!! note

        不建议同时启用 MacVLAN 和 SR-IOV。另外启用 SR-IOV 需要硬件支持，安装前确认物理主机的网卡是否支持 SR-IOV。

7. 配置完成，点击`安装`。

## 验证

1. 检查各组件是否正常 Running：

    包括 Multus、Meta-plugins、SR-IOV CNI（如果启用）、SRIOV-Device-Plugins（如果启用）。

    ![install_finished](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/install_finished.png)

2. 创建工作负载，以 MacVLAN 为例：

    - 如果 type 为 macvlan-overlay，那么需要在 Pod 的 Annotations 中插入以下的注解：

        ```yaml
          annotations:
            k8s.v1.cni.cncf.io/networks: kube-system/macvlan-vlan0
        ```

        `k8s.v1.cni.cncf.io/networks`：表示会在 Pod 中除默认 CNI 之外再插入一张 MacVLAN 网卡。

    - 如果 type 为 macvlan-standalone，那么需要在 Pod 的 Annotations 中插入以下的注解：

        ```yaml
          annotations:
            v1.multus-cni.io/default-network: kube-system/macvlan-vlan0
        ```

        `v1.multus-cni.io/default-network`：修改 Pod 的默认网卡。如果不指定，将通过集群默认 CNI 为 Pod 分配第一张网卡。

        以 type 为 macvlan-overlay 为例：

        ```yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: macvlan-overlay
          namespace: default
        spec:
          replicas: 2
          selector:
            matchLabels:
              app.kubernetes.io/instance: dao2048-macvlan-overlay
              app.kubernetes.io/name: dao2048-macvlan-overlay
          template:
            metadata:
              annotations:
                ipam.spidernet.io/ippool: |-
                  {
                      "interface": "net1",  # (1)
                      "ipv4": [
                        "172-81-0-1"
                      ],
                      "ipv6": [
                        "172-81-0-1-v6"
                      ]
                  }
                k8s.v1.cni.cncf.io/networks: kube-system/macvlan-vlan0  # (2)
                ...
        ```

        1. 指定 Pod 第二张网卡 (net1) 从哪一个 IP 池中分配 IP
        2. 设置 Pod 第二张网卡

        - `ipam.spidernet.io/ippool`：指定从哪一个 IP 池为 MacVLAN 网卡分配 IP 地址。
          如果不指定，将会从默认池中分配。更多 Spiderpool 使用说明请参考 [Spiderpool](../spiderpool/index.md)。
        - `k8s.v1.cni.cncf.io/networks`：通过指定 MacVLAN Multus CRD，为 Pod 再分配一张 MacVLAN 网卡 (net1)。

        创建成功：

        ```shell
        root@master:~# kubectl get po  -o wide | grep overlay
        macvlan-overlay-b968998d8-mbtbp           1/1     Running   0          54s     10.250.186.234   master   <none>           <none>
        macvlan-overlay-589d6ddc68-kk798          1/1     Running   0          43s     10.253.255.73    172-17-8-120   <none>           <none>
        ```

3. 测试连通性。

    可以看到 Pod 的第一张网卡仍然由 Calico 分配，第二张网卡由 MacVLAN 分配：

    ```shell
    root@master:~# kubectl exec -it macvlan-overlay-589d6ddc68-kk798 sh
    kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
    / # ip a
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
          valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host
          valid_lft forever preferred_lft forever
    2: tunl0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN qlen 1000
        link/ipip 0.0.0.0 brd 0.0.0.0
    4: eth0@if503978: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1430 qdisc noqueue state UP
        link/ether ba:b0:dc:d9:91:1c brd ff:ff:ff:ff:ff:ff
        inet 10.253.255.73/32 scope global eth0
          valid_lft forever preferred_lft forever
        inet6 fd00:10:244::eaa:bafd/128 scope global
          valid_lft forever preferred_lft forever
        inet6 fe80::b8b0:dcff:fed9:911c/64 scope link
          valid_lft forever preferred_lft forever
    5: net1@if7: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP
        link/ether 4e:31:cb:b5:68:13 brd ff:ff:ff:ff:ff:ff
        inet 172.17.8.193/21 brd 172.17.15.255 scope global net1
          valid_lft forever preferred_lft forever
        inet6 fd00:1033::172:17:8:14b/64 scope global
          valid_lft forever preferred_lft forever
        inet6 fe80::4c31:cbff:feb5:6813/64 scope link
          valid_lft forever preferred_lft forever
    ```

## 测试

MacVLAN 网卡的 IP 地址段从宿主机分配，所以在宿主机网络路由可达的情况下，可以直接访问该 Pod 的 MacVLAN 网卡，测试步骤如下：

1. 在集群节点中访问 `10.253.255.73` 和 `172.17.8.193`。

    ```shell
    # ping pod eth0
    root@master:~# ping 10.253.255.73
    PING 10.253.255.73 (10.253.255.73) 56(84) bytes of data.
    64 bytes from 10.253.255.73: icmp_seq=1 ttl=64 time=0.170 ms
    64 bytes from 10.253.255.73: icmp_seq=2 ttl=64 time=0.088 ms
    64 bytes from 10.253.255.73: icmp_seq=3 ttl=64 time=0.077 ms
    64 bytes from 10.253.255.73: icmp_seq=4 ttl=64 time=0.117 ms
    64 bytes from 10.253.255.73: icmp_seq=5 ttl=64 time=0.073 ms
    ^C
    --- 10.253.255.73 ping statistics ---
    5 packets transmitted, 5 received, 0% packet loss, time 4076ms
    rtt min/avg/max/mdev = 0.073/0.105/0.170/0.035 ms

    # ping pod net1
    root@master:~# ping 172.17.8.193
    PING 172.17.8.193 (172.17.8.193) 56(84) bytes of data.
    64 bytes from 172.17.8.193: icmp_seq=1 ttl=64 time=0.115 ms
    64 bytes from 172.17.8.193: icmp_seq=2 ttl=64 time=0.068 ms
    64 bytes from 172.17.8.193: icmp_seq=3 ttl=64 time=0.091 ms
    64 bytes from 172.17.8.193: icmp_seq=4 ttl=64 time=0.103 ms
    ^C
    --- 172.17.8.193 ping statistics ---
    4 packets transmitted, 4 received, 0% packet loss, time 3072ms
    rtt min/avg/max/mdev = 0.068/0.094/0.115/0.017 ms
    ```

2. 在集群外访问 `172.17.8.193`。

    ```shell
    $ ping 172.17.8.193
    PING 172.17.8.193 (172.17.8.193): 56 data bytes
    64 bytes from 172.17.8.193: icmp_seq=0 ttl=62 time=37.668 ms
    64 bytes from 172.17.8.193: icmp_seq=1 ttl=62 time=44.025 ms
    64 bytes from 172.17.8.193: icmp_seq=2 ttl=62 time=39.606 ms
    ^C64 bytes from 172.17.8.193: icmp_seq=3 ttl=62 time=40.599 ms

    --- 172.17.8.193 ping statistics ---
    4 packets transmitted, 4 packets received, 0.0% packet loss
    round-trip min/avg/max/stddev = 37.668/40.474/44.025/2.305 ms
    ```

3. 访问集群中的 Calico Pod。

    ```shell
    root@master:~# kubectl get po  -o wide | grep nginx
    nginx-8f458dc5b-kshpw                 1/1     Running   0          2d3h   10.250.186.210   172-17-8-110   <none>           <none>
    nginx-8f458dc5b-wgkpg                 1/1     Running   0          46h    10.253.255.72    172-17-8-120   <none>           <none>

    root@master:~# kubectl exec -it macvlan-overlay-b968998d8-mbtbp  sh
    kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
    / # ping 10.250.186.210
    PING 10.250.186.210 (10.250.186.210): 56 data bytes
    64 bytes from 10.250.186.210: seq=0 ttl=63 time=0.247 ms
    64 bytes from 10.250.186.210: seq=1 ttl=63 time=0.151 ms
    ^C
    --- 10.250.186.210 ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 0.151/0.199/0.247 ms
    / # ping 10.253.255.72
    PING 10.253.255.72 (10.253.255.72): 56 data bytes
    64 bytes from 10.253.255.72: seq=0 ttl=62 time=0.596 ms
    64 bytes from 10.253.255.72: seq=1 ttl=62 time=0.428 ms
    64 bytes from 10.253.255.72: seq=2 ttl=62 time=0.387 ms
    ^C
    --- 10.253.255.72 ping statistics ---
    3 packets transmitted, 3 packets received, 0% packet loss
    round-trip min/avg/max = 0.387/0.470/0.596 ms
    ```

4. 访问 ClusterIP。

    ```shell
    root@master:~# kubectl get svc | grep kubernetes
    Kubernetes               ClusterIP   172.96.0.1             <none>        443/TCP                                       78d
    root@172-17-8-110:~# kubectl get svc | grep nginx
    nginx-172-17-8-110-v4    NodePort    172.96.53.151          <none>        80:31696/TCP,5201:32137/TCP,12865:31253/TCP   78d
    nginx-172-17-8-110-v6    NodePort    2001:4860:fd00::85db   <none>        80:32452/TCP,5201:32658/TCP,12865:32231/TCP   78d
    root@master:~# kubectl exec -it macvlan-overlay-5c87d74c46-fzkln sh
    kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
    / # curl 172.96.53.151
    <!DOCTYPE html>
    <html>
    <head>
    <title>Welcome to nginx!</title>
    <style>
    html { color-scheme: light dark; }
    body { width: 35em; margin: 0 auto;
    font-family: Tahoma, Verdana, Arial, sans-serif; }
    </style>
    </head>
    <body>
    <h1>Welcome to nginx!</h1>
    <p>If you see this page, the nginx web server is successfully installed and
    working. Further configuration is required.</p>

    <p>For online documentation and support please refer to
    <a href="http://nginx.org/">nginx.org</a>.<br/>
    Commercial support is available at
    <a href="http://nginx.com/">nginx.com</a>.</p>

    <p><em>Thank you for using nginx.</em></p>
    </body>
    </html>
    ```

## 卸载

卸载 Multus-underlay 还需要删除每个节点上的 Multus 配置文件：

```shell
root@master:~# rm /etc/cni/net.d/00-multus.conf
root@master:~# rm -rf /etc/cni/net.d/multus.d
```
