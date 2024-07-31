# Integrated Registry (Admin)

The Integrated Registry (Admin) is the entrance for central management of platform container registries.
It supports integrating external container registries such as Harbor Registry and Docker Registry,
as well as automatically integrating managed Harbors created by the platform. After integrated registry,
platform administrators can assign a private registry space to one or more workspaces (namespaces under workspaces)
by binding the registry space to the workspace, or set the registry space as public for all namespaces on the platform to use.

## Main Features

- Supports integration with mainstream container registries such as Harbor Registry and Docker Registry, helping you centrally manage platform-level container registries.
- Supports quickly viewing data such as registry addresses, number of registry spaces and storage usage through overview page.
- Supports creating and setting the registry space status as public or private. If the registry space status is public,
  its images can be used by all namespaces on the platform. If the registry space status is private, only namespaces under
  workspaces that have been bound to the registry space can use the private images, ensuring their security.
- Automatically integrates managed Harbors, which will be automatically integrated into the integrated registry list
  after a managed Harbor instance is created, for unified management.

## Advantages

- Unified management entrance for unified management of integrated container registries and managed Harbor instances.
- High security: private images can only be pulled when deployed by binding the registry space to the workspace.
- Convenience and efficiency: Once a registry space is set as public, all namespaces within the platform can pull
  the public images under it when deploying applications.
- Supporting main types of container registries: Harbor Registry, Docker Registry.

## Operating Steps

Refer to [Video Tutorial](../../videos/kangaroo.md#_3) to familiarize yourself with the following operating steps:

1. Log in to DCE 5.0 as a user with the Admin role, click __Container Registry__ -> __Integrated Registry (Admin)__
  from the left navigation bar.

    ![Integration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/integrated01.png)

1. Click the __Integrated Registry__ button in the upper right corner.

    ![Click Button](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/integrated02.png)

1. Select the registry type, fill in the integration name, registry address, username, and password, and click __OK__.

    ![Fill Parameters](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/integrated03.png)

    !!! note

        For a Harbor registry, an Admin-level username/password must be provided.

1. Return to the integrated registry list. The integrated repositories will have labels such as
  `Integrated`, `Healthy`, or `Unhealthy`. You can perform operations such as __Unbind__ and __Edit__.

    ![More Operations](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/integrated04.png)

Next step: [Create registry space](registry-space.md)
