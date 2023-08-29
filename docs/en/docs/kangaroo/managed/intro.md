# Manage Harbor

Harbor is an open-source container registry service for safe hosting and efficient distribution of OCI-compliant Artifacts such as container images and Helm Charts.
Can help you manage Artifact consistently and securely across cloud-native computing platforms such as Kubernetes and Docker.
DCE 5.0 provides a fast deployment capability based on Harbor, and through a series of convenient channels such as connecting with Workbench and container management module in the platform, and binding with the workspace,
It realizes a one-stop high-availability, high-performance, and high-efficiency deployment, management, and use of full-cycle container registry services.

## Product Features

- Support multi-copy deployment to achieve high availability
- Support importing platform users into native Harbor instances
- Provide a native Harbor instance entry, and the user's operations on the platform UI and operations in the native Harbor will take effect in real time
- Support using the platform to build a database or access an external database
- Support using the platform to build a Redis instance or access an external Redis instance
- Support specifying internal storage or using external S3 compatible object storage

## Functional advantages

- Multiple container registry instances to meet the needs of multiple container registrys in various environments such as development, testing, and production.
- Break the calling barriers between modules, and support rapid image pull when deploying applications in Workbench and container management module
- Provides a unified management control plane, allowing administrators to manage the full life cycle of multiple Harbor instances on the same interface.

## Steps

1. [Install Harbor Operator](./operator.md)
1. [Create a managed Harbor instance](./harbor.md)
