# Integrated Registry (Workspace)

Integrated Registry (Workspace) is a convenient way to access registries for workspaces.
Workspace admin can flexibly integrate registry for their workspace members as needed.
Once integrated, members can use all public and private images under the workspace by
clicking the `Choose Image` button when deploying applications in namespaces under the
workspace, achieving quick application deployment.

- Support for associating Harbor and Docker registry instances
- For Harbor instances, in addition to accessing the administrator account,
  you can also access the robot account to achieve the same access effect

## Benefits

- Flexible and convenient: Workspace administrators can independently access one or more
  Harbor/Docker type container registrys for use by workspace members.
- Global linkage: After accessing, when deploying applications on Workbench,
  you can press the `Choose Image` button to choose the image in the registry with one click to achieve rapid application deployment.

## Steps

1. Log in to DCE 5.0 as a user with the Workspace Admin role, and click `Container Registry` -> `Integrated Registry (Workspace)` from the left navigation bar.

    ![Integrated Registry (Workspace)](../images/integrated01.png)

1. Click the `Integrated Registry` button in the upper right corner.

    ![click button](../images/inte-ws01.png)

1. After filling in the form information, click `OK`.

    ![filling](../images/inte-ws02.png)

    !!! note

        1. If the Docker Registry has not set a password, you can leave it blank,
           and the Harbor registry must fill in the username/password.
        1. For a hands-on demo, see [Integrated Registry Video Demo](../../videos/kangaroo.md)
