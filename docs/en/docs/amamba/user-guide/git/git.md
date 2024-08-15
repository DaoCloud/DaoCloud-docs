# Manage your Git Repository

The Workbench supports the import of external repositories and provides
basic management capabilities for the imported repositories.

## Enable the Repository Navigation Menu

By default, after deploying the Workbench, the repository is hidden in the navigation bar. You can enable this feature by modifying the configuration file.

1. In __Container Management__, select the
   [global service cluster](../../../kpanda/user-guide/clusters/cluster-role.md#global-service-cluster),
   and search for `amamba-config` in the __ConfigMaps__ .

    <!-- add screenshot later -->

2. Click __Edit YAML__ and modify `featureGates` to include `Gitlab=true`.

    <!-- add screenshot later -->

3. After successfully modifying, search for `amamba-apiserver` in the deployment,
   and click __Restart__ .

    <!-- add screenshot later -->

4. Once the restart is successful, go to the __Workbench__ and
   you will see the repository navigation menu.

## Create a Branch

The Workbench has already imported a repository and bound it to the current workspace.

1. In the left navigation bar, select __Repository__ .

2. In the repository list, select a repository to enter the details page.

    <!-- add screenshot later -->

3. Under the __Branch__ tab, click __Create Branch__ .

    <!-- add screenshot later -->

4. Fill in the related arguments, branch name, and source, then click __OK__ .

    <!-- add screenshot later -->

5. The system will return to the branch list and display a success message.
   You can click the right-side __┇__ to perform more operations.

## Create a Tag

1. Under the __Tag__ tab, click __Create Tag__.

    <!-- add screenshot later -->

2. Fill in the related arguments, tag name, source, and description, then click __OK__ .

    <!-- add screenshot later -->

3. The system will automatically return to the tag list,
   and the newly created tag will appear in the list.
