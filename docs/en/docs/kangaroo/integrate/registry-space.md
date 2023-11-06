---
hide:
   - toc
---

# Registry space

Harbor provides the image isolation feature based on the registry space (project). There are two types of registry spaces: public and private:

- Public container registry: All users can access, usually store public images, there is a public registry space by default.
- Private container registry: Only authorized users can access it, usually storing the image image of the registry space itself.

Prerequisite: An external Harbor registry has been created or integrated.

1. Log in to DCE 5.0 as a user with the Admin role, and click `Container Registry` -> `Integrated Registry (Admin)` from the left navigation bar.

    ![Integrated Registry (Admin)](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/bind01.png)

1. Click a registry name.

    ![click a name](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/bind02.png)

1. Click `Registry Space` in the left navigation bar, and click `Create registry space` in the upper right corner.

    ![click button](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/reg-space01.png)

1. Fill in the registry space name, check the type and click `OK`.

    ![filling](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/reg-space02.png)

1. Return to the list of registry spaces, find the newly created registry space, click `⋮` on the right, you can perform [bind/unbind workspace](./bind-to-ws.md), delete and other operations.

    ![filling](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/reg-space03.png)

!!! info

     - If the registry space status is `public`, the images in the space can be pulled and used by all Kubernetes namespaces
       on the platform;
     - If the status of the registry space is `private`, the registry space can only be used by the Kubernetes namespace
       under the workspace (tenant) after the administrator Admin binds the registry space to one or more workspaces (tenants).

Next step: [Bind Workspace](./bind-to-ws.md)
