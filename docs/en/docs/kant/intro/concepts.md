# Basic Concepts

- Edge Unit

    Refers to the collection of computing resources required for container operation, including the cloud-based Master and edge-side working Node.
    The Edge Unit is the same concept as the cluster in K8S, but the networking method is different. The Master node is deployed on the cloud, and one cloud-based Master (with multiple backups) corresponds to an edge cluster.

- Edge Node

    It is the basic element of a container cluster, which can be a cloud host or a physical machine used as a carrier for running containerized applications. The edge application will run on the node in the form of a Pod.

- Batch Registered Nodes

    The same type of edge nodes can be pre-installed with software and automatically added to the platform after the nodes are booted and connected to the network.
    Batch registered nodes have a one-to-many relationship with edge nodes, improving management efficiency and saving operation and maintenance costs.

- Edge Node Group

    It abstracts nodes according to specific attributes into a node group concept to uniformly manage and operate nodes in different edge regions by node group dimensions.

- End Device

    An end device can be as small as a sensor or controller, or as large as a smart camera or industrial control machine. End device can be connected to edge nodes, support access through Modbus protocol, and be managed uniformly.

- Workload

    It is an API object that manages application replicas. Specifically, it is a Pod without local state. These Pods are completely independent and have the same function. They can be updated in a rolling manner, and the number of instances can be flexibly expanded or reduced.

- Batch Deployment

    Defining and deploying stateless workloads with the same configuration or small differences to a node group is a task or batch deployment action.

- ConfigMap

    It is non-sensitive configuration information saved in the form of key/value pairs. Pods can use it as configuration files in environment variables, command line parameters, or data volumes.

- Secret

    It is an object that contains a small amount of sensitive information such as passwords, tokens, and keys saved in the form of key/value pairs. Decouple sensitive information from container images, and do not include confidential data in application code.

- Message Endpoint

    The sender or receiver of messages, which can be end device, cloud services, etc.

- Message Routing

    The path of message forwarding.
