# 任务参数说明

根据 __ .spec.completions__ 和 __ .spec.Parallelism__ 的设置，可以将任务（Job）划分为以下几种类型:

| Job 类型                    | 说明                                                         |
| -------------------------- | ------------------------------------------------------------ |
| 非并行 Job                  | 创建一个 Pod 直至其 Job 成功结束                               |
| 具有确定完成计数的并行 Job | 当成功的 Pod 个数达到 __ .spec.completions__ 时，Job 被视为完成 |
| 并行 Job                   | 创建一个或多个 Pod 直至有一个成功结束                          |

**参数说明**

| RestartPolicy               | 创建一个 Pod 直至其成功结束                                    |
| --------------------------- | ------------------------------------------------------------ |
| .spec.completions           | 表示 Job 结束需要成功运行的 Pod 个数，默认为 1               |
| .spec.parallelism           | 表示并行运行的 Pod 的个数，默认为 1                          |
| spec.backoffLimit           | 表示失败 Pod 的重试最大次数，超过这个次数不会继续重试。      |
| .spec.activeDeadlineSeconds | 表示 Pod 运行时间，一旦达到这个时间，Job 即其所有的 Pod 都会停止。且activeDeadlineSeconds 优先级高于 backoffLimit，即到达 activeDeadlineSeconds 的 Job 会忽略backoffLimit 的设置。 |

以下是一个 Job 配置示例，保存在 myjob.yaml 中，其计算 π 到 2000 位并打印输出。

```yaml
apiVersion: batch/v1
kind: Job            #当前资源的类型
metadata:
  name: myjob
spec:
  completions: 50        # Job结束需要运行50个Pod，这个示例中就是打印π 50次
  parallelism: 5        # 并行5个Pod
  backoffLimit: 5        # 最多重试5次
  template:
    spec:
      containers:
      - name: pi
        image: perl
        command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: Never #重启策略
```

**相关命令**

```bash
kubectl apply -f myjob.yaml  #启动 job
kubectl get job #查看这个job
kubectl logs myjob-1122dswzs 查看Job Pod 的日志
```
