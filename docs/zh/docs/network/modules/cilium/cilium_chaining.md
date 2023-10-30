# Cilium 为 IPVlan 支持网络策略

本文介绍 IPVlan 如何与 Cilium 集成，为 IPVlan CNI 提供网络策略能力。

## 背景

目前社区中大多数 Underlay 类型的 CNI 如 IPVlan、Macvlan 等, 并不支持 Kubernetes 原生的网络策略能力，我们可借助 Cilium chaining-mode 功能为 IPVlan 提供网络策略能力。
但 Cilium 在 1.12 版本正式移除了对 IPVlan Dataplane 的支持, 详见 [removed-options](https://docs.cilium.io/en/v1.12/operations/upgrade/#removed-options) 。
由于受到 [Terway](https://github.com/AliyunContainerService/terway) 的启发， [cilium-chaining](https://github.com/spidernet-io/cilium-chaining) 项目基于 Cilium
v1.12.7 版本修改 IPVlan Dataplane 部分, 使 Cilium 能够以 chaining-mode 的方式与 IPVlan 一起工作。
解决 IPVlan 不支持 Kubernetes 原生的网络策略能力。

接下来，我们将通过一个例子来介绍这个功能。

## 环境准备

1. 要求节点内核版本至少大于 4.19
2. 准备一个 Kubernetes 集群，并注意不能安装 Cilium
3. 已安装 [Helm](https://helm.sh/docs/intro/install/)

## 安装 Spiderpool

1. 安装 Spiderpool

    ```bash
    helm repo add spiderpool https://spidernet-io.github.io/spiderpool

    helm repo update spiderpool

    helm install spiderpool spiderpool/spiderpool --namespace kube-system --set multus.multusCNI.defaultCniCRName="ipvlan-ens192" ---set plugins.installCNI=true
    ```

   > 如果您的集群未安装 Macvlan CNI, 可指定 Helm 参数 `--set plugins.installCNI=true` 安装 Macvlan 到每个节点。
   >
   > 如果您是国内用户，可以指定参数 `--set global.imageRegistryOverride=ghcr.m.daocloud.io` 避免 Spiderpool 的镜像拉取失败。
   >
   > 通过 `multus.multusCNI.defaultCniCRName` 指定集群的 Multus clusterNetwork，clusterNetwork 是 Multus 插件的一个特定字段，用于指定 Pod 的默认网络接口。

2. 创建 SpiderIPPool 实例

   创建与网络接口 `ens192` 在同一个子网的 IP 池以供 Pod 使用，以下是创建相关的 SpiderIPPool 示例：

    ```shell
    cat <<EOF | kubectl apply -f -
    apiVersion: spiderpool.spidernet.io/v2beta1
    kind: SpiderIPPool
    metadata:
      name: ippool-ens192
    spec:
      ips:
      - "10.6.185.200-10.6.185.230"
      subnet: 10.6.0.0/16
      gateway: 10.6.0.1
      multusName: 
      - ipvlan-ens192
    EOF
    ```

3. 验证安装

   ```shell
    ~# kubectl get po -n kube-system | grep spiderpool
    spiderpool-agent-7hhkz                   1/1     Running     0              13m
    spiderpool-agent-kxf27                   1/1     Running     0              13m
    spiderpool-controller-76798dbb68-xnktr   1/1     Running     0              13m
    spiderpool-init                          0/1     Completed   0              13m
    ~# kubectl get sp
    NAME            VERSION   SUBNET          ALLOCATED-IP-COUNT   TOTAL-IP-COUNT   DISABLE
    ippool-test     4         10.6.0.0/16     0                    10               false
   ```

## 安装 Cilium-chaining

1. 使用以下命令安装 cilium-chaining 组件:

    
    helm repo add cilium-chaining https://spidernet-io.github.io/cilium-chaining

    helm repo update cilium-chaining

    helm install cilium-chaining/cilium-chaining --namespace kube-system


2. 验证安装:


     ~# kubectl  get po -n kube-system
     NAME                                     READY   STATUS      RESTARTS         AGE
     cilium-chaining-4xnnm                    1/1     Running     0                5m48s
     cilium-chaining-82ptj                    1/1     Running     0                5m48s

## 配置 CNI

创建 Multus NetworkAttachmentDefinition CR, 如下是创建 IPvlan NetworkAttachmentDefinition 配置的示例：


```shell
IPVLAN_MASTER_INTERFACE="ens192"
CNI_CHAINING_MODE="terway-chainer"
cat <<EOF | kubectl apply -f -
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: ipvlan-ens192
  namespace: kube-system
spec:
  config: |
   {
     "cniVersion": "0.4.0",
     "name": "${CNI_CHAINING_MODE}",
     "plugins": [
      {
         "type": "ipvlan",
         "mode": "l2",
         "master": "${IPVLAN_MASTER_INTERFACE}",
         "ipam": {
         "type": "spiderpool"
         }
      },
      {
        "type": "cilium-cni"
      },
     {
        "type": "coordinator"
     }]
   }
EOF
```

> 在上面的配置中，指定 master 为 ens192, ens192 必须存在与节点上
> 
> 将 cilium 嵌入到 CNI 配置中，放置与 ipvlan plugin 之后
> 
> 注意 CNI 的 name 必须和安装 cilium-chaining 时的 cniChainingMode 保持一致，否则无法正常工作

## 创建测试应用

### 创建应用

以下的示例 Yaml 中，会创建 1 组 DaemonSet 应用和 其中使用 `v1.multus-cni.io/default-network`：用于指定应用所使用的 CNI 配置文件:

```shell
APP_NAME=test
cat <<EOF | kubectl create -f -
apiVersion: apps/v1
kind: DaemonSet
metadata:
  labels:
    app: ${APP_NAME}
  name: ${APP_NAME}
  namespace: default
spec:
  selector:
    matchLabels:
      app: ${APP_NAME}
  template:
    metadata:
      labels:
        app: ${APP_NAME}
      annotations:
        v1.multus-cni.io/default-network: kube-system/ipvlan-ens192
    spec:
      containers:
      - image: docker.io/centos/tools
        imagePullPolicy: IfNotPresent
        name: ${APP_NAME}
        ports:
        - name: http
          containerPort: 80
          protocol: TCP
EOF
```

查看 Pod 运行状态：

```bash
~# kubectl get po -owide
NAME                    READY   STATUS              RESTARTS   AGE     IP             NODE          NOMINATED NODE   READINESS GATES
test-55c97ccfd8-l4h5w   1/1     Running             0          3m50s   10.6.185.217   worker1       <none>           <none>
test-55c97ccfd8-w62k7   1/1     Running             0          3m50s   10.6.185.206   controller1   <none>           <none>
```

### 验证网络策略是否生效

  - 测试 Pod 与跨节点、跨子网 Pod 的通讯情况

      ```shell
     ~# kubectl exec -it test-55c97ccfd8-l4h5w -- ping -c2 10.6.185.30
     PING 10.6.185.30 (10.6.185.30): 56 data bytes
     64 bytes from 10.6.185.30: seq=0 ttl=64 time=1.917 ms
     64 bytes from 10.6.185.30: seq=1 ttl=64 time=1.406 ms
   
     --- 10.6.185.30 ping statistics ---
     2 packets transmitted, 2 packets received, 0% packet loss
     round-trip min/avg/max = 1.406/1.661/1.917 ms
     ~# kubectl exec -it test-55c97ccfd8-l4h5w -- ping -c2 10.6.185.206
     PING 10.6.185.206 (10.6.185.206): 56 data bytes
     64 bytes from 10.6.185.206: seq=0 ttl=64 time=1.608 ms
     64 bytes from 10.6.185.206: seq=1 ttl=64 time=0.647 ms
   
     --- 10.6.185.206 ping statistics ---
     2 packets transmitted, 2 packets received, 0% packet loss
     round-trip min/avg/max = 0.647/1.127/1.608 ms

      ```
  - 创建禁止 Pod 与外部通信的网络策略

      ```shell
      ~# cat << EOF | kubectl apply -f -
      kind: NetworkPolicy
      apiVersion: networking.k8s.io/v1
      metadata:
        name: deny-all
      spec:
        podSelector:
          matchLabels:
            app: test
        policyTypes:
        - Egress
        - Ingress
      ```
 
     > deny-all 根据 label 匹配所有 pod, 该策略禁止 Pod 对外通信
  
  - 再次验证 Pod 对外通信

      ```shell
      ~# kubectl exec -it test-55c97ccfd8-l4h5w -- ping -c2 10.6.185.206
      kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
      PING 10.6.185.206 (10.6.185.206): 56 data bytes
      --- 10.6.185.206 ping statistics ---
      14 packets transmitted, 0 packets received, 100% packet loss
      ```
    
从结果看出，Pod 访问外部的流量被禁止，网络策略生效，证明通过 Cilium-chaining 项目 帮助 IPVlan 实现网络策略能力。