# Description of task parameters

According to the settings of __.spec.completions__ and __.spec.Parallelism__ , tasks (Job) can be divided into the following types:

| Job Type | Description |
| -------------------------- | ---------------------- ----------------------------------------- |
| Non-parallel Job | Creates a Pod until its Job completes successfully |
| Parallel Jobs with deterministic completion counts | A Job is considered complete when the number of successful Pods reaches __.spec.completions__ |
| Parallel Job | Creates one or more Pods until one finishes successfully |

**Parameter Description**

| RestartPolicy | Creates a Pod until it terminates successfully |
| --------------------------- | --------------------- ------------------------------------------ |
| .spec.completions | Indicates the number of Pods that need to run successfully when the Job ends, the default is 1 |
| .spec.parallelism | Indicates the number of Pods running in parallel, the default is 1 |
| spec.backoffLimit | Indicates the maximum number of retries for a failed Pod, beyond which no more retries will continue. |
| .spec.activeDeadlineSeconds | Indicates the Pod running time. Once this time is reached, the Job, that is, all its Pods, will stop. And activeDeadlineSeconds has a higher priority than backoffLimit, that is, the job that reaches activeDeadlineSeconds will ignore the setting of backoffLimit. |

The following is an example Job configuration, saved in myjob.yaml, which calculates π to 2000 digits and prints the output.

```yaml
apiVersion: batch/v1
kind: Job #The type of the current resource
metadata:
  name: myjob
spec:
  completions: 50 # Job needs to run 50 Pods at the end, in this example it prints π 50 times
  parallelism: 5 # 5 Pods in parallel
  backoffLimit: 5 # retry up to 5 times
  template:
    spec:
      containers:
      - name: pi
        image: perl
        command: ["perl", "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: Never #restart policy
```

**Related commands**

```bash
kubectl apply -f myjob.yaml #start job
kubectl get job #View this job
kubectl logs myjob-1122dswzs View Job Pod logs
```