# Manage External Registry

If you have one or more Harbor, Docker and Jfrog Artifacty container registries, you can use the DCE 5.0 container registry for unified management. Depending on the role permissions of the operator, two methods can be used:

- Integrated Registry (Workspace): Support Harbor, Docker and Jfrog Artifacty
- Integrated Registry (Admin): Support Harbor and Docker

## Integrated Registry (Workspace)

If you are a Workspace Admin, you can use the Integrated Registry (Workspace) feature to integrate
an existing container registry with the DCE platform for use by workspace members.
The simple steps to perform this operation are as follows:

1. Log in with the Workspace Admin role, click `Integrated Registry (Workspace)` from the left navigation bar,
   and click the `Integrated Registry` button in the upper right corner.

    ![integrate registry](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/relate02.png)

2. Fill in the form information, and click `OK`.

    ![fill](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/relate03.png)

    !!! note

        - If the Docker Registry container registry has not set a password, you can leave it blank, but the Harbor registry must fill in the username/password.
        - For a hands-on demo, see [Integrated Registry Video Demo](../../videos/kangaroo.md).

## Integrated Registry (Admin)

If you are an Admin (platform administrator), you can also integrate an existing container registry
with the DCE platform using the registry integration feature.

Registry integration serves as a centralized management entry for platform container registry.
Platform administrators can bind a registry space to one or more workspaces (namespaces within workspaces)
by allocating a private registry space to them. Alternatively, they can set a registry space to be public and
accessible to all namespaces on the platform.

The steps are as follows:

1. Log in with the Admin role, and click `Integrated Registry (Admin)` on the left navigation bar.

    ![nav](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/interg01.png)

2. Click the `Integrated Registry` button in the upper right corner.

    ![button](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/interg02.png)

3. Select the registry type, fill in the integration name, registry address, username, and password, and click `OK`.

    ![fill](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/interg03.png)

4. In the integrated registry list, hover the cursor over a certain registry, click the eye icon to view the overview.

    ![view](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/interg04.png)

5. The overview page displays the basic information and statistical information of the current registry and
   also provides a quick start at the top that is convenient for managing registry space, workspace, and creating applications.

    ![overview](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/interg05.png)
