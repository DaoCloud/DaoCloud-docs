# Cilium Network Policy Support for IPVlan

This article describes how IPVlan integrates with Cilium to provide network policy capabilities for IPVlan CNI.

## Background

Most Underlay CNIs such as IPVlan, Macvlan, etc. do not support Kubernetes native network policy capability, so we can use Cilium chaining-mode feature to provide network policy capability for IPVlan.
However, Cilium officially removed support for IPVlan Dataplane in version 1.12, see [removed-options](https://docs.cilium.io/en/v1.12/operations/upgrade/#removed-options).
Inspired by [Terway](https://github.com/AliyunContainerService/terway), [cilium-chaining](https://github.com/spidernet-io/cilium-chaining) project is based on the Cilium
v1.12.7 to modify the IPVlan Dataplane section so that Cilium can work with IPVlan in chaining-mode.
This solves the problem that IPVlan does not support the network policy capabilities native to Kubernetes.

Next, we'll walk through an example of this feature.

## Environment Preparation

1. Node kernel versions should be greater than 4.19
2. A Kubernetes cluster without Cilium installed
3. [Helm](https://helm.sh/docs/intro/install/) is installed

## Install Spiderpool

1. Install Spiderpool

    ```bash
    helm repo add spiderpool https://spidernet-io.github.io/spiderpool

    helm repo update spiderpool

    helm install spiderpool spiderpool/spiderpool --namespace kube-system --set multus.multusCNI.defaultCniCRName="ipvlan-ens192" ---set plugins.installCNI=true
    ```

    > If your cluster does not have Macvlan CNI installed, specify the Helm parameter `-set plugins.installCNI=true` to install Macvlan on each node.
    >
    > If you are a user from the Chinese Mainland, you can specify the parameter `-set global.imageRegistryOverride=ghcr.m.daocloud.io` to avoid image pull failures for Spiderpool.
    >
    > Specify the Multus clusterNetwork for the cluster via `multus.multusCNI.defaultCniCRName`. clusterNetwork is a specific field of the Multus plugin that specifies the default network interface for the Pod.

2. Create a SpiderIPPool instance

   To create a pool of IPs on the same subnet as the network interface `ens192` for Pod, here is an example of creating a SpiderIPPool:

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

3. Validate installation

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

## Install Cilium-chaining

1. Install the cilium-chaining component using the following command:

    
    helm repo add cilium-chaining https://spidernet-io.github.io/cilium-chaining

    helm repo update cilium-chaining

    helm install cilium-chaining/cilium-chaining --namespace kube-system


2. Validate installation:


    ~# kubectl  get po -n kube-system
    NAME                                     READY   STATUS      RESTARTS         AGE
    cilium-chaining-4xnnm                    1/1     Running     0                5m48s
    cilium-chaining-82ptj                    1/1     Running     0                5m48s

## Configure CNI

To create a Multus NetworkAttachmentDefinition CR, the following is an example of creating an IPvlan NetworkAttachmentDefinition configuration:

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

> In the above configuration, specify master as ens192, which must exist on the node.
> 
> Embed Cilium into the CNI configuration, placing it after the ipvlan plugin.
> 
> The name of the CNI must match the cniChainingMode used during the installation of cilium-chaining, otherwise it will not work properly.

## Create a Test Application

### Create an Application

The following example YAML will create a group of DaemonSet applications that utilize the `v1.multus-cni.io/default-network` to specify the CNI configuration file for the application:

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

Check the running status of Pod:

```bash
~# kubectl get po -owide
NAME                    READY   STATUS              RESTARTS   AGE     IP             NODE          NOMINATED NODE   READINESS GATES
test-55c97ccfd8-l4h5w   1/1     Running             0          3m50s   10.6.185.217   worker1       <none>           <none>
test-55c97ccfd8-w62k7   1/1     Running             0          3m50s   10.6.185.206   controller1   <none>           <none>
```

### Validate the Effectiveness of Network Policies

- Test the communication between Pods across nodes and subnets

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

- Create a network policy that restricts Pods from communicating with the external network

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
 
    > The deny-all policy matches all Pods based on their labels and prohibits them from communicating with the external network.
  
- Re-validate the accessibility of Pods to the external network.

    ```shell
    ~# kubectl exec -it test-55c97ccfd8-l4h5w -- ping -c2 10.6.185.206
    kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
    PING 10.6.185.206 (10.6.185.206): 56 data bytes
    --- 10.6.185.206 ping statistics ---
    14 packets transmitted, 0 packets received, 100% packet loss
    ```

From the results, it can be seen that the access of Pods to the external network is blocked, confirming the effectiveness of the network policy. This demonstrates how the Cilium-chaining project enables IPVlan to enforce network policy capabilities.
