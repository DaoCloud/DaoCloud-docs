# Workload status

A workload is an application running on Kubernetes, and in Kubernetes, whether your application is composed of a single same component or composed of many different components, you can use a set of Pods to run it. Kubernetes provides five built-in workload resources to manage pods:

- [Stateless Workloads](../create-deployment.md)
- [Stateful Workloads](../create-statefulset.md)
- [Daemonset](../create-daemonset.md)
- [job](../create-job.md)
- [Cron job](../create-cronjob.md)

You can also expand workload resources by setting [Custom Resource CRD](../../custom-resources/create.md). In the fifth-generation container management, it supports full lifecycle management of workloads such as creation, update, capacity expansion, monitoring, logging, deletion, and version management.

## Pod Status

Pod is the smallest computing unit created and managed in Kubernetes, that is, a collection of containers. These containers share storage, networking, and management policies that control how the containers run.
Pods are typically not created directly by users, but through workload resources.
Pods follow a predefined lifecycle, starting at __Pending__ [phase](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase), if at least one of the primary containers starts normally, it enters __Running__ , and then enters the __Succeeded__ or __Failed__ stage depending on whether any container in the Pod ends in a failed state.

## Workload Status

The fifth-generation container management module designs a built-in workload life cycle state set based on factors such as Pod status and number of replicas, so that users can more realistically perceive the running status of workloads.
Because different workload types (such as stateless workloads and tasks) have inconsistent management mechanisms for Pods, different workloads will have different life cycle states during operation, as shown in the following table:

### Stateless load, stateful load, daemon state

| Status | Description |
| :---------------------- | :------------------------ -------------------------------------- |
| Waiting | 1. A workload is in this state while its creation is in progress. <br>2. After an upgrade or rollback action is triggered, the workload is in this state. <br>3. Trigger operations such as pausing/scaling, and the workload is in this state. |
| Running | This state occurs when all instances under the load are running and the number of replicas matches the user-defined number. |
| Deleting | When a delete operation is performed, the payload is in this state until the delete is complete. |
| Exception | Unable to get the status of the workload for some reason. This usually occurs because communication with the pod's host has failed. |
| Not Ready | When the container is in an abnormal, pending state, this state is displayed when the load cannot be started due to an unknown error |

### Task Status

| Status | Description |
| :------- | :--------------------------------------- -------------------- |
| Waiting | The workload is in this state while task creation is in progress. |
| Executing | The task is in progress and the workload is in this state. |
| Execution Complete | The task execution is complete and the workload is in this state. |
| Deleting | A delete operation is triggered and the workload is in this state. |
| Exception | Pod status could not be obtained for some reason. This usually occurs because communication with the pod's host has failed. |

### Timing task status

| Status | Description |
| :----- | :---------------------------------------- ------------------ |
| Waiting | The scheduled task is in this state when it is being created. |
| Started | After the scheduled task is successfully created, the scheduled task is in this state when it is running normally or when the paused task is started. |
| Stopped | The scheduled task is in this state when the stop task operation is performed. |
| Deleting | The deletion operation is triggered, and the scheduled task is in this state. |

When the workload is in an abnormal or unready state, you can move the mouse over the state value of the load, and the system will display more detailed error information through a prompt box. You can also view the [log](../../../../insight/user-guide/data-query/log.md) or events to obtain related running information of the workload.