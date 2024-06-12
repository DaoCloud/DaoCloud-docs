# Using Volcano's Gang Scheduler

The Gang scheduling strategy is one of the core scheduling algorithms of the volcano-scheduler. 
It satisfies the "All or nothing" scheduling requirement during the scheduling process, preventing 
arbitrary scheduling of Pods that could waste cluster resources. The specific algorithm observes 
whether the number of scheduled Pods under a Job meets the minimum running quantity. 
When the Job's minimum running quantity is satisfied, scheduling actions are performed for all Pods under the Job; 
otherwise, no actions are taken.

## Use Cases

The Gang scheduling algorithm, based on the concept of a Pod group, is particularly suitable for scenarios 
that require multi-process collaboration. AI scenarios often involve complex workflows, such as Data Ingestion, 
Data Analysis, Data Splitting, Training, Serving, and Logging, which require a group of containers to work together. 
This makes the Gang scheduling strategy based on container groups very appropriate. 

In multi-threaded parallel computing communication scenarios under the MPI computation framework, 
Gang scheduling is also very suitable because it requires master and slave processes to work together. 
High relevance among containers in a container group may lead to resource contention, and overall scheduling allocation 
can effectively resolve deadlocks.

In scenarios with insufficient cluster resources, the Gang scheduling strategy significantly improves 
the utilization of cluster resources. For example, if the cluster can currently accommodate only 2 Pods, 
but the minimum number of Pods required for scheduling is 3, then all Pods of this Job will remain pending until 
the cluster can accommodate 3 Pods, at which point the Pods will be scheduled. This effectively prevents the 
partial scheduling of Pods, which would not meet the requirements and would occupy resources, making other Jobs unable to run.

## Concept Explanation

The Gang Scheduler is the core scheduling plugin of Volcano, and it is enabled by default upon installing Volcano. 
When creating a workload, you only need to specify the scheduler name as Volcano.

Volcano schedules based on PodGroups. When creating a workload, there is no need to manually create PodGroup resources; 
Volcano will automatically create them based on the workload information. Below is an example of a PodGroup:

```yaml
apiVersion: scheduling.volcano.sh/v1beta1
kind: PodGroup
metadata:
  name: test
  namespace: default
spec:
  minMember: 1  # (1)!
  minResources:  # (2)!
    cpu: "3"
    memory: "2048Mi"
  priorityClassName: high-prority # (3)!
  queue: default # (4)!
```

1. Represents the **minimum** number of Pods or tasks that need to run under this PodGroup. If the cluster resources 
  do not meet the requirements to run the number of tasks specified by miniMember, the scheduler will not 
  schedule any tasks within this PodGroup.
2. Represents the minimum resources required to run this PodGroup. If the allocatable resources of the cluster
   do not meet the minResources, the scheduler will not schedule any tasks within this PodGroup.
3. Represents the priority of this PodGroup, used by the scheduler to sort all PodGroups within the queue during scheduling. 
  **system-node-critical** and **system-cluster-critical** are two reserved values indicating the highest priority. 
  If not specifically designated, the default priority or zero priority is used.
4. Represents the queue to which this PodGroup belongs. The queue must be pre-created and in the open state.

## Use Case

In a multi-threaded parallel computing communication scenario under the MPI computation framework, we need to ensure 
that all Pods can be successfully scheduled to ensure the task is completed correctly. Setting minAvailable to 4 
means that 1 mpimaster and 3 mpiworkers are required to run.

```yaml
apiVersion: batch.volcano.sh/v1alpha1
kind: Job
metadata:
  name: lm-mpi-job
  labels:
    "volcano.sh/job-type": "MPI"
spec:
  minAvailable: 4
  schedulerName: volcano
  plugins:
    ssh: []
    svc: []
  policies:
    - event: PodEvicted
      action: RestartJob
  tasks:
    - replicas: 1
      name: mpimaster
      policies:
        - event: TaskCompleted
          action: CompleteJob
      template:
        spec:
          containers:
            - command:
                - /bin/sh
                - -c
                - |
                  MPI_HOST=`cat /etc/volcano/mpiworker.host | tr "\n" ","`;
                  mkdir -p /var/run/sshd; /usr/sbin/sshd;
                  mpiexec --allow-run-as-root --host ${MPI_HOST} -np 3 mpi_hello_world;
              image: docker.m.daocloud.io/volcanosh/example-mpi:0.0.1
              name: mpimaster
              ports:
                - containerPort: 22
                  name: mpijob-port
              workingDir: /home
              resources:
                requests:
                  cpu: "500m"
                limits:
                  cpu: "500m"
          restartPolicy: OnFailure
          imagePullSecrets:
            - name: default-secret
    - replicas: 3
      name: mpiworker
      template:
        spec:
          containers:
            - command:
                - /bin/sh
                - -c
                - |
                  mkdir -p /var/run/sshd; /usr/sbin/sshd -D;
              image: docker.m.daocloud.io/volcanosh/example-mpi:0.0.1
              name: mpiworker
              ports:
                - containerPort: 22
                  name: mpijob-port
              workingDir: /home
              resources:
                requests:
                  cpu: "1000m"
                limits:
                  cpu: "1000m"
          restartPolicy: OnFailure
          imagePullSecrets:
            - name: default-secret
```

Generate the resources for PodGroup:

```yaml
apiVersion: scheduling.volcano.sh/v1beta1
kind: PodGroup
metadata:
  annotations:
  creationTimestamp: "2024-05-28T09:18:50Z"
  generation: 5
  labels:
    volcano.sh/job-type: MPI
  name: lm-mpi-job-9c571015-37c7-4a1a-9604-eaa2248613f2
  namespace: default
  ownerReferences:
  - apiVersion: batch.volcano.sh/v1alpha1
    blockOwnerDeletion: true
    controller: true
    kind: Job
    name: lm-mpi-job
    uid: 9c571015-37c7-4a1a-9604-eaa2248613f2
  resourceVersion: "25173454"
  uid: 7b04632e-7cff-4884-8e9a-035b7649d33b
spec:
  minMember: 4
  minResources:
    count/pods: "4"
    cpu: 3500m
    limits.cpu: 3500m
    pods: "4"
    requests.cpu: 3500m
  minTaskMember:
    mpimaster: 1
    mpiworker: 3
  queue: default
status:
  conditions:
  - lastTransitionTime: "2024-05-28T09:19:01Z"
    message: '3/4 tasks in gang unschedulable: pod group is not ready, 1 Succeeded,
      3 Releasing, 4 minAvailable'
    reason: NotEnoughResources
    status: "True"
    transitionID: f875efa5-0358-4363-9300-06cebc0e7466
    type: Unschedulable
  - lastTransitionTime: "2024-05-28T09:18:53Z"
    reason: tasks in gang are ready to be scheduled
    status: "True"
    transitionID: 5a7708c8-7d42-4c33-9d97-0581f7c06dab
    type: Scheduled
  phase: Pending
  succeeded: 1
```

From the PodGroup, it can be seen that it is associated with the workload through ownerReferences and 
sets the minimum number of running Pods to 4.
