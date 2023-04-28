# 预留磁盘

本章节介绍如何在界面上预留磁盘，此功能的使用场景如下：

运维管理员有磁盘的规划需求，需要预留部分磁盘不被 Hwameistor 使用，需要自行进行 Reserved操作

## **使用说明**

1. Local Disk 的使用状态和预留状态为 2 个状态，任何状态的 LD 都可以 Reserved/Unreserved。
2. Hwameistor 在启动初期会自动检测系统盘并标记为 Reserveds
3. LD 只有三种状态：**Pending，Available，Bound**。LD 使用状态和 Reserved 情况如下：

| 使用状态  | 是否 Reserved | 场景说明                                                     |
| :-------- | :------------ | :----------------------------------------------------------- |
| Pending   | --            | 初始化状态                                                   |
| Pending   | Reserved      | 初始化瞬间被用户预留                                         |
| Available | --            | 空闲磁盘，可被 Hwameistor 分配                               |
| Available | Reserved      | 空闲磁盘但是规划作为他用，无法被 Hwameistor 分配无文件系统，但实际此磁盘已被使用，同时被用户标记成 Reserved |
| Bound     | --            | 被 Hwameistor 使用的磁盘被系统或者外部程序使用，并手动去除了 Reserved 状态 |
| Bound     | Reserved      | 被系统或者外部程序使用，并手动去除 Reserved 状态被 Hwamristor 使用，同时用户手动标记为 Reserved 状态，当磁盘上的数据释放后，不在被 Hwameistor 系统使用 |

## 操作步骤

进入对应`集群`，选择`存储`-->`Hwameistor`；点击`节点` 进入节点详情页面，找到对应的磁盘；点击 `...`，选择`预留磁盘`；点击`确认`进行预留。

预留后磁盘将不会被 Hwameistor 使用。

![](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/reserveddisk.jpg)
