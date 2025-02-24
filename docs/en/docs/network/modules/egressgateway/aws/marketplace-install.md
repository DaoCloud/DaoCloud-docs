# Installing EgressGateway from AWS Marketplace

EgressGateway provides a cost-effective, scalable egress traffic management solution that meets enterprise requirements for fixed public IP functionality. It serves as an ideal alternative to NAT Gateway, enabling lower-cost and more fine-grained egress connection control.

This guide explains how to install EgressGateway from AWS Marketplace.

## Prerequisites

Before installation, ensure you meet the following prerequisites:

- Subscribe to EgressGateway.
- Create a Kubernetes cluster.

## Installing with Helm

After subscribing to EgressGateway, install it on your Kubernetes cluster using the Helm Chart.

!!! note

    The `username` and `password-stdin` correspond to your AWS login credentials.

```shell
export HELM_EXPERIMENTAL_OCI=1
aws ecr get-login-password --region us-east-1 | helm registry login --username AWS --password-stdin 709825985650.dkr.ecr.us-east-1.amazonaws.com
mkdir awsmp-chart && cd awsmp-chart
helm pull oci://709825985650.dkr.ecr.us-east-1.amazonaws.com/daocloud-hong-kong/egressgateway --version 0.0.2
tar xf $(pwd)/* && find $(pwd) -maxdepth 1 -type f -delete
helm install --generate-name --namespace <ENTER_NAMESPACE_HERE> ./*
```

## Getting Started

Once the installation is complete, follow these steps to start using EgressGateway.

### Creating a Gateway Instance

1. Select gateway nodes and label them.

    ```shell
    ~ kubectl get nodes -A -o wide
    NAME                             STATUS   ROLES    AGE   VERSION               INTERNAL-IP      EXTERNAL-IP                         
    ip-172-16-103-117.ec2.internal   Ready    <none>   25m   v1.30.0-eks-036c24b   172.16.103.117   34.239.162.85  
    ip-172-16-61-234.ec2.internal    Ready    <none>   25m   v1.30.0-eks-036c24b   172.16.61.234    54.147.15.230
    ip-172-16-62-200.ec2.internal    Ready    <none>   25m   v1.30.0-eks-036c24b   172.16.62.200    54.147.16.130  
    ```

    In this demo, we select `ip-172-16-103-117.ec2.internal` and `ip-172-16-62-200.ec2.internal` as gateway nodes and label them with `role: gateway`.

    ```shell
    kubectl label node ip-172-16-103-117.ec2.internal role=gateway
    kubectl label node ip-172-16-62-200.ec2.internal role=gateway
    ```

2. Create a gateway instance and use labels to match the gateway nodes. Example YAML:

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

### Deploying a Test Pod

After creating the gateway instance, deploy a Pod to validate the setup. In this demo, we run the Pod on the `ip-172-16-61-234.ec2.internal` node. Example YAML:

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

Verify that the Pod is in the `Running` state.

```shell
~ kubectl get pods -o wide
NAME                                        READY   STATUS    RESTARTS   AGE   IP               NODE                             NOMINATED NODE   READINESS GATES
egressgateway-agent-zw426                   1/1     Running   0          15m   172.16.103.117   ip-172-16-103-117.ec2.internal   <none>           <none>
egressgateway-agent-zw728                   1/1     Running   0          15m   172.16.61.234    ip-172-16-61-234.ec2.internal    <none>           <none>
egressgateway-controller-6cc84c6985-9gbgd   1/1     Running   0          15m   172.16.51.178    ip-172-16-61-234.ec2.internal    <none>           <none>
mock-app                                    1/1     Running   0          12m   172.16.51.74     ip-172-16-61-234.ec2.internal    <none>           <none>
```

### Configuring a Gateway Policy for Pods

An EgressGateway policy defines which Pods' egress traffic should be forwarded through EgressGateway nodes and specifies additional configuration details. Any Pod matching the policy that attempts to access an external address (outside Node IPs, CNI Pod CIDR, or ClusterIP) will be forwarded through the EgressGateway node.

Example YAML:

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

### Testing the Egress IP Address

Exec into the container and run `curl ipinfo.io` to verify that the Pod is using the gateway node's IP to access the internet. `ipinfo.io` will return the public IP.

!!! note

    Since EgressGateway implements high availability (HA) with an active-standby mechanism, the egress IP will change automatically if a failover occurs.

```shell
kubectl exec -it -n default mock-app bash
curl ipinfo.io
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

## Getting Help

For more information, refer to the detailed [EgressGateway documentation](../index.md).
