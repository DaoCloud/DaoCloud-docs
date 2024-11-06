# DRF（Dominant Resource Fairness） 调度策略

DRF 调度策略认为占用资源较少的任务具有更高的优先级。这样能够满足更多的作业，不会因为一个胖业务，
饿死大批小业务。DRF 调度算法能够确保在多种类型资源共存的环境下，尽可能满足分配的公平原则。

## 使用方式

DRF 调度策略默认已启用，无需任何配置。

```shell
kubectl -n volcano-system view configmaps volcano-scheduler-configmap
```

## 使用案例

在 AI 训练，或大数据计算中，通过有限运行使用资源少的任务，这样可以让集群资源使用率更高，而且还能避免小任务被饿死。
如下创建两个 Job，一个是小资源需求，一个是大资源需求，可以看出来小资源需求的 Job 优先运行起来。

```shell
cat <<EOF | kubectl apply -f -  
apiVersion: batch.volcano.sh/v1alpha1  
kind: Job  
metadata:  
  name: small-resource  
spec:  
  schedulerName: volcano  
  minAvailable: 4  
  priorityClassName: small-resource  
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
                  cpu: "1"  
          restartPolicy: OnFailure  
---  
apiVersion: batch.volcano.sh/v1alpha1  
kind: Job  
metadata:  
  name: large-resource  
spec:  
  schedulerName: volcano  
  minAvailable: 4  
  priorityClassName: large-resource  
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
                  cpu: "2"  
          restartPolicy: OnFailure  
EOF
```
