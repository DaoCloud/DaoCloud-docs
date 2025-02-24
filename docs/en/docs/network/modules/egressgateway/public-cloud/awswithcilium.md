# Using EgressGateway with Cilium CNI on AWS

This guide explains how to deploy and use EgressGateway in an AWS Kubernetes environment with Cilium CNI. EgressGateway supports multiple nodes as high-availability (HA) egress gateways for Pods, allowing you to reduce public IP costs while implementing fine-grained control over outbound traffic.

Compared to Cilium’s native egress functionality, EgressGateway provides HA capabilities. If HA is not required, consider using Cilium’s built-in egress feature first.

The following sections will walk you through installing EgressGateway, creating a test Pod, and configuring an egress policy to route its outbound traffic through a gateway node.

## Creating the Cluster and Installing Cilium

Follow the [Cilium installation guide](https://docs.cilium.io/en/stable/gettingstarted/k8s-install-default/) to create an AWS Kubernetes cluster and install Cilium.  
At the time of writing, this guide uses Cilium version **1.15.6**. If you encounter unexpected behavior with a different version, please provide feedback.

Ensure that the EC2 nodes in your Kubernetes cluster have [public IP addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html). You can verify this by connecting to a node via SSH and running:

```shell
curl ipinfo.io
```

If the command returns your node’s public IP, it confirms that your instance has internet access.

## Installing EgressGateway

Add and update the Helm repository:

```shell
helm repo add egressgateway https://spidernet-io.github.io/egressgateway/
helm repo update
```

Install EgressGateway with IPv4 enabled and IPv6 disabled. The `feature.clusterCIDR.extraCidr` setting specifies the internal CIDR range of the cluster.  
If an `EgressPolicy` CR does not define `spec.destSubnet`, EgressGateway will forward all outbound traffic (excluding internal CIDR ranges) through the gateway node.  
If `spec.destSubnet` is specified, only traffic matching the defined subnets will be forwarded.

```shell
helm install egress --wait \
 --debug egressgateway/egressgateway \
 --set feature.enableIPv4=true \
 --set feature.enableIPv6=false \
 --set feature.clusterCIDR.extraCidr[0]=172.16.0.0/16
```

## Creating the EgressGateway CR

### Checking Current Nodes

```shell
kubectl get nodes -o wide
```

Example output:

```
NAME                             STATUS   ROLES    AGE   VERSION               INTERNAL-IP      EXTERNAL-IP                         
ip-172-16-103-117.ec2.internal   Ready    <none>   25m   v1.30.0-eks-036c24b   172.16.103.117   34.239.162.85  
ip-172-16-61-234.ec2.internal    Ready    <none>   25m   v1.30.0-eks-036c24b   172.16.61.234    54.147.15.230
ip-172-16-62-200.ec2.internal    Ready    <none>   25m   v1.30.0-eks-036c24b   172.16.62.200    54.147.16.130  
```

Select `ip-172-16-103-117.ec2.internal` and `ip-172-16-62-200.ec2.internal` as gateway nodes, then label them:

```shell
kubectl label node ip-172-16-103-117.ec2.internal role=gateway
kubectl label node ip-172-16-62-200.ec2.internal role=gateway
```

Create the `EgressGateway` CR:

```yaml
apiVersion: egressgateway.spidernet.io/v1beta1
kind: EgressGateway
metadata:
  name: "egressgateway"
spec:
  nodeSelector:
    selector:
      matchLabels:
        role: gateway
```

## Deploying a Test Pod

### Selecting a Node

```shell
kubectl get nodes -o wide
```

We will deploy a test Pod on `ip-172-16-61-234.ec2.internal`.

### Creating the Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mock-app
  labels:
    app: mock-app
spec:
  nodeName: ip-172-16-61-234.ec2.internal
  containers:
  - name: nginx
    image: nginx
```

Verify that the Pod is running:

```shell
kubectl get pods -o wide
```

Example output:

```
NAME                                        READY   STATUS    RESTARTS   AGE   IP               NODE                             NOMINATED NODE   READINESS GATES
egressgateway-agent-zw426                   1/1     Running   0          15m   172.16.103.117   ip-172-16-103-117.ec2.internal   <none>           <none>
egressgateway-agent-zw728                   1/1     Running   0          15m   172.16.61.234    ip-172-16-61-234.ec2.internal    <none>           <none>
egressgateway-controller-6cc84c6985-9gbgd   1/1     Running   0          15m   172.16.51.178    ip-172-16-61-234.ec2.internal    <none>           <none>
mock-app                                    1/1     Running   0          12m   172.16.51.74     ip-172-16-61-234.ec2.internal    <none>           <none>
```

## Creating the EgressPolicy CR

This `EgressPolicy` CR matches the `mock-app` Pod, specifying that its outbound traffic should be routed through the EgressGateway.

```yaml
apiVersion: egressgateway.spidernet.io/v1beta1
kind: EgressPolicy
metadata:
  name: test-egw-policy
  namespace: default
spec:
  egressIP:
    useNodeIP: true
  appliedTo:
    podSelector:
      matchLabels:
        app: mock-app
  egressGatewayName: egressgateway
```

## Verifying Outbound IP Address

Exec into the test Pod and check the outbound IP:

```shell
kubectl exec -it mock-app -- bash
curl ipinfo.io
```

Example response:

```json
{
  "ip": "34.239.162.85",
  "hostname": "ec2-34-239-162-85.compute-1.amazonaws.com",
  "city": "Ashburn",
  "region": "Virginia",
  "country": "US",
  "loc": "39.0437,-77.4875",
  "org": "AS14618 Amazon.com, Inc.",
  "postal": "20147",
  "timezone": "America/New_York",
  "readme": "https://ipinfo.io/missingauth"
}
```

This confirms that the Pod is using the EgressGateway’s node IP (`34.239.162.85`) as its outbound address.

Since EgressGateway provides HA, if the primary gateway node fails, traffic will automatically shift to the backup node, changing the public IP accordingly.

### Summary

- **EgressGateway** provides HA for outbound traffic from Kubernetes Pods.
- **AWS EC2 nodes with public IPs** are used as egress gateways.
- **Helm** is used to install EgressGateway.
- **EgressGateway CR** selects gateway nodes via labels.
- **EgressPolicy CR** ensures traffic from specific Pods is routed through the gateway.
- **Failover** automatically shifts outbound traffic to an alternate gateway if a node fails.

Would you like any additional modifications or explanations? 🚀
