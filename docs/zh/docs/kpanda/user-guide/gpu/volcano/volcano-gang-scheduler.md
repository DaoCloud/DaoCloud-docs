# 使用 Volcano 的 Gang Scheduler

Gang 调度策略是 volcano-scheduler 的核心调度算法之一，它满足了调度过程中的 “All or nothing” 的调度需求，
避免 Pod 的任意调度导致集群资源的浪费。具体算法是，观察 Job 下的 Pod 已调度数量是否满足了最小运行数量，
当 Job 的最小运行数量得到满足时，为 Job 下的所有 Pod 执行调度动作，否则，不执行。

## 使用场景

基于容器组概念的 Gang 调度算法十分适合需要多进程协作的场景。AI 场景往往包含复杂的流程，
Data Ingestion、Data Analysts、Data Splitting、Trainer、Serving、Logging 等，
需要一组容器进行协同工作，就很适合基于容器组的 Gang 调度策略。
MPI 计算框架下的多线程并行计算通信场景，由于需要主从进程协同工作，也非常适合使用 Gang 调度策略。
容器组下的容器高度相关也可能存在资源争抢，整体调度分配，能够有效解决死锁。

在集群资源不足的场景下，gang 的调度策略对于集群资源的利用率的提升是非常明显的。
比如集群现在只能容纳 2 个 Pod，现在要求最小调度的 Pod 数为 3。
那现在这个 Job 的所有的 Pod 都会 pending，直到集群能够容纳 3 个 Pod，Pod 才会被调度。
有效防止调度部分 Pod，不满足要求又占用了资源，使其他 Job 无法运行的情况。

## 概念说明

Gang Scheduler 是 Volcano 的核心的调度插件，安装 Volcano 后默认就开启了。
在创建工作负载时只需要指定调度器的名称为 Volcano 即可。

Volcano 是以 PodGroup 为单位进行调度的，在创建工作负载时，并不需要手动创建 PodGroup 资源，
Volcano 会根据工作负载的信息自动创建。下面是一个 PodGroup 的示例：

```yaml
apiVersion: scheduling.volcano.sh/v1beta1
kind: PodGroup
metadata:
  name: test
  namespace: default
spec:
  minMember: 1  # (1)!
  minResources: priorityClassName # (2)!
    cpu: "3"
    memory: "2048Mi"
  priorityClassName: high-prority # (3)!
  queue: default # (4)!
```

1. 表示该 PodGroup 下 **最少** 需要运行的 Pod 或任务数量。
   如果集群资源不满足 miniMember 数量任务的运行需求，调度器将不会调度任何一个该 PodGroup 内的任务。
2. 表示运行该 PodGroup 所需要的最少资源。当集群可分配资源不满足 minResources 时，调度器将不会调度任何一个该 PodGroup 内的任务。
3. 表示该 PodGroup 的优先级，用于调度器为该 queue 中所有 PodGroup 进行调度时进行排序。
   **system-node-critical** 和 **system-cluster-critical** 是 2 个预留的值，表示最高优先级。不特别指定时，默认使用 default 优先级或 zero 优先级。
4. 表示该 PodGroup 所属的 queue。queue 必须提前已创建且状态为 open。

## 使用案例

在 MPI 计算框架下的多线程并行计算通信场景中，我们要确保所有的 Pod 都能调度成功才能保证任务正常完成。
设置 minAvailable 为 4，表示要求 1 个 mpimaster 和 3 个 mpiworker 能运行。

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

生成 PodGroup 的资源：

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

从 PodGroup 可以看出，通过 ownerReferences 关联到工作负载，并设置最小运行的 Pod 数为 4。
