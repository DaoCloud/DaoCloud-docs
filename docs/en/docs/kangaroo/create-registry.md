---
hide:
  - toc
---

# Create registry space

Harbor provides the image isolation function based on the registry space (project). There are two types of registry spaces: public and private:

- Public container registry: all users can access, usually store public images, there is a library public registry space by default.
- Private container registry: Only authorized users can access it, usually storing the image of the registry space itself.

Prerequisite: An external Harbor repository has been created or integrated.

1. Log in to the web console as a user with the Admin role, and click `container registry` from the left navigation bar.

    ![container registry](images/hosted01.png)

1. Click `Managed Harbor` on the left navigation bar, click a registry name, and navigate to the `registry space` menu.

1. Click the `Create registry space` button in the upper right corner, fill in the name of the registry space, select the type and click `OK`.

    ![Create instance](images/create01.png)

!!! info

    If the status of the registry space is public, the images in the space can be pulled and used by all Kubernetes namespaces on the platform;
    If the status of the registry space is private, the registry space can only be pulled and used by the Kubernetes namespace under the workspace (tenant) after the administrator Admin binds the registry space to one or more workspaces (tenants).