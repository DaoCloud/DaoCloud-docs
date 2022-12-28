#nmstate

With the advent of hybrid cloud, node network setup becomes more challenging. Different environments have different network requirements.
The Container Network Interface (CNI) standard implements a different solution, which solves the communication problem of Pods in the cluster, including setting IPs and creating routes for them.

In all of these cases, however, nodes must have networking set up before pods can be scheduled.
Setting up networking in a dynamic, heterogeneous cluster, with dynamic network requirements, is a challenge in itself.

The nmstate project aims to configure the network on the node through k8s CRD, which can simplify the network configuration to a certain extent.

## limit

`nmstate` depends on NetworkManager, so not all Linux distributions support it, such as ubuntu, etc. do not support it. And the version of NetworkManager must be `>= 1.20`

The version of NetworkManager can be checked by:

```shell
[root@master ~]# /usr/sbin/NetworkManager --version
1.22.8-4.el8
```

See the nmstate Helm chart README for more details.

## Install

```shell
helm repo add daocloud https://daocloud.github.io/network-charts-repackage/
helm install nmstate -n nmstate daocloud/nmstate --create-namespace
```

For more installation details, please refer to the Helm chart README file.

After the installation is complete, create a CR instance and trigger the nmstate controller to work:

```sh
cat <<EOF | kubectl create -f -
apiVersion: nmstate.io/v1
kind: NMState
metadata:
  name: nmstate
EOF
```

After the installation is complete, you can check whether it is working properly by the following methods:

```shell
[root@10-6-185-30 ~]# kubectl get nns
NAME AGE
10-6-185-30 3d4h
10-6-185-40 3d4h
```

Each nns object is nmstate to collect all network information of the node, including all interfaces, IP addresses, routes, etc.

## use

This section shows some examples.

- Configure an IP address for a node's NIC

    ```shell
    cat << EOF | kubectl apply -f -
    apiVersion: nmstate.io/v1
    kind: NodeNetworkConfigurationPolicy
    metadata:
      name: static-ip
    spec:
      nodeSelector:
        kubernetes.io/hostname: node02
      desiredState:
        interfaces:
        -name: eth1
          type: ethernet
          state: up
          ipv4:
            address:
            - ip: 10.244.0.2
              prefix-length: 24
            dhcp: false
            enabled: true
    ```

    in,
    
    - `nodeSelector`: indicates which node this network configuration will take effect on
    - `desiredState`: Indicates the desired configuration, including network card, IP, etc.

- create vlan subinterface

    ```shell
    cat << EOF | kubectl apply -f -
    apiVersion: nmstate.io/v1
    kind: NodeNetworkConfigurationPolicy
    metadata:
      name: vlan
    spec:
      desiredState:
        interfaces:
        - name: eth1.102
          type: vlan
          state: up
          vlan:
            id: 102
            base-iface: eth1
          ipv4:
            dhcp: true
            enabled: true
    ```

    This will create a vlan subinterface named eth1.102 on all nodes in the cluster.

- create bond interface

    ```shell
    cat << EOF | kubectl apply -f -
    apiVersion: nmstate.io/v1
    kind: NodeNetworkConfigurationPolicy
    metadata:
      name: bond-vlan30
    spec:
      nodeSelector:
        kubernetes.io/hostname: 10-6-185-30
      desiredState:
        interfaces:
        - name: bond0
          type: bond
          state: up
          ipv4:
            dhcp: false
            address:
            - ip: 172.39.0.30
              prefix-length: 16
            enabled: true
          ipv6:
            address:
            - ip: fc00:172:39::30
              prefix-length: 64
            enabled: true
          link-aggregation:
            mode: active-backup
            port:
            - ens161
            - ens256
        - name: bond0.144
          type: vlan
          state: up
          ipv4:
            address:
            -ip: 172.144.185.30
              prefix-length: 16
            dhcp: false
            enabled: true
          ipv6:
            address:
            - ip: fd00:144::172:144:185:30
              prefix-length: 64
            enabled: true
          vlan:
            base-iface: bond0
            id: 144
        - name: bond0.145
          type: vlan
          state: up
          ipv4:
            address:
            - ip: 172.145.185.30
              prefix-length: 16
            dhcp: false
            enabled: true
          ipv6:
            address:
            - ip: fd00:145::172:144:185:30
              prefix-length: 64
            enabled: true
          vlan:
            base-iface: bond0
            id: 145
    ```

After creating this object, it will do several things:

- Based on ens161 and ens256, create a bond0 interface, the mode is active and standby, and configure the IP address
- Based on bond0, create vlan subinterfaces: bond0.144 and bond0.145 respectively. And configure the IP address

After the object is created, you can check whether the configuration is complete and successful in the following ways:

```shell
[root@10-6-185-30]# kubectl get nncp
NAME STATUS REASON
bond-vlan30 Available Successfully Configured
```

This indicates that the configuration has been successful, and then check the interface:

```shell
[root@10-6-185-30]# ip a s bond0.144
90: bond0.144@bond0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 00:50:56:b4:e9:41 brd ff:ff:ff:ff:ff:ff
    inet 172.144.185.30/16 brd 172.144.255.255 scope global noprefixroute bond0.144
       valid_lft forever preferred_lft forever
    inet6 fd00:144::172:144:185:30/64 scope global noprefixroute
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feb4:e941/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
```

For more examples, please refer to: https://github.com/nmstate/kubernetes-nmstate/tree/main/docs/examples