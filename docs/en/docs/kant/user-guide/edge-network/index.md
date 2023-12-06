# Application Mesh Overview

In edge computing scenarios, the cloud manages a large number of distributed edge nodes.
However, these edge nodes are often located in poor network environments with weak connectivity
and network fluctuations. The network topology is complex, and edge nodes in different regions
often have no network connectivity. To address the communication issues between edge services
in edge scenarios, cloud-edge collaboration provides the capability of application mesh, which
supports service discovery and traffic proxying, enabling closed-loop communication for edge services.

The following concepts are involved in application mesh:

Service: A service defines the instances of workloads and the access methods to these instances.
By using service names instead of IP addresses, applications on different nodes can communicate with each other.

As shown in the diagram below, application instances on edge nodes can communicate with each other by accessing the corresponding services.

Application mesh capabilities rely on EdgeMesh. Before using the mesh capabilities, users need to
deploy EdgeMesh. Refer to the deployment process in [Deploying EdgeMesh](./deploy-edgemesh.md).
