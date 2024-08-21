# View Defects

This page describes how to view defects within the project of a Jira instance.

## Enable the Project Management Navigation Menu

By default, after DCE 5.0 Workbench is deployed, the feature of project management is hidden
in the navigation bar. You can enable this feature by modifying the configuration file.

1. In __Container Management__, select the
   [global service cluster](../../../kpanda/user-guide/clusters/cluster-role.md#global-service-cluster),
   and search for `amamba-config` in the __ConfigMaps__.

    <!-- add screenshot later -->

2. Click __Edit YAML__ and modify `featureGates` to include `Jira=true`.

    <!-- add screenshot later -->

3. After successfully modifying, search for `amamba-apiserver` in the deployments, and click __Restart__.

    <!-- add screenshot later -->

4. Once the restart is successful, go to the __Workbench__ and
   you will see the project management navigation menu.

## Prerequisites

- A Jira instance has been successfully integrated into the current platform.
  Refer to [Integrated Toolchain](../tools/integrated-toolchain.md).

- Projects from the integrated Jira instance have been assigned to the current workspace.
  Refer to [Manage Toolchain Instances](../tools/toolchain-instances.md).

## Steps

1. In the workbench, select a workspace and navigate to __Development Management__ -> __Defects__ page.

2. On the defects page, view the Issues under the Jira project.
   A workspace can bind to multiple projects from integrated Jira instances.

    <!-- add screenshot later -->

3. You can filter Issues by status, priority, type, creator, or assignee.

    <!-- add screenshot later -->
