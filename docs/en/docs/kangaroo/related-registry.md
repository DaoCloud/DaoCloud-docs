# Associated warehouse

The associated warehouse is a convenient warehouse access function provided for the workspace.
The workspace administrator (Workspace Admin) can flexibly access the mirror repository for the workspace as needed for use by workspace members.
After accessing, when members deploy applications in the namespace under the workspace, they can pull all public and private images under the workspace with one click through the `Select Image` button to achieve rapid application deployment.

- Support for associating Harbor and Docker warehouse instances
- For Harbor instances, in addition to accessing the administrator account, you can also access the robot account to achieve the same access effect

## Advantage

- Flexible and convenient: Workspace administrators can independently access one or more Harbor/Docker type mirror warehouses for use by workspace members.
- Global linkage: After accessing, when deploying applications on the application workbench, you can press the `Select Image` button to select the image in the warehouse with one click to achieve rapid application deployment.

## Steps

1. Log in to the web console as a user with the Workspace Admin role, and click `Mirror Warehouse` -> `Associated Warehouse` from the left navigation bar.

    ![Mirror Warehouse](images/related01.png)

1. Click the `Associate Warehouse` button in the upper right corner.

    ![Relate Warehouse](images/relate02.png)

1. After filling in the form information, click `OK`.

    ![Fill out the form](images/relate03.png)

    !!! note

        1. If the Docker Registry mirror warehouse has not set a password, you can leave it blank, and the Harbor warehouse must fill in the username/password.
        1. For a hands-on demo, see [Linked Warehouse Video Demo](../videos/kangaroo.md)