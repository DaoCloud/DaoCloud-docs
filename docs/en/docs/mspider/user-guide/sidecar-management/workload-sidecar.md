# Workload Sidecar Management

You can perform various operations on workloads regarding sidecar injection, such as enabling,
disabling, and setting resource quota.

## View Sidecar Injection Information

In the left navigation menu, click __Mesh Sidecar__ -> __Workload__ and select a cluster to
view all workloads, their related namespaces, sidecar injection statuses, and resource quota under that cluster.

![Workload Sidecar List](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/wl-sidecar01.png)

The columns are defined as follows:

| Column Name | Definition |
| ----------- | ---------- |
| Workload    | All workloads in the selected cluster (excluding system workloads that cannot have sidecars injected) |
| Status      | Three statuses:<br />Injected - The automatic sidecar injection is completed.<br />Uninjected - Automatic sidecar injection is disabled.<br />Pending Restart - The istio-injection of the corresponding namespace has changed but the related Pod has not been restarted yet. |
| Namespace   | The namespace to which this workload belongs. |
| Service     | The service(s) related to this workload, which may contain multiple items. You can click to expand the list. |
| Injected Pod/All Pods | The injection status of the workload's Pods. The format is "Number of pods with sidecars injected / Total number of injectable Pods." If the injection status of the workload is "Injected," but some Pods are Uninjected, such as 3/5, this item will be highlighted to remind you of the failed injections. |
| CPU Request/Limit | Contains two values: requested resources and limited resources. If you have not set any resource limit, this project will show as "Not Set." The format is "Request / Limit." |
| Memory Request/Limit | Contains two values: requested resources and limited resources. If you have not set any resource limit, this project will show as "Not Set." The format is "Request / Limit." |
| Operation | Injection Enable, Clear Policy, Sidecar Resource Limits, View Sidecar Status and Traffic Pass-Through Settings |

When there are many workloads, you can sort them by name and search for them using the search function.

## View Sidecar Running Status

If one workload has a sidecar injected, click the __⋮__ at the end of the row and
select __Check Sidecar Status__ from the pop-up menu.

![Sidecar Running Status](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/wl-sidecar02.png)

You can see the sidecar's current running status, resource requests, and limits.

![Sidecar Running Status](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/wl-sidecar02-01.png)

## Enable Sidecar Injection

You can enable automatic sidecar injection for one or more workloads and restart
their corresponding Pods. Please ensure that the Pods can be restarted before
performing this operation. Follow these steps:

1. Select one or more workloads that have not had sidecars injected, click __Enable Injection__ at the top right.

    ![Select Sidecar Injection](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/wl-sidecar03.png)

2. In the pop-up dialog, confirm the selected workload(s) and check the __Restart Now__ checkbox. Click __OK__ .

    ![Confirm](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/wl-sidecar04.png)

3. Return to the workload list, and you can see the __Status__ of the selected workloads
   has changed, such as from __Uninjected__ to __Injected__ . After completing the Pod restarts,
   the sidecar injection will be completed, and the relevant injection progress can be
   viewed in the __Pods Injected__ column.

!!! note

    If the namespace to which the workload belongs has executed the __Injection Enable/Disable__ 
    operation but has not restarted the workload, the workload cannot perform new sidecar-related
    operations. You need to restart it before executing the new sidecar operation.

## Disable Sidecar Injection

You can disable automatic sidecar injection for one or more workloads and restart
their corresponding Pods. Please ensure that the Pods can be restarted before performing
this operation. Follow these steps:

1. Select one or more workloads that have had sidecars injected, click __Injection Disable__ at the top right.

    ![Select Sidecar Injection](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/sc-disable01.png)

2. In the pop-up dialog, confirm the selected workload(s) and check the __Restart Now__ checkbox. Click __OK__ .

    ![Confirm](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/sc-disable02.png)

3. Return to the workload list, and you can see that the __Status__ of the selected workloads
   has changed to __Uninjected__ . After completing the Pod restarts, the sidecar injection will
   be disabled, and the relevant uninstall progress can be viewed in the __Pods Injected__ column.

    ![Successful Sidecar Injection](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/sc-disable03.png)

!!! note

    If the namespace to which the workload belongs has executed the __Injection Enable/Disable__ 
    operation but has not restarted the workload, the workload cannot perform new sidecar-related
    operations. You need to restart it before executing the new sidecar operation.

## Set Resource Quota for Sidecar

You can set CPU and memory limits for one or more workloads that have had sidecars injected. Follow these steps:

1. Select one or more workloads that have had sidecars injected, click __Sidecar Resource Quota__ at the top right.

    ![Resource quota](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/sc-disable01.png)

2. In the pop-up dialog, set the resource quota for the selected workload(s) and click __OK__ .

    ![Set rResource quota](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/wl-sidecar07.png)

3. Return to the workload list, and you can see that the resource quotas of the selected
   workloads are displayed in the __CPU Request/Limit__ and __Memory Request/Limit__ columns.

## Cleanup Policy

You can clean up the sidecar policy for one or more workloads that have had sidecars injected. Follow these steps:

1. Select one or more workloads that have had sidecars injected, click __Cleanup Policy__ at the top right.

    ![Cleanup policy](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/sc-disable01.png)

2. In the pop-up dialog, confirm the selected workload(s) and click __OK__ .

    ![Confirm Selection](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/wl-sidecar10.png)

3. Return to the workload list, and you can see that the sidecar policy of the selected workloads has been cleaned up.

## Sidecar Upgrade

In DCE 5.0 Service Mesh, a sidecar refers to an Envoy proxy used to implement traffic control
and routing rules within the service mesh. Sidecar upgrade refers to upgrading the Envoy proxy
from an older version to a newer version.

Reasons for upgrading the sidecar include:

1. Security updates: The new version may have fixed security vulnerabilities or other security issues.
   To ensure the security of the service mesh, it is necessary to upgrade the sidecar to the latest version.
2. Feature enhancement: The new version may add some new features or improve existing ones to enhance
   the performance and reliability of the service mesh.
3. Error fixing: The new version may fix some errors or bugs to increase the stability and reliability
   of the service mesh.
4. Version obsolescence: Over time, the old version of Envoy proxy may become outdated and no longer supported.
   Therefore, it is necessary to upgrade to the latest version for better support and maintenance.

However, before upgrading the sidecar, sufficient testing and verification are needed to ensure that
the upgrade process does not have any negative impact on the service mesh.

For specific operational steps, please refer to [Sidecar Upgrade](../../install/sidecar-update.md).
