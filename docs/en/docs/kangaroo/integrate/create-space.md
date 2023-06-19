---
hide:
   - toc
---

# registry space

Harbor provides the image isolation feature based on the image space (project). There are two types of registry spaces: public and private:

- Public container registry: All users can access, usually store public images, there is a public registry space by default.
- Private container registry: Only authorized users can access it, usually storing the image image of the registry space itself.

Prerequisite: An external Harbor repository has been created or integrated.

1. Log in to the web console as a user with the Admin role, and click `container registry` -> `Repository Integration (Administrator)` from the left navigation bar.

     

1. Click on a repository name.

     

1. Click `registry space` in the left navigation bar, and click `Create registry space` in the upper right corner.

     

1. Fill in the registry space name, check the type and click `OK`.

     

1. Return to the list of registry spaces, prompt `registry space created successfully`.

     

1. Find the newly created registry space, click `⋮` on the right, you can perform [bind/unbind workspace](./bind-to-ws.md), delete and other operations.

     

!!! info

     - If the image space status is `public`, the images in the space can be pulled and used by all Kubernetes namespaces on the platform;
     - If the status of the image space is `private`, the image space can only be used by the Kubernetes namespace under the workspace (tenant) after the administrator Admin binds the image space to one or more workspaces (tenants).

Next step: [Bind Workspace](./bind-to-ws.md)