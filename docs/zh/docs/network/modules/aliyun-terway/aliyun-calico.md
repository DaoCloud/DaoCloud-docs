# 阿里云运行 Calico 

本文将介绍如何在阿里云自建集群上，安装使用 [Calico](https://github.com/projectcalico/calico) 作为集群 CNI。

## 安装集群

在阿里云上准备好一套自建 Kubernetes 集群，或按照 [搭建 Kubernetes 集群](usage.md#搭建Kubernetes集群) 文档手动搭建一套集群。 集群安装完成之后，下载 Calico 的部署清单文件:

```shell
~# wget https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/calico.yaml
```

> 推荐使用以下命令加速镜像拉取: sed -i 's?docker.io?docker.m.daocloud.io?g' calico.yaml

下面分别演示使用隧道模式和路由模式:

## 隧道模式(IPIP)

Vxlan 和 IPIP 协议不依赖底层网络如何实现，通过封装构建一个大二层覆盖网络以实现网络联通，所以能够运行在大多数公有云上，此模式不依赖 [CCM]()。Calico 部署清单文件默认使用 IPIP 模式，使用以下命令安装:

```shell
~# kubectl apply -f calico.yaml
```

等待安装完成:

```shell
# kubectl get po -n kube-system | grep calico
calico-kube-controllers-769669454f-c9pw6                    1/1     Running     0              1m
calico-node-679wb                                           1/1     Running     0              1m
calico-node-6wzkj                                           1/1     Running     0              1m
```

创建测试 deployment，验证联通性:

```shell
~# kubectl  get po -o wide
NAME                    READY   STATUS    RESTARTS   AGE   IP               NODE                  NOMINATED NODE   READINESS GATES
test-77877f4755-24gqt   1/1     Running   0          13m   10.244.236.193   cn-chengdu.i-2vcxxr   <none>           <none>
test-77877f4755-2d6r8   1/1     Running   0          13m   10.244.140.2     cn-chengdu.i-2vcxxs   <none>           <none>
~# kubectl  get svc
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP   172.21.0.1     <none>        443/TCP        31d
test         ClusterIP   172.21.0.83    <none>        80/TCP         2m

~# # 跨节点访问 Pod 
~# kubectl exec test-77877f4755-24gqt -- ping -c1 10.244.140.2
PING 10.244.140.2 (10.244.140.2) 56(84) bytes of data.
64 bytes from 10.244.140.2: icmp_seq=1 ttl=62 time=0.471 ms

--- 10.244.140.2 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.471/0.471/0.471/0.000 ms

~# # 访问外部
~# kubectl exec test-77877f4755-24gqt -- ping -c1 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=109 time=38.5 ms

--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 38.479/38.479/38.479/0.000 ms

~# # 访问 ClusterIP
~# kubectl exec test-77877f4755-24gqt -- curl -i 172.21.0.83
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   153  100   153    0     0  93463      0 --:--:-- --:--:-- --:--:--  149k
HTTP/1.1 200 OK
Content-Type: application/json
Date: Wed, 27 Sep 2023 08:15:34 GMT
Content-Length: 153
```

经过测试: IPIP 和 Vxlan 模式下各种通信正常，并且不依赖 [CCM]()发布路由以实现 Pod 间的通信, 但 LoadBalancer Service 的实现依赖 [CCM]()

## 非隧道模式

当 Calico 运行在非隧道模式，Pod 之间通信直接对接底层网络，所以常常需要一些其他设备发布路由，以使 Pod 子网路由集群外可达。在非公有云上需要支持运行 BGP 协议的路由器，在公有云上需要支持一些往外的组件发布 Pod 子网路由到 VPC 网络，如阿里云的 [CCM]()。
但 [CCM]()组件发布路由常常以节点为单位，这就要求不同节点的 Pod 属于不同的段，同一节点的 Pod 属于同一个段。而 Calico 自有的 IPAM: calico-ipam 无法满足这一点(calico-ipam 以 block 为单位, 而不是以节点为单位)。所以针对这种情况，我们可以通过切换 ipam 为
`host-local` 或 `spiderpool` 来解决。

> 节点的 PodCIDR 对应 Node.spec.podCIDR 字段

* host-local: 非常简单的 ipam，从节点的 PodCIDR 中分配 IP, 分配的数据存放于本地磁盘, 无其他 ipam 能力
* spiderpool: 提供非常强大的 IPAM 能力，支持按节点分配IP、支持固定 IP、多网卡分配 IP 等高级特性

在介绍如何使用之前，需要先安装 [CCM组件](),参考 [安装CCM文档](usage.md#安装CCM组件，发布VPC路由), 并且切换 Calico 为 非隧道模式，修改 calico-node daemonSet 部署清单文件中以下几个环境变量为 Never:

```shell
            # Enable IPIP
            - name: CALICO_IPV4POOL_IPIP
              value: "Never"
            # Enable or Disable VXLAN on the default IP pool.
            - name: CALICO_IPV4POOL_VXLAN
              value: "Never"
            # Enable or Disable VXLAN on the default IPv6 IP pool.
            - name: CALICO_IPV6POOL_VXLAN
              value: "Never"
            # Set MTU for tunnel device used if ipip is enabled
```

### Host-local 作为 IPAM

首先切换 IPAM 为 `host-local`，这需要修改 Calico 安装清单文件中 ConfigMap, 如下:

```shell
# Source: calico/templates/calico-config.yaml
# This ConfigMap is used to configure a self-hosted Calico installation.
kind: ConfigMap
apiVersion: v1
metadata:
  name: calico-config
  namespace: kube-system
data:
  # Typha is disabled.
  typha_service_name: "none"
  # Configure the backend to use.
  calico_backend: "bird"

  # Configure the MTU to use for workload interfaces and tunnels.
  # By default, MTU is auto-detected, and explicitly setting this field should not be required.
  # You can override auto-detection by providing a non-zero value.
  veth_mtu: "0"

  # The CNI network configuration to install on each node. The special
  # values in this config will be automatically populated.
  cni_network_config: |-
    {
      "name": "k8s-pod-network",
      "cniVersion": "0.3.1",
      "plugins": [
        {
          "type": "calico",
          "log_level": "info",
          "log_file_path": "/var/log/calico/cni/cni.log",
          "datastore_type": "kubernetes",
          "nodename": "__KUBERNETES_NODE_NAME__",
          "mtu": __CNI_MTU__,
          "ipam": {
                  "type": "host-local",
                  "ranges": [[{ "subnet": "usePodCidr" }]]
          },
          "policy": {
              "type": "k8s"
          },
          "kubernetes": {
              "kubeconfig": "__KUBECONFIG_FILEPATH__"
          }
        },
        {
          "type": "portmap",
          "snat": true,
          "capabilities": {"portMappings": true}
        },
        {
          "type": "bandwidth",
          "capabilities": {"bandwidth": true}
        }
      ]
    }
---
```

> ipam 部分切换为 host-local, 并且指定使用节点的 PodCIDR 作为 Pod 的子网

安装并等待 Calico 就绪之后，创建测试应用可以发现 Pod 的 IP 属于节点 的 PodCIDR(10.244.0.0/24 和 10.244.1.0/24):

```shell
~# k get po -o wide
NAME                    READY   STATUS    RESTARTS   AGE   IP           NODE                  NOMINATED NODE   READINESS GATES
test-77877f4755-58hlc   1/1     Running   0          5s    10.244.0.2   cn-chengdu.i-2vcxxr   <none>           <none>
test-77877f4755-npcgs   1/1     Running   0          5s    10.244.1.2   cn-chengdu.i-2vcxxs   <none>           <none>
```

经过测试，Pod 的各种通信正常。

## Spiderpool 作为 IPAM

1. 首先切换 IPAM 为 `spiderpool`，这需要修改 Calico 安装清单文件中 ConfigMap, 如下:

```shell
# Source: calico/templates/calico-config.yaml
# This ConfigMap is used to configure a self-hosted Calico installation.
kind: ConfigMap
apiVersion: v1
metadata:
  name: calico-config
  namespace: kube-system
data:
  # Typha is disabled.
  typha_service_name: "none"
  # Configure the backend to use.
  calico_backend: "bird"

  # Configure the MTU to use for workload interfaces and tunnels.
  # By default, MTU is auto-detected, and explicitly setting this field should not be required.
  # You can override auto-detection by providing a non-zero value.
  veth_mtu: "0"

  # The CNI network configuration to install on each node. The special
  # values in this config will be automatically populated.
  cni_network_config: |-
    {
      "name": "k8s-pod-network",
      "cniVersion": "0.3.1",
      "plugins": [
        {
          "type": "calico",
          "log_level": "info",
          "log_file_path": "/var/log/calico/cni/cni.log",
          "datastore_type": "kubernetes",
          "nodename": "__KUBERNETES_NODE_NAME__",
          "mtu": __CNI_MTU__,
          "ipam": {
                  "type": "spiderpool"
          },
          "policy": {
              "type": "k8s"
          },
          "kubernetes": {
              "kubeconfig": "__KUBECONFIG_FILEPATH__"
          }
        },
        {
          "type": "portmap",
          "snat": true,
          "capabilities": {"portMappings": true}
        },
        {
          "type": "bandwidth",
          "capabilities": {"bandwidth": true}
        }
      ]
    }
```

切换 IPAM 为 Spiderpool 并等待就绪

> 如果遇到 Calico 无法启动，并报以下错误，可以尝试删除每个节点 `/var/lib/cni/networks/k8s-pod-network/`

```shell
2023-09-27 10:14:42.096 [ERROR][1] ipam_plugin.go 106: failed to migrate ipam, retrying... error=failed to get add IPIP tunnel addr 10.244.1.1: The provided IP address is not in a configured pool
```


2. 安装 Spiderpool

使用以下命令安装 Spiderpool:

```shell
~# helm repo add spiderpool https://spidernet-io.github.io/spiderpool
~# helm repo update spiderpool
~# helm install spiderpool spiderpool/spiderpool --namespace kube-system --wait
```

> 需要提前安装 Helm 二进制
> Spiderpool 默认会安装 Multus 组件，如果你不需要 Multus 或已经安装 Multus，可以使用 `--set multus.multusCNI.install=false"` 关闭安装 Multus。

安装完成之后，需要为每个节点的 podCIDR 创建一个对应的 Spiderpool IP 池供 Pod 使用:

```shell
~# kubectl  get nodes -o=custom-columns='NAME:.metadata.name,podCIDR:.spec.podCIDR'
NAME                  podCIDR
cn-chengdu.i-2vcxxr   10.244.0.0/24
cn-chengdu.i-2vcxxs   10.244.1.0/24
```

创建以下 Spiderpool IP 池:

```yaml
apiVersion: spiderpool.spidernet.io/v2beta1
kind: SpiderIPPool
metadata:
  name: cn-chengdu.i-2vcxxr
spec:
  default: true
  ips:
  - 10.244.0.1-10.244.0.253
  subnet: 10.244.0.0/16
  nodeName:
  - cn-chengdu.i-2vcxxr
---
apiVersion: spiderpool.spidernet.io/v2beta1
kind: SpiderIPPool
metadata:
  name: cn-chengdu.i-2vcxxs
spec:
  default: true
  ips:
  - 10.244.1.1-10.244.1.253
  subnet: 10.244.0.0/16
  nodeName:
  - cn-chengdu.i-2vcxxs
```

> 注意 ips 中属于对应 nodeName 节点的 podCIDR 

3. 创建测试应用，并测试联通性

```shell
~# kubectl get po -o wide
NAME                    READY   STATUS    RESTARTS   AGE   IP             NODE                                NOMINATED NODE   READINESS GATES
test-77877f4755-nhm4f   1/1     Running   0          27s   10.244.0.179   cn-chengdu.i-2vcxxr   <none>           <none>
test-77877f4755-sgqbx   1/1     Running   0          27s   10.244.1.193   cn-chengdu.i-2vcxxs   <none>           <none>
~# kubectl get svc
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP   172.21.0.1     <none>        443/TCP        31d
test         ClusterIP   172.21.0.166   <none>        80/TCP         3m43s
```

```shell
~# kubectl exec test-77877f4755-nhm4f -- ping -c1 10.244.1.193
PING 10.244.1.193 (10.244.1.193) 56(84) bytes of data.
64 bytes from 10.244.1.193: icmp_seq=1 ttl=62 time=0.434 ms

--- 10.244.1.193 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.434/0.434/0.434/0.000 ms
```

测试访问 ClusterIP:

```shell
~# kubectl  exec test-77877f4755-nhm4f -- curl -i 172.21.0.166
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   153  100   153    0     0   127k      0 --:--:-- --:--:-- --:--:--  149k
HTTP/1.1 200 OK
Content-Type: application/json
Date: Wed, 27 Sep 2023 10:27:48 GMT
Content-Length: 153
```

经过测试，Pod 各种联通性正常。另外 Calico 创建的 Pod 也可以使用 Spiderpool 的其他高级 IPAM 能力。
