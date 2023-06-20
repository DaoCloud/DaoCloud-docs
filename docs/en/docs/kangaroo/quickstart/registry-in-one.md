# Managing External Container Registries

If you have one or more Harbor or Docker container registries, you can use the DCE 5.0 container registries for unified management. Depending on the role permissions of the operator, two methods can be used:

- Integrated Registry
- Integrated Registry

## Integrated Registry

If you are a Workspace Admin, you can integrate the existing container registry with the DCE platform through the integrated registry feature for use by members of the workspace. The simple operation steps are as follows:

1. Log in with the Workspace Admin role, click "Integrated Registry" from the left navigation bar, and click the "Integrated Registry" button in the upper right corner.

2. Fill in the form information, and click "OK".

    !!! note

        - If the Docker Registry container registry has not set a password, you can leave it blank, but the Harbor registry must fill in the username/password.
        - For a hands-on demo, see [Integrated Registry Video Demo](../../videos/kangaroo.md).

## Integrated Registry

If you are an Admin (platform administrator), you can also integrate the existing container registry into the DCE platform through the registry integration function. Registry integration is the entrance to the container registry of the centralized management platform. The platform administrator can assign a private registry space to one or more workspaces (namespaces under the workspace) by binding the registry space to the workspace or set the registry space as public for use by all namespaces of the platform.

The steps are as follows:

1. Log in with the Admin role, and click "Registry Integration" on the left navigation bar.

    

2. Click the "Registry Integration" button in the upper right corner.

    

3. Select the registry type, fill in the integration name, registry address, username, and password, and click "OK".

    

4. In the integrated registry list, hover the cursor over a certain registry, click the eye icon to view the overview.

    

5. The overview page displays the basic information and statistical information of the current registry and also provides a quick start at the top that is convenient for managing registry space, workspace, and creating applications.
