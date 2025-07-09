# DRF (Dominant Resource Fairness) Scheduling Policy

The DRF scheduling policy prioritizes tasks that consume fewer resources. This allows more jobs to be satisfied and prevents a single large job from starving many smaller jobs. The DRF scheduling algorithm ensures as fair a resource allocation as possible in environments where multiple resource types coexist.

## How to Use

The DRF scheduling policy is enabled by default and requires no additional configuration.

```shell
kubectl -n volcano-system view configmaps volcano-scheduler-configmap
```

## Usage Example

In AI training or big data computing scenarios, running smaller resource-consuming tasks first with limited resources improves cluster utilization and avoids starving small jobs.

Below, two Jobs are created: one with small resource requirements and one with large resource requirements. You can see that the job with smaller resource needs will be scheduled first.

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
