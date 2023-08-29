# Spiderpool：Calico 固定应用 IP 的一种新选择

![spiderpool](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/spiderpool.png)

**Calico 是一套开源的网络和网络安全解决方案**，也是作为 Kubernetes 容器网络解决方案 (CNI: Container Network Interface) 的一种实现。
它基于 Linux 纯三层路由实现，在一些场景下用户可以将 Pod 子网的路由通过 Calico BGP 模式宣告到网关，
来自集群外的客户端可以直接通过 Pod 的 IP 访问 Pod，同时还可以保留客户端的源 IP。

## 当前痛点

在 Calico Underlay 网络模式下，用户还希望 Deployment 或 StatefulSet 类型应用的 IP 地址，能够被固定或是在一个指定的 IP 范围中浮动，因为:

- Pod 的 IP 地址常常受防火墙策略管控，防火墙只会允许特定的 IP 或者 IP 范围内的目标访问
- 传统微服务应用直接使用 Pod IP 进行微服务注册
- 一些场景下业务 IP 为固定的 IP，不会变化

Calico 通过在 Pod 中注入注解: `cni.projectcalico.org/ipAddrs` 可以实现 Pod 级别的 IP 固定，但是 **在使用中我们发现以下不足** :

- 固定 IP 只在 Pod 级别生效，对 Deployment、StatefulSet 类型无能为力；
- 需要管理员保证 Pod 的注解 IP 是不重叠的，避免出现 IP冲突。尤其是在大规模集群下，难以排查冲突的 IP；
- 固定 IP 地址的配置、管理繁琐，不具有云原生化。

## 解决方式：[Spiderpool](https://github.com/spidernet-io/spiderpool)

针对上述不足，我们尝试通过 Spiderpool 来实现这点需求。
Spiderpool 是一个 Kubernetes 的 IPAM 插件项目，其主要针对于 Underlay 网络的 IP 地址管理需求而设计，
能够为任何兼容第三方 IPAM 插件的 CNI 项目所使用。它主要具有以下几个特点：

- 能为 Deployment、StatefulSet 类型自动化分配固定 IP 地址，并且做到 IP 地址数量随副本数量自动扩缩容
- 以 CRD 方式管理、配置 IP 池，极大减少运维成本
- 支持第三方控制器创建的 Pod
- 支持为 Pod 多网卡指定不同子网

下面将对 Spiderpool 进行展开介绍。

## 安装 Spiderpool

以下是笔者参考
[Spiderpool 官方文档](https://spidernet-io.github.io/spiderpool/usage/get-started-calico/#configure-calico-bgp-optional)搭建了一套
Calico BGP 模式搭配 Spiderpool 的环境，网络环境拓扑图如下:

![spiderpool](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/spiderpool01.png)

根据自身环境创建 SpiderSubnet 实例: nginx-subnet-v4，体验 Spiderpool 固定 IP 等功能。

```none
[root@master ~]# kubectl get ss
NAME              VERSION   SUBNET          ALLOCATED-IP-COUNT   TOTAL-IP-COUNT
nginx-subnet-v4   4         10.244.0.0/16   0                    25602
```

## 自动为应用固定 IP 池

该功能支持从 SpiderSubnet(10.244.0.0/16) 子网中自动创建 IP 池，并绑定到应用 Pod。并且支持 Pod IP 固定、IP 池数量随副本数量自动扩缩容等功能。

使用 Spiderpool 自动池功能, 创建两个副本的 Nginx Deployment 应用:

```shell
  cat <<EOF | kubectl create -f -
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: nginx
  spec:
    replicas: 2
    selector:
      matchLabels:
        app: nginx
    template:
      metadata:
        annotations:
          ipam.spidernet.io/subnet: '{"ipv4":["nginx-subnet-v4"]}'
          ipam.spidernet.io/ippool-ip-number: '+3'
        labels:
          app: nginx
      spec:
        containers:
        - name: nginx
          image: nginx
          imagePullPolicy: IfNotPresent
          ports:
          - name: http
            containerPort: 80
            protocol: TCP
```

- ipam.spidernet.io/subnet：Spiderpool 从 "nginx-subnet-v4" 子网中随机选择一些 IP 来创建固定 IP 池，并与应用绑定
- ipam.spidernet.io/ippool-ip-number：'+3' 表示 IP 池的 IP 总量为比副本数多三个，解决应用滚动发布时有临时 IP 可用

当应用 Deployment 被创建，Spiderpool 中自动创建了一个名为 auto-nginx-v4-eth0-452e737e5e12 的 IP 池，
并与应用绑定。IP 范围为：10.244.100.90-10.244.100.95，池 IP 数量为 5：

```none
[root@master1 ~]# kubectl get po -o wide
NAME                     READY   STATUS        RESTARTS   AGE     IP              NODE      NOMINATED NODE   READINESS GATES
nginx-644659db67-6lsmm   1/1     Running       0          12s     10.244.100.93    worker5   <none>           <none>
nginx-644659db67-n7ttd   1/1     Running       0          12s     10.244.100.91    master1   <none>           <none>

[root@master1 ~]# kubectl get sp
NAME                              VERSION   SUBNET          ALLOCATED-IP-COUNT   TOTAL-IP-COUNT   DEFAULT   DISABLE
auto-nginx-v4-eth0-452e737e5e12   4         10.244.0.0/16   2                    5                false     false

[root@master ~]# kubectl get sp auto-nginx-v4-eth0-452e737e5e12 -o jsonpath='{.spec.ips}' 
["10.244.100.90-10.244.100.95"]
```

Pod 的 IP 被固定在自动池: auto-nginx-v4-eth0-452e737e5e12(10.244.100.90-10.244.100.95) 中范围内，重启 Pod 其 IP 也被固定在此范围内:

```none
[root@master1 ~]# kubectl get po -o wide
NAME                     READY   STATUS        RESTARTS   AGE     IP              NODE      NOMINATED NODE   READINESS GATES
nginx-644659db67-szgcg   1/1     Running       0          23s     10.244.100.90    worker5   <none>           <none>
nginx-644659db67-98rcg   1/1     Running       0          23s     10.244.100.92    master1   <none>           <none>
```

扩容副本，新副本的 IP 地址从自动池: auto-nginx-v4-eth0-452e737e5e12(10.244.100.90-10.244.100.95) 中自动分配，并且 IP 池随副本数量自动扩容:

```none
[root@master1 ~]# kubectl scale deploy nginx --replicas 3  # scale pods
deployment.apps/nginx scaled

[root@master1 ~]# kubectl get po -o wide
NAME                     READY   STATUS        RESTARTS   AGE     IP              NODE      NOMINATED NODE   READINESS GATES
nginx-644659db67-szgcg   1/1     Running       0          1m     10.244.100.90    worker5   <none>           <none>
nginx-644659db67-98rcg   1/1     Running       0          1m     10.244.100.92    master1   <none>           <none>
nginx-644659db67-brqdg   1/1     Running       0          10s    10.244.100.94    master1   <none>           <none>

[root@master1 ~]# kubectl get sp
NAME                              VERSION   SUBNET          ALLOCATED-IP-COUNT   TOTAL-IP-COUNT   DEFAULT   DISABLE
auto-nginx-v4-eth0-452e737e5e12   4         10.244.0.0/16   3                    6                false     false
```

## 手动指定 IP 池

在某些场景下，用户希望直接应用 IP 从一个固定的 IP 范围中分配，而不是由 Spiderpool 随机分配，下面是将展示此功能:

创建 IP 池:

```shell
cat << EOF | kubectl apply -f -
apiVersion: spiderpool.spidernet.io/v2beta1
kind: SpiderIPPool
metadata:
  name: nginx-v4-ippool
  spec:
    ipVersion: 4
    subnet: 10.244.0.0/16
    ips:
    - 10.244.120.10-10.244.120.20
```

spec.subnet 表示该 IP 池属于哪一个子网

spec.ips 固定 IP 地址范围，范围为 10.244.120.10-10.244.120.20，共计 10 个 IP

通过注解 `ipam.spidernet.io/ippool` 手动指定 IP 池：nginx-v4-ippool，创建应用：nginx-m：

```shell
  cat <<EOF | kubectl create -f -
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: nginx-m
  spec:
    replicas: 2
    selector:
      matchLabels:
        app: nginx
    template:
      metadata:
        annotations:
         ipam.spidernet.io/ippool: '{"ipv4":["nginx-v4-ippool"]}'
        labels:
          app: nginx
      spec:
        containers:
        - name: nginx
          image: nginx
          imagePullPolicy: IfNotPresent
          ports:
          - name: http
            containerPort: 80
            protocol: TCP
```

Spiderpool 从 nginx-v4-ippool 池中分配两个 IP 并绑定到应用。Pod 无论重启或是扩容，仍然从该池中分配 IP ，达到固定 IP 的效果:

```none
[root@master1 ~]# kubectl get po -o wide | grep nginx-m
NAME                       READY   STATUS        RESTARTS   AGE     IP               NODE      NOMINATED NODE   READINESS GATES
nginx-m-7c879df6bc-26dcq   1/1     Running       0          23s     10.244.120.12    worker5   <none>           <none>
nginx-m-7c879df6bc-nwdtp   1/1     Running       0          23s     10.244.120.14    master1   <none>           <none>

[root@master1 ~]# kubectl get sp
NAME                              VERSION   SUBNET          ALLOCATED-IP-COUNT   TOTAL-IP-COUNT   DEFAULT   DISABLE
auto-nginx-v4-eth0-452e737e5e12   4         10.244.0.0/16   3                    6                false     false
nginx-v4-ippool                   4         10.244.0.0/16   2                    11               false     false
```

## 结论

经过测试: 集群外客户端可直接通过 Nginx Pod 的 IP 正常访问，集群内部通讯 Nginx Pod 跨节点也都通信正常 (包括跨 Calico 子网)。
在 Calico underlay 场景下，我们可借助 Spiderpool 轻松帮助我们实现 Deployment 等类型应用固定 IP 的需求，这也为该场景下提供了一个新的选择。

更多功能介绍参考 [Spiderpool 官方文档](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/)。

[了解 DCE 5.0 云原生网络](../network/intro/index.md){ .md-button }

[下载 DCE 5.0](../download/index.md){ .md-button .md-button--primary }
[安装 DCE 5.0](../install/index.md){ .md-button .md-button--primary }
[申请社区免费体验](../dce/license0.md){ .md-button .md-button--primary }
