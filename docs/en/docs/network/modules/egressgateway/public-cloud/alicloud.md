# Using EgressGateway on Alibaba Cloud

This guide explains how to use EgressGateway on Alibaba Cloud. On Alibaba Cloud, since IP addresses (including Elastic Public IPs) are bound to specific nodes, the feature of floating Egress IPs between nodes is not supported. Instead, we use node IPs (rather than a specified IP pool) as Egress IPs. When using node IPs as Egress IPs, if multiple nodes are selected as Egress gateways for high availability (HA), the Egress IP will switch to another node's IP if one node fails.

## Use Cases

* **East-West traffic in a VPC network:**

    There are two clusters, A and B. Cluster B requires that incoming traffic originates from an IP address on an allowlist. To meet this requirement, an EgressGateway is deployed in Cluster A so that all traffic to Cluster B originates from the Egress IP, which external applications can apply special policies to.

* **North-South traffic in a VPC network:**

    Some workloads in the cluster need to access the internet, but their nodes do not have public IPs. These workloads can access external networks via the public IP of a designated Egress node.

## Prerequisites

* A Kubernetes cluster with at least two nodes.
* The Calico networking component installed.

## Installing EgressGateway

Before installation, set Calico’s `iptables` mode to `Append`.

If Calico was installed via YAML, run:

```shell
kubectl set env daemonset -n calico-system calico-node FELIX_CHAININSERTMODE=Append
```

If Calico is managed via the Calico Operator, run:

```shell
kubectl patch felixconfigurations default --type='merge' -p '{"spec":{"chainInsertMode":"Append"}}'
```

### Add the Helm repository

```shell
helm repo add egressgateway https://spidernet-io.github.io/egressgateway/
helm repo update
```

### Install EgressGateway via Helm

```shell
helm install egress --wait --debug egressgateway/egressgateway
```

### Verify that all pods are running

```shell
kubectl get pods -A | grep egressgateway
```

Example output:

```shell
default    egressgateway-agent-lkglz                  1/1     Running   0    86m
default    egressgateway-agent-s5xwk                  1/1     Running   0    86m
default    egressgateway-controller-6cd86df57-xm2d4   1/1     Running   0    86m
```

## Deploying a Test Service

Create a new VM as a server in the VPC network (East-West traffic). In this example, the new VM’s IP is `172.17.81.29`.

![new-vm](../../../images/new-vm.png)

Start a test server that listens on port `8080` and returns the client's IP address:

```shell
docker run -d --net=host ghcr.io/spidernet-io/egressgateway-nettools:latest /usr/bin/nettools-server -protocol web -webPort 8080
```

## Creating a Test Pod

### Check cluster nodes

```shell
kubectl get nodes
```

Example output:

```shell
NAME    STATUS   ROLES           AGE   VERSION
node1   Ready    control-plane   66m   v1.30.0
node2   Ready    <none>          66m   v1.30.0
```

Deploy a pod on `node1`. Later, we will configure the EgressGateway to allow this pod to route traffic through `node2`'s IP.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  containers:
    - image: nginx
      imagePullPolicy: IfNotPresent
      name: nginx
      resources: {}
  nodeName: node1
```

### Verify that the pod is running

```shell
kubectl get pods -o wide | grep nginx
```

Example output:

```shell
nginx  1/1  Running  0  77m  10.200.166.133  node1  <none>  <none>
```

## Creating an EgressGateway CR

An `EgressGateway` CR allows you to designate specific nodes as Egress gateways. In the following example, `nodeSelector` matches `node2` as the Egress gateway.

```yaml
apiVersion: egressgateway.spidernet.io/v1beta1
kind: EgressGateway
metadata:
  name: "egressgateway"
spec:
  nodeSelector:
    selector:
      matchLabels:
        egress: "true"
```

## Selecting a Node as the Egress Gateway

### Check the cluster nodes

```shell
kubectl get nodes
```

Example output (where `node2` has a public IP of `8.217.200.161`):

```shell
NAME    STATUS   ROLES           AGE   VERSION
node1   Ready    control-plane   66m   v1.30.0
node2   Ready    <none>          66m   v1.30.0
```

Label `node2` so that it matches the EgressGateway configuration:

```shell
kubectl label node node2 egress=true
```

Verify that `node2` is recognized as an Egress node:

```shell
kubectl get egw egressgateway -o yaml
```

Expected output:

```yaml
apiVersion: egressgateway.spidernet.io/v1beta1
kind: EgressGateway
metadata:
  name: egressgateway
spec:
  nodeSelector:
    selector:
      matchLabels:
        egress: "true"
status:
  nodeList:
  - name: node2
    status: Ready
```

## Creating an EgressPolicy

An `EgressPolicy` CR defines which pods should use the Egress gateway for external traffic.  
In this example, `34.117.186.192` is the IP address of `ipinfo.io`, which you can obtain using `dig ipinfo.io`.

```yaml
apiVersion: egressgateway.spidernet.io/v1beta1
kind: EgressPolicy
metadata:
  name: nginx-egress-policy
spec:
  egressGatewayName: egressgateway
  egressIP:
    useNodeIP: true
  appliedTo:
    podSelector:
      matchLabels:
        app: nginx
  destSubnet:
    - 172.17.81.29/32   # East-West test service IP
    - 34.117.186.192/32 # IP for testing North-South traffic (ipinfo.io)
```

## Testing East-West Traffic

Run the following command inside the `nginx` pod:

```shell
curl 172.17.81.29:8080
```

Expected output:

```shell
Remote IP: 172.17.81.28:59022
```

This confirms that traffic is correctly routed through the Egress gateway.

## Testing North-South Traffic

Run the following command inside the `nginx` pod:

```shell
curl ipinfo.io
```

Expected output (showing that `node2`'s public IP is used):

```json
{
  "ip": "8.217.200.161",
  "city": "Hong Kong",
  "region": "Hong Kong",
  "country": "HK",
  "loc": "22.2783,114.1747",
  "org": "AS45102 Alibaba (US) Technology Co., Ltd.",
  "timezone": "Asia/Hong_Kong",
  "readme": "https://ipinfo.io/missingauth"
}
```

This confirms that `node1`'s pod successfully routes internet-bound traffic through `node2`'s public IP.

---

This concludes the setup and validation of EgressGateway on Alibaba Cloud! 🚀
