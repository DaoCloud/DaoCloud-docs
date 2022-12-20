# Create a CronJob with image

CronJobs (CronJob) are suitable for performing periodic operations, such as backup and report generation. These tasks can be configured to recur periodically (eg: daily/weekly/monthly); you can define the time interval at which the task will start executing.

## prerequisites

Before creating a CronJob from a image, the following prerequisites need to be met:

- The container management platform [has joined the Kubernetes cluster](../Clusters/JoinACluster.md) or [has created the Kubernetes cluster](../Clusters/CreateCluster.md), and can access the UI interface of the cluster.

- A [Namespace Creation](../Namespaces/createtens.md), [User Creation](../../../ghippo/04UserGuide/01UserandAccess/User.md) has been done, the user should have [`NS Edit`](../Permissions/PermissionBrief.md#ns-edit) or higher permission, please refer to [Namespace Authorization](../Permissions/Cluster-NSAuth.md) for details.

- When there are multiple containers in a single instance, please make sure that the ports used by the containers do not conflict, otherwise the deployment will fail.

Follow the steps below to create a CronJob.

## Image creation

1. After successfully logging in as the `NS Edit` user, click `Cluster List` in the upper left corner to enter the cluster list page. Click on a cluster name to enter `Cluster Details`.

     ![Cluster Details](../../images/deploy01.png)

2. Click `Workload` on the left navigation bar to enter the workload list, click the `CronJob` tab, and click the `Image creation` button in the upper right corner.

     ![Workload](../../images/cronjob01.png)

3. The `Create Timed Task` page will be displayed.

### Basic information configuration

Enter the deployment page and configure information according to the table below. Click 'Next' when done.

![Workload](../../images/cronjob02.png)

- Workload name: Enter the name of the new workload, which must be unique. Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter and end with a lowercase English letter or number. For example cronjob-01.
- Cluster: Select the cluster where the newly created workload resides. When a workload is created within a cluster, the workload is created in the current cluster. Clusters cannot be changed. When a workload is created outside a cluster, the workload is created on the selected cluster. For example Cluster-01.
- Namespace: Select the namespace where the newly created workload resides. For more information about namespaces, please refer to [Namespace Overview](../Namespaces/createns.md). If you do not set a namespace, the system will use the default namespace by default. For example Namespace-01.
- Number of Instances: Enter the number of Pod instances for the workload. If you do not set the number of instances, the system will create 2 Pod instances by default.
- Description: Enter the description information of the workload and customize the content. The number of characters should not exceed 512.

### Container configuration

Container configuration is only configured for a single container. To add multiple containers to a container group, click `+` on the left to add multiple containers.

After completing all the container configuration information below, click Next.

=== "Basic information (required)"

     ![Basic Information](../../images/cronjob03.png)

     After entering the information as follows, click `Confirm`.

     - Container Name: Enter a name for the newly created container. Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter and end with a lowercase English letter or number. For example backup_log.
     - Container image: The image name selected from the image registry, and also supports manual input of the image name (the name must be an existing image name in the image registry, otherwise it will not be available). If you want to connect to an external private image, you need to first [Create image registry key](../ConfigMapsandSecrets/create-secret.md), and then pull the image. For example backupjob.
     - Update policy: When the container is updated, the image pull policy. After it is enabled, the workload will pull the image again every time it is restarted/upgraded, otherwise it will only pull the image when there is no image with the same name and version on the node. Default: Always pull images.
     - Privileged container: By default, the container cannot access any device on the host. After enabling the privileged container, the container can access all devices on the host and enjoy all the permissions of the running process on the host. Enabled by default.
     - CPU Quotas: Minimum and maximum usage of container CPU resources. Requests: The minimum CPU value that the container needs to use. Limit: The maximum CPU allowed to be used by the container. It is recommended to set the upper limit of the container quota to avoid system failure caused by excessive container resources.
     - Memory quota: The minimum and maximum usage of container memory resources. Application: The minimum memory value that the container needs to use. Limit: The maximum amount of memory the container is allowed to use. It is recommended to set the upper limit of the container quota to avoid system failure caused by excessive container resources.

=== "Lifecycle (optional)"

     The container life cycle configuration is used to set the commands that need to be executed when the container starts, after starting, and before stopping. For details, please refer to [Container Lifecycle Configuration](PodConfig/lifescycle.md).

     ![Lifecycle](../../images/deploy06.png)

=== "Health Check (optional)"

     Container health checks are used to determine the health status of containers and applications. Helps improve app usability. For details, please refer to [Container Health Check Configuration](PodConfig/healthcheck.md).

     ![Health Check](../../images/deploy07.png)

=== "Environment variables (optional)"

     Container environment variable configuration is used to configure container parameters in Pods, add environment flags or pass configurations to Pods, etc. For details, please refer to [Container Environment Variable Configuration](PodConfig/EnvironmentVariables.md).

     ![environment variable](../../images/deploy08.png)

=== "Data storage (optional)"

     Container data storage configuration is used to configure container mounted data volumes and data persistence settings. For details, please refer to [Container Data Storage Configuration](PodConfig/EnvironmentVariables.md).

     ![datastore](../../images/deploy09.png)

=== "Security settings (optional)"

     Set container permissions according to the table below to protect the system and other containers from them.

     ![Security Settings](../../images/deploy10.png)

=== "Container logs (optional)"

     Set the container log collection policy and configure the log directory. Used to collect container logs for unified management and analysis. For details, please refer to [Container Log Configuration](PodConfig/EnvironmentVariables.md).
    
     ![container log](../../images/deploy11.png)

### Timing task configuration

![Cronjob configuration](../../images/cronjob04.png)

- Timing rules: Rules can be set based on hours, days, weeks, and months. The default is 2.
- Concurrency rules: Whether to allow multiple Job tasks to execute in parallel.

     - `Forbid`: When the previous task is not completed, no new task will be created. If the execution time of the new task is up but the old task is not completed, CronJob will ignore the execution of the new task.
     - `Allow`: CronJobs support new jobs, and multiple tasks can run in parallel.
     - `Replace`: It is time to create a new task, but the previous task has not been completed, and the new task will replace the previous task.
    
- Task records: You can set the number of task records for successful or failed task execution. If it is set to 0, it means not to keep. Keep the number of successful tasks: 0. Number of failed tasks retained: 0.
- Timeout period: When the task execution time exceeds this time, the task will be marked as an execution failure, and all Pods under the task will be deleted. When it is empty, it means that no timeout is set. The default is 600 ms.
- Number of retries: the number of times the task can be retried, the default value is 6.
- Restart strategy: whether to restart the task execution, the supported restart strategies are: no restart, restart when failure occurs.

### Advanced configuration

In addition to basic information configuration, DCE also provides a wealth of advanced configurations, which can configure functions such as upgrade policies, scheduling policies, labels and annotations.

### Labels and annotations

You can click the `Add` button to add labels and annotations to the workload instance Pod.

![Cronjob configuration](../../images/cronjob05.png)

## Complete creation

After confirming that all parameters have been entered, click the `Create` button to complete the workload creation. Wait for the workload status to change to `Running`.
If the workload status is abnormal, please refer to [Workload Status](../Workloads/PodConfig/workload-status.md) for specific exception information.