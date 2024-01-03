# Create a canary release task

Based on the open source project [Argo Rollout](https://argoproj.github.io/argo-rollouts/), Workbench provides powerful grayscale publishing capabilities. Grayscale release can release new application versions without affecting the old version. According to the pre-defined rules, the traffic is gradually switched to the new version. When the new version runs without problems, all traffic will be automatically migrated from the old version to the new version.

## prerequisites

1. Create a [workspace](../../../ghippo/user-guide/workspace/workspace.md) and a [user](../../../ghippo/user-guide/access-control/user.md), the user needs to join the workspace and have the __Workspace Editor__ role.

- Create an application and enable __Grayscale Release__ , refer to [Build microservice application based on Git repository](../wizard/create-app-git.md), [Deploy Java application based on Jar package](../wizard/jar-java-app.md).

- Istiod and Argo Rollout have been installed on the cluster where the object is published. For specific installation methods, refer to [Managing Helm Apps](../../../kpanda/user-guide/helm/helm-app.md).


## Steps

1. Enter the __Workbench__ module, click __Gray Release__ in the left navigation bar, and then click __Create Release Task__->__Canary Release__ in the upper right corner of the page.

    <!--![]()screenshots-->

2. Fill in the basic information with reference to the following requirements, and then click __Next__ .

    - Name: Fill in the name of the publishing task. Maximum 63 characters, can only contain lowercase letters, numbers, and a separator ("-"), and must start and end with a lowercase letter or number
    - Cluster: Select the cluster where the published object resides. You need to make sure that the cluster has Istio and Argo Rollout deployed.
    - Namespace: Select the namespace where the object to be published is located, and the application that has enabled "Grayscale Publishing" has been deployed in this namespace.
    - Stateless payload: select specific publishing objects.

        <!--![]()screenshots-->

3. Refer to the following instructions to configure publishing rules.
    - Number of instances: the number of copies applied when performing grayscale publishing tasks.
    - Traffic scheduling strategy:

        - Release traffic ratio in the current stage: the traffic ratio for the grayscale version in each traffic cycle.
        - Waiting time after reaching the flow rate: increase the flow period for the grayscale version, that is, how long to wait before automatically entering the next grayscale flow rate.

            > If set to 0 or not filled in, the publishing task will be permanently suspended when it reaches this step.

    - Monitoring and analysis: Once enabled, you can use the capabilities of Prometheus for monitoring. Automatically perform monitoring analysis throughout the release process based on pre-defined monitoring metrics and collection intervals. If the defined rules are not met, it will automatically roll back to the old version, and grayscale publishing will fail.

        <!--![]()screenshots-->

4. Click __Create and update application__ at the bottom of the page, then set the mirror address of the grayscale version in the pop-up box and click __OK__ .

    At this point, the number of copies of the original workload will be set to 0.

    <!--![]()screenshots-->

5. The system automatically jumps to the task list page of the grayscale release, prompting __updated version successful__ .

    <!--![]()screenshots-->