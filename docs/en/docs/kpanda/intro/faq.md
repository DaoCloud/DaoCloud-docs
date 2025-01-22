---
MTPE: windsonsea
Date: 2024-10-25
---

# Common Issues in Container Management <a id="top" />

This page lists some common issues that may be encountered in container management (Kpanda) and provides convenient troubleshooting solutions.

- [Permission issues in container management and global management modules](#permissions)
- Helm installation:
    - [Helm application installation failed with "OOMKilled" message](#oomkilled)
    - [Unable to pull kpanda-shell image during Helm application installation](#kpanda-shell)
    - [Helm chart interface does not display the most recently uploaded chart to Helm repo](#no-chart)
    - [Stuck in installing state and unable to remove application for reinstallation after Helm installation failure](#cannot-remove-app)
- [Scheduling exception after removing node affinity and other scheduling policies](#scheduling-exception)
- Application backup:
    - [What is the logic behind Kcoral's detection of Velero status in the working cluster?](#kcoral-logic-for-velero)
    - [How does Kcoral obtain available clusters during cross-cluster backup and restore?](#kcoral-get-cluster)
    - [Kcoral backed up pods and deployments with the same label, but two pods appear after restore](#2pod-with-same-label)
- [Why do scaling records still exist after uninstalling VPA, HPA, and CronHPA?](#autoscaling-log)
- [Why does the console open abnormally in low-version clusters?](#console-error)
- Creating and integrating clusters:
    - [How to reset a created cluster](#reset-cluster)
    - [Failed to install plugins when integrating cluster](#failed-plugin)
    - [Why does cluster creation fail when enabling **kernel tuning for newly created clusters** in advanced settings?](#conntrack)
    - [`kpanda-system` namespace remains in terminating state after cluster disconnection](#ns-terminating)

## Permission Issues <a id="permissions" />

Regarding permission issues in the container management and global management modules, users often ask why they can see a certain cluster or why they cannot see a cluster. Here are three cases to investigate related permission issues:

- Permissions in the container management module are divided into cluster permissions and namespace permissions. If a user is bound, they can view the corresponding clusters and resources. For specific permission details, refer to [Cluster Permission Description](../user-guide/permissions/permission-brief.md).

    ![Container Management Permissions](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq201.png)

- User authorization in the global management module: Use the admin account to visit __Global Management__ -> __User and Access Control__ -> __Users__, and find the corresponding user. In the __Authorized User Groups__ tab, if there are roles like Admin, Kpanda Owner, etc., that have container management permissions, then even if there are no cluster or namespace permissions bound in container management, the user can still see all clusters. Refer to the [User Authorization Documentation](../../ghippo/user-guide/access-control/user.md).

    ![Global Management User Authorization](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq202.png)

- Workspace binding in the global management module: Log in to __Global Management__ -> __Workspaces and Hierarchies__ to see your authorized workspaces. Click on the workspace name.

    1. If the workspace is authorized only to you, you can see your account in the authorization tab and then check the resource group or shared resource tabs. If the resource group is bound to a namespace or shared resources are bound to a cluster, your account will be able to see the corresponding cluster.

    2. If you are granted a global management-related role, you will not see your account in the authorization tab, nor will you see the cluster resources bound to the workspace in the container management module.

    ![Global Management Workspace Binding](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq203.png)

[Back to Top :arrow_up:](#top)

## Issues with Helm Installation

1. Helm installation failed with "OOMKilled" message <a id="oomkilled" />

    ![Failure Situation](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kpanda/images/faq1.png)

    As shown, the container management automatically creates a Job responsible for the application installation. In version v0.6.0, due to improper job resource settings, OOM issues affected the application installation. This bug has been fixed in version 0.6.1. If you upgrade to v0.6.1, it will only take effect in newly created or integrated clusters; existing clusters need to be manually adjusted to take effect.

    ??? note "Click to View How to Adjust the Script"

        - The following scripts are executed in the global service cluster.
        - Find the corresponding cluster; this article uses skoala-dev as an example to obtain the corresponding skoala-dev-setting configmap.
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
            ```

            Modify the clusterSetting -> helm_operation_job_template_resources to appropriate values. The values corresponding to v0.6.1 are cpu: 100m, memory: 400Mi.

    [Back to Top :arrow_up:](#top)

2. Unable to pull kpanda-shell image during Helm installation <a id="kpanda-shell" />

    When integrating an offline environment, clusters often encounter failures to pull the kpanda-shell image when installing Helm applications, as shown:

    ![Image Pull Failure](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq301.png)

    At this time, simply go to the cluster operation and maintenance - cluster settings page, in the advanced configuration tab, and modify the Helm operation base image to a kpanda-shell image that can be pulled normally by the cluster.

    ![Modify Image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq302.png)

    [Back to Top :arrow_up:](#top)

3. Helm chart UI does not display the most recently uploaded chart to Helm repo <a id="no-chart" />

    ![Template](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq401.png)

    At this time, simply refresh the corresponding Helm repository in the Helm repository.

    ![Refresh Repository](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq402.png)

    [Back to Top :arrow_up:](#top)

4. Stuck in installing state and unable to remove application for reinstallation after Helm installation failure <a id="cannot-remove-app" />

    ![Deletion Failure](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq501.png)

    At this time, simply go to the custom resource page, find the helmreleases.helm.kpanda.io CRD, and delete the corresponding helmreleases CR.

    ![Find CR](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq502.png)

    ![Delete CR](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq503.png)

    [Back to Top :arrow_up:](#top)

## Scheduling Issues <a id="scheduling-exception" />

After removing node affinity and other scheduling policies through **Workload**, scheduling exceptions occur.

![Scheduling Exception](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq601.png)

At this time, it may be because the policies were not deleted cleanly. Click edit and delete all policies.

![Edit](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq602.png)

![Delete](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq603.png)

![Normal Scheduling](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq604.png)

[Back to Top :arrow_up:](#top)

## Application Backup Issues

Kcoral is the development code for application backup.

1. What is the logic behind Kcoral's detection of Velero status in the working cluster? <a id="kcoral-logic-for-velero" />

    ![Detection](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq701.png)

    - The working cluster has the standard Velero components installed under the velero namespace.
    - The velero control plane deployment is running and has reached the desired replica count.
    - The velero data plane node agent is running and has reached the desired replica count.
    - Velero has successfully connected to the target MinIO (BSL status is Available).

2. How does Kcoral obtain available clusters during cross-cluster backup and restore? <a id="kcoral-get-cluster" />

    When Kcoral performs cross-cluster backup and restore of applications, it helps users filter the list of clusters that can perform cross-cluster restores on the restore page. The logic is as follows:

    ![Filtering](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq801.png)

    - Filters out clusters that have not installed Velero.
    - Filters out clusters with abnormal Velero status.
    - Retrieves and returns the list of clusters that connect to the same MinIO and Bucket as the target cluster.

    Therefore, as long as they connect to the same MinIO and Bucket, and Velero is running, cross-cluster backups (with write permissions) and restores can be performed.

3. Kcoral backed up pods and deployments with the same label, but two pods appear after restore. <a id="2pod-with-same-label" />

    The reason for this phenomenon is that during restoration, the Pod labels were modified, causing their labels to not match the parent resource ReplicaSet / Deployment labels at the time of backup, resulting in two times the number of Pods upon restoration.

    To avoid this situation, try to avoid modifying the labels of any resources in the associated resources.

    [Back to Top :arrow_up:](#top)

## Log Issues <a id="autoscaling-log" />

Why do scaling records still exist after uninstalling VPA, HPA, and CronHPA?

Although the corresponding components were uninstalled through the Helm Addon market, the records related to application scaling still remain, as shown in the figure:

![Edit](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq901.png)

This is an issue with helm uninstall, as it does not uninstall the corresponding CRD, leading to data residue. At this point, we need to manually uninstall the corresponding CRD to complete the final cleanup.

## Console Issues <a id="console-error" />

Why does the console open abnormally in low-version clusters?

In Kubernetes clusters with low versions (below v1.18), opening the console may result in CSR resource request failures. When opening the console, a certificate request is made through the CSR resource by the currently logged-in user in the target cluster. If the cluster version is too low or this feature's controller is not enabled, it will lead to certificate request failures, thus preventing connection to the target cluster.

For the certificate request process, refer to [kubernetes website](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/).

**Solution:**

- If the cluster version is above v1.18, check if the kube-controller-manager has the CSR feature enabled, and ensure the following controllers are functioning properly:

    ```shell
    ttl-after-finished,bootstrapsigner,csrapproving,csrcleaner,csrsigning
    ```

- For low-version clusters, the only solution is to upgrade the version.

    [Back to Top :arrow_up:](#top)

## Issues with Creating and Integrating Clusters

1. How to reset a created cluster? <a id="reset-cluster" />

    There are two situations for created clusters:

    - Failed cluster creation: If the cluster creation fails due to incorrect parameter settings during the creation process, you can select to retry in the failed cluster and reset the parameters to recreate it.
    - Successfully created cluster: This cluster can be uninstalled first and then recreated. To uninstall the cluster, you need to disable cluster protection.

    ![Disable Cluster Protection](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq1101.png)

    ![Uninstall Cluster](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq1102.png)

    [Back to Top :arrow_up:](#top)

2. Failed to install plugins when integrating cluster <a id="failed-plugin" />

    For clusters integrated in an offline environment, you need to configure the CRI proxy repository to ignore TLS verification before installing plugins (this needs to be executed on all nodes).

    === "Docker"

        1. Modify the file `/etc/docker/daemon.json`

        2. Add "insecure-registries": ["172.30.120.243","temp-registry.daocloud.io"],

            The content after modification should be as follows:
        
            ![Modify Configuration](../images/faq01.png)

        3. Restart Docker 

            ```shell
            systemctl restart docker
            systemctl daemon-reload
            ```

    === "containerd"

        1. Modify `/etc/containerd/config.toml`

        2. The content after modification should be as follows:

            ```shell
            [plugins."io.containerd.grpc.v1.cri".registry.mirrors."docker.io"]
            endpoint = ["https://registry-1.docker.io"]
            [plugins."io.containerd.grpc.v1.cri".registry.mirrors."temp-registry.daocloud.io"]
            endpoint = ["http://temp-registry.daocloud.io"]
            [plugins."io.containerd.grpc.v1.cri".registry.configs."http://temp-registry.daocloud.io".tls]
            insecure_skip_verify = true
            ```
            
            ![Modify Configuration](../images/faq02.png)

        3. Pay attention to spaces and line breaks to ensure the configuration is correct. After modification, run:

            ```shell
            systemctl restart containerd
            ```

3. Why does cluster creation fail when enabling **kernel tuning for newly created clusters** in advanced settings? <a id="conntrack" />

    1. Check if the kernel module conntrack is loaded by executing the following command:

        ```shell
        lsmod |grep conntrack
        ```

    2. If the return is empty, it indicates that it is not loaded. Reload it with the following command:

        ```shell
        modprobe ip_conntrack
        ```
        
    !!! note

        If the kernel module has been upgraded, it may also lead to cluster creation failure.

4. `kpanda-system` namespace remains in terminating state after cluster disconnection. <a id="ns-terminating" />

    Check if the APIServices status is normal. The command to check is as follows. If the current status is false, try to repair the APIServices or delete the service.

    ```shell
    kubectl get apiservices
    ```

    [Back to Top :arrow_up:](#top)
