# Multicluster network communication principle and architecture analysis

In recent years, multicluster architecture has become a "cliché". We like high availability and multi-availability zones in different places, and the multicluster architecture is born with such capabilities.
On the other hand, we also hope to reduce costs through multicluster hybrid clouds, and take advantage of the respective advantages and characteristics of different clusters, so as to use the latest technologies of different clusters and support increasingly complex cloud services in reality.
The most essential problem is that there is an upper limit to the carrying capacity in the single cluster mode, and when the cluster fails, it cannot fail over quickly.

It is for these various reasons that multicluster has almost become a new trend in cloud computing.
With the birth of the new architecture, new problems have emerged one after another, especially in multicluster use cases, where business governance, monitoring, and network communication are also facing severe challenges.
At this time, I have to mention service mesh. Theoretically speaking, this technology has the ability to solve the above problems from its design genes in multicloud and multicluster use cases.

Why is it said that service mesh can support complex multicloud cases?
The service mesh sinks its own capabilities to the infrastructure level, so in theory, in a multicloud environment, it can naturally perceive various information of its own cloud business, such as service address, link relationship between services, etc. information,
The mesh aggregates the perceived information into a complete multicloud network topology. In a known and controllable multicloud topology, users can observe and control business communications from a high latitude.

The above is only a theoretical analysis, and no amount of theoretical analysis is as good as a practical demonstration. Therefore, we will conduct an overall analysis of how our service mesh product (Mspider) supports a multicloud environment from the shallower to the deeper.

## Advantages of multicloud service mesh

First, let's go back to the original starting point, why should we choose a multicloud service mesh?
All technologies exist to solve problems, and technologies that do not have advantages and solve problems are false and meaningless.
So let's briefly introduce what advantages the service mesh in the multicloud scenario can bring us compared to the single-cluster scenario.

### Fault isolation and failover

In a single-cluster scenario, when there is a problem with business service A, we transfer the business traffic to another business instance in the same cluster.
However, if the cluster fails, multiple businesses will fail at the same time. At this time, how to transfer all the businesses of the cluster to another cluster is already very time-consuming and complicated.
But in the actual production environment, every minute and every second is very expensive.
However, in a multicloud scenario, failover at the cluster level is a basic capability, and users can quickly transfer all their business traffic.
Users only need to define failover strategies between clusters, for example, when cluster A fails, transfer business traffic to cluster B.

### Geo-awareness and failover

In a multicloud environment, the region on the cloud is defined; when the business is healthy, the communication between businesses can be based on the principle of proximity, and when a failure occurs, it can be quickly transferred to the nearest regional environment.

The importance of geographical awareness for multicloud is self-evident.
Because the real world and the actual geographical area will affect network communication, there are various factors such as time and space resources in the middle.
For example, when all the clusters in Beijing, China fail, it is definitely unreasonable to randomly transfer business to the United States, but in the actual environment, the clusters in Shanghai, China are idle there.

### Multi-dimensional team or project isolation

Although the volume of multicloud has expanded, the complexity of the team has not increased. The team can divide multicloud into different regions, different clusters, and different business projects.
When the team has multicloud capabilities, it only needs to manage its own related clusters and businesses.

### Observation capabilities in cloudy dimensions

In single-cluster mode, users can only know the business operation status in the current cluster, and the business communication between each cluster is opaque and independent. Users cannot perceive the business communication traces outside the cluster.

However, in multicloud cases, as long as they belong to the same mesh, the mesh can aggregate and analyze the communication between different clusters under the same network, and draw it into a complete multicloud network topology.
Just like the original single cluster is just a 2D photo, in the multicloud scene, the service mesh can provide a 3D topological network.
It's not just an increase in scope, but an increase in dimensional levels.

## Principles of network communication under multicloud

After understanding the huge advantages of multicloud cases, we return to reality. What problems are there in multicloud cases?
Which of these issues is the most fundamental?
First of all, let's understand this literally, multiple cloud environments? Multiple cloud vendors?
Multiple cloud clusters? The multiple here means that there are differences.
Moreover, in the multicloud world, network communication is a very hard-core issue. Can cloud vendors communicate directly?
How to communicate unimpeded between multiple clusters?

In the case of a single cluster, all workloads are on the same network (cluster internal network), but in a multicluster scenario, there may be various factors in each cluster that cause the network to be unable to communicate. Here are some common situations:

- Geographic issues lead to network isolation between the actual networks of the cluster
- When initializing the cluster, keeping the default configuration results in the same cluster subnet, so there will be IP conflicts between clusters.
   There are problems in the network communication among multiple clusters in the above situations. In order to maintain the independence of the internal network of the cluster and the network connection between the cluster networks, Istio provides two network models. Users can freely according to the cluster status and user needs. Choose a different network model.

### Single network model

As the name implies, in the case of a single network, network instances between multiple clusters can communicate directly. At this time, no mesh operation is required, and network communication between services can be direct. The architecture diagram is as follows:



The advantage of the single network model is very obvious. When users communicate, there is no need for complicated configuration and transit, so the network analysis is more intuitive, so it can also bring higher network performance.

What I have to mention at this time is that some users may ask, what should I do if I have multiple clusters and there are network conflicts among the multiple clusters, but I want to choose a single network model for the network between multiple clusters? Here are some problems that need to be solved in network transformation:

- Subnet conflict: It is necessary to solve the subnet conflict between the cluster instance network and the cluster service network
- Network isolation problem: The network between clusters may be isolated due to various factors such as region and security. Users can choose to solve the Pod IP routing across multiple clusters through tunnels or direct routing.

### Multi-network model

In the multi-network model, workload instances in different networks cannot communicate directly, so the service mesh provides a solution to allow business instances to access each other through one or more Mesh gateways, so as to solve the problem that the work instance networks cannot communicate with each other The problem.

During service communication, the mesh will perform service discovery according to the network partition. When the requested service and the target service do not belong to the same network partition, the service request will be forwarded to the east-west gateway of the target partition, and routed to the real target service through the east-west gateway.



## Choose multicloud service mesh architecture

After the above network considerations, users may be curious about the service mesh's own architecture, for example, where are the service mesh control plane components located?
How to run multicluster mode?
What advantages or disadvantages does this architecture have?
Let's analyze the architecture provided by the existing service mesh in detail. Now there are three main architectures:

- Single cluster single control plane
- Multicluster single control plane
- Multicluster and multi-control plane

### Single cluster single control plane

In the simplest case, a mesh can be run with a control plane on a single cluster.



### Multicluster single control plane

Multicluster deployments can also share control plane instances.
In this case, the shared control plane instance of the core is deployed in the core control cluster, and the communication strategy of the mesh core is controlled by **shared control plane instance**.
In the slave cluster, there is actually a slave control plane instance whose core capability is **controlling the sidecar life cycle management of the cluster**.





Think about a question, how does the sidecar from the cluster establish a connection with the shared control plane? When answering, the shared control plane needs to expose its own control plane services.

In the single network model, the shared control plane of the main cluster can be accessed through a stable IP (such as the cluster IP).

However, in the multicluster of the multi-network model, it is necessary to **expose** the shared control plane to the outside world through the Mesh gateway.

In the actual production environment, it can be flexibly selected according to the actual cloud provider or internal network planning;
Such as internal load balancers, avoid exposing the control plane to the public network, because of its potential security risks.

In the above description, the shared control plane belongs to a certain mesh cluster. In fact, its remote shared control plane can also be deployed in a cluster outside the mesh.
In this way, the control plane and data plane of the mesh can be physically isolated, avoiding problems on the control plane and data plane of the main cluster at the same time, and can disperse risks.



### Multicluster multi-control plane

For high availability, you can deploy multiple control plane instances across multiple clusters, zones, or regions.

In a multicluster scenario with multiple shared control planes, each control plane belongs to a certain cluster,
The shared control plane accepts user-defined configuration (such as __Service__ , __ServiceEntry__ , __DestinationRule__ , etc.) from the Kubernetes API Server of its own cluster.
So each master control plane cluster has an independent source of configuration.

So there is a problem here, how to configure multiple control plane clusters synchronously?
This is a complex problem that requires additional synchronization operations.
In a large-scale production environment, it may be necessary to cooperate with CI/CD tools to automate the process to achieve configuration synchronization.



Under this multi-control plane model, it is necessary to pay a great price in terms of deployment difficulty and configuration complexity.
But it can also reap higher returns. Its core advantages lie in:

- **High Availability**: If the control plane is unavailable, the scope of failure is limited to workloads in the cluster managed by that control plane.
- **Configuration Isolation**: You can make configuration changes in one cluster, zone or zone without affecting other clusters.
- **Rolling release of the control plane by region**: Rolling release of the mesh control plane can be carried out in different control plane areas, including the canary release of the mesh control plane, and its scope of influence is only the area where the control plane is located area.

## Service discovery in multicloud environment

After understanding the service mesh control plane architecture, we have to mention the communication and operation principles of the service mesh data plane.
Understanding these principles can improve our ability to solve problems encountered in the actual operation of the service mesh. Among them, the core technology in the service mesh data plane communication is the service discovery capability.

In single-cluster mode, the service mesh control plane will obtain all services registered in the cluster from the cluster registry, and then aggregate the service information obtained by the cluster registry into a list of service endpoints, which will be provided to each sidecar.

The service discovery capability in a multicluster scenario is more complicated because there is registration center isolation between clusters. The solution adopted by the mesh to run multicluster is that the service mesh control plane will observe and record the service of the registration center in each cluster ,
Then aggregate the **same-named services** under the **same namespace** in the cluster, and finally sort out a complete list of **mesh service endpoints**, and then send it to the sidecar in the mesh. Therefore, the service can have the ability to discover other cluster service endpoints.

Therefore, in order to be able to access the multicluster registration center of its control plane, the mesh control plane needs to authorize the remote key from the cluster to the control plane cluster it belongs to during the deployment phase.
After authorization, the control plane can perform service discovery for multiple clusters, so it has subsequent cross-cluster load balancing capabilities.



Under the multicluster mesh deployment model, the default strategy for multicluster services is: each cluster balances the load.
But in a complex and huge production environment, in fact, many services only need to communicate with traffic in certain areas. At this time, the local priority load balancing strategy can be adopted (for specific methods, refer to [Locality Load Balancing mentioned by Istio official](https ://istio.io/latest/docs/tasks/traffic-management/locality-load-balancing/)).

In some cases, we will find that the cross-cluster traffic load capacity is not frequently operated, and the cross-cluster load all the time is not what we expected.
For example, we just need blue-green deployment, and its versions are located in different clusters;
For example, when a service of a certain cluster fails, it can be switched to the service of the standby cluster.
These scenes are incidental. The frequency of occurrence is very low, but it is just needed.

How can we achieve this through the mesh? Under the Istio service mesh, there are two ways:

1. We don’t need to exchange the __API Server__ remote key of the cluster, so that the cluster can only perform service discovery within its own cluster.
   If you need to load cross-cluster traffic, you can use __ServiceEntry__ to cooperate with an external loader.

     

2. Disable the traffic load between multiple clusters by configuring the __VirtualService__ and __DestinationRule__ policies.

## Service Mesh Technical Solution

In the above chapters, we briefly focus on the three core dimensions of the service mesh (networkmodel, control plane architecture, and data plane service discovery) to analyze its related principles and advantages.
But at this time, we will find that there are multiple solutions in the introduction of the network model and control plane architecture, so how do we choose the specific solution?

DaoCloud has been deeply involved in service mesh products for many years, has actual landing customers, and has experience in evolving from single cluster to multicluster customer solutions. Our products have also undergone verification and practice of various solutions, collecting use cases of multiple customers, Finally, the architecture selection scheme of our multicluster service mesh product is as follows: free network model + multicluster single control plane.

### Network Model

When choosing a mesh model to land, it is not either A or B.
For example, if a user needs higher performance and the cost of connecting some clusters is within the user's tolerance, the user can choose a single network mode for some cluster networks, and choose a multi-network mode for clusters that cannot connect to the cluster network.

Each model has its own unique advantages and costs, so can I have both?
The answer is yes, we all do. Therefore, we propose a concept of a universal network model, and users can choose a network model according to their own needs:

- single network
- Multiple networks
- Single network + multiple networks

Such a rich network model solution allows us to better meet user needs and solve practical problems.

### Multicluster single control plane

Up to this part, many people will ask why they choose the multicluster single control plane mode? From the above article, it seems that the capabilities provided by multicluster and multi-control planes are not richer?

Here I have to mention that there is a very painful point when implementing multicluster and multi-control planes: the cost of multi-control planes from deployment to operation to maintenance is very high.
How did we come to this conclusion? In the early stage, we internally chose multicluster and multi-control plane verification, but found some disadvantages of multi-control plane in this process:

- Complex strategies and high hidden dangers:

     - Complex configuration: Different control planes require different strategies. Although it is an independent control plane strategy from another perspective, in a multicluster scenario, the cluster is definitely one or two, and the total number of applications will also expand with the expansion of the cluster. It becomes more complicated, and it is very easy for some clusters to forget the configuration, or to change the configuration and need to configure multiple sets of the same strategy repeatedly.
     - Policy conflict: There are many sets of control plane policies, and users need to accurately grasp each policy, otherwise it is easy to cause policy conflicts.

- High cost of control plane deployment and upgrade maintenance: When there are multiple sets of control planes, we need to maintain the deployment and upgrade of multiple sets of control planes.
- Pollution of multiple control plane clusters: Since the mesh needs to aggregate multicluster namespaces and services, it pollutes the control plane cluster. Let me illustrate with an example: when cluster A has namespaces N1 and N2; cluster B has namespace N3; and both clusters A and B are control plane clusters, cluster A needs to add N3, and cluster B needs to add N1 and N2. It is very scary when the multicluster and the business in the cluster reach a certain volume.

However, most of the above problems can be avoided in the multicluster single control plane mode, especially the complex governance strategy. All strategies will be unified in one cluster, so the difficulty of configuration and management will be greatly reduced.

### Service Mesh Architecture

Let's take a look at the actual architecture of a service mesh:



In fact, the original multicluster single control plane cannot solve the problem of polluting multiple control plane clusters mentioned above, but if we look at the above architecture carefully, you will find that there is a big difference between this part of the architecture and the solutions provided by the community. The difference is that there is an additional set of service mesh components in the control plane cluster. The biggest feature of this set of components is that it provides a virtual cluster, which is connected to the mesh control plane, and the purpose is to integrate mesh resources and control Isolate the resources of the control plane cluster to avoid the generation of dirty resources. At this time, the problem of governance resources polluting the cluster can be perfectly solved, and the deletion of control plane policy resources by user misoperation can be avoided.

Summarize the advantages of the service mesh technology selection scheme:

- **Easier Management**: Centralizing the management of the entire service mesh in one control plane can help organizations manage the entire service mesh more conveniently and quickly.
- **Low-complexity configuration and better performance**: By unifying all the data of the entire service mesh in one control plane, the routing and governance policies of the service can be processed more quickly, thereby improving the overall service network mesh performance.
- **Stronger Security**: In single control plane multicluster mode, we can better control access to the entire service mesh and use stricter security policies to protect its data.
- **Support cross-cluster load and disaster recovery capability**: It can flexibly configure cross-cluster traffic load and disaster recovery strategies.
- **Unified and efficient policy configuration**: There is no need to configure complicated control plane configuration synchronization and merging issues, especially the more control planes, the larger the volume of its business services, and its synchronization and merging must be a very complicated and There is a risk.
- **Flexible control plane and data plane isolation**: The service mesh allows users to isolate the mesh control plane from the data plane cluster, and also supports the cluster to have both the control plane and the data plane in the case of limited user resources under the same cluster.
- **Flexible switching of network modes**: The default scenario of the service mesh is that multiple clusters are located on a single network, but the multi-network mode can also support deployment.
- **mesh resource isolation**: In the open source mode, the control plane cluster needs to manage the mesh policies of all clusters. At this time, the namespace of the control plane cluster will be polluted, or some mesh resources will be affected by the operation of the cluster itself (e.g. a namespace is deleted).

## Reference

Some pictures in This page are from [Istio official website](https://istio.io/latest/docs/) and [DaoCloud documentation website](https://docs.daocloud.io/).

See [Istio Deployment Models](https://istio.io/latest/docs/ops/deployment/deployment-models/).