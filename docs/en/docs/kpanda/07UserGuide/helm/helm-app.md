# Manage Helm applications

The container management module supports interface-based management of Helm, including creating Helm instances using Helm templates, customizing Helm instance parameters, and managing the full lifecycle of Helm instances.

This section will take [cert-manager](https://cert-manager.io/docs/) as an example to introduce how to create and manage Helm applications through the container management interface.

## Prerequisites

- The container management platform [has joined the Kubernetes cluster](../Clusters/JoinACluster.md) or [has created the Kubernetes cluster](../Clusters/CreateCluster.md), and can access the UI interface of the cluster.

- Completed a [Namespace Creation](../Namespaces/createtens.md), [User Creation](../../../ghippo/04UserGuide/01UserandAccess/User.md), and created a Grant [`NS Admin`](../Permissions/PermissionBrief.md#ns-admin) or higher permissions, please refer to [Namespace Authorization](../Permissions/Cluster-NSAuth.md) for details.

## Install the Helm application

Follow the steps below to install the Helm application.

1. Click on a cluster name to enter `Cluster Details`.

    ![helm](../../images/crd01.png)

2. In the left navigation bar, click `Helm Application` -> `Helm Template` to enter the Helm template page.

    On the Helm template page, select the [Helm repository](helm-repo.md) named `addon`, and all the Helm chart templates under the `addon` repository will be displayed on the interface.
    Click on the Chart named `cert-manager`.

    ![helm](../../images/helm01.png)

3. On the installation page, you can see the relevant detailed information of the Chart, select the version to be installed in the upper right corner of the interface, and click the `Install` button. Here select v1.9.1 version for installation.

    ![helm](../../images/helm02.png)

4. Configure `Name`, `Namespace` and `Version Information`. You can also customize parameters by modifying YAML in the **Parameter Configuration** area below. Click `OK`.

    ![helm](../../images/helm03.png)

5. The system will automatically return to the list of Helm applications, and the status of the newly created Helm application is `Installing`, and the status will change to `Running` after a period of time.

    ![helm](../../images/helm04.png)

## Update the Helm application

After we have completed the installation of a Helm application through the interface, we can perform an update operation on the Helm application. Note: Update operations using the UI are only supported for Helm apps installed via the UI.

Follow the steps below to update the Helm application.

1. Click on a cluster name to enter `Cluster Details`.

    ![helm](../../images/crd01.png)

2. On the left navigation bar, click `Helm Application` to enter the Helm application list page.

    On the Helm application list page, select the Helm application that needs to be updated, click the `...` operation button on the right side of the list, and select the `Update` operation in the drop-down selection.

    ![helm](../../images/helm08.png)

3. After clicking the `Update` button, the system will jump to the update interface, where you can update the Helm application as needed. Here we take updating the http port of the `dao-2048` application as an example.

    ![helm](../../images/helm09.png)

4. After modifying the corresponding parameters. You can click the `Change` button under the parameter configuration to compare the files before and after the modification. After confirming that there is no error, click the `OK` button at the bottom to complete the update of the Helm application.

    ![helm](../../images/helm10.png)

5. The system will automatically return to the Helm application list, and a pop-up window in the upper right corner will prompt `update successful`.

    ![helm](../../images/helm11.png)

## View Helm operation records

Every installation, update, and deletion of Helm applications has detailed operation records and logs for viewing.

1. In the left navigation bar, click `Cluster Operations` -> `Recent Operations`, and then select the `Helm Operations` tab at the top of the page. Each record corresponds to an install/update/delete operation.

    ![helm](../../images/helm05.png)

2. To view the detailed log of each operation: Click `⋮` on the right side of the list, and select `Log` from the pop-up menu.

    ![helm](../../images/helm06.png)

3. At this point, the detailed operation log will be displayed in the form of console at the bottom of the page.

    ![helm](../../images/helm07.png)

## Delete the Helm application

Follow the steps below to delete the Helm application.

1. Find the cluster where the Helm application to be deleted resides, click the cluster name, and enter `Cluster Details`.

    ![helm](../../images/crd01.png)

2. In the left navigation bar, click `Helm Application` to enter the Helm application list page.

    On the Helm application list page, select the Helm application you want to delete, click the `...` operation button on the right side of the list, and select `Delete` from the drop-down selection.

    ![helm](../../images/helm12.png)

3. Enter the name of the Helm application in the pop-up window to confirm, and then click the `Delete` button.

    ![helm](../../images/helm13.png)