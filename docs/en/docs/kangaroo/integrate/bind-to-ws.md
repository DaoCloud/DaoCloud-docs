# Bind/Unbind Workspace

There are two types of registry spaces: public and private. The images in a public registry space are public, 
which can be pulled by all platform users, while the images in a private registry space can only be pulled 
by members of a workspace after the image is bound to that workspace. 

- For public images, users can deploy applications by clicking __Choose Image__ button in the Container Management module,
  selecting images from all public image repositories under __Container Registry__ -> __Integrated Registry__ to deploy 
  the application without any configuration.
- For private images, however, the workspace (tenant) needs to be assigned the private registry space by an 
administrator before members under the workspace can use them, ensuring the security of private images.

**Prerequisites:** An external Harbor registry has been created or integrated, and [a registry space has been created](../integrate/registry-space.md).

## Binding Steps

Generally, for private registry spaces, binding to a workspace is helpful to allow members to use the images.

1. Log in to DCE 5.0 as a user with the Admin role, click __Container Registry__ -> __Integrated Registry (Admin)__ 
   from the left navigation bar.

    ![Integration](../images/integrated01.png)

1. Click a registry name.

    ![Click Name](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/integrated02.png)

1. Click __Registry Space__ in the left navigation bar, then click the __┇__ on the right of a specific registry space, and select __Bind/unbind workspace__ .

    ![Bind/Unbind](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/bind03.png)

    If no workspace is bound, the Workspace column will display `No binding`.

1. In the pop-up window, select one or more workspaces, and then click __OK__ .

    ![Binding](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/bind04.png)

    To unbind a workspace, simply click the __x__ in the selected workspaces list.

1. The prompt message "Bound/Unbound workspace successfully" will be displayed,
   and the Workspace column will display the bound workspace when you move the cursor over it.

    ![Binding](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/bind05.png)

    Users under this workspace (tenant) can pull images from this registry space.

## FAQs

1. When deploying an application in a Kubernetes namespace and clicking the __Choose Image__ button, 
   you are unable to Choose Images from the registry space.

    - Check whether the Kubernetes namespace is bound to a workspace (it needs to be bound).
    - Check whether the registry space is bound to the workspace where the Kubernetes namespace is located (it needs to be bound).
    - Check whether the registry space status is private or public, and switch tabs as necessary.

    ![Image registry](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/bind06.png)

2. What is the difference between assigning a registry space to a workspace for use and integrating a registry under the workspace?

    Platform administrators can centrally manage and assign a registry space to multiple workspaces
    at once without having to associate each one separately.

    Workspace administrators can integrate external image repositories for their members to use as needed,
    without relying entirely on platform administrators, making it more flexible to use.

Next step: [Deploy Applications](../../amamba/user-guide/wizard/create-app-git.md)