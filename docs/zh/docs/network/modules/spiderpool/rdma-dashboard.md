# Spiderpool RDMA 看板介绍

## Spiderpool RDMA Node - 节点看板

### Throughput

![RDMA Dashboard](../../../images/rdma/rdma-docs1.png)

![RDMA Dashboard](../../../images/rdma/rdma-docs2.png)

| 面板名称                               | 面板说明                                                     |
| :------------------------------------- | :----------------------------------------------------------- |
| Read Throughput Utilization by Device  | 该节点不同 RDMA 物理设备读吞吐量百分比看板（百分比是根据该网卡端口的传输带宽/最大传输带宽所得）。 |
| Write Throughput Utilization by Device | 该节点不同 RDMA 物理设备写吞吐量百分比看板（百分比是根据该网卡端口的传输带宽/最大传输带宽所得）。 |
| Read Throughput by Device              | 该节点不同 RDMA 物理设备读吞吐量看板。                       |
| Write Throughput by Device             | 该节点不同 RDMA 物理设备写吞吐量看板。                       |
| Read Throughput by Pod                 | 统计该节点 Pod 读带宽，如果发现节点带宽占用异常，可以通过该看板来排查哪个 Pod 占用了较大的带宽。 |
| Write Throughput by Pod                | 统计该节点 Pod 写带宽，如果发现节点带宽占用异常，可以通过该看板来排查哪个 Pod 占用了较大的带宽。 |

### Basic (ECN/CNP/SEQ)

![RDMA Dashboard](../../../images/rdma/rdma-docs3.png)

![RDMA Dashboard](../../../images/rdma/rdma-docs4.png)

![RDMA Dashboard](../../../images/rdma/rdma-docs5.png)

![RDMA Dashboard](../../../images/rdma/rdma-docs6.png)

| 面板名称                                 | 面板说明                                                     |
| :--------------------------------------- | :----------------------------------------------------------- |
| Read Pause by Priority                   | 物理端口上接收到的链路层暂停报文数量。如果该计数器持续增加，说明网络出现了拥塞，无法有效承载来自适配器的流量。约等于上游在告诉我，请暂停发送数据一会儿。 |
| Write Pause by Priority                  | 网卡向网络中其它设备发送了多少暂停请求。当 RDMA 流量占用的队列接近饱和时，网卡会发送 PFC Pause 帧给上游设备，要求其暂停发送相同优先级的流量。 |
| Read Discards by Priority                | 没有及时触发流控，导致上游继续发包，NIC 来不及处理。 网卡想把数据 DMA 到主机内存但失败，例如 RDMA 通信已经关闭场景。 |
| CNP Packets Sent Rate by Device          | 当 NP 检测到收到的报文的 ECN 位 被设置时，它就会生成并发送 CNP（Congestion Notification Packet，拥塞通知包） 给发送方，提示发送方减缓数据发送速度。 |
| ECN Marked RoCEv2 Packets Rate by Device | 统计接收端 NP 收到的、在网络中被标记为严重拥塞的 RoCEv2 数据包的数量。 |
| CNP Packets Handled Rate by Device       | 统计网络中反应点 HCA 处理了多少个 CNP 拥塞通知包，以此来限制和调节数据的发送速率，避免网络过载。 |
| Out of Sequence Packets Rate by Device   | 接收到的乱序数据包数量。                                     |
| CNP Packets Ignored Rate by Device       | 由反应点（Reaction Point）HCA 接收但被忽略的 CNP（拥塞通知包）数量。 |

### Detail

![RDMA Dashboard](../../../images/rdma/rdma-docs7.png)

![RDMA Dashboard](../../../images/rdma/rdma-docs8.png)

![RDMA Dashboard](../../../images/rdma/rdma-docs9.png)

![RDMA Dashboard](../../../images/rdma/rdma-docs10.png)

![RDMA Dashboard](../../../images/rdma/rdma-docs11.png)

| 面板名称                           | 面板说明                                                     |
| :--------------------------------- | :----------------------------------------------------------- |
| RX Write Requests                  | 接收端收到的 RDMA Write 请求的数量。                         |
| RX Read Requests                   | 接收端收到的 RDMA Read 请求的数量                            |
| RX Atomic Requests                 | 接收端收到的 原子操作（Atomic）请求的数量。                  |
| RX DCT Connect                     | 接收端处理的 DCT（Dynamic Connection Transport）连接请求的数量（传输模式 RC、UD、DCT 优缺点，见附表 1）。 |
| Out of buffer                      | 由于关联的 QP（Queue Pair）缺少 WQE（Work Queue Element）而发生的数据包丢失数量。 |
| Duplicate Reques                   | 接收到的数据包数量。重复请求指的是之前已经执行过的请求。     |
| RNR NAK Retry Error                | 接收到的 RNR NAK（Receiver Not Ready 拒绝确认）数据包数量。此时 QP 的重试次数限制未被超过。 |
| Packet Seq Error                   | 接收到的 NAK（序列错误）数据包数量。此时 QP 的重试次数限制未被超过。（在 RDMA/InfiniBand 通信中，每个 Queue Pair (QP) 都有一个 可靠连接（RC）协议，用来保证数据可靠传输。发送方发出的每个包都有一个 序列号，接收方会检查序列号来保证包顺序和完整性。） |
| Implied NAK SEQ Error              | 请求方发送 ACK 的次数，其确认的 PSN（Packet Sequence Number）大于 RDMA Read 或响应所期望的 PSN。 |
| Local ACK Timeout Error            | 发送端 RC、XRC 或 DCT QP 的 ACK 定时器到期的次数。由于 QP 的重试次数限制尚未超过，因此仍然是可恢复的错误。 |
| Resp Local Length Error            | 接收端检测到本地长度错误（Local Length Error, LLE）的次数。  |
| Resp CQE Error                     | 接收端检测到完成队列元素（CQE）带有错误的次数。              |
| Req CQE Error                      | 发送端检测到完成队列元素（CQE）带有错误的次数。              |
| Req Remote Invalid Request         | 发送端检测到远端无效请求（Remote Invalid Request, RIR）错误的次数 |
| Req detected Remote Access Errors  | 发送端检测到远端访问（Remote Access）错误的次数。            |
| Resp detected Remote Access Errors | 接收端检测到远端访问（Remote Access）错误的次数。            |
| Resp CQE Flush Error               | 接收端检测到完成队列元素（CQE）以 flushe 错误完成的次数。    |
| Req CQE Flush Error                | 发送端检测到完成队列元素（CQE）以 flushe 错误完成的次数。    |
|                                    |                                                              |

**附表1 ：**传输模式 RC、UD、DCT 优缺点。

| 传输模式 | 优点                                                         | 缺点 / 特点                                                  |
| :------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **RC**   | 语义完整支持原子操作点对点延迟最小                           | 每对端点需要一个 QP扩展性差                                  |
| **UD**   | 单 QP 可支持多播/多端点可扩展                                | 不可靠- 需要自己处理重传、排序、序列化- 通常用于消息层协议（如 MPI 的某些实现） |
| **DCT**  | 提供接近 RC 的可靠性与 RDMA 原语允许多发起方复用较少的发起 QP（DCI）降低服务端资源开销 | 折中方案：既不像 RC 完全点对点，也不像 UD 完全无连接，需要 DCT 支持的硬件/驱动 |

### RoCE

![RDMA Dashboard](../../../images/rdma/rdma-docs12.png)

| 面板名称                                   | 面板说明                                                     |
| :----------------------------------------- | :----------------------------------------------------------- |
| RoCE Adaptive Retransmissions Count        | RoCE 流量的自适应重传次数，在网络丢包或拥塞情况下，RoCE 会自适应调整重传策略，提高可靠性。 |
| RoCE Adaptive Retransmission Timeout Count | RoCE 流量因自适应重传导致超时的次数。                        |
| RoCE Slow Restart Count                    | 使用 RoCE 慢启动（slow restart）的次数，在拥塞或长时间空闲后，RoCE 会逐步恢复发送速率，避免网络突然过载。 |
| RoCE Slow Restart CNP Count                | 慢启动期间可能触发 CNP，以通知发送端降低发送速率。           |

## Spiderpool RDMA Cluster - 集群看板

![RDMA Dashboard](../../../images/rdma/rdma-docs13.png)

该看板分为 3 个部分：

- **Summary**

    | 面板名称                       | 面板说明                   |
    | ------------------------------ | -------------------------- |
    | Node Total (RDMA Capacity)     | 具有 RMDA 能力的节点数量。 |
    | Workload Total (RDMA Capacity) | RDMA 工作负载数量统计。    |
    | Pod Total (RDMA Capacity)      | RDMA Pod 数量看板。        |

- **Hotspot**
    - Hotspot 部分，主要用来排查集群热点工作负载，这样可以规划应用是否充分负载均衡或者是确认工作负载是否合理。
        - Top 10 Read Throughput by Node
        - Top 10 Write Throughput by Node
        - Top 10 Read Throughput by Pod
        - Top 10 Write Throughput by Pod
        - Top 10 Read Throughput by Workload
        - Top 10 Write Throughput by Workload
- **Node** **Status**
    - 这部分与 Node 单独的面板中的统计是相同的，具体含义可以参考上面，这部分不同的是集群下所有节点的视角，可以方便直接发现哪个节点出现了问题。
        - Read Pause by Node PF
        - Write Pause by Node PF
        - Read Discards by Node PF
        - CNP Packets Sent Rate by Node PF
        - NP ECN Marked ROCE Packets by Node PF
        - RP CNP Handled by Node PF
        - Out of Sequence by Node PF
        - RP CNP Ignored by Node PF
- **Pod Status**
    - Pod Status 统计了常见的 Pod 乱序/丢包，方便在集群这边快速查看问题。
        - Out of Sequence by Pods (Top 10)
        - Read Discards by Pods (Top 10)

## Spiderpool RDMA AI Workload - 工作负载看板

![RDMA Dashboard](../../../images/rdma/rdma-docs14.png)

RDMA Workload 可以用来监控某一组 workload 的 Pod，比如 PytorchJob 往往跨越多个节点，有时候一个 Pod 异常可能导致整组的 PytorchJob 训练失败。

通过 Workload 视角可以很方便定位问题 Pod，具体指标含义可以参考前面 Node 面板的说明，这里仅仅对象是 Workload 下的 Pod。

## Spiderpool RDMA SRIOV Pod - RDMA pod 看板

![RDMA Dashboard](../../../images/rdma/rdma-docs15.png)

RDMA Pod 是对某个特定 Pod 的监控，当使用集群级别或者节点级别面板排查到某个 Pod 出现问题后，可以使用
Pod 面板无干扰的进行排查，具体指标含义可以参考前面 Node 面板的说明，这里仅仅对象是单个 Pod。
