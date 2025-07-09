# Preemption Scheduling Strategy

Volcano implements the preemption scheduling strategy through the Priority plugin. When cluster resources are limited and multiple Jobs are waiting to be scheduled, using the default Kubernetes scheduler may cause Jobs with more Pods to get more resources. Volcano-scheduler provides an algorithm that supports different Jobs sharing cluster resources in a fair-share manner.

The Priority plugin allows users to customize the priority of Jobs and Tasks, and tailor scheduling policies at different levels as needed. For example, in scenarios requiring higher real-time performance such as finance or IoT monitoring, the Priority plugin ensures these are scheduled first.

## Usage

Priority is determined based on the Value field in the configured PriorityClass; the larger the value, the higher the priority. It is enabled by default and does not require modification. You can confirm or modify it with the following command:

```shell
kubectl -n volcano-system edit configmaps volcano-scheduler-configmap
```

## Example

Assume there are two idle nodes in the cluster and three workloads with different priorities: high-priority, med-priority, and low-priority. When the high-priority workload runs and occupies all cluster resources, the med-priority and low-priority workloads submitted afterward will be pending because all resources are used by the higher priority workload. After the high-priority workload finishes, according to the priority scheduling principle, the med-priority workload will be scheduled first.

1. Create 3 priority definitions with priority.yaml: high-priority, med-priority, and low-priority.

    ```yaml title="View priority.yaml"
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

2. Check the priority class information.

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

3. Create a high-priority workload `high-priority-job` that occupies all cluster resources.

    ```bash title="View high-priority-job"
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

    Check Pod running status:

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

    At this point, cluster node resources are fully occupied.

4. Create medium-priority workload `med-priority-job` and low-priority workload `low-priority-job`.

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

    Check Pod running status; cluster resources are insufficient, so Pods are Pending:

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

5. Delete the high-priority workload to release cluster resources; the medium-priority workload will be scheduled first.

    Run `kubectl delete -f high_priority_job.yaml` to release resources and check Pod scheduling status:

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
