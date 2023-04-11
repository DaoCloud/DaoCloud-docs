# Associated registry

The associated registry is a convenient registry access function provided for the workspace.
The workspace administrator (Workspace Admin) can flexibly access the container registry for the workspace as needed for use by workspace members.
After accessing, when members deploy applications in the namespace under the workspace, they can pull all public and private images under the workspace with one click through the `Select Image` button to achieve rapid application deployment.

- Support for associating Harbor and Docker registry instances
- For Harbor instances, in addition to accessing the administrator account, you can also access the robot account to achieve the same access effect

## Benefits

- Flexible and convenient: Workspace administrators can independently access one or more Harbor/Docker type container registrys for use by workspace members.
- Global linkage: After accessing, when deploying applications on the application workbench, you can press the `Select Image` button to select the image in the registry with one click to achieve rapid application deployment.

## Steps

1. Log in to the web console as a user with the Workspace Admin role, and click `container registry` -> `Associated registry` from the left navigation bar.

    

1. Click the `Associate registry` button in the upper right corner.

    

1. After filling in the form information, click `OK`.

    

    !!! note

        1. If the Docker Registry container registry has not set a password, you can leave it blank, and the Harbor registry must fill in the username/password.
        1. For a hands-on demo, see [Linked registry Video Demo](../videos/kangaroo.md)
