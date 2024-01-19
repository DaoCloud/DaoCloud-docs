# Fast

Fast is a Kubernetes CNI based on [eBPF](https://ebpf.io) implementation.
At present, the following two capabilities have been realized:

- Network basic connectivity based on eBPF
- Manage cluster containers' IP address

## Architecture

![fast](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/community/images/fast.png)

Components:

- fast-cni
    - implement CNI capabilities
    - access fast-agent fetch pod IP and store to the node local eBPF map
    - attach eBPF program to NIC
- fast-agent
    - the interface that implements IP allocation
    - obtain the cluster pod IP and store the information to the cluster eBPF map
    - init eBPF map
- fast-controller-manager
    - custom resources control
    - gc management to prevent IP leakage
- fast-ctl
    - node command tool for eBPF map

## Quick Start

### Single-cluster IPAM

In overlay scenario, fix the IP address of cluster containers

1. Create ips

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

2. Create a deployment and associate it with ips via annotations

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

3. View the IP address of the container

    The IP address of the container is fixed in the range defined by the ips

    ```shell
    [root@york-master ~]# kubectl get po -o wide
    NAME                      READY   STATUS    RESTARTS   AGE   IP            NODE          NOMINATED NODE   READINESS GATES
    busybox-757455cf7-4p9fq   1/1     Running   0          4s    10.244.10.1   10-29-15-49   <none>           <none>
    busybox-757455cf7-f5lr9   1/1     Running   0          4s    10.244.10.0   10-29-15-50   <none>           <none>
    ```

### Network connectivity test

1. Create another application

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

    Once created, there are four containers

    ```shell
    [root@york-master ~]# kubectl get po -o wide
    NAME                        READY   STATUS    RESTARTS   AGE     IP             NODE          NOMINATED NODE   READINESS GATES
    busybox-757455cf7-4p9fq     1/1     Running   0          2m11s   10.244.10.1    10-29-15-49   <none>           <none>
    busybox-757455cf7-f5lr9     1/1     Running   0          2m11s   10.244.10.0    10-29-15-50   <none>           <none>
    busybox1-5f98488b8d-2xc49   1/1     Running   0          10s     10.244.100.0   10-29-15-50   <none>           <none>
    busybox1-5f98488b8d-v42dq   1/1     Running   0          10s     10.244.100.1   10-29-15-49   <none>           <none>
    ```

2. Same node container network connection

    You can see that the network is reachable

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

3. Different nodes container network connection

    You can see that the network is reachable too

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

## What's Next

More will be coming Soon. Youlcome to [open an issue](https://github.com/Fish-pro/fast/issues) and [propose a PR](https://github.com/Fish-pro/fast/pulls). 🎉🎉🎉
