# 服务网格的控制面组件

| 组件名称                     | 位置         | 描述           | 默认资源设置             |
| ---------------------------- | ------------ | ---------------------------- | ---------------- |
| mspider-ui                   | 全局管理集群 | 服务网格界面                                                                                         | requests: CPU: 未设置；内存: 未设置<br> limits: CPU: 未设置；内存: 未设置 |
| mspider-ckube                | 全局管理集群 | Kubernetes API Server 的加速组件，用于调用全局集群相关的资源                                        | requests: CPU: 未设置；内存: 未设置<br/> limits: CPU: 未设置；内存: 未设置 |
| mspider-ckube-remote         | 全局管理集群 | 用于调用远程集群的 Kubernetes， 聚合多集群资源，并且加速                                            | requests: CPU: 未设置；内存: 未设置<br/> limits: CPU: 未设置；内存: 未设置 |
| mspider-gsc-controller       | 全局管理集群 | 服务网格管理组件，用于网格创建，网格配置等网格控制面生命周期管理，以及权限管理等 Mspider  控制面能力 | requests: CPU: 未设置；内存: 未设置 <br/>limits: CPU: 未设置；内存: 未设置 |
| mspider-api-service          | 全局管理集群 | 为 Mspider 后台 API 交互，等控制行为提供接口                                                     | requests: CPU: 未设置；内存: 未设置 <br/>limits: CPU: 未设置；内存: 未设置 |
| 托管网格                     |              |                                                                                                      |                                                                        |
| istiod-{meshID}-hosted       | 控制面集群   | 用于托管网格的策略管理                                                                               | requests: CPU: 100m；内存: 100m <br/>limits: CPU: 未设置；内存: 未设置 |
| mspider-mcpc-ckube-remote    | 控制面集群   | 调用远程的网格工作集群，加速并且聚合多集群资源                                                       | requests: CPU: 100m；内存: 50m<br/>limits: CPU: 500m；内存: 500m     |
| mspider-mcpc-mcpc-controller | 控制面集群   | 聚合网格多集群相关数据面信息                                                                         | requests: CPU: 100m；内存: 0<br/> limits: CPU: 300m；内存: 1.56G      |
| {meshID}-hosted-apiserver    | 控制面集群   | 托管控制面虚拟集群 API Server                                                                       | requests: CPU: 未设置；内存: 未设置<br/> limits: CPU: 未设置；内存: 未设置 |
| {meshID}-etcd    | 控制面集群   | 托管控制面虚拟集群 etcd，用于托管网格的策略存储                                                                       | requests: CPU: 未设置；内存: 未设置<br/> limits: CPU: 未设置；内存: 未设置 |
| istiod                       | 工作集群     | 主要用于所在集群的边车生命周期管理                                                                   | requests: CPU: 100；内存: 100<br/> limits: CPU: 未设置；内存: 未设置  |
| 专有网格                     |              |                                                                                                      |                                                                        |
| istiod                       |              | 用于策略创建、下发、边车生命周期管理的工作                                                           | requests: CPU: 100；内存: 100<br/> limits: CPU: 未设置；内存: 未设置  |
| mspider-mcpc-ckube-remote    | 工作集群     | 调用远程的网格工作集群                                                                               | requests: CPU: 100m；内存: 50m<br/> limits: CPU: 500m；内存: 500m     |
| mspider-mcpc-mcpc-controller | 工作集群     | 收集集群数据面信息                                                                                   | requests: CPU: 100m；内存: 0<br/> limits: CPU: 300m；内存: 1.56G      |
| 外接网格                     |              |                                                                                                      |                                                                        |
| mspider-mcpc-ckube-remote    | 工作集群     | 调用远程的网格工作集群                                                                               | requests: CPU: 100m；内存: 50m<br/> limits: CPU: 500m；内存: 500m     |
| mspider-mcpc-mcpc-controller | 工作集群     | 收集集群数据面信息                                                                                   | requests: CPU: 100m；内存: 0<br/> limits: CPU: 300m；内存: 1.56G      |

服务网格的各控制面组件预设资源设置如上表所示，用户可以在[容器管理](../../../kpanda/user-guide/workloads/create-deployment.md)模块查找相应的工作负载，为工作负载自定义 CPU、内存资源。
