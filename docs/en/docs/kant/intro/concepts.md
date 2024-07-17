---
MTPE: windsonsea
date: 2024-07-17
hide:
  - toc
---

# Concepts

- **Edge Unit**

    An Edge Unit comprises the computing resources necessary for container operations, including a cloud-based Master and edge-side working Nodes. It functions similarly to a cluster in Kubernetes (K8S) but differs in networking methods. The Master node is deployed in the cloud, with one cloud-based Master (and multiple backups) corresponding to an edge cluster.

- **Edge Node**

    An Edge Node is a fundamental component of a container cluster, which can be either a cloud host or a physical machine serving as a carrier for running containerized applications. Edge applications run on the node in the form of Pods.

- **Batch Registered Nodes**

    Batch Registered Nodes are edge nodes of the same type, pre-installed with necessary software. These nodes automatically join the platform upon booting and network connection. This one-to-many relationship with edge nodes enhances management efficiency and reduces operational and maintenance costs.

- **Edge Node Group**

    An Edge Node Group abstracts nodes based on specific attributes, creating a node group concept for uniform management and operation across different edge regions.

- **End Device**

    An End Device can range from a small sensor or controller to a large smart camera or industrial control machine. These devices can connect to edge nodes, support access via the Modbus protocol, and be managed uniformly.

- **Workload**

    A Workload (deployment) is an API object that manages application replicas, specifically Pods without local state. These Pods are independent yet identical in function, allowing for rolling updates and flexible scaling of instances.

- **Batch Deployment**

    Batch Deployment involves defining and deploying stateless workloads with identical or slightly varied configurations to a node group.

- **ConfigMap**

    A ConfigMap stores non-sensitive configuration information as key/value pairs. Pods can use this information as configuration files, environment variables, command line parameters, or data volumes.

- **Secret**

    A Secret is an object containing sensitive information such as passwords, tokens, and keys, stored as key/value pairs. It decouples sensitive information from container images, ensuring that confidential data is not included in application code.

- **Rule Endpoint**

    A Rule Endpoint is a standard endpoint for sending or receiving messages, available in three types: REST, EventBus, and ServiceBus.

- **Message Routing**

    Message Routing defines the delivery path of messages from the source message endpoint to the target message endpoint.

- **Edge Mesh**

    Edge Mesh provides a non-intrusive microservice governance solution, enabling complete lifecycle management and traffic governance. It supports various capabilities, including load balancing.
