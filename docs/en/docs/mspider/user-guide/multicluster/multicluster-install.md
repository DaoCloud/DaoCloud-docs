# MultiCloud Deployment of Service Mesh

This page explains how to deploy a service mesh in a multicloud environment.

## Prerequisites

### Cluster Requirements

1. **Cluster Type and Version**: Determine the type and version of your current cluster to ensure that the service mesh you install can run properly on it.
2. **Reliable IP Address**: The control plane cluster must provide a reliable IP address for other data plane clusters to access the control plane.
3. **Authorization**: The cluster joining the mesh needs to provide a remote key with sufficient permissions, allowing Mspider to install components on the cluster and for Istio control plane to access the API Server of other clusters.

### Multi-Cluster Region Planning

In Istio, regions, zones, and subzones are concepts used to maintain service availability in a multi-cluster deployment. Specifically:

- **Region** represents a major geographical area, usually referring to a data center region of the cloud provider. In Kubernetes, the label [ `topology.kubernetes.io/region` ](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/#topologykubernetesioregion) identifies the region of a node.
- **Zone** represents a smaller area within a data center, typically representing a sub-region. In Kubernetes, the label [ `topology.kubernetes.io/zone` ](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/#topologykubernetesiozone) identifies the zone of a node.
- **SubZone** is an even smaller area within a zone. Since Kubernetes does not have the concept of partitions, Istio introduces a custom node label [ `topology.istio.io/subzone` ](https://github.com/istio/api/blob/master/networking/v1alpha3/label/labels.proto#L84) to define a partition.

These concepts help Istio manage service availability across different regions. For example, in a multi-cluster deployment, if a service fails in Zone A, Istio can automatically reroute the service traffic to Zone B to ensure service availability.

To configure this, you need to add the corresponding labels to **each node** in the cluster:

| Areas    | Labels                         |
| ------- | ----------------------------- |
| Region  | topology.kubernetes.io/region |
| Zone    | topology.kubernetes.io/zone   |
| SubZone | topology.istio.io/subzone     |

Adding labels can be done by finding the corresponding cluster in the container management platform and configuring labels for the respective nodes.

![Add Node Label](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/add-node-label.png)

![Add Node Labels](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/add-node-labels2.png)

### Mesh Planning

#### Mesh Basic Information

- Mesh ID
- Mesh Version
- Mesh Cluster

#### Network Planning

Verify the network connectivity between clusters and configure accordingly. This section mainly focuses on two parts of the multi-network mode configuration:

- Plan network IDs
- Deploy and configure East-West mesh
- Expose the mesh control plane to other working clusters.

There are two network modes:

- Single Network Mode
   > Determine if the Pod networks between clusters can communicate directly.
   > If the Pod networks can communicate directly, it means they are in the same network mode. However, if there is a **conflict in Pod networks**, a different network mode needs to be selected.
- Multi-Network Mode
   > If the networks between clusters are not connected, assign **network IDs** to the clusters and install East-West gateways in different network regions.
   > Configure relevant settings. The specific steps are explained in the following chapter [Installation and Configuration of Mesh Components in Different Network Modes](#installation-and-configuration-of-mesh-components-for-different-network-modes).

### Planning Form

Consolidate the cluster and mesh-related planning mentioned above into a form for easier reference.

#### Cluster Planning

| Cluster Name    | Cluster Type | Cluster Pod Subnet (podSubnet) | Pod Network Connectivity | Cluster Nodes & Network Regions | Cluster Version | Master IP      |
| --------------- | ------------ | ----------------------------- | ----------------------- | ------------------------------ | --------------- | -------------- |
| mdemo-cluster1  | Standard k8s | "10.201.0.0/16"               | -                       | master: region1/zone1/subzone1 | 1.25            | 10.64.30.130   |
| mdemo-cluster2  | Standard k8s | "10.202.0.0/16"               | -                       | master: region1/zone2/subzone2 | 1.25            | 10.6.230.5     |
| mdemo-cluster3  | Standard k8s | "10.100.0.0/16"               | -                       | master: region1/zone3/subzone3 | 1.25            | 10.64.30.131   |

#### Mesh Planning

| Configuration Item | Value                                       |
| ------------------ | ------------------------------------------- |
| Mesh ID            | mdemo-mesh                                   |
| Mesh Mode          | Managed Mode                                |
| Network Mode       | Multi-Network Mode (Requires East-West Gateway Installation and Network ID Planning) |
| Mesh Version       | 1.15.3-mspider                              |
| Hosted Cluster     | mdemo-cluster1                              |
| Work Clusters      | mdemo-cluster1, mdemo-cluster2, mdemo-cluster3 |

#### Network Planning

Based on the information provided in the previous form, there is no network connectivity between clusters. Therefore, the mesh is in multi-network mode, and the following configurations need to be planned:

| Cluster Name    | Cluster Mesh Role | Cluster Network Identifier (Network ID) | Hosted-Istiod LB IP | East-West LB IP | Ingress LB IP |
| --------------- | ----------------- | --------------------------------------- | ------------------- | --------------- | ------------- |
| mdemo-cluster1  | Hosted Cluster, Work Cluster | network-c1                            | 10.64.30.71         | 10.64.30.73    | 10.64.30.72   |
| mdemo-cluster2  | Work Cluster       | network-c2                            | -                   | 10.6.136.29     | -             |
| mdemo-cluster3  | Work Cluster       | network-c3                            | -                   | 10.64.30.77     | -             |

## Intergrating Clusters and Component Preparation

Users need to prepare clusters that meet the requirements. The clusters can be newly created (the cluster creation capability of the container management platform can be used), or they can be existing clusters.

However, all clusters required for the subsequent mesh must be integrated into the container management platform.

### Intergrating Clusters

If the clusters were not created through the container management platform, such as existing clusters or clusters created using custom methods (e.g., kubeadm or Kind clusters), they need to be integrated into the container management platform.

![Intergrating Clusters](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/kpanda-import-cluster0.png)

![Intergrating Clusters](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/kpanda-import-cluster.png)

### Confirming Observability Components (Optional)

Observability is a key capability of the mesh, and one of the critical observability components is the Insight Agent. Therefore, if you want to have observability capabilities for the mesh, you need to install this component.

Clusters created through the container management platform will have the Insight Agent component installed by default.

For other methods, you need to go to the container management interface, find "Helm Applications" in your cluster, and select "insight-agent" to install.

![Helm Applications](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/kpanda-insgiht-agent-check.png)

![Install Insight](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/kpanda-install-insight-agent.png)

![Install Insight](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/kpanda-install-insight-agent1.png)

## Mesh Deployment

Create a mesh using the service mesh and add the planned clusters to the corresponding mesh.

### Create a Mesh

First, go to the mesh management page and click __Create Mesh__ :

![Create Mesh](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/create-mesh1.png)

The specific parameters for creating a mesh are shown in the image:

1. Select "Hosted Mesh" as the mesh mode. In a multicloud environment, only hosted mesh mode can manage multiple clusters.
2. Enter a unique mesh name.
3. Select a pre-selected mesh version that meets the prerequisites.
4. Choose the cluster where the hosted control plane is located.
5. Load Balancer IP: This parameter is required for exposing the control plane's Istiod. It needs to be prepared in advance.
6. Container Registry: In a private cloud environment, you need to upload the required mesh images to a repository. For public clouds, it is recommended to use `release.daocloud.io/mspider` .

![Upload Images](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/create-mesh2.png)

The mesh will be in the "Creating" state, and you need to wait for the creation to complete. The status will change from "Creating" to "Running."

### Expose the Hosted Istiod of the Mesh Control Plane

#### Confirm the Hosted Mesh Control Plane Services

After ensuring that the mesh is in a normal state, check if the services under the __istio-system__ namespace in the control plane cluster __mdemo-cluster1__ have successfully bound to LoadBalancer IPs.

![Bind LB IP](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/hosted-istiod-lb-check.png)

If the service __istiod-mdemo-cluster-hosted-lb__ of the hosted mesh control plane does not have a LoadBalancer IP assigned, additional steps are required.

#### Allocate EXTERNAL IP

The method for requesting or allocating LoadBalancer IPs may differ in different environments, especially in public cloud environments. You need to create LoadBalancer IPs according to the methods provided by your public cloud provider.

In this demonstration, we use Metallb to allocate IP addresses to the corresponding LoadBalancer services. For deployment and configuration details, refer to the section on [Installing and Configuring Metallb](#metallb-installation-and-configuration).

After deploying Metallb, check the [Hosted Control Plane Services](#expose-the-hosted-istiod-of-the-mesh-control-plane) again.

#### Verify the Smoothness of the Hosted Control Plane Istiod's EXTERNAL IP

To verify the connectivity of the hosted control plane Istiod in a non-hosted cluster environment, you can use curl. If it returns a 400 error, it indicates that the network connection is successful:

```bash
hosted_istiod_ip="10.64.30.71"
curl -I "${hosted_istiod_ip}:443"
# HTTP/1.0 400 Bad Request
```

#### Confirm and Configure the Hosted Control Plane Istiod Parameters

1. Obtain the EXTERNAL IP of the hosted control plane service

    In the control plane cluster __mdemo-cluster1__ of the mesh __mdemo-mesh__ , confirm that the hosted control plane service __istiod-mdemo-mesh-hosted-lb__ has been assigned a LoadBalancer IP, and record its IP address. An example is shown below:

    ![Confirmation](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/hosted-istiod-lb-ip.png)

    Confirm that the __EXTERNAL-IP__ of the hosted control plane service __istiod-mdemo-mesh-hosted-lb__ is `10.64.30.72` .

2. Manually configure the Istiod parameters for the hosted control plane

    First, access the global control plane cluster __kpanda-global-cluster__ in the container management platform (if you're unsure about the location of the relevant cluster, you can ask the responsible person or refer to [Querying the Global Service Cluster](#querying-global-service-clusters)).

    - Search for the resource __GlobalMesh__ in the __Custom Resources__ module.
    - Find the corresponding mesh __mdemo-mesh__ in the __mspider-system__ namespace.
    - Edit the YAML file.

    - In the YAML file, add the parameter `istio.custom_params.values.global.remotePilotAddress` under the field `.spec.ownerConfig.controlPlaneParams` .
    - Set its value to the __EXTERNAL-IP__ address of __istiod-mdemo-mesh-hosted-lb__ recorded earlier: `10.64.30.72` .

    ![Add Parameter](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/get-gm-crd.png)

    ![Add Parameter](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/edit-gm-yaml.png)

    ![Add Parameter](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/edit-gm-yaml1.png)

### Add the Work Cluster

Add a cluster to the service mesh through the graphical interface.

1. After the control plane of the mesh is successfully created, select the corresponding mesh and go to the mesh management page -> __Cluster Management__ -> __Add Cluster__ :

    ![Add Cluster](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/add-cluster1.png)

2. Select the desired work cluster and wait for the installation of mesh components in the cluster to complete.

    ![Install Components](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/add-cluster2.png)

3. During the integration process, the cluster status will change from "Connecting" to "Connected":

    ![Integration Successful](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/add-cluster3.png)

#### Check if the MultiCloud Control Plane is Working Properly

Since the current work cluster has a different network than the control plane cluster pods, you need to expose the Istiod of the control plane to the public network as described in the [Expose the Hosted Istiod](#expose-the-hosted-istiod-of-the-mesh-control-plane) section above.

To verify if the Istio-related components in the work cluster are running properly, check if the __istio-ingressgateway__ in the __istio-system__ namespace of the work cluster is functioning correctly:

![Verification](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/check-work-istiod.png)

## Installation and Configuration of Mesh Components for Different Network Modes

This section is divided into two parts:

1. Configuring the "Network ID" for all work clusters
2. Installing the East-West Gateway in clusters with non-interconnected networks

Let's first address the question: Why do we need to install an East-West Gateway?
Since the Pod networks between work clusters cannot directly communicate, there can be network issues when services communicate across clusters. Istio provides a solution called the East-West Gateway. When the target service is in a different network, its traffic will be forwarded to the East-West Gateway of the target cluster, which will then route the request to the actual target service.

Now that we understand the principle of the East-West Gateway mentioned above, another question arises: How does Istio differentiate services in different networks?
Istio requires users to define the "Network ID" explicitly when installing Istio in each work cluster, which is why it is the first step.

### Manually Configure the "Network ID" for Work Clusters

Due to the differences in work cluster networks, the "Network ID" needs to be manually configured for each work cluster. If the Pod networks between clusters can directly communicate in your environment, you can configure them with the same "Network ID".

Let's begin configuring the "Network ID" following these steps:

1. First, access the global control plane cluster __kpanda-global-cluster__ (if you're unsure about the location of the relevant cluster, you can ask the responsible person or refer to [Querying the Global Service Cluster](#_30)).
2. In the __Custom Resources__ module, search for the resource __MeshCluster__ .
3. Find the work clusters that have been added to the mesh under the __mspider-system__ namespace. For this example, the work clusters are: __mdemo-cluster2__ and __mdemo-cluster3__ .
4. Take __mdemo-cluster2__ as an example and edit the YAML file.

    - Find the field `.spec.meshedParams[].params` in the YAML and add the "Network ID" field to the parameter list.
    - Notes for the parameter list:
        - Confirm that __global.meshID: mdemo-mesh__ represents the same mesh ID.
        - Confirm that the cluster role `global.clusterRole: HOSTED_WORKLOAD_CLUSTER` represents a work cluster.
    - Add the parameter `istio.custom_params.values.global.network` with the value of the Network ID from the initial [planning form](#planning-form): __network-c2__ 

    ![Edit YAML](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/add-network-id1.png)

    ![Edit YAML](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/add-network-id2.png)

    ![Edit YAML](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/add-network-id3.png)

Repeat the above steps for all work clusters ( __mdemo-cluster1__ , __mdemo-cluster2__ , __mdemo-cluster3__ ) by adding the "Network ID".

### Identify the "Network ID" for the __istio-system__ in Work Clusters

In the container management platform, go to the corresponding work cluster namespaces ( __mdemo-cluster1__ , __mdemo-cluster2__ , __mdemo-cluster3__ ) and add a label to identify the network.

- Label Key: `topology.istio.io/network` 
- Label Value: __${CLUSTER_NET}__ 

Using __mdemo-cluster3__ as an example, locate the __Namespace__ and select __istio-system__ for editing the labels.

![Identify Network ID](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/edit-istio-system-label.png)

![Identify Network ID](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/add-istio-system-networkid.png)

### Manually Install the East-West Gateway

#### Create Gateway Instance

After confirming that all Istio-related components in the work clusters are ready, you can proceed with installing the East-West Gateway.

Install the East-West Gateway in the work cluster using the IstioOperator resource. The YAML for the East-West Gateway is as follows:

!!! note

    Be sure to modify the parameters based on the "Network ID" of the current cluster.

```bash linenums="1"
# cluster1
CLUSTER_NET_ID=network-c1
CLUSTER=mdemo-cluster1
LB_IP=10.64.30.73

# cluster2
CLUSTER_NET_ID=network-c2
CLUSTER=mdemo-cluster2
LB_IP=10.6.136.29

# cluster3
CLUSTER_NET_ID=network-c3
CLUSTER=mdemo-cluster3
LB_IP=10.64.30.77

MESH_ID=mdemo-mesh
HUB=release-ci.daocloud.io/mspider
ISTIO_VERSION=1.15.3-mspider
cat <<EOF > eastwest-iop.yaml
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
              value: ${CLUSTER_NET_ID}  # 修改为当前集群的网络 ID
          service:
            loadBalancerIP: ${LB_IP}  # 修改为本集群为东西网关规划的 LB IP
            ports:
              - name: tls
                port: 15443
                targetPort: 15443
            type: LoadBalancer
        label:
          app: istio-eastwestgateway
          istio: eastwestgateway
          topology.istio.io/network: ${CLUSTER_NET_ID}  # 修改为当前集群的网络 ID
        name: istio-eastwestgateway
  profile: empty
  tag: ${ISTIO_VERSION}
  values:
    gateways:
      istio_ingressgateway:
        injectionTemplate: gateway
    global:
      network: ${CLUSTER_NET_ID}  # 修改为当前集群的网络 ID
      hub: ${HUB}  # 可选，如果无法翻墙或者私有仓库，请修改
      meshID: ${MESH_ID}  # 修改为当前集群的 网格 ID（Mesh ID）
      multiCluster:
        clusterName: ${CLUSTER}  # 修改为当前
EOF
```

The creation process is as follows:

1. Access the corresponding work cluster in the container management platform.
2. Search for __IstioOperator__ in the __Custom Resources__ module.
3. Select the __istio-system__ namespace.
4. Click __Create YAML__ .

![Create Gateway Instance](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/create-ew.png)

![Create Gateway Instance](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/create-ew2.png)

### Create East-West Gateway Resource

Create a rule in the mesh's "Gateway Rules" to create the East-West Gateway:

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
    - hosts:
        - "*.local"
      port:
        name: tls
        number: 15443
        protocol: TLS
      tls:
        mode: AUTO_PASSTHROUGH
```

### Configure Global Mesh Network Settings

After installing the East-West Gateway and configuring the gateway resolution rules, you need to declare the East-West Gateway configuration in all clusters.

1. Access the global control plane cluster __kpanda-global-cluster__ in the container management platform (if unsure, ask the responsible person or refer to [Querying the Global Service Cluster](#querying-global-service-clusters)).

2. In the __Custom Resources__ section, search for the resource __GlobalMesh__ .

3. Find the corresponding mesh __mdemo-mesh__ under the __mspider-system__ namespace.

4. Edit the YAML file.

    - Add a series of `istio.custom_params.values.global.meshNetworks` parameters in the `.spec.ownerConfig.controlPlaneParams` field in the YAML.

```yaml
# These two lines are required
# Format: istio.custom_params.values.global.meshNetworks.${CLUSTER_NET_ID}.gateways[0].address
#         istio.custom_params.values.global.meshNetworks.${CLUSTER_NET_ID}.gateways[0].port

istio.custom_params.values.global.meshNetworks.network-c1.gateways[0].address: 10.64.30.73  # cluster1
istio.custom_params.values.global.meshNetworks.network-c1.gateways[0].port: '15443'  # cluster3 East-West Gateway port
istio.custom_params.values.global.meshNetworks.network-c2.gateways[0].address: 10.6.136.29  # cluster2
istio.custom_params.values.global.meshNetworks.network-c2.gateways[0].port: '15443'  # cluster2 East-West Gateway port
istio.custom_params.values.global.meshNetworks.network-c3.gateways[0].address: 10.64.30.77  # cluster3
istio.custom_params.values.global.meshNetworks.network-c3.gateways[0].port: '15443'  # cluster3 East-West Gateway port
```

![Add Parameters](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/add-gm-meshnetowork0.png)

## Network Connectivity Demo Application and Verification

### Deploying the Demo

The main applications are __[helloworld](https://github.com/istio/istio/blob/1.16.0/samples/helloworld/helloworld.yaml)__ and __[sleep](https://github.com/istio/istio/blob/1.16.0/samples/sleep/sleep.yaml)__ (these two demos are test applications provided by Istio).

Cluster Deployment Overview:

Cluster | helloworld and Version | sleep
---|----------------|------
mdemo-cluster1 | :heart: VERSION=vc1 | :heart:
mdemo-cluster1 | :heart: VERSION=vc2 | :heart:
mdemo-cluster1 | :heart: VERSION=vc3 | :heart:

#### Deploying the Demo in the Container Management Platform

It is recommended to use the container management platform to create corresponding workloads and applications. Find the corresponding cluster in the container management platform and follow the steps below:

Using __mdemo-cluster1__ as an example, deploy __helloworld__ with __vc1__ version:

Important points for each cluster:

- Image addresses:
    - helloworld: docker.m.daocloud.io/istio/examples-helloworld-v1
    - Sleep: curlimages/curl

- Add the following **labels** to the __helloworld__ workload:
    - app: helloworld
    - version: ${VERSION}

- Add the corresponding version **environment variable** to the __helloworld__ workload:
    - SERVICE_VERSION: ${VERSION}

![Deploy Demo](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/create-demo11.png)

![Deploy Demo](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/create-demo22.png)

![Deploy Demo](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/create-demo33.png)

![Deploy Demo](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/create-demo55.png)

#### Deploying the Demo via Command Line

During the deployment process, you will need the following configuration files:

- [gen-helloworld.sh](https://github.com/istio/istio/blob/1.16.0/samples/helloworld/gen-helloworld.sh)
- [sleep.yaml](https://github.com/istio/istio/blob/1.16.0/samples/sleep/sleep.yaml)

```bash linenums="1"
# -------------------- cluster1 --------------------
kubectl create  namespace sample
kubectl label namespace sample istio-injection=enabled

# deploy helloworld vc1
bash gen-helloworld.sh --version vc1 | sed -e "s/docker.io/docker.m.daocloud.io/" | kubectl apply  -f - -n sample

# deploy sleep
kubectl apply  -f sleep.yaml -n sample

# -------------------- cluster2 --------------------
kubectl create  namespace sample
kubectl label namespace sample istio-injection=enabled

# deploy helloworld vc2
bash gen-helloworld.sh --version vc2 | sed -e "s/docker.io/docker.m.daocloud.io/" | kubectl apply  -f - -n sample

# deploy sleep
kubectl apply  -f sleep.yaml -n sample

# -------------------- cluster3 --------------------
kubectl create  namespace sample
kubectl label namespace sample istio-injection=enabled

# deploy helloworld vc3
bash gen-helloworld.sh --version vc3 | sed -e "s/docker.io/docker.m.daocloud.io/" | kubectl apply  -f - -n sample

# deploy sleep
kubectl apply  -f sleep.yaml -n sample
```

### Verifying the Demo Cluster Network

```bash linenums="1"
# Run this command on any cluster
while true; do kubectl exec -n sample -c sleep \
               "$(kubectl get pod -n sample -l app=sleep -o jsonpath='{.items[0].metadata.name}')" \
              -- curl -sS helloworld.sample:5000/hello; done

# The expected result will rotate between different versions of the three clusters, as shown below:
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

## Expansion

### Other Cluster Creation Methods

#### Creating Clusters via Container Management Platform

There are multiple ways to create clusters, and it is recommended to use the cluster creation feature in the container management platform. However, users have the flexibility to choose other methods. The alternative solutions provided in this document can be found in the [Other Cluster Creation Methods](#other-cluster-creation-methods) section of the expansion chapter.

![Create Cluster](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/kpanda-create-cluster1.png)

![Create Cluster](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/kpanda-create-cluster2.png)

![Create Cluster](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/kpanda-create-cluster3.png)

![Create Cluster](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/kpanda-create-cluster4.png)

You can select additional components that need to be expanded for your cluster, and the observability capability of the mesh relies on Insight-agent.

![Install Insight](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/kpanda-create-cluster5.png)

If your cluster requires more advanced configurations, you can add them in this step.

![Advanced Cluster Configuration](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/kpanda-create-cluster6.png)

Cluster creation may take approximately 30 minutes.

![Waiting](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/kpanda-create-cluster7.png)

#### Create cluster via kubeadm

```bash
kubeadm init --image-repository registry.aliyuncs.com/google_containers \
             --apiserver-advertise-address=10.64.30.131 \
             --service-cidr=10.111.0.0/16 \
             --pod-network-cidr=10.100.0.0/16 \
             --cri-socket /var/run/cri-dockerd.sock
```

#### Create kind cluster

```bash linenums="1"
cat <<EOF > kind-cluster1.yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
networking:
  podSubnet: "10.102.0.0/16" # Define the planned pod subnet during network planning
  serviceSubnet: "10.122.0.0/16" # Define the planned service subnet during network planning
  apiServerAddress: 10.6.136.22
nodes:
  - role: control-plane
    image: kindest/node:v1.25.3@sha256:f52781bc0d7a19fb6c405c2af83abfeb311f130707a0e219175677e366cc45d1
    extraPortMappings:
      - containerPort: 35443 # If unable to allocate LoadBalancer, use nodePort temporary solution
        hostPort: 35443 # Set the bind address on the host

EOF
cat <<EOF > kind-cluster2.yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
networking:
  podSubnet: "10.103.0.0/16" # Define the planned pod subnet during network planning
  serviceSubnet: "10.133.0.0/16" # Define the planned service subnet during network planning
  apiServerAddress: 10.6.136.22
nodes:
  - role: control-plane
    image: kindest/node:v1.25.3@sha256:f52781bc0d7a19fb6c405c2af83abfeb311f130707a0e219175677e366cc45d1
    extraPortMappings:
      - containerPort: 35443 # If unable to allocate LoadBalancer, use nodePort temporary solution
        hostPort: 35444 # Set the bind address on the host

EOF

kind create cluster --config kind-cluster1.yaml --name mdemo-kcluster1
kind create cluster --config kind-cluster2.yaml --name mdemo-kcluster2
```

### Metallb Installation and Configuration

#### Demo Cluster Metallb Network Pool Planning Record

| Cluster Name    | IP Pool                  | IP Allocation |
| --------------- | ------------------------ | ------------- |
| mdemo-cluster1  | 10.64.30.71-10.64.30.73  | -             |
| mdemo-cluster2  | 10.6.136.25-10.6.136.29  | -             |
| mdemo-cluster3  | 10.64.30.75-10.64.30.77  | -             |

#### Installation

#### Helm Installation in Container Management Platform

It is recommended to use the __Helm Apps__ -> __Helm Charts__ -> find metallb -> __Install__ option in the container management platform.

![Install metallb](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/install-metallb-from-helm.png)

![Install metallb](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/install-metallb-from-helm1.png)

##### Manual Installation

Refer to the [MetalLB official documentation](https://metallb.org/installation/).

Note: If the cluster's CNI uses calico, you need to disable calico's BGP mode, otherwise it will affect the normal operation of MetalLB.

```bash linenums="1"
# If kube-proxy uses IPVS mode, you need to enable staticARP
# see what changes would be made, returns nonzero returncode if different
kubectl get configmap kube-proxy -n kube-system -o yaml | \
sed -e "s/strictARP: false/strictARP: true/" | \
kubectl diff -f - -n kube-system

# actually apply the changes, returns nonzero returncode on errors only
kubectl get configmap kube-proxy -n kube-system -o yaml | \
sed -e "s/strictARP: false/strictARP: true/" | \
kubectl apply -f - -n kube-system

# Deploy metallb
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.7/config/manifests/metallb-native.yaml

# Check pod status
kubectl get pods -n metallb-system

# Configure metallb
cat << EOF | kubectl apply -f -
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: first-pool
  namespace: metallb-system
spec:
  addresses:
  - 10.64.30.75-10.64.30.77  # Modify according to the planning
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
  - enp1s0
  # - ens192  # Modify based on the network card name of different machines
EOF
```

#### Assigning Specific IPs to Corresponding Services

```bash
kubectl annotate service -n istio-system istiod-mdemo-mesh-hosted-lb metallb.universe.tf/address-pool='first-pool'
```

#### Verification

```bash linenums="1"
kubectl create deploy nginx --image docker.m.daocloud.io/nginx:latest --port 80 -n default
kubectl expose deployment nginx --name nginx-lb --port 8080 --target-port 80 --type LoadBalancer -n default

# Get the EXTERNAL-IP of the corresponding service
kubectl get svc -n default
# NAME         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
# kubernetes   ClusterIP      10.212.0.1       <none>        443/TCP          25h
# nginx-lb     LoadBalancer   10.212.249.64    10.6.230.71   8080:31881/TCP   10s

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

### Querying Global Service Clusters

Through the container management platform's cluster list interface, search for __Cluster Role: Global Service Cluster__ .

![Global Service Cluster](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/multicluster/images/get-kpanda-global-cluster.png)
