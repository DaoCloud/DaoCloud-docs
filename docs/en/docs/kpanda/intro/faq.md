---
hide:
  - toc
---

# FAQs

This page lists some frequently asked questions that may arise in container management, providing you convenience to perform troubleshooting.

1. Helm application installation failed with "OOMKilled" error message

    ![failure case](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kpanda/images/faq1.png)

    As shown in the figure, the container management module will automatically create and launch a Job responsible for installing the specific application. In version v0.6.0, due to unreasonable job resource settings, OOM was caused, affecting application installation. This bug has been fixed in version 0.6.1. If you upgrade to the environment of v0.6.1, it will only take effect in new created or accessed clusters. Existing clusters need to be manually adjusted to take effect.

    ??? note "Adjustment Script"

        - The following scripts are executed in the global service cluster
        - Find the corresponding cluster, take skoala-dev as an example in this article, and obtain the corresponding skoala-dev-setting configmap.
        - After updating the configmap, it will take effect.

            ```shell
            kubectl get cm -n kpanda-system skoala-dev-setting -o yaml
            apiVersion: v1
            data:
            clusterSetting: '{"plugins":[{"name":1,"intelligent_detection":true},{"name":2,"enabled":true,"intelligent_detection":true},{"name":3},{"name":6,"intelligent_detection":true},{"name":7,"intelligent_detection":true},{"name":8,"intelligent_detection":true},{"name":9,"intelligent_detection":true}],"network":[{"name":4,"enabled":true,"intelligent_detection":true},{"name":5,"intelligent_detection":true},{"name":10},{"name":11}],"addon_setting":{"helm_operation_history_limit":100,"helm_repo_refresh_interval":600,"helm_operation_base_image":"release-ci.daocloud.io/kpanda/kpanda-shell:v0.0.6","helm_operation_job_template_resources":{"limits":{"cpu":"50m","memory":"120Mi"},"requests":{"cpu":"50m","memory":"120Mi"}}},"clusterlcm_setting":{"enable_deletion_protection":true},"etcd_backup_restore_setting":{"base_image":"release.daocloud.io/kpanda/etcdbrctl:v0.22.0"}}'
            kind: ConfigMap
                metadata:
                labels:
                    kpanda.io/cluster-plugins: ""
                name: skoala-dev-setting
                namespace: kpanda-system
                ownerReferences:
                - apiVersion: cluster.kpanda.io/v1alpha1
                    blockOwnerDeletion: true
                    controller: true
                    kind: Cluster
                    name: skoala-dev
                    uid: f916e461-8b6d-47e4-906e-5e807bfe63d4
                uid: 8a25dfa9-ef32-46b4-bc36-b37b775a9632

                Modify `clusterSetting-> helm_operation_job_template_resources` to the appropriate value, and the value corresponding to version v0.6.1 is `cpu: 100m,memory: 400Mi`.
                ```

1. Permission issues between container management module and global management module

    Users often ask why they can see or not see a specific cluster. How do we troubleshoot related permission issues? There are three situations:

    - The permissions of the container management module are divided into cluster permissions and namespace permissions. If a user is bound, the user can view the corresponding clusters and resources. For specific permission descriptions, refer to [Cluster Permission Description](../user-guide/permissions/permission-brief.md).


    - Authorization of users in the global management module: Use the admin account to enter __Global Management__ -> __User and Access Control__ -> __Users__ menu, find the corresponding user. In the __Authorized User Groups__ tab, if there are roles such as Admin, Kpanda Owner, etc. that have container management permissions, even if the cluster permission or namespace permission is not bound in the container management module, the user can see all clusters. Refer to [User Authorization Document](../../ghippo/user-guide/access-control/user.md).

    - Workspace binding in the global management module: Use an account to enter __Global Management__ -> __Workspace and Folder__ , and you can see your authorized workspace. Click the workspace name.

        1. If the workspace is separately authorized to oneself, the user can see their account on the authorization tab. Then check the resource group or shared resource tab. If the resource group is bound with the namespace or the shared resource is bound with the cluster, the user can see the corresponding cluster.

        1. If granted relevant roles related to global management, the user cannot view their own account on the authorization tab, and also cannot see the cluster resources bound to the workspace in the container management module.

1. When installing Helm applications, kpanda-shell image cannot be pulled

    After offline installation, it is common to encounter the failure of pulling the kpanda-shell image when installing Helm applications on the connected cluster, as shown in the figure:

    ![pulling image failed](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kpanda/images/faq301.png)

    At this time, just go to the cluster management-cluster settings page, advanced configuration tab, and modify the Helm operation base image to a kpanda-shell image that can be pulled normally by the cluster.

1. The latest chart uploaded to the corresponding Helm Repo is not displayed in the Helm Chart interface, as shown in the figure:

    At this time, just go to the Helm repository and refresh the corresponding Helm repository.

1. When the installation of Helm applications fails and cannot be deleted and reinstalled, as shown in the figure:

    At this time, just go to the Custom Resource Definition (CRD) page, find the helmreleases.helm.kpanda.io CRD, and then find and delete the corresponding helmreleases CR.

1. After deleting node affinity and other scheduling policies of workloads, the scheduling is abnormal, as shown in the figure:

    At this time, it may be because the policy was not completely removed. Click Edit and remove all policies.

1. What is the logic of Kcoral detecting the status of Velero in the working cluster?

    - The working cluster installs the standard velero component under the velero namespace.

    - The velero deployment in the Velero control plane is running and reaches the expected number of replicas.

    - The node agent of velero data plane is running and reaches the expected number of replicas.

    - Velero successfully connects to the target MinIO (BSL status is Available).

1. When backing up and restoring across clusters, how does Kcoral obtain available clusters?

    When using Kcoral to backup and restore applications across clusters, on the recovery page, Kcoral will help users filter the list of clusters that can perform cross-cluster recovery, with the following logic:

    - Filter the list of clusters that do not have Velero installed.

    - Filter the list of clusters where Velero is in an abnormal state.

    - Get the list of clusters that are docked with the same MinIO and Bucket as the target cluster and return them.

    So as long as the same MinIO and Bucket are docked and Velero is in a running state, cross-cluster backup (requires write permission) and restoration can be performed.

1. After uninstalling VPA, HPA, CronHPA, why are the corresponding elastic scaling records still there?

    Although the corresponding components were uninstalled through Helm Addon Market, the relevant records in the application elastic scaling interface still exist, as shown in the figure:

    This is a problem with helm uninstall, which does not uninstall the corresponding CRD, resulting in residual data. At this time, we need to manually uninstall the corresponding CRD to complete the final cleanup work.

1. Why is the console of a lower version cluster opened abnormally?

    In Kubernetes clusters with versions below v1.18, opening the console will result in csr resource request failure. When opening the console, certificates are requested through csr resources in the target cluster according to the currently logged-in user. If the cluster version is too low or this feature is not enabled in the controller, certificate application will fail and it will be impossible to connect to the target cluster.

    Refer to the certificate signing request process: https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/

    Solution:

    - If the cluster version is higher than v1.18, check whether the kube-controller-manager has enabled the csr function, and ensure that the following controllers are enabled:

        ```shell
        ttl-after-finished,bootstrapsigner,csrapproving,csrcleaner,csrsigning
        ```

    - The only solution for lower version clusters is to upgrade the version.

1. How to reset a created cluster?

    Created clusters can be divided into two cases:

    - Failed to create cluster: During the creation of the cluster, due to incorrect parameter settings, the cluster creation failed. In this case, you can choose to retry the installation of the failed cluster, and then reset the parameters and recreate it.

    - Successfully created cluster: For this type of cluster, you can first uninstall the cluster, and then recreate it. Turning off the cluster protection feature is necessary to uninstall the cluster.
