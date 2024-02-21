---
hide:
  - toc
---

# FAQs

This page lists some frequently asked questions that may arise in container management, providing you convenience to perform troubleshooting.

1. Helm application installation failed with "OOMKilled" error message

    ![failure case](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kpanda/images/faq1.png)

    As shown in the figure, the container management module will automatically create and launch a Job responsible for installing the specific application. In version v0.6.0, due to unreasonable job resource settings, OOM was caused, affecting application installation. This bug has been fixed in version 0.6.1. If you upgrade to the environment of v0.6.1, it will only take effect in new created or accessed clusters. Existing clusters need to be manually adjusted to take effect.

    ??? note "Click to check how to adjust script"

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
            ```

            Modify `clusterSetting` -> `helm_operation_job_template_resources` to the appropriate value,
            and the value corresponding to version v0.6.1 is `cpu: 100m,memory: 400Mi`.

1. Permission issues between the container management module and the global management module

    Users often ask why they can see a particular cluster or why they cannot see a specific cluster.
    How can we troubleshoot related permission issues? The permissions in the container management module
    are divided into cluster permissions and namespace permissions. If a user is bound, they can view the
    corresponding cluster and resources. For specific permission details, refer to the
    [Cluster Permission Explanation](../user-guide/permissions/permission-brief.md).

    ![Container Management Permissions](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq201.png)

    In the global management module, user authorization includes using the admin account, going to __Global Management__ -> __Users and Access Control__ -> __Users__ menu, finding the corresponding user. In the __Authorize User Group__ tab, if there are roles such as Admin, Kpanda Owner, etc., that have container management permissions, even if the cluster permissions or namespace permissions are not bound in the container management, they can see all clusters. For more information, refer to [User Authorization Documentation](../../ghippo/user-guide/access-control/user.md)

    ![Global Management User Authorization](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq202.png)

    In the global management module, workspace binding involves using the account to go to __Global Management__ -> __Workspaces and Hierarchies__, where you can see your authorized workspace. Click on the workspace name.

    1. If the workspace is authorized for you individually, you can see your account in the authorization tab, then check the resource group or shared resource tab. If the resource group is bound to a namespace or the shared resource is bound to a cluster, then your account can see the corresponding cluster.

    2. If you have been granted a global management-related role, you will not see your account in the authorization tab, and you will not be able to see the cluster resources bound to the workspace in the container management module.

    ![Global Management Workspace Binding](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq203.png)

2. When installing applications with Helm, unable to pull the kpanda-shell image

    After offline installation, connected clusters often encounter failures in pulling the kpanda-shell image, as shown in the image:

    ![Image Pull Failure](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq301.png)

    In this case, simply go to the cluster management - cluster settings page, advanced configuration tab, and modify the Helm base image to a kpanda-shell image that can be successfully pulled by the cluster.

    ![Modify Image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq302.png)

1. Helm Chart interface does not display the latest Chart uploaded to the corresponding Helm Repo, as shown in the image:

    ![Template](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq401.png)

    In this case, simply refresh the corresponding Helm repository.

    ![Refresh Repository](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq402.png)

1. When an application installation with Helm fails and is stuck in installation, unable to delete the application for reinstallation, as shown in the image:

    ![Deletion Failure](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq501.png)

    In this case, simply go to the custom resources page, find the helmreleases.helm.kpanda.io CRD, and then delete the corresponding helmreleases CR.

    ![Find CR](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq502.png)

    ![Delete CR](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq503.png)

1. After removing node affinity and other scheduling strategies in Workloads, abnormal scheduling occurs, as shown in the image:

    ![Scheduling Abnormality](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq601.png)

    In this case, it may be due to the incomplete removal of the strategy. Click on edit and delete all strategies.

    ![Edit](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq602.png)

    ![Delete](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq603.png)

    ![Normal Scheduling](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq604.png)

1. What is the logic behind Kcoral checking the Velero status of a working cluster?

    ![Detection](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq701.png)

    - The working cluster has installed standard Velero components in the velero namespace.
    - The velero control plane, specifically the velero deployment, is in a running state and meets the expected replica count.
    - The velero data plane, specifically the node agent, is in a running state and meets the expected replica count.
    - Velero successfully connects to the target MinIO (BSL status is Available).

1. When performing cross-cluster backup and restore with Kcoral, how does it determine the available clusters?

    When performing cross-cluster backup and restore applications with Kcoral, in the restore page, Kcoral will help filter the list of clusters capable of performing cross-cluster restore based on the following logic:

    ![Filter](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq801.png)

    - Filtering out clusters that have not installed Velero.
    - Filtering out clusters with abnormal Velero status.
    - Obtaining a list of clusters that are connected to the same MinIO and Bucket as the target cluster and returning them.

    Therefore, as long as the clusters are connected to the same MinIO and Bucket, and Velero is in a running state, cross-cluster backup (requires write permission) and restore can be performed.

1. After uninstalling VPA, HPA, CronHPA, why do the corresponding elastic scaling records still exist?

    Even though the components were uninstalled through the Helm Addon market, the related records in the application elastic scaling interface remain, as shown in the image:

    ![Edit](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq901.png)

    This is a problem with helm uninstall, as it does not uninstall the corresponding CRD, causing residual data. In this case, we need to manually uninstall the corresponding CRD to complete the final cleanup.

1. Why does the console fail to open on clusters with lower versions?

    In Kubernetes clusters with lower versions (below v1.18), opening the console results in a CSR resource request failure. When opening the console, the current logged-in user in the target cluster requests a certificate through the CSR resource. If the cluster version is too low or this functionality is not enabled in the controller, the certificate request fails, preventing connection to the target cluster.

    Refer to the [certificate request process](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/).

    Solution:

    - If the cluster version is greater than v1.18, check if kube-controller-manager has enabled the csr feature, ensuring the following controllers are normal:

        ```shell
        ttl-after-finished,bootstrapsigner,csrapproving,csrcleaner,csrsigning
        ```

    - The only solution for lower version clusters is to upgrade the version.

1. How to reset a created cluster?

    Created clusters fall into two categories:

    - Clusters that failed to create: Clusters that failed to create due to parameter errors during the creation process can be retried by selecting retry on the failed installation and then reconfiguring the parameters for a new creation.
    - Successfully created clusters: These clusters can be uninstalled first, and then recreated. Uninstalling a cluster requires disabling cluster protection to uninstall the cluster.

    ![Disable Cluster Protection](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq1101.png)

    ![Uninstall Cluster](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/faq1102.png)

1. Failure to install plugins when connecting to a cluster

    In offline environments connected clusters, before installing plugins, you need to configure the CRI proxy repository to ignore TLS verification (needs to be executed on all nodes).

    === "Docker"

        1. Modify the file `/etc/docker/daemon.json`

        2. Add "insecure-registries": ["172.30.120.243","temp-registry.daocloud.io"], to the content after modification:

            ![Modify Configuration](../images/faq01.png)

        3. Restart docker

            ```shell
            systemctl restart docker
            systemctl daemon-reload
            ```

    === "containerd"

        1. Modify `/etc/containerd/config.toml`

        2. After modification, the content should be as follows:

            ```shell
            [plugins."io.containerd.grpc.v1.cri".registry.mirrors."docker.io"]
            endpoint = ["https://registry-1.docker.io"]
            [plugins."io.containerd.grpc.v1.cri".registry.mirrors."temp-registry.daocloud.io"]
            endpoint = ["http://temp-registry.daocloud.io"]
            [plugins."io.containerd.grpc.v1.cri".registry.configs."http://temp-registry.daocloud.io".tls]
            insecure_skip_verify = true
            ```
            
            ![Modify Configuration](../images/faq02.png)

        3. Pay attention to spaces and line breaks, ensure the configuration is correct, and after modification, execute:

            ```shell
            systemctl restart containerd
            ```

1. When creating a cluster, enabling **Kernel Tuning for New Clusters** in advanced settings causes cluster creation failure.

    1. Check if the conntrack kernel module is loaded by running the following command:

        ```shell
        lsmod |grep conntrack
        ```

    2. If it returns empty, it means it is not loaded. Reload it by running the following command:

        ```shell
        modprobe ip_conntrack
        ```

    !!! note

        Upgrading the kernel module can also cause cluster creation failures.
