# 优先级抢占（Preemption scheduling）策略

Volcano 通过 Priority 插件实现了优先级抢占策略，即 Preemption scheduling 策略。在集群资源有限且多个 Job 等待调度时，
如果使用 Kubernetes 默认调度器，可能会导致具有更多 Pod 数量的 Job 分得更多资源。而 Volcano-scheduler 提供了算法，支持不同的 Job 以 fair-share 的形式共享集群资源。

Priority 插件允许用户自定义 Job 和 Task 的优先级，并根据需求在不同层次上定制调度策略。
例如，对于金融场景、物联网监控场景等需要较高实时性的应用，Priority 插件能够确保其优先得到调度。

## 使用方式

优先级的决定基于配置的 PriorityClass 中的 Value 值，值越大优先级越高。默认已启用，无需修改。可通过以下命令确认或修改。

```shell
kubectl -n volcano-system edit configmaps volcano-scheduler-configmap
```

## 使用案例

假设集群中存在两个空闲节点，并有三个优先级不同的工作负载：high-priority、med-priority 和 low-priority。
当 high-priority 工作负载运行并占满集群资源后，再提交 med-priority 和 low-priority 工作负载。
由于集群资源全部被更高优先级的工作负载占用，med-priority 和 low-priority 工作负载将处于 pending 状态。
当 high-priority 工作负载结束后，根据优先级调度原则，med-priority 工作负载将优先被调度。

1. 通过 priority.yaml 创建 3 个优先级定义，分别为：high-priority，med-priority，low-priority。

    ```yaml title="查看 priority.yaml"
    cat <<EOF | kubectl apply -f - 
    apiVersion: scheduling.k8s.io/v1 
    kind: PriorityClass 
    items: 
      - metadata: 
          name: high-priority 
        value: 100 
        globalDefault: false 
        description: "This priority class should be used for volcano job only." 
      - metadata: 
          name: med-priority 
        value: 50 
        globalDefault: false 
        description: "This priority class should be used for volcano job only." 
      - metadata: 
          name: low-priority 
        value: 10 
        globalDefault: false 
        description: "This priority class should be used for volcano job only." 
    EOF
    ```
2. 查看优先级定义信息。

    ```bash
    kubectl get PriorityClass
    ```
    ```console
    NAME                      VALUE        GLOBAL-DEFAULT   AGE  
    high-priority             100          false            97s  
    low-priority              10           false            97s  
    med-priority              50           false            97s  
    system-cluster-critical   2000000000   false            6d6h  
    system-node-critical      2000001000   false            6d6h
    ```
  
3. 创建高优先级工作负载 high-priority-job，占用集群的全部资源。

    ```bash title="查看 high-priority-job"
    cat <<EOF | kubectl apply -f -  
    apiVersion: batch.volcano.sh/v1alpha1  
    kind: Job  
    metadata:  
      name: priority-high  
    spec:  
      schedulerName: volcano  
      minAvailable: 4  
      priorityClassName: high-priority  
      tasks:  
        - replicas: 4  
          name: "test"  
          template:  
            spec:  
              containers:  
                - image: alpine  
                  command: ["/bin/sh", "-c", "sleep 1000"]  
                  imagePullPolicy: IfNotPresent  
                  name: running  
                  resources:  
                    requests:  
                      cpu: "4"  
              restartPolicy: OnFailure  
    EOF
    ```

    通过 `kubectl get pod` 查看 Pod运行 信息：

    ```bash
    kubectl get pods
    ```
    ```console
    NAME                   READY   STATUS    RESTARTS   AGE  
    priority-high-test-0   1/1     Running   0          3s  
    priority-high-test-1   1/1     Running   0          3s  
    priority-high-test-2   1/1     Running   0          3s  
    priority-high-test-3   1/1     Running   0          3s
    ```

    此时，集群节点资源已全部被占用。

4. 创建中优先级工作负载 med-priority-job 和低优先级工作负载 low-priority-job。

    ```bash title="med-priority-job"
    cat <<EOF | kubectl apply -f -  
    apiVersion: batch.volcano.sh/v1alpha1  
    kind: Job  
    metadata:  
      name: priority-medium  
    spec:  
      schedulerName: volcano  
      minAvailable: 4  
      priorityClassName: med-priority  
      tasks:  
        - replicas: 4  
          name: "test"  
          template:  
            spec:  
              containers:  
                - image: alpine  
                  command: ["/bin/sh", "-c", "sleep 1000"]  
                  imagePullPolicy: IfNotPresent  
                  name: running  
                  resources:  
                    requests:  
                      cpu: "4"  
              restartPolicy: OnFailure  
    EOF
    ```

    ```bash title="low-priority-job"
    cat <<EOF | kubectl apply -f -  
    apiVersion: batch.volcano.sh/v1alpha1  
    kind: Job  
    metadata:  
      name: priority-low  
    spec:  
      schedulerName: volcano  
      minAvailable: 4  
      priorityClassName: low-priority  
      tasks:  
        - replicas: 4  
          name: "test"  
          template:  
            spec:  
              containers:  
                - image: alpine  
                  command: ["/bin/sh", "-c", "sleep 1000"]  
                  imagePullPolicy: IfNotPresent  
                  name: running  
                  resources:  
                    requests:  
                      cpu: "4"  
              restartPolicy: OnFailure  
    EOF
    ```

    通过 `kubectl get pod` 查看 Pod 运行信息，集群资源不足，Pod 处于 Pending 状态：

    ```bash
    kubectl get pods
    ```
    ```console
    NAME                     READY   STATUS    RESTARTS   AGE  
    priority-high-test-0     1/1     Running   0          3m29s  
    priority-high-test-1     1/1     Running   0          3m29s  
    priority-high-test-2     1/1     Running   0          3m29s  
    priority-high-test-3     1/1     Running   0          3m29s  
    priority-low-test-0      0/1     Pending   0          2m26s  
    priority-low-test-1      0/1     Pending   0          2m26s  
    priority-low-test-2      0/1     Pending   0          2m26s  
    priority-low-test-3      0/1     Pending   0          2m26s  
    priority-medium-test-0   0/1     Pending   0          2m36s  
    priority-medium-test-1   0/1     Pending   0          2m36s  
    priority-medium-test-2   0/1     Pending   0          2m36s  
    priority-medium-test-3   0/1     Pending   0          2m36s
    ```

5. 删除 high_priority_job 工作负载，释放集群资源，med_priority_job 会被优先调度。
   执行 `kubectl delete -f high_priority_job.yaml` 释放集群资源，查看 Pod 的调度信息：

    ```bash
    kubectl get pods
    ```
    ```console
    NAME                     READY   STATUS    RESTARTS   AGE  
    priority-low-test-0      0/1     Pending   0          5m18s  
    priority-low-test-1      0/1     Pending   0          5m18s  
    priority-low-test-2      0/1     Pending   0          5m18s  
    priority-low-test-3      0/1     Pending   0          5m18s  
    priority-medium-test-0   1/1     Running   0          5m28s  
    priority-medium-test-1   1/1     Running   0          5m28s  
    priority-medium-test-2   1/1     Running   0          5m28s  
    priority-medium-test-3   1/1     Running   0          5m28s
    ```
