# Fast

Fast 是基于 [eBPF](https://ebpf.io) 实现的 Kubernetes CNI。目前，已经实现了以下两个功能：

- 基于 eBPF 的网络基本连通性
- 管理集群容器的 IP 地址

## 架构

![fast](images/fast.png)

组件：

- fast-cni
    - 实现 CNI 功能
    - 访问 fast-agent 获取 Pod IP，并将其存储到节点本地的 eBPF map 中
    - 在 NIC 上附加 eBPF 程序
- fast-agent
    - 实现 IP 分配的接口
    - 获取集群的 Pod IP，并将信息存储到集群的 eBPF map 中
    - 初始化 eBPF map
- fast-controller-manager
    - 自定义资源控制
    - 执行 GC 管理，防止 IP 泄漏
- fast-ctl
    - 用于 eBPF map 的节点命令行工具

## 快速入门

### 单集群 IPAM

在覆盖网络场景中，固定集群容器的 IP 地址

1. 创建 ips 对象

    ```shell
    cat << EOF | kubectl create -f -
    apiVersion: sample.fast.io/v1alpha1
    kind: Ips
    metadata:
      name: sample-ips
    spec:
      subnet: 10.244.0.1/32
      ips:
        - 10.244.10.0-10.244.90.0
    EOF
    ```

2. 创建 Deployment，并通过注释与 ips 对象关联

    ```shell
    cat << EOF | kubectl create -f -
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: busybox
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: busybox
      template:
        metadata:
          annotations:
            fast.io/ips: sample-ips
          labels:
            app: busybox
        spec:
          containers:
            - name: busybox
              image: busybox:latest
              imagePullPolicy: IfNotPresent
              command:
                - sleep
                - "10000"
              ports:
                - name: http
                  containerPort: 80
                  protocol: TCP
    EOF
    ```

3. 查看容器的 IP 地址

    容器的 IP 地址被固定在 ips 定义的范围内

    ```shell
    [root@york-master ~]# kubectl get po -o wide
    NAME                      READY   STATUS    RESTARTS   AGE   IP            NODE          NOMINATED NODE   READINESS GATES
    busybox-757455cf7-4p9fq   1/1     Running   0          4s    10.244.10.1   10-29-15-49   <none>           <none>
    busybox-757455cf7-f5lr9   1/1     Running   0          4s    10.244.10.0   10-29-15-50   <none>           <none>
    ```

### 网络连通性测试

1. 创建另一个应用程序

    ```bash
    cat << EOF | kubectl create -f -
    apiVersion: sample.fast.io/v1alpha1
    kind: Ips
    metadata:
      name: default-ips
    spec:
      subnet: 10.244.0.1/32
      ips:
        - 10.244.100.0-10.244.200.250
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: busybox1
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: busybox1
      template:
        metadata:
          labels:
            app: busybox1
        spec:
          containers:
            - name: busybox1
              image: busybox:latest
              imagePullPolicy: IfNotPresent
              command:
                - sleep
                - "10000"
              ports:
                - name: http
                  containerPort: 80
                  protocol: TCP
    EOF
    ```

    创建后，共有四个容器

    ```shell
    [root@york-master ~]# kubectl get po -o wide
    NAME                        READY   STATUS    RESTARTS   AGE     IP             NODE          NOMINATED NODE   READINESS GATES
    busybox-757455cf7-4p9fq     1/1     Running   0          2m11s   10.244.10.1    10-29-15-49   <none>           <none>
    busybox-757455cf7-f5lr9     1/1     Running   0          2m11s   10.244.10.0    10-29-15-50   <none>           <none>
    busybox1-5f98488b8d-2xc49   1/1     Running   0          10s     10.244.100.0   10-29-15-50   <none>           <none>
    busybox1-5f98488b8d-v42dq   1/1     Running   0          10s     10.244.100.1   10-29-15-49   <none>           <none>
    ```

2. 同一节点的容器网络连接

    可以看到网络是可达的

    ```shell
    [root@york-master ~]# kubectl exec -it busybox-757455cf7-4p9fq -- ping 10.244.100.1
    PING 10.244.100.1 (10.244.100.1): 56 data bytes
    64 bytes from 10.244.100.1: seq=0 ttl=64 time=0.398 ms
    64 bytes from 10.244.100.1: seq=1 ttl=64 time=0.117 ms
    64 bytes from 10.244.100.1: seq=2 ttl=64 time=0.098 ms
    64 bytes from 10.244.100.1: seq=3 ttl=64 time=0.111 ms
    64 bytes from 10.244.100.1: seq=4 ttl=64 time=0.111 ms
    ^C
    --- 10.244.100.1 ping statistics ---
    5 packets transmitted, 5 packets received, 0% packet loss
    round-trip min/avg/max = 0.098/0.167/0.398 ms
    ```

3. 不同节点的容器网络连接

    同样可以看到网络是可达的

    ```shell
    [root@york-master ~]# kubectl exec -it busybox-757455cf7-4p9fq -- ping 10.244.100.0
    PING 10.244.100.0 (10.244.100.0): 56 data bytes
    64 bytes from 10.244.100.0: seq=0 ttl=64 time=1.029 ms
    64 bytes from 10.244.100.0: seq=1 ttl=64 time=0.593 ms
    64 bytes from 10.244.100.0: seq=2 ttl=64 time=0.614 ms
    64 bytes from 10.244.100.0: seq=3 ttl=64 time=0.522 ms
    64 bytes from 10.244.100.0: seq=4 ttl=64 time=0.704 ms
    ^C
    --- 10.244.100.0 ping statistics ---
    5 packets transmitted, 5 packets received, 0% packet loss
    round-trip min/avg/max = 0.522/0.692/1.029 ms
    ```

## 接下来的计划

更多内容即将到来。欢迎[提交 issue](https://github.com/Fish-pro/fast/issues)
和[提交 PR](https://github.com/Fish-pro/fast/pulls)。🎉🎉🎉
