# Run Calico on Alibaba Cloud

This page introduce how to install and use [Calico](https://github.com/projectcalico/calico) as the cluster CNI in a self-built Alibaba Cloud cluster.

## Install Clusters

To get started, prepare a self-built Kubernetes cluster on Alibaba Cloud. Alternatively, you can manually set up a cluster by following the instructions about [building a Kubernetes cluster](usage.md#set-up-the-kubernetes-cluster). Once the cluster is ready, download the Calico deployment manifest file:

```shell
~# wget https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/calico.yaml
```

> To speed up image pulling, we recommend running the following command: `sed -i 's?docker.io?docker.m.daocloud.io?g' calico.yaml`

Next, let's explore the installation process for both tunnel mode (IPIP) and route mode:

## Tunnel Mode (IPIP)

Tunneling protocols like VXLAN and IPIP enable network connectivity regardless of the underlying network implementation. They create a large Layer 2 overlay network that can be used in most public cloud environments. In this mode, the [CCM](https://github.com/AliyunContainerService/alicloud-controller-manager) is not required. The default Calico deployment manifest file uses IPIP mode. Install Calico using the following command:

```shell
~# kubectl apply -f calico.yaml
```

Wait for the installation to complete:

```shell
# kubectl get po -n kube-system | grep calico
calico-kube-controllers-769669454f-c9pw6                    1/1     Running     0              1m
calico-node-679wb                                           1/1     Running     0              1m
calico-node-6wzkj                                           1/1     Running     0              1m
```

Create a test deployment to verify connectivity:

```shell
~# kubectl  get po -o wide
NAME                    READY   STATUS    RESTARTS   AGE   IP               NODE                  NOMINATED NODE   READINESS GATES
test-77877f4755-24gqt   1/1     Running   0          13m   10.244.236.193   cn-chengdu.i-2vcxxr   <none>           <none>
test-77877f4755-2d6r8   1/1     Running   0          13m   10.244.140.2     cn-chengdu.i-2vcxxs   <none>           <none>
~# kubectl  get svc
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP   172.21.0.1     <none>        443/TCP        31d
test         ClusterIP   172.21.0.83    <none>        80/TCP         2m

~# # Access Pods across nodes 
~# kubectl exec test-77877f4755-24gqt -- ping -c1 10.244.140.2
PING 10.244.140.2 (10.244.140.2) 56(84) bytes of data.
64 bytes from 10.244.140.2: icmp_seq=1 ttl=62 time=0.471 ms

--- 10.244.140.2 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.471/0.471/0.471/0.000 ms

~# # Access external targets
~# kubectl exec test-77877f4755-24gqt -- ping -c1 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=109 time=38.5 ms

--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 38.479/38.479/38.479/0.000 ms

~# # Access ClusterIP
~# kubectl exec test-77877f4755-24gqt -- curl -i 172.21.0.83
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   153  100   153    0     0  93463      0 --:--:-- --:--:-- --:--:--  149k
HTTP/1.1 200 OK
Content-Type: application/json
Date: Wed, 27 Sep 2023 08:15:34 GMT
Content-Length: 153
```

After testing, it was found that communication between Pods is functional in both IPIP and Vxlan modes without relying on the [CCM](https://github.com/AliyunContainerService/alicloud-controller-manager) for route publication. However, the implementation of LoadBalancer Services does depend on the CCM.

## Non-tunnel Mode

In non-tunnel mode, Calico enables direct communication between Pods by connecting with the underlying network. Additional devices or components may be required to publish routes, allowing Pod subnets to be reachable from outside the cluster. On non-public clouds, routers supporting the BGP protocol are needed, while on public clouds, components like Alibaba Cloud's CCM are used to publish Pod subnet routes to the VPC network.
However, the route publication provided by the CCM component is usually based on nodes. This requires Pods on different nodes to belong to different subnets, while Pods on the same node should belong to the same subnet. Unfortunately, Calico's built-in IPAM (calico-ipam) cannot meet this requirement, as it allocates IP addresses in blocks rather than per node. To address this limitation, we can switch the IPAM to either `host-local` or `spiderpool`.

> The PodCIDR of a node corresponds to the Node's spec.podCIDR field.

* host-local: a simple IPAM solution that allocates IP addresses from the node's PodCIDR. The allocated data is stored on the local disk without any additional IPAM capabilities.
* Spiderpool: provide robust IPAM capabilities, including IP allocation per node, support for fixed IP addresses, and IP allocation for multiple network interfaces

Before diving into how to use, make sure to install the [CCM component](https://github.com/AliyunContainerService/alicloud-controller-manager) following the instructions in the [CCM installation](usage.md#install-the-ccm-component-and-publish-vpc-routes). Additionally, switch Calico to non-tunnel mode by modifying specific environment variables to "Never" in the calico-node daemonSet deployment manifest file:

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

### Use Host-local as IPAM

To switch to `host-local` IPAM, modify the ConfigMap in the Calico installation manifest file as follows:

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
          "mtu": __CNI_MTU__ ,
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

> Switch the IPAM to host-local and specify the node's PodCIDR as the subnet for Pods

After installing and ensuring Calico is ready, create a test application to observe that the Pods' IP addresses belong to the node's PodCIDR (10.244.0.0/24 and 10.244.1.0/24):

```shell
~# k get po -o wide
NAME                    READY   STATUS    RESTARTS   AGE   IP           NODE                  NOMINATED NODE   READINESS GATES
test-77877f4755-58hlc   1/1     Running   0          5s    10.244.0.2   cn-chengdu.i-2vcxxr   <none>           <none>
test-77877f4755-npcgs   1/1     Running   0          5s    10.244.1.2   cn-chengdu.i-2vcxxs   <none>           <none>
```

The test finds that communication between Pods functions correctly.

## Use Spiderpool as IPAM

1. To switch to `spiderpool` IPAM, modify the ConfigMap in the Calico installation manifest file as follows:

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
              "mtu": __CNI_MTU__ ,
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

    Switch the IPAM to Spiderpool and wait for it to be ready.

    !!! note

        If you encounter any issues where Calico fails to start and reports the following error, try deleting the `/var/lib/cni/networks/k8s-pod-network/` on each node.

        ```shell
        2023-09-27 10:14:42.096 [ERROR][1] ipam_plugin.go 106: failed to migrate ipam, retrying... error=failed to get add IPIP tunnel addr 10.244.1.1: The provided IP address is not in a configured pool
        ```

2. Install Spiderpool

    Run the following command to install  Spiderpool:

    ```shell
    ~# helm repo add spiderpool https://spidernet-io.github.io/spiderpool
    ~# helm repo update spiderpool
    ~# helm install spiderpool spiderpool/spiderpool --namespace kube-system --wait
    ```

    > Helm binary should be installed in advance
    > By default, Spiderpool installs the Multus component. If you don't need Multus or have already installed it, you can disable Multus installation by using `--set multus.multusCNI.install=false"`.

    After the installation is complete, you need to create a dedicated Spiderpool IP pool for the podCIDR of each node to be used by Pods:

    ```shell
    ~# kubectl  get nodes -o=custom-columns='NAME:.metadata.name,podCIDR:.spec.podCIDR'
    NAME                  podCIDR
    cn-chengdu.i-2vcxxr   10.244.0.0/24
    cn-chengdu.i-2vcxxs   10.244.1.0/24
    ```

    Create the following Spiderpool IP pools:

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

    > The IPs in the pool should belong to the corresponding nodeName node's podCIDR.

3. Create a test application and verify connectivity. 

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

    Test accessing ClusterIP:

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

    After testing, it has been confirmed that the communication between Pods functions correctly. Additionally, Pods created by Calico can utilize other advanced IPAM capabilities provided by Spiderpool.
