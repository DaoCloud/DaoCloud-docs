# Deploy the Helm Application Based on the Helm Chart

Workbench supports building applications in four ways: [Git Repo](create-app-git.md), [Jar package](jar-java-app.md), container image, and Helm chart. This article describes how to deploy Helm applications through Helm Charts.

## prerequisites

- Need to create a workspace and a user, the user needs to join the workspace and give __workspace edit__ role.
  Refer to [Creating a workspace](../../../ghippo/user-guide/workspace/workspace.md) and [User](../../../ghippo/user-guide/access-control/user.md).

## Steps

1. After entering Workbench module, click __Wizard__ on the left navigation bar, and then select __Helm Chart__ .

    ![Based on Helm](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/helm01.png)

2. Select the cluster where the application needs to be deployed at the top of the page, and then click the Helm Chart card to be deployed, such as "docker-registry".

    !!! note

        - Click the list on the right of __Repositories__ to filter the Helm repository
        - Click the list on the right of __Type__ to filter the type of Helm Chart
        - You can also directly enter the name of the Chart in the search box on the right to quickly find the Helm application that needs to be deployed

    ![Basic Info](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/helm02.png)

3. Read the application's installation prerequisites, parameter configuration instructions and other information, select the version to be installed in the upper right corner, and click __Install__ .

    ![Install](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/helm03.png)

4. Set basic information such as application name and namespace, then configure parameters through the form or YAML below, and finally click __OK__ at the bottom of the page.

    - Ready Wait: When enabled, it will wait for all associated resources under the application to be in the ready state before marking the application installation as successful.
    - Failed to delete: If the plugin installation fails, delete the associated resources that have already been installed. After it is enabled, the ready wait will be enabled synchronously by default.
    - Detailed log: When enabled, a detailed log of the installation process will be recorded.
    - Click the __Change__ tab under __Parameter Configuration__ to view the parameter changes using the comparison view.

        ![Container Settings](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/helm04.png)

5. The page automatically jumps to the Helm application list under the overview page, and you can view the installed Helm applications under the current cluster.

    > Click the application name to jump to the container management module to view application details.

    ![Helm App](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/helm05.png)

!!! note

    If you need to update and delete the Helm application, you need to click the application name to jump to the container management module, and perform update and deletion on the application details page and more operations.

    ![Update/Delete](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/helm06.png)
