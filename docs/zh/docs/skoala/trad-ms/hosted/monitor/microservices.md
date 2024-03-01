# 微服务监控

微服务引擎通过内置 Grafana 提供全方位的监控功能，覆盖各个微服务、系统组件、以及服务调用链路等监控对象。
其中，微服务监控功能可以提供对托管注册中心下各个微服务的监控信息，包括服务响应时间、并发量、异常 QPS、阻塞 QPS、通过 QPS、成功 QPS 等多个维度的信息。

!!! note

    集群中需要[安装 insight-agent 组件](../../../../insight/quickstart/install/install-agent.md)后才能使用监控功能。

查看微服务监控的步骤如下：

1. 进入微服务引擎模块，点击目标注册中心的名称。

    ![点击名称](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/monitor01.png)

2. 在左侧导航栏点击 __监控__ -> __微服务监控__ 。

    ![导航栏](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/monitor05.png)

3. 选择对应的微服务命名空间、服务、实例和资源即可查看该命名空间下的微服务监控数据。

    > 点击仪表盘名称可以进一步查看或分享该监控信息。在页面右上角可切换统计时间窗口和刷新周期。

    ![查看信息](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/monitor06.png)

## 微服务监控指标说明

| 指标                                 | 含义                                                         |
| :----------------------------------- | :----------------------------------------------------------- |
| 通过/拒绝 QPS                        | 资源请求通过的QPS/资源请求拒绝的QPS。                        |
| 响应时间                             | 资源请求的实时响应时间                                       |
| QPS 仪表盘                           | 资源请求的通过的QPS、资源请求的拒绝的QPS、资源请求的异常的QPS、资源请求的成功的QPS、资源请求的被占用的QPS、资源请求的并发数 |
| JDK                                  | JVM信息指标                                                  |
| Status                               | 应用实例的健康状态                                           |
| State                                | 连续时间内应用实例的健康状态                                 |
| Uptime                               | 实例的运行时间                                               |
| Start time                           | 实例的启动时间                                               |
| CPU Cores                            | 可用的CPU数量                                                |
| Total RAM                            | 总物理内存的大小                                             |
| Total SWAP                           | 总交换空间大小                                               |
| Open file descriptors                | 打开的文件描述符数量                                         |
| Class Loading count                  | 应用已加载的类数量                                           |
| Classes Loaded                       | 当前已加载的 JVM 类的数量                                    |
| CPU Time                             | 当前进程的 CPU 时间                                          |
| CPU System load average              | 系统 CPU 负载                                                |
| CPU Process Load (1m avg)            | 平均进程 CPU 负载                                            |
| CPU System Load (1m avg)             | 平均系统 CPU 负载                                            |
| Memory Utilization                   | 实例的可用物理内存占总物理内存的百分比                       |
| SWAP Utilization                     | 实例的可用交换空间占总交换空间的百分比                       |
| CPU load                             | 系统在运行过程中的 CPU 使用情况                              |
| Open File Descriptors                | 进程打开文件描述符数量                                       |
| Physical memory                      | 物理内存                                                     |
| Process Memory                       | 进程内存                                                     |
| JVM Memory Used [heap]               | JVM中已使用的堆内存                                          |
| JVM Memory Used [nonheap]            | JVM中已使用的非堆内存                                        |
| JVM Memory Usage [heap]              | JVM 堆内存使用量相对于最大可用内存的百分比、JVM 堆内存使用量占操作系统总物理内存的百分比 |
| JVM Memory Usage [nonheap]           | JVM 堆内存使用量占操作系统总物理内存的百分比                 |
| JVM Memory committed                 | JVM中的已提交内存大小                                        |
| Memory pool [Code Cache]             | JVM内存池代码【缓冲区】                                      |
| Memory pool [Compressed Class Space] | JVM内存池【压缩类空间】                                      |
| Memory pool [Eden Space]             | JVM内存池【伊甸园区】                                        |
| Memory pool [Metaspace]              | JVM内存池【元空间】                                          |
| Memory pool [Survivor Space]         | JVM内存池幸存者区                                            |
| Memory pool [Tenured Gen]            | JVM内存池老年代                                              |
| GC count increase                    | JVM 垃圾回收（GC）的次数增量                                 |
| GC count rate                        | JVM 垃圾回收（GC）的速率                                     |
| GC Time increase                     | JVM 垃圾回收（GC）的总时间增量                               |
| GC Time rate                         | JVM 垃圾回收（GC）的平均速率                                 |
| JVM Threads current                  | JVM中当前的活跃线程数量                                      |
| JVM Threads current increase         | JVM中当前的活跃线程增长量                                    |
| JVM Threads current rate             | JVM中当前的活跃线程增长率                                    |
| Class Loading count                  | JVM 当前已加载类的数量                                       |
| Classes Loaded                       | JVM 已加载类的总数                                           |
| Classes Loaded increase              | JVM 当前已加载类的数量的增量                                 |
| Classes Loaded rate                  | JVM 当前已加载类的数量变化的平均速率                         |
