# 使用 Volcano Binpack 调度策略

binpack 调度算法的目标是尽量把已被占用的节点填满（尽量不往空白节点分配）。具体实现上，binpack 调度算法会给投递的节点打分，分数越高表示节点的资源利用率越高。通过尽可能填满节点，将应用负载靠拢在部分节点，这种调度算法能够尽可能减小节点内的碎片，在空闲的机器上为申请了更大资源请求的Pod预留足够的资源空间，使集群下空闲资源得到最大化的利用。

## 前置条件

预先在 DCE5.0 上[安装 Volcano 组件](https://docs.daocloud.io/kpanda/user-guide/gpu/volcano/volcano_user_guide/)。

## Binpack算法原理

Binpack 在对一个节点打分时，会根据 Binpack 插件自身权重和各资源设置的权重值综合打分。首先，对Pod请求资源中的每类资源依次打分，以 CPU 为例，CPU 资源在待调度节点的得分信息如下：
CPU.weight * (request + used) / allocatable
即CPU权重值越高，得分越高，节点资源使用量越满，得分越高。Memory、GPU等资源原理类似。其中：

- CPU.weight为用户设置的CPU权重
  
- request为当前Pod请求的CPU资源量
  
- used为当前节点已经分配使用的CPU量
  
- allocatable为当前节点CPU可用总量
   

通过Binpack策略的节点总得分如下：
binpack.weight * (CPU.score + Memory.score + GPU.score) / (CPU.weight+ Memory.weight+ GPU.weight) * 100
即binpack插件的权重值越大，得分越高，某类资源的权重越大，该资源在打分时的占比越大。其中：

- binpack.weight为用户设置的装箱调度策略权重
  
- CPU.score为CPU资源得分，CPU.weight为CPU权重
  
- Memory.score为Memory资源得分，Memory.weight为Memory权重
  
- GPU.score为GPU资源得分，GPU.weight为GPU权重

![原理](../images/volcano-binpack1.png)

如图所示，集群中存在两个节点，分别为 Node1 和Node 2，在调度Pod时，Binpack 策略对两个节点分别打分。
假设集群中CPU.weight配置为1，Memory.weight配置为1，GPU.weight配置为2，binpack.weight配置为5。

1. Binpack对Node 1的打分信息如下：
  
2. 各资源按照公式计算得分，具体信息如下：
  1. CPU Score：CPU.weight * (request + used) / allocatable = 1 * （2 + 4）/ 8 = 0.75
    
  2. Memory Score：Memory.weight * (request + used) / allocatable = 1 * (4 + 8) / 16 = 0.75
    
  3. GPU Score： GPU.weight * (request + used) / allocatable = 2 * （4 + 4）/ 8 = 2
    
3. 节点总得分按照binpack.weight * (CPU.score + Memory.score + GPU.score) / (CPU.weight+ Memory.weight+ GPU.weight) * 100公式进行计算，具体如下：
  
4. 假设binpack.weight配置为5，Node 1在Binpack策略下的得分：5 * （0.75 + 0.75 + 2）/（1 + 1 + 2）* 100 = 437.5
  
5. Binpack对Node 2的打分信息如下：
  1. CPU Score：CPU.weight * (request + used) / allocatable = 1 * （2 + 6）/ 8 = 1
    
  2. Memory Score：Memory.weight * (request + used) / allocatable = 1 * (4 + 8) / 16 = 0.75
    
  3. GPU Score：GPU.weight * (request + used) / allocatable = 2 * （4 + 4）/ 8 = 2
    
6. Node 2在Binpack策略下的得分：5 * （1 + 0.75 + 2）/（1 + 1 + 2）* 100 = 468.75
  

综上，Node 2得分大于Node 1，按照Binpack策略，Pod将会优先调度至Node 2。

## 使用案例
Binpack 调度插件在安装 Volcano 的时候默认就会开启；如果用户没有配置权重，则使用如下默认的配置权重。

```
- plugins:  
  - name: binpack  
    arguments:  
      binpack.weight: 1  
      binpack.cpu: 1  
      binpack.memory: 1
```
默认权重不能体现堆叠特性，因此我们修改一下，将 `binpack.weight: 10` 。

```
$ kubectl -n volcano-system edit configmaps volcano-scheduler-configmap
```

```
- plugins:  
  - name: binpack  
    arguments:  
      binpack.weight: 10  
      binpack.cpu: 1  
      binpack.memory: 1  
      binpack.resources: nvidia.com/gpu, example.com/foo  
      binpack.resources.nvidia.com/gpu: 2  
      binpack.resources.example.com/foo: 3
```
改为之后重启 volcano-scheduler pod 即可生效。


我们创建一个如下的 Deployment，在两个 Node 的集群上可以看到 Pod 被调度到一个 Node 上。


```
apiVersion: apps/v1  
kind: Deployment  
metadata:  
  name: binpack-test  
  labels:  
    app: binpack-test  
spec:  
  replicas: 2  
  selector:  
    matchLabels:  
      app: test  
  template:  
    metadata:  
      labels:  
        app: test  
    spec:  
      schedulerName: volcano  
      containers:  
      - name: test  
        image: busybox  
        imagePullPolicy: IfNotPresent  
        command: ['sh', '-c', 'echo "Hello, Kubernetes!" && sleep 3600']  
        resources:  
          requests:  
            cpu: 500m  
          limits:  
            cpu: 500m
```
调度在一个节点上。
![结果](../images/volcano-binpacknode.png)


