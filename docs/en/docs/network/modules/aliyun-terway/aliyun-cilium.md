# Run Cilium on Alibaba Cloud

This page introduces how to use Cilium as the cluster CNI in an Alibaba Cloud self-built Kubernetes cluster. With Cilium, you can experience various capabilities such as network acceleration and network policies on Alibaba Cloud.

> Please ensure that your ECS instances meet the minimum kernel version requirements for running Cilium.

## Install Clusters

To get started, prepare a self-built Kubernetes cluster on Alibaba Cloud. Alternatively, you can manually set up a cluster by following the instructions about [building a Kubernetes cluster](usage.md#set-up-the-kubernetes-cluster).

## Install Cilium

Refer to the [Cilium doc](https://docs.cilium.io/en/stable/gettingstarted/k8s-install-default/) to install Cilium binary:

```shell
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
```

On Alibaba Cloud, Cilium can be deployed in either tunnel or native mode. The deployment parameters differ slightly between these two modes. The following sections will provide detailed explanations for each mode:

### Tunnel Mode

Cilium supports running in tunnel mode with Vxlan (default) and Geneve protocols, similar to Calico's tunnel mode. In this mode, Cilium abstracts the Pod network into a Layer 2 overlay network using protocols like Vxlan or Geneve. It doesn't rely on or require connection with the underlying network implementation. Therefore, you don't need to install any additional plugins like CCM for route publishing. To install Cilium in tunnel mode, use the following command:

```shell
cilium install 
```

> All parameters are set to default, and Cilium encapsulates Pod packets based on the Vxlan protocol.

Wait for the Cilium components to be running, then create a test application to verify the communication between Pods:

```shell
~# kubectl  get po -o wide
NAME                    READY   STATUS    RESTARTS   AGE   IP               NODE                  NOMINATED NODE   READINESS GATES
test-77877f4755-2jz2c   1/1     Running   0          1m   10.244.1.39       cn-chengdu.i-2vcxxr   <none>           <none>
test-77877f4755-rjlg6   1/1     Running   0          1m   10.244.0.86     cn-chengdu.i-2vcxxs   <none>           <none>
~# kubectl  get svc
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP   172.21.0.1     <none>        443/TCP        32d
test         ClusterIP   172.21.0.53    <none>        80/TCP         2m

~# # Access Pods across nodes 
~# kubectl  exec test-77877f4755-2jz2c -- ping -c1 10.244.0.86
PING 10.244.0.86 (10.244.0.86) 56(84) bytes of data.
64 bytes from 10.244.0.86: icmp_seq=1 ttl=63 time=0.571 ms

--- 10.244.0.86 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.571/0.571/0.571/0.000 ms

~# # Access external targets
~# kubectl exec test-77877f4755-24gqt -- ping -c1 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=107 time=63.8 ms

--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 63.758/63.758/63.758/0.000 ms

~# # Access ClusterIP
~# kubectl exec test-77877f4755-24gqt -- curl -i 172.21.0.53
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 28 Sep 2023 03:54:28 GMT
Content-Length: 151
````

The test shows that all types of connectivity between Pods work properly.

### Native Mode

Cilium also supports running in native mode on Alibaba Cloud. In this mode, the Pod network directly connects to the underlying network without additional encapsulation, resulting in better performance. However, it requires the CCM component to publish Pod subnet routes to the VPC network. Additionally, some specific configurations need to be made in Cilium. Please refer to the following command:

> Refer to the doc [CCM Installation](usage.md#install-the-ccm-component-and-publish-vpc-routes) to install CCM

```shell
cilium install --set ipam.mode=kubernetes --set routingMode=native --set ipv4NativeRoutingCIDR=10.244.0.0/16 
```

> Adjust ipam.mode to kubernetes to allocate Pod IP addresses from each node's podCIDR.
> Set routingMode to native mode instead of the default tunnel mode.
> Set ipv4NativeRoutingCIDR to specify the subnet to be routed, which should be the cluster's ClusterCIDR (you can find this by checking the kubeadm-config ConfigMap).

Wait for Cilium to be in the Running state, create a test application, and validate connectivity:

```shell
~# kubectl  get po -o wide
NAME                    READY   STATUS    RESTARTS   AGE   IP             NODE                                NOMINATED NODE   READINESS GATES
test-77877f4755-v9mrj   1/1     Running   0          4s    10.244.1.166   cn-chengdu.i-2vc5zub002vrlwursb4s   <none>           <none>
test-77877f4755-w95wn   1/1     Running   0          4s    10.244.0.98    cn-chengdu.i-2vc5zub002vrlwursb4r   <none>           <none>
~# kubectl  get svc
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP   172.21.0.1     <none>        443/TCP        31d
test         ClusterIP   172.21.0.98    <none>        80/TCP         16s
```

You will notice that the Pod IPs are bound to their respective nodes. Test the connectivity between Pods:

```shell
# cross-node Pod communication 
~# kubectl  exec test-77877f4755-v9mrj -- ping -c1 10.244.0.98
PING 10.244.0.98 (10.244.0.98) 56(84) bytes of data.
64 bytes from 10.244.0.98: icmp_seq=1 ttl=60 time=0.800 ms

--- 10.244.0.98 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.800/0.800/0.800/0.000 ms

# Pod access Service
~# kubectl  exec test-77877f4755-v9mrj -- curl -i 172.21.0.98
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   152  100   152    0     0  32871      0 --:--:-- --:--:-- --:--:-- 38000
HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 28 Sep 2023 04:17:33 GMT
Content-Length: 152
```

The test shows that all types of connectivity between Pods work properly.
