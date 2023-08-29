# Deploy the Helm application based on the Helm chart

Workbench supports building applications in four ways: [Git repository](create-app-git.md), [Jar package](jar-java-app.md), container image, and Helm chart. This article describes how to deploy Helm applications through Helm Charts.

## prerequisites

- Need to create a workspace and a user, the user needs to join the workspace and give `workspace edit` role.
  Refer to [Creating a workspace](../../../ghippo/user-guide/workspace/workspace.md), [Users and roles](../../../ghippo/user-guide/access-control/user.md).

## Steps

1. After entering Workbench module, click `Wizard` on the left navigation bar, and then select `Based on Helm chart`.

    <!--![]()screenshots-->

2. Select the cluster where the application needs to be deployed at the top of the page, and then click the Helm Chart card to be deployed, such as "docker-registry".

    !!! note

        - Click the list on the right of `Repositories` to filter the Helm repository
        - Click the list on the right of `Type` to filter the type of Helm Chart
        - You can also directly enter the name of the Chart in the search box on the right to quickly find the Helm application that needs to be deployed

    <!--![]()screenshots-->

3. Read the application's installation prerequisites, parameter configuration instructions and other information, select the version to be installed in the upper right corner, and click `Install`.

    <!--![]()screenshots-->

4. Set basic information such as application name and namespace, then configure parameters through the form or YAML below, and finally click `OK` at the bottom of the page.

    - Ready Wait: When enabled, it will wait for all associated resources under the application to be in the ready state before marking the application installation as successful.
    - Failed to delete: If the plugin installation fails, delete the associated resources that have already been installed. After it is enabled, the ready wait will be enabled synchronously by default.
    - Detailed log: When enabled, a detailed log of the installation process will be recorded.
    - Click the `Change` tab under `Parameter Configuration` to view the parameter changes using the comparison view.

        <!--![]()screenshots-->

5. The page automatically jumps to the Helm application list under the overview page, and you can view the installed Helm applications under the current cluster.

    > Click the application name to jump to the container management module to view application details.
    
    <!--![]()screenshots-->

!!! note

    If you need to update and delete the Helm application, you need to click the application name to jump to the container management module, and perform update and deletion on the application details page and more operations.

    <!--![]()screenshots-->