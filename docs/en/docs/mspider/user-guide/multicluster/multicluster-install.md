# Mesh multicloud deployment

This page explains how to deploy a service mesh in a multicloud environment.

## Prerequisites

### Cluster requirements

1. **Cluster type and version**: Specify the type and version of the current cluster to ensure that the service mesh installed later can run normally in the cluster.
2. **Provide reliable IP**: The control plane cluster must provide a reliable IP for other data plane clusters to access the control plane.
3. **Authorization**: The cluster that joins the mesh needs to provide a remote key with sufficient permissions to allow Mspider to install components on the cluster and the Istio control plane to access the API Server of other clusters.

### Multicluster regional planning

In Istio, Regions, Zones, and SubZones are concepts used to maintain service availability in multicluster deployments. Specifically:

- **Region** represents a large region, usually used to represent the data center region of the entire cloud provider; in Kubernetes, the label [`topology.kubernetes.io/region`](https://kubernetes.io/docs/reference/kubernetes-api/labels-annotations-taints/#topologykubernetesioregion) determines the region of the node.
- **Zone** represents a small zone, usually used to represent a sub-zone in a data center; in Kubernetes, the label [`topology.kubernetes.io/zone`](https://kubernetes.io/docs/reference/kubernetes-api/labels-annotations-taints/#topologykubernetesiozone) to determine the zone of a node.
- **SubZone** is a smaller area used to represent a smaller part of the Zone. The concept of partitions does not exist in Kubernetes, so Istio introduces custom node labels [`topology.istio.io/subzone`](https://github.com/istio/api/blob/82b9feb5a1c091ad9a28311c62b4f6f07803a9fa/label/labels.yaml# L84) to define partitions.

The role of these concepts is mainly to help Istio manage the availability of services between different regions. For example, in a multicluster deployment, if a service fails in Zone A, Istio can be configured to automatically divert service traffic to Zone B to ensure service availability.

The configuration method is to add the corresponding Label to **each node** of the cluster:

| Area | Label |
| ------- | ----------------------------- |
| Region | topology.kubernetes.io/region |
| Zone | topology.kubernetes.io/zone |
| SubZone | topology.istio.io/subzone |

To add a Label, you can find the corresponding cluster through the container management platform, and configure the Label for the corresponding node


### mesh Planning

#### mesh basic information

- mesh ID
- mesh version
- mesh cluster

#### Network Planning

Confirm the network status between clusters and configure according to different statuses
This part mainly lies in the configuration of the two parts of the multi-network mode:

- Planning Network ID
- Deployment and configuration of east-west mesh
- How to expose the mesh control surface to other worker clusters.

There are two network modes:

- Single network mode
     > It is clear whether the Pod network between clusters can be directly connected.
     > If the Pod network can communicate directly, it proves that it is the same network mode, but it should be noted that if there is a conflict between the **Pod network**, you need to choose a different network mode
- Multi-network mode
     > If the network between the clusters is disconnected, you need to divide the **network ID** for the cluster, and you need to install east-west gateways in clusters in different network areas,
     > And configure related configurations. The specific operation steps are in the following chapter [Installation and Configuration of mesh Components in Different Network Modes](#_21).

### planning form

The cluster and mesh-related plans mentioned above are gathered into a form, which is convenient for users to refer to.

#### Cluster Planning

| Cluster Name | Cluster Type | Cluster Pod Subnet (podSubnet) | Pod Network Communication Relationship | Cluster Node & Network Area | Cluster Version | Master IP |
| -------------- | -------- | ------------------------- | ---------------- | ------------------------------- | -------- | ------------|
| mdemo-cluster1 | standard k8s | "10.201.0.0/16" | - | master: region1/zone1/subzone1 | 1.25 | 10.64.30.130 |
| mdemo-cluster2 | standard k8s | "10.202.0.0/16" | - | master: region1/zone2/subzone2 | 1.25 | 10.6.230.5 |
| mdemo-cluster3 | standard k8s | "10.100.0.0/16" | - | master: region1/zone3/subzone3 | 1.25 | 10.64.30.131 |

#### mesh Planning

| configuration item | value |
| -------- | ----------------------------------------- ------ |
| Mesh ID | mdemo-mesh |
| mesh Mode | Managed Mode |
| Network mode | Multi-network mode (need to install east-west gateway, plan network ID) |
| mesh version | 1.15.3-mspider |
| Managed Cluster | mdemo-cluster1 |
| Working clusters | mdemo-cluster1, mdemo-cluster2, mdemo-cluster3 |

#### Network Planning

As known from the above table, there is no network communication between the clusters, so the mesh is in multi-network mode, and the following configuration needs to be planned:

| cluster name | cluster mesh role | cluster network identifier (network ID) | hosted-istiod LB IP | eastwest LB IP | ingress LB IP |
| -------------- | ------------------ | --------------- ------- | ------------------- | -------------- | ------- ------ |
| mdemo-cluster1 | managed cluster, worker cluster | network-c1 | 10.64.30.71 | 10.64.30.73 | 10.64.30.72 |
| mdemo-cluster2 | working cluster | network-c2 | - | 10.6.136.29 | - |
| mdemo-cluster3 | working cluster | network-c3 | - | 10.64.30.77 | - |

## Access cluster and component preparation

Users need to prepare a cluster that meets the requirements. The cluster can be newly created (the creation capability of the container management platform can also be used to create a cluster), or it can be an existing cluster.

However, the clusters required for subsequent meshs must be connected to the container management platform.

### Access to the cluster

If the cluster is not created through the container management platform, such as an existing cluster, or a cluster created through a custom method (like kubeadm or Kind cluster), you need to connect the cluster to the container management platform.





### Confirm observable components (optional)

The observability of the key capability of the mesh, the key observability component is Insight Agent, so if you need to have the observation capability of the mesh, you need to install its component.

The cluster created by creating a cluster on the container management platform will have the Insight Agent component installed by default.

For other methods, you need to find the `Helm application` in the cluster in the container management interface, and select `insight-agent` to install.







## Mesh ceployment

Create a mesh through the service mesh, and add the planned cluster to the corresponding mesh.

### Create mesh

First in the mesh management page -> `Create mesh`:



The specific parameters for creating the mesh are shown in the figure:

1. Select a managed mesh: In a multicloud environment, only the managed mesh mode can manage multiple clusters
2. Enter a unique mesh name
3. According to the pre-condition environment, select the pre-selected mesh version that meets the requirements
4. Select the cluster where the managed control plane resides
5. Load balancing IP: This parameter is required by the Istiod that exposes the control plane and needs to be prepared in advance
6. container registry: In the private cloud, you need to upload the mirror image required by the mesh to the registry. For the public cloud, it is recommended to fill in `release.daocloud.io/mspider`



The mesh is being created, you need to wait for the mesh to be created, and the status will change from `creating` to `running`;

### Expose Mesh Hosted Control Surface Hosted Istiod

#### Confirm managed mesh control plane service

After ensuring that the mesh status is normal, observe whether the Services under `istio-system` of the control plane cluster `mdemo-cluster1` are successfully bound to the LoadBalancer IP.



Found no LoadBalancer IP assigned for service `istiod-mdemo-cluster-hosted-lb` hosting the mesh control plane requires additional processing.

#### Assign EXTERNAL IP

There are different ways to apply for or allocate LoadBalancer IP in different environments, especiallyIt is a public cloud environment, and the LoadBalancer IP needs to be created according to the method provided by the public cloud vendor.

This page demonstrates that the demo adopts the metallb method to assign an IP to the LoadBalancer Service. For related deployment and configuration, refer to the [Metallb Installation Configuration](#metallb) section.

After deploying metallb, [confirm hosted mesh control plane service](#_17) again.

#### Verify managed control plane Istiod `EXTERNAL IP` is unobstructed

Verify the managed control plane Istiod in an unmanaged cluster environment. This practice is verified by curl. If a 400 error is returned, it can be basically determined that the network has been opened:

```bash
hosted_istiod_ip="10.64.30.71"
curl -I "${hosted_istiod_ip}:443"
# HTTP/1.0 400 Bad Request
```

#### Confirm and configure mesh hosting control plane Istiod parameters

1. Get Managed mesh Control Plane Service `EXTERNAL IP`

     In the mesh `mdemo-mesh` control plane cluster `mdemo-cluster1`, confirm that the hosted mesh control plane service `istiod-mdemo-mesh-hosted-lb` has been allocated LoadBalancer IP, and record its IP, as follows:

     

     Confirm hosted mesh control plane service `istiod-mdemo-mesh-hosted-lb` `EXTERNAL-IP` is `10.64.30.72`.

1. Manually configure mesh hosting control plane Istiod parameters

     First, enter the global control plane cluster `kpanda-global-cluster` on the container management platform (if you cannot confirm the location of the relevant cluster, you can ask the corresponding person in charge or pass [Query Global Service Cluster](#_30))

     -> `custom resource module` search resource `GlobalMesh`
     -> Next, find the corresponding mesh `mdemo-mesh` in `mspider-system`
     -> Then edit the YAML

     - Add `istio.custom_params.values.global.remotePilotAddress` parameter in `.spec.ownerConfig.controlPlaneParams` field in YAML;
     - Its value is the `istiod-mdemo-mesh-hosted-lb` `EXTERNAL-IP` address noted above: `10.64.30.72`.

     

     

     

### Add worker cluster

Add clusters on the service mesh GUI.

1. After the mesh control plane is successfully created, select the corresponding mesh and enter the mesh management page -> `Cluster Management` -> `Add Cluster`:

     

1. After selecting the desired working cluster, wait for the cluster installation mesh component to complete;

     

1. During the access process, the cluster status will change from `Accessing` to `Accessed`:

     

#### Detect whether the multicloud control plane is normal

Since the current working cluster is different from the pod network of the mesh control plane cluster, it is necessary to expose the Istiod of the control plane to the public network through the above [Exposing mesh Hosted Control Plane Hosted Istiod](#hosted-istiod).

To verify whether the Istio-related components of the working cluster can run normally, you need to check whether the `istio-ingressgateway` under the `istio-system` namespace can run normally in the working cluster:



## Install and configure mesh components in different network modes

This part is mainly divided into two parts:

1. Configure `Network ID` for all worker clusters
2. Install east-west gateways in all clusters that do not communicate with each other

Here is a question first: Why do you need to install an east-west gateway?
Since the Pod mesh between working clusters cannot be directly connected, network problems will also occur when services communicate across clusters. Istio provides a solution that is the East-West Gateway.
When the target service is located in a different network, its traffic will be forwarded to the east-west gateway of the target cluster, and the east-west gateway will parse the request and forward the request to the real target service.

After understanding the principle of the east-west gateway above, there is a new question, how does Istio distinguish which network the service is in?
Istio requires the user to define the `network ID` shown when installing Istio per worker cluster, which is why the first step exists.

### Manually configure the `Network ID` for the worker cluster

Due to the different working cluster networks, it is necessary to manually configure `network ID` for each working cluster.
If in the actual environment, the Pod networks between the clusters can reach each other directly, they can be configured with the same `network ID`.

Let's start configuring `Network ID`, the specific process is as follows:

1. First enter the global control plane cluster `kpanda-global-cluster` (if you cannot confirm the location of the relevant cluster, you can ask the corresponding person in charge or pass [Query Global Service Cluster](#_30))
2. Then search resource `MeshCluster` in `Custom Resource Module` ->
3. Find the working clusters added to the mesh under the `mspider-system` namespace. The working clusters in this case are: `mdemo-cluster2`, `mdemo-cluster3`
4. Take `mdemo-cluster2` as an example, edit YAML

     - Find the field `.spec.meshedParams[].params`, and add the field `Network ID` to the parameter column
     - Notes on parameter columns:
         - Need to confirm whether `global.meshID: mdemo-mesh` is the same mesh ID
         - Need to confirm whether the cluster role `global.clusterRole: HOSTED_WORKLOAD_CLUSTER` is a working cluster
     - Add parameter `istio.custom_params.values.global.network` with value according to network ID in original [planning form](#_8): `network-c2`

     

     

     

Repeat the above steps to add `network ID` to all working clusters (`mdemo-cluster1, mdemo-cluster2, mdemo-cluster3`).

### Identify the `network ID` for the `istio-system` of the worker cluster

Enter the container management platform, enter the corresponding working cluster: `mdemo-cluster1, mdemo-cluster2, mdemo-cluster3` namespaces and add network labels.

- Tag Key: `topology.istio.io/network`
- Label value: `${CLUSTER_NET}`

Let's take mdemo-cluster3 as an example, find `namespace`, select `istio-system` -> `modify label`.





### Manually install East-West Gateway

#### Create a gateway instance

After confirming that all Istio-related components in the working cluster are in place, start installing the East-West Gateway.

Install the east-west gateway through the IstioOperator resource in the working cluster. The YAML of the east-west gateway is as follows:

!!! note

     Be sure to modify the parameters according to the `network ID` of the current cluster.

```bash linenums="1"
#cluster1
CLUSTER_NET_ID=network-c1
CLUSTER=mdemo-cluster1
LB_IP=10.64.30.73

#cluster2
CLUSTER_NET_ID=network-c2
CLUSTER=mdemo-cluster2
LB_IP=10.6.136.29

#cluster3
CLUSTER_NET_ID=network-c3
CLUSTER=mdemo-cluster3
LB_IP=10.64.30.77

MESH_ID=mdemo-mesh
HUB=release-ci.daocloud.io/mspider
ISTIO_VERSION=1.15.3-mspider
cat <<EOF> eastwest-iop.yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
metadata:
   name: eastwest
   namespace: istio-system
spec:
   components:
     ingressGateways:
       - enabled: true
         k8s:
           env:
             - name: ISTIO_META_REQUESTED_NETWORK_VIEW
               value: ${CLUSTER_NET_ID} # Change to the network ID of the current cluster
           service:
             loadBalancerIP: ${LB_IP} # Change to the LB IP planned by this cluster for the east-west gateway
             ports:
               - name: tls
                 port: 15443
                 targetPort: 15443
             type: LoadBalancer
         label:
           app: istio-eastwestgateway
           istio: eastwestgateway
           topology.istio.io/network: ${CLUSTER_NET_ID} # Change to the network ID of the current cluster
         name: istio-eastwestgateway
   profile: empty
   tag: ${ISTIO_VERSION}
   values:
     gateways:
       istio_ingressgateway:
         injectionTemplate: gateway
     global:
       network: ${CLUSTER_NET_ID} # Change to the network ID of the current cluster
       hub: ${HUB} # Optional, if you can't bypass the wall or private registry, please modify
       meshID: ${MESH_ID} # Change to the mesh ID (Mesh ID) of the current cluster
       multiCluster:
         clusterName: ${CLUSTER} # modify to current
EOF
```

It is created by:

1. Enter the corresponding working cluster on the container management platform
2. `Custom Resources` module search `IstioOperator`
3. Check the `istio-system` namespace
4. Click `Create YAML`





### Create East-West Gateway Gateway resource

Create a rule in the mesh's `Gateway Rules`:

```yaml
apiVersion: networking.istio.io/v1beta1
kind: Gateway
metadata:
   name: cross-network-gateway
   namespace: istio-system
spec:
   selector:
     istio: eastwestgateway
   servers:
     -hosts:
         - "*.local"
       port:
         name: tls
         number: 15443
         protocol: TLS
       tls:
         mode: AUTO_PASSTHROUGH
```

### Set the mesh global network configuration

After installing the east-west gateway and the resolution rules of the gateway, you need to declare the configuration of the east-west gateway in the mesh in all clusters.
Enter the global control plane cluster `kpanda-global-cluster` on the container management platform (if you cannot confirm the location of the relevant cluster, you can ask the corresponding person in charge or pass [Query Global Service Cluster](#_30))

-> Search for the resource `GlobalMesh` in the `Custom Resources` section
-> Next find the corresponding mesh `mdemo-mesh` in `mspider-system`
-> Then edit the YAML

> Add a series of `istio.custom_params.values.global.meshNetworks` parameters in `.spec.ownerConfig.controlPlaneParams` field in YAML

```YAML
#! ! The two lines of configuration are indispensable
# Format: istio.custom_params.values.global.meshNetworks.${CLUSTER_NET_ID}.gateways[0].address
# istio.custom_params.values.global.meshNetworks.${CLUSTER_NET_ID}.gateways[0].port

istio.custom_params.values.global.meshNetworks.network-c1.gateways[0].address: 10.64.30.73 # cluster1
istio.custom_params.values.global.meshNetworks.network-c1.gateways[0].port: '15443' # cluster3 east-west gateway port
istio.custom_params.values.global.meshNetworks.network-c2.gateways[0].address: 10.6.136.29 # cluster2
istio.custom_params.values.global.meshNetworks.network-c2.gateways[0].port: '15443' # cluster2 east-west mesh port
istio.custom_params.values.global.meshNetworks.network-c3.gateways[0].address: 10.64.30.77 # cluster3
istio.custom_params.values.global.meshNetworks.network-c3.gateways[0].port: '15443' # cluster3 east-west gateway port
```



## Network connectivity demo application and verification

### Deploy the demo

There are mainly two applications: [helloworld](https://github.com/istio/istio/blob/1.16.0/samples/helloworld/helloworld.yaml) and [sleep](https://github.com/istio /istio/blob/1.16.0/samples/sleep/sleep.yaml) (these two demos belong to the test application provided by Istio)

Cluster deployment:

cluster | helloworld and version | sleep
---|----------------|------
mdemo-cluster1 | :heart: VERSION=vc1 | :heart:
mdemo-cluster1 | :heart: VERSION=vc2 | :heart:
mdemo-cluster1 | :heart: VERSION=vc3 | :heart:

#### Container management platform deployment demo

It is recommended to use the container management platform to create corresponding workloads and applications, find the corresponding cluster on the container management platform, and enter the [Console] to perform the following operations.

The following takes mdemo-cluster1 to deploy helloworld vc1 as an example:

Points to note for each of these clusters:

- Mirror address:

     - helloworld: docker.m.daocloud.io/istio/examples-helloworld-v1
     - Sleep: curlimages/curl

- **helloworld** workload increases corresponding to **label**
     - app: helloworld
     - version: ${VERSION}
- **helloworld** Workload increase corresponding version **environment variables**
     - SERVICE_VERSION: ${VERSION}









#### Command line deployment demo

The configuration files that need to be used in the deployment process are:

- [gen-helloworld.sh](https://github.com/istio/istio/blob/1.16.0/samples/helloworld/gen-helloworld.sh)
- [sleep.yaml](https://github.com/istio/istio/blob/1.16.0/samples/sleep/sleep.yaml)

```bash linenums="1"
# -------------------- cluster1 --------------------
kubectl create namespace sample
kubectl label namespace sample istio-injection=enabled

# deploy helloworld vc1
bash gen-helloworld.sh --version vc1 | sed -e "s/docker.io/docker.m.daocloud.io/" | kubectl apply -f - -n sample

# deploy sleep
kubectl apply -f sleep.yaml -n sample

# -------------------- cluster2 --------------------
kubectl create namespace sample
kubectl label namespace sample istio-injection=enabled

# deploy helloworld vc2
bash gen-helloworld.sh --version vc2 | sed -e "s/docker.io/docker.m.daocloud.io/" | kubectl apply -f - -n sample

# deploy sleep
kubectl apply -f sleep.yaml -n sample

# -------------------- cluster3 --------------------
kubectl create namespace sample
kubectl label namespace sample istio-injection=enabled

# deploy helloworld vc3
bash gen-helloworld.sh --version vc3 | sed -e "s/docker.io/docker.m.daocloud.io/" | kubectl apply -f - -n sample

# deploy sleep
kubectl apply -f sleep.yaml -n sample
```

### Verify the demo cluster network

```bash linenums="1"
# Arbitrarily choose a cluster to execute
while true; do kubectl exec -n sample -c sleep \
                "$(kubectl get pod -n sample -l app=sleep -o jsonpath='{.items[0].metadata.name}')" \
               -- curl -sS helloworld.sample:5000/hello; done

# Expected results will poll different versions of the three clusters, the results are as follows:
# Hello version: vc2, instance: helloworld-vc2-5d67bc48d8-2tpxd
# Hello version: vc2, instance: helloworld-vc2-5d67bc48d8-2tpxd
# Hello version: vc2, instance: helloworld-vc2-5d67bc48d8-2tpxd
# Hello version: vc2, instance: helloworld-vc2-5d67bc48d8-2tpxd
# Hello version: vc1, instance: helloworld-vc1-846f79cc4d-2d8kd
# Hello version: vc1, instance: helloworld-vc1-846f79cc4d-2d8kd
# Hello version: vc1, instance: helloworld-vc1-846f79cc4d-2d8kd
# Hello version: vc3, instance: helloworld-vc3-55b7b5869f-trl8v
# Hello version: vc1, instance: helloworld-vc1-846f79cc4d-2d8kd
# Hello version: vc3, instance: helloworld-vc3-55b7b5869f-trl8v
# Hello version: vc2, instance: helloworld-vc2-5d67bc48d8-2tpxd
# Hello version: vc1, instance: helloworld-vc1-846f79cc4d-2d8kd
# Hello version: vc2, instance: helloworld-vc2-5d67bc48d8-2tpxd
```

## Expand

### Other ways to create a cluster

#### Create a cluster through container management

There are many ways to create a cluster. It is recommended to use the cluster creation function in container management, but users can choose other creation methods. For other solutions provided in This page, please refer to [Other ways to create clusters] in the extended chapter (#_26)









You can flexibly select the components that need to be expanded in the cluster, and the observability of the mesh must rely on Insight-agent



If the cluster needs to define more advanced cluster configurations, they can be added in this step.



It takes about 30 minutes to create the cluster.



#### Create a cluster with kubeadm

```bash
kubeadm init --image-repository registry.aliyuncs.com/google_containers \
              --apiserver-advertise-address=10.64.30.131 \
              --service-cidr=10.111.0.0/16\
              --pod-network-cidr=10.100.0.0/16 \
              --cri-socket /var/run/cri-dockerd.sock
```

#### Create a kind cluster

```bash linenums="1"
cat <<EOF > kind-cluster1.yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
networking:
   podSubnet: "10.102.0.0/16" # Install the network planning phase, define the planned pod subnet
   serviceSubnet: "10.122.0.0/16" # Installation network planning phase, define the planned service subnet
   apiServerAddress: 10.6.136.22
nodes:
   -role: control-plane
     image: kindest/node:v1.25.3@sha256:f52781bc0d7a19fb6c405c2af83abfeb311f130707a0e219175677e366cc45d1
     extraPortMappings:
       - containerPort: 35443 # If you cannot apply for LoadBalancer, you can temporarily use the nodePort method
         hostPort: 35443 # set the bind address on the host

EOF
cat <<EOF > kind-cluster2.yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
networking:
   podSubnet: "10.103.0.0/16" # Install the network planning phase, define the planned pod subnet
   serviceSubnet: "10.133.0.0/16" # Installation network planning phase, define the planned service subnet
   apiServerAddress: 10.6.136.22
nodes:
   -role: control-plane
     image: kindest/node:v1.25.3@sha256:f52781bc0d7a19fb6c405c2af83abfeb311f130707a0e219175677e366cc45d1
     extraPortMappings:
       - containerPort: 35443 # If you cannot apply for LoadBalancer, you can temporarily use the nodePort method
         hostPort: 35444 # set the bind address on the host

EOF

kind create cluster --config kind-cluster1.yaml --name mdemo-kcluster1
kind create cluster --config kind-cluster2.yaml --name mdemo-kcluster2
```

### Metallb installation configuration

#### Demo cluster metallb network pool planning record

| Cluster name | IP pool | IP allocation |
| -------------- | ----------------------- | ---------- -|
| mdemo-cluster1 | 10.64.30.71-10.64.30.73 | - |
| mdemo-cluster2 | 10.6.136.25-10.6.136.29 | - |
| mdemo-cluster3 | 10.64.30.75-10.64.30.77 | - |

#### Install

#### Container management platform Helm installation

It is recommended to use `Helm application` -> `Helm chart` in the container management platform -> find metallb -> `install`.





##### Manual installation

See [MetalLB official documentation](https://metallb.org/installation/).

Note: If the CNI of the cluster uses calico, you need to disable the BGP mode of calico, otherwise it will affect the normal work of MetalLB.

```bash linenums="1"
# If kube-proxy is using IPVS mode, you need to enable staticARP
# see what changes would be made, returns nonzero returncode if different
kubectl get configmap kube-proxy -n kube-system -o yaml | \
sed -e "s/strictARP: false/strictARP: true/" | \
kubectl diff -f - -n kube-system

# actually apply the changes, returns nonzero returncode on errors only
kubectl get configmap kube-proxy -n kube-system -o yaml | \
sed -e "s/strictARP: false/strictARP: true/" | \
kubectl apply -f - -n kube-system

# deploy metallb
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.7/config/manifests/metallb-native.yaml

# Check pod running status
kubectl get pods -n metallb-system

# configure metallb
cat << EOF | kubectl apply -f -
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
   name: first-pool
   namespace: metallb-system
spec:
   addresses:
   - 10.64.30.75-10.64.30.77 # Modified according to the plan
EOF
cat << EOF | kubectl apply -f -
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
   name: example
   namespace: metallb-system
spec:
   ipAddressPools:
   - first-pool
   interfaces:
   -enp1s0
   # - ens192 # According to the name of the network card of different machines, please modify it
EOF
```

#### Add the specified IP to the corresponding service

```bash
kubectl annotate service -n istio-system istiod-mdemo-mesh-hosted-lb metallb.universe.tf/address-pool='first-pool'
```

#### Verify

```bash linenums="1"
kubectl create deploy nginx --image docker.m.daocloud.io/nginx:latest --port 80 -n default
kubectl expose deployment nginx --name nginx-lb --port 8080 --target-port 80 --type LoadBalancer -n default

# Get the corresponding service EXTERNAL-IP
kubectl get svc -n default
# NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S) AGE
# kubernetes ClusterIP 10.212.0.1 <none> 443/TCP 25h
# nginx-lb LoadBalancer 10.212.249.64 10.6.230.71 8080:31881/TCP 10s

curl -I 10.6.230.71:8080
# HTTP/1.1 200 OK
# Server: nginx/1.21.6
# Date: Wed, 02 Mar 2022 15:31:15 GMT
# Content-Type: text/html
# Content-Length: 615
# Last-Modified: Tue, 25 Jan 2022 15:03:52 GMT
# Connection: keep-alive
# ETag: "61f01158-267"
# Accept-Ranges: bytes
```

### Query the global service cluster

Sets managed by containersOn the group list interface, search for `Cluster Role: Global Service Cluster`.


