# 在阿里云上运行 Cilium

本文将介绍如何在阿里云自建 Kubernetes 集群上使用 Cilium 作为集群 CNI，您能够在阿里云上体验 Cilium 的各种能力，包括网络加速、网络策略等。

> 注意: 使用 Cilium 有内核要求，请检查您的 ECS 实例是否满足 Cilium 最低内核版本要求

## 安装集群

在阿里云上准备好一套自建 Kubernetes 集群，或按照 [搭建 Kubernetes 集群](usage.md#搭建Kubernetes集群) 文档手动搭建一套集群。

## 安装 Cilium

使用 Cilium 二进制安装，首先参考[官方文档](https://docs.cilium.io/en/stable/gettingstarted/k8s-install-default/) 安装 Cilium 二进制:

```shell
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
```

在阿里云上，支持 Cilium 以 tunnel 和 native 模式运行，这两种方式部署参数稍些不同, 下面将单独介绍:

### Tunnel 模式

Cilium tunnel 模式支持 Vxlan(默认) 和 Geneve 协议，这类似 Calico 的隧道模式。在这种模式下，Cilium 不关系底层网络如何实现，也不需要跟它们对接。通过 Vxlan 等协议将 Pod 网络虚拟化一个二层覆盖网络，然后接入到主机网络，所以
在这种模式下，Cilium 不依赖类似 CCM 等插件发布 Pod 的路由。所以在这个模式下，您不需要安装 CCM。使用下面的命令安装:

```shell
cilium install 
```

> 所有参数都为默认情况下，Cilium 基于 Vxlan 协议封装 Pod 数据包

等待 Cilium 组件 Running，创建测试应用测试通信是否正常:

```shell
$ kubectl  get po -o wide
NAME                    READY   STATUS    RESTARTS   AGE   IP               NODE                  NOMINATED NODE   READINESS GATES
test-77877f4755-2jz2c   1/1     Running   0          1m   10.244.1.39       cn-chengdu.i-2vcxxr   <none>           <none>
test-77877f4755-rjlg6   1/1     Running   0          1m   10.244.0.86     cn-chengdu.i-2vcxxs   <none>           <none>
$ kubectl  get svc
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP   172.21.0.1     <none>        443/TCP        32d
test         ClusterIP   172.21.0.53    <none>        80/TCP         2m

# 跨节点访问 Pod
$ kubectl  exec test-77877f4755-2jz2c -- ping -c1 10.244.0.86
PING 10.244.0.86 (10.244.0.86) 56(84) bytes of data.
64 bytes from 10.244.0.86: icmp_seq=1 ttl=63 time=0.571 ms

--- 10.244.0.86 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.571/0.571/0.571/0.000 ms

# 访问外部
$ kubectl exec test-77877f4755-24gqt -- ping -c1 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=107 time=63.8 ms

--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 63.758/63.758/63.758/0.000 ms

# 访问 ClusterIP
$ kubectl exec test-77877f4755-24gqt -- curl -i 172.21.0.53
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 28 Sep 2023 03:54:28 GMT
Content-Length: 151
```

经过测试，Pod 各种连通性正常。

### Native 模式

Cilium 支持在阿里云上运行 Native 模式，在此模式下，Pod 网络直接对接底层网络，没有额外封装，所以性能相对较好。但需要依赖 CCM 组件发布 Pod 子网路由到 VPC 网络，另外 Cilium 需要做一些特殊配置, 参考以下命令:

> 安装 CCM，参考 [安装CCM文档](usage.md#安装CCM组件，发布VPC路由)

```shell
cilium install --set ipam.mode=kubernetes --set routingMode=native --set ipv4NativeRoutingCIDR=10.244.0.0/16 
```

> ipam.mode 需要调整为 kubernetes，使 Pod 的 IP 从各自节点的 podCIDR 中分配
> routingMode 设置为 native 模式，而不是默认的隧道模式
> ipv4NativeRoutingCIDR 需要设置为需要路由发布的子网，这里填集群的 ClusterCIDR 即可(你可以通过查看 kubeadm-config configmap 找到)

等待 Cilium Running，创建测试应用，验证连通性:

```shell
$ kubectl  get po -o wide
NAME                    READY   STATUS    RESTARTS   AGE   IP             NODE                                NOMINATED NODE   READINESS GATES
test-77877f4755-v9mrj   1/1     Running   0          4s    10.244.1.166   cn-chengdu.i-2vc5zub002vrlwursb4s   <none>           <none>
test-77877f4755-w95wn   1/1     Running   0          4s    10.244.0.98    cn-chengdu.i-2vc5zub002vrlwursb4r   <none>           <none>
$ kubectl  get svc
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP   172.21.0.1     <none>        443/TCP        31d
test         ClusterIP   172.21.0.98    <none>        80/TCP         16s
```

可以发现 Pod 的 IP 段与节点绑定，测试连通性:

```shell
# Pod 跨节点
$ kubectl  exec test-77877f4755-v9mrj -- ping -c1 10.244.0.98
PING 10.244.0.98 (10.244.0.98) 56(84) bytes of data.
64 bytes from 10.244.0.98: icmp_seq=1 ttl=60 time=0.800 ms

--- 10.244.0.98 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.800/0.800/0.800/0.000 ms

# Pod 访问 Service
$ kubectl  exec test-77877f4755-v9mrj -- curl -i 172.21.0.98
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   152  100   152    0     0  32871      0 --:--:-- --:--:-- --:--:-- 38000
HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 28 Sep 2023 04:17:33 GMT
Content-Length: 152
```

经过测试， Pod 各种连通性正常。