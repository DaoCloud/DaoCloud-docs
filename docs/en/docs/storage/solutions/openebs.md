# OpenEBS storage solution

DCE 5.0 supports many third-party storage solutions. We tested OpenEBS and finally integrated it in the app store as an Addon.
The following is the research and evaluation of OpenEBS.

Instructions for installing, deploying, and uninstalling the graphical interface of the App Store Addon will be provided later.

## What is CAS

[Container Attached Storage (CAS)](../terms/cas.md) is software that includes a microservices-based storage controller orchestrated by Kubernetes.
These storage controllers can run anywhere Kubernetes can run, including on any cloud, bare metal server, or traditional shared storage system.
Crucially, the data itself is also accessible through the container rather than being stored in a shared scale-out storage system outside the platform.

![openebs-1](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/openebs-1.svg)

CAS is a trend that fits well with the trend of non-aggregated data and small autonomous teams running small, loosely coupled workloads.
Developers remain autonomous and can spin up their own CAS containers using whatever storage is available to the Kubernetes cluster.

CAS also reflects a broader solution trend: reshape specific classes of resources or create new classes of resources by building on Kubernetes and microservices and providing functionality to Kubernetes-based microservices environments.
For example, new items such as security, DNS, networking, network policy management, messaging, tracing, logging, etc. have emerged in the cloud native ecosystem.

### Advantages of CAS

#### Agile

Each storage volume in CAS has a containerized storage controller and corresponding containerized replica.
So resource maintenance and tuning around these components is really agile.
Kubernetes' rolling upgrade capability enables seamless upgrades of storage controllers and storage replicas.
Resources such as CPU and memory can be tuned using container cGroups.

#### Storage Policy Granularity

Containerizing storage software and dedicating storage controllers to each volume allows for the most granular storage policies.
Using the CAS architecture, you can configure all storage policies on a per-volume basis.
Additionally, you can monitor storage parameters for each volume and dynamically update storage policies to achieve the desired results for each workload.
Control of storage throughput, IOPS, and latency increases with increasing granularity in volume storage policies.

#### Avoid locking

Avoiding cloud vendor lock-in is a common goal for many Kubernetes users.
However, stateful applications typically still rely on cloud providers and technologies for their data, or on the underlying traditional shared storage systems, NAS or SAN.
With the CAS approach, the storage controller can migrate data in the background based on the workload, making live migration much simpler.
In other words, the granularity of control of CAS simplifies the movement of stateful workloads from one Kubernetes cluster to another in a non-disruptive manner.

#### Cloud Native

CAS containerizes storage software and uses Kubernetes Custom Resource Definitions (CRDs) to represent underlying storage resources such as disks and StorageClass.
This model enables storage to be seamlessly integrated into other cloud native tools.
Cloud native tools such as Prometheus, Grafana, Fluentd, Weavescope, Jaeger, etc. can be used to configure, monitor, and manage storage resources.

Similar to hyperconverged systems, the storage and performance of volumes in CAS are scalable.
Since each volume has its own storage controller, storage can scale as much as the node's storage capacity allows.
As the number of container applications in a given Kubernetes cluster grows, more nodes are added, increasing the overall availability of storage capacity and performance, making storage available for new application containers.
This scalability process is similar to successful hyperconverged systems such as Nutanix.

## OpenEBS principle and architecture

OpenEBS is the leading open source implementation of the Container Attached Storage (CAS) pattern.
As part of this approach, OpenEBS uses containers to dynamically configure volumes and provide data services such as high availability.
OpenEBS relies on and extends Kubernetes itself to orchestrate its volume services.

![openebs-2](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/openebs-2.svg)

OpenEBS has many components, which can be divided into the following two categories:

- OpenEBS data engine
- OpenEBS control plane

### Data Engine

Data engines are at the heart of OpenEBS and are responsible for performing reads and writes to the underlying persistent storage on behalf of the stateful workloads they serve.

The data engine is responsible for:

- Aggregate the available capacity in the block devices allocated to them, and then partition volumes for applications.
- Provides standard system or network transport interfaces (NVMe/iSCSI) to connect to local or remote volumes
- Provides volume services such as synchronous replication, compression, encryption, maintaining snapshots, accessing incremental or full snapshots of data, etc.
- Provide strong consistency while persisting data to the underlying storage device

OpenEBS follows a microservices model to implement the data engine, where functionality is further decomposed into different layers, allowing flexible exchange of layers and making the data engine ready for future changes in applications and data center technologies.

The OpenEBS data engine consists of the following layers:

![openebs-3](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/openebs-3.svg)

#### Volume Access Layer

Stateful workloads use standard POSIX-compliant mechanisms to perform read and write operations.
Depending on the type of workload, an application may prefer to perform reads and writes directly to raw block devices or using standard file systems such as XFS, Ext4.

The CSI node driver or Kubelet will take care of attaching the volume to the desired node where the pod will run, formatting it if necessary and mounting the filesystem for access by the pod.
Users can choose to set mount options and filesystem permissions at this layer, which will be performed by the CSI node driver or kubelet.

Details required for attaching volumes (using local, iSCSI, or NVMe) and mounting (Ext4, XFS, etc.) are available through the Persistent Volume Specification.

#### Volume service layer

This layer is often called the Volume Target Layer or even the Volume Controller layer because it is responsible for providing logical volumes.
Application reads and writes are performed through Volume Targets - which controls access to volumes, synchronously replicates data to other nodes in the cluster,
And helps decide which replica acts as primary and facilitates rebuilding data to an old or restarted replica.

The implementation model that the data engine uses to provide high availability is what differentiates OpenEBS from other traditional storage controllers.
Instead of using a single storage controller to perform IO on multiple volumes, OpenEBS creates a storage controller (called Target/Nexus) per volume with a specific list of nodes that will hold the volume's data.
Each node will have full data for volumes distributed using synchronous replication.

Using a single controller to synchronously replicate data to a fixed set of nodes (rather than distributing it through multiple metadata controllers), reduces the overhead of managing metadata and also reduces the blast radius associated with node failures and other nodes participating in rebuilds failed node.

The OpenEBS volume service layer exposes volumes as:

- device or directory path in case of local PV,
- iSCSI target in case of cStor and Jiva
- NVMe Target in case of Mayastor

#### Volume data layer

The OpenEBS data engine creates volume copies on top of the storage layer. Volume copies are pinned to a node and created on top of the storage layer.
A copy can be any of the following:

- subdirectory - if the storage layer used is a file system directory
- full device or partition device - if the storage tier used is a block device
- Logical volumes - if the storage layer used is a device pool from LVM or ZFS.
- If the application only requires local storage, a persistent volume will be created using one of the above directories, devices (or partitions), or logical volumes.
    The OpenEBS control plane will be used to provide one of the above replicas.

OpenEBS can add a high availability layer on top of local storage using one of its replication engines - Jiva, cStor and Mayastor.
In this case, OpenEBS uses lightweight storage defined storage controller software that can receive read/write operations via network endpoints,
Then passed to the underlying storage layer. OpenEBS then uses this replica network endpoint to maintain a synchronized replica of the volume across nodes.

OpenEBS volume copies typically go through the following states:

- Initializing, registering to its volume during initial configuration
- Healthy, when replicas can participate in read/write operations
- Offline, when the node or storage where the replica resides fails
- Rebuild, when a node or storage failure has been corrected and a replica is receiving data from other healthy replicas
- terminate, when the volume is deleted and the replica is deleted and the space is reclaimed

#### Storage layer

The storage layer forms the basic building blocks for persisting data. The storage layer consists of block devices attached to nodes (either locally via PCIe, SAS, NVMe or via remote SAN/cloud).
A storage layer can also be a subdirectory on top of a mounted filesystem.

The storage layer is outside the scope of the OpenEBS data engine and is available for Kubernetes storage fabrics using standard operating system or Linux software fabrics.

Data Engine uses storage as a device or device pool or as a file system directory.

### Control Plane

A control plane in the context of OpenEBS refers to a set of tools or components deployed in a cluster that are responsible for:

- Manage storage available on kubernetes worker nodes
- Configure and manage data engines
- Interface with CSI to manage the lifecycle of volumes
- Interface with CSI and other tools to perform operations such as snapshot, clone, resize, backup, restore, etc.
- Integrate into other tools like Prometheus/Grafana for telemetry and monitoring
- Integrate into other tools for debugging, troubleshooting or log management

The OpenEBS control plane consists of a set of microservices that are themselves managed by Kubernetes, making OpenEBS truly Kubernetes-native.
Configurations managed by the OpenEBS control plane are saved as Kubernetes custom resources. The feature of the control plane can be broken down into the following stages:

![openebs-4](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/openebs-4.svg)

#### YAML or Helm chart

Administrators can install OpenEBS components using a highly configurable Helm chart or kubectl/YAML.
OpenEBS installations are also supported through managed Kubernetes products such as OpenShift, EKS, DO, Rancher as marketplace applications or tightly integrated into Kubernetes distributions as add-ons or plugins such as MicroK8s, Kinvolk, Kubesphere.

As part of the OpenEBS installation, the control plane components of the selected data engine will be installed as cluster and/or node components using standard Kubernetes primitives such as Deployments, DaemonSets, Statefulsets, etc.
The OpenEBS installation is also responsible for loading OpenEBS custom resource definitions into Kubernetes.

The OpenEBS control plane components are all stateless, relying on the Kubernetes etcd server (a custom resource) to manage their internal configuration state and report the status of various components.

#### Declarative API

OpenEBS supports a declarative API to manage all its operations, and the API is exposed as a Kubernetes custom resource.
Kubernetes CRD validators and admission webhooks are used to validate user-supplied input and verify that operations are allowed.

The declarative API is a natural extension of what Kubernetes administrators and users are accustomed to, where they can define intents via YAML, and then Kubernetes and the associated OpenEBS operators reconcile the state with the user's intent.

A declarative API can be used to configure the data engine and set volume profiles/policies.
Even data engine upgrades are performed using this API. These APIs can be used to:

- Manage the configuration of each data engine
- How to manage storage needs to be managed or StorageClass
- Manage volumes and their services - create, snapshot, clone, backup, restore, delete
- Manage pool and volume upgrades

#### Data Engine Operator

All Data Engine operations from discovering the underlying storage to creating pools and volumes are packaged as Kubernetes Operators.
Each data engine either runs on top of a configuration provided during installation, or is controlled through a corresponding Kubernetes custom resource.

Data Engine Operators can operate cluster-wide or on specific nodes.
Cluster-wide operators are typically involved in operations that involve interacting with Kubernetes components - coordinating the scheduling or migration of pools and volumes on various nodes.
Node-level operators operate on local operations such as creating volumes, replicas, snapshots, etc. on storage or pools available on the node.Data Engine Operators are also often referred to as the control plane of a data engine, as they help manage the volumes and data services provided by the corresponding data engine.
Some data engines such as cstor, jiva, and mayastor can have multiple Operators depending on the functionality provided or required, where local volume operations can be embedded directly into the corresponding CSI controller/configurator.

#### CSI Driver (Dynamic Volume Configurator)

The CSI driver acts as a facilitator for managing the lifecycle of volumes in Kubernetes.
CSI driver operation is controlled or customized by parameters specified in StorageClass. The CSI driver consists of three layers:

- Kubernetes or Orchestrator functionality - Kubernetes native and bind applications to volumes
- Kubernetes CSI layer - translates Kubernetes native calls into CSI calls - passes user-supplied information to the CSI driver in a standard way
- Storage Drivers - These are CSI Compliant and work closely with the Kubernetes CSI layer to receive requests and process them.
- The storage driver is responsible for:

Exposes the functionality of the data engine:

- Interact directly with the data engine or data engine operator to perform volume creation and deletion operations
- Interface with the data engine to attach/detach volumes to the node where the container using the volume is running
- Interfaces with standard linux utilities to format, mount/unmount volumes to containers

#### Plug-ins

OpenEBS is focused on storage operations and provides plugins for other popular tools to perform operations outside of core storage functionality, but is essential for running OpenEBS in production.
Examples of such actions include:

- Application consistent backup and recovery (delivered through integration into Velero)
- Monitoring and Alerting (delivered via integration into Prometheus, Grafana, Alert Manager)
- Enforce security policies (provided via integration with PodSecurityPolicies or Kyerno)
- Logging (provided via integration with any standard logging stack set up by admins like ELK, Loki, Logstash, etc.)
- Visualization (available via standard Kubernetes dashboards or custom Grafana dashboards)

#### CLI command line

All administrative features on OpenEBS can be performed through kubectl, since OpenEBS uses custom resources to manage all its configuration and report the status of components.

Additionally, OpenEBS has released an alpha kubectl plugin to help provide information about pools and volumes using a single command that aggregates information obtained through multiple kubectl commands.
