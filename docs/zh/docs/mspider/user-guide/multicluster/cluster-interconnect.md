# 多云网络互联

多云网络互联是在多集群模式下，多集群之间网络互不相通（Pod 无法直接建立通讯）的情况下提供的一套解决方案，可以快速地将多集群的网络连通，实现跨集群的 Pod 互相访问。

## 使用场景

如果您的环境满足以下条件，可尝试请使用多云网络互联功能：

1. 使用的是托管网格，至少包含了 2 个或以上的集群
2. 托管网格的工作集群之间的网络存在无法直接连通的情况（工作集群 Pod CIDR 规划冲突、集群网络不在同一数据中心等）

!!! note

    多云网络互联仅适用于托管网格。

## 名词解释与使用说明

- 网络分组：
    - 用于辨别网格内集群的网络拓扑关系。
    - 如果**某些集群的网络能够直接互通（跨集群的 Pod IP 没有冲突且能够直接连通），那么这些集群应该被放在一个网络分组里**，否则将属于不同的网络分组。
    - 网络分组和集群的网络 CNI 实现类型没有明确的关联关系。
- 东西网关：
    - 用于不同网络分组间通信互联，一个网络分组内可以创建多个。
    - 用户可以在网络分组下任意集群创建东西网关，当移动集群至其他网络分组时，东西网关也会随之迁移。
    - 东西网关所用负载均衡 IP 通常有集群所在的云平台自动分配，也可以由用户配置设定。
- 基本设置：创建用于东西网关的`网关规则`配置，该配置将开放 15443 端口用于网络分组间的通信，用户可以在`网关规则`列表中查看 CRD 文件详细内容，但不建议修改，可能会导致网络通信失败。
- 网络分组列表：
    - 展示当前创建的网络分组及分组下集群、东西网关信息；
    - 在该列表下用户可以对网络分组、分组下集群及东西网关执行增删操作，并可以在网络分组间迁移集群。
- 互联列表：
    - 包含至少一个东西网关的网络分组可以加入互联列表，加入互联的网络分组可以和其他网络分组通信。
    - 已加入互联的网络分组可以修改负载均衡 IP，但如需修改其他配置（例如增删集群、东西网关），需要先移除`网络分组互联`列表。
    - 加入互联和移除互联会引起网格控制面的重启，建议谨慎操作。

## 操作流程

建议操作流程如下图所示

![操作流程](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-process.png)

## 操作步骤

1. 进入某个托管网格，点击启用开关，在成功启用后将自动创建用于东西网关的`网关规则`。点击`创建网络分组`按钮，至少网络分组添加至少一个工作集群。

    ![创建](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-CreateGroupButton.jpg)

1. 为网络分组填入名称，并添加至少一个集群。

    ![创建对话框](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-CreateGroupDialog.png)

    !!! note

         1. 网络分组名称创建后无法修改。
         2. 注意同一网络分组内的集群需确保处于同一网络类型并可以互通，否则可能造成互联失败。

2. 网络分组内添加或移出集群。

    创建网络分组后，即可为分组内添加更多的集群，**同一分组的集群需确保处于同一网络类型并可以互通，否则可能造成互联失败**。

    ![添加集群](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-AddCluster.png)

    添加完成后即可在网络分组下看到多个集群。

    ![集群列表](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-ClusterList.jpg)

    !!! note

        1. 网络分组中至少要保留一个集群，如需移除所有集群，请删除网络分组
        2. 网络分组内的成员集群发生变化是一件非常重要的事情，请慎重操作
        3. 变更后会在规则变更后再生效前会存在网络延迟，建议在业务低峰期进行操作
        4. 跨网络分组内的成员集群发生变化后，会涉及到工作负载 `Pod` 的边车需要重启后流量才会生效

3. 创建/删除东西网关。

    东西网关用于网络分组间通信，可以在分组内的任一集群上创建一个或多个网关。点击一个集群右侧的 `⋮`，选择`编辑东西网关`：

    ![编辑东西网关](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-destirule01.png)

    创建配置项如下：

    - `负载均衡注释`为可选设置，部分云平台会以注释方式提供负载均衡 IP 分配，请参考云平台提供的技术文档；
    - `东西网关副本数`默认为 1，如果需要提高网关可用性，可创建多个副本；点击`确定`；

        ![网关参数](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-destirule02.png)

        选择一个东西网关，点击操作中的`删除东西网关`，可以删除该网关，如图所示：

        ![删除网关](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-destirule03.png)

    !!! note

        每个网络分组至少需要创建一个东西网关，否则无法加入互联。

4. 网络分组互联

    1. 如果要将一个网络分组加入互联，点击`加入互联`按钮。

        ![加入互联](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-join.png)

    2. 勾选一个网络分组，点击`下一步`。

        ![选择集群](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-join01.png)

    3. 选择可用的`东西网关地址`，点击`确定`。

        ![选择东西网关地址](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-join02.png)

    4. 在互联列表中可以看到新加入的网络分组，列表内的分组之间彼此建立了通信。

    !!! note

        - 没有东西网关的网络分组无法加入互联
        - 加入分组互联操作会引起网格控制面重启，建议加入互联前确保网络分组配置无误

## 其他操作

1. 更新东西网关地址。

    用户可以对处于互联状态的网络分组增删东西网关地址。在互联列表中勾选一个分组，点击`更新东西网关地址`。

    ![更新东西网关地址](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-update.png)

    更新地址后点击`确定`。

    ![确定](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-update01.png)

1. 移出互联

    如果网络分组不再需要和其他网络分组建立互联，或需要调整分组内集群及东西网关设置，可以移出互联。
    在网络分组互联中，选择需要移除的网络分组，点击`移出互联`按钮，出现下图对话框。

    ![移出互联](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-removeclusterfromC.png)

    经过二次确认，网络分组即可移出互联列表。

    !!! warn

        - 网络分组内的集群是可以互相通信的，无法直接通讯的集群需要依靠网络分组的东西向网关进行通讯，因此需要加入互联
        - 如果要修改某个网络分组内的集群信息，强烈建议先讲集群移出网络互联，修改完成后再加入互联，减少对整体网络互联的影响

2. 删除网络分组

    在需要删除的网络分组操作下拉框中点击`删除网络分组`，即可删除所选网络分组。

    ![删除分组](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-deletegroup.png)

3. 关闭`多云网络互联`功能

    在顶部`基本设置`区域，点击`启用`状态的滑块，将弹出关闭多云互联的前提条件：

    ![关闭互联](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-closeinterconn.png)

    先移除网络分组：

    ![创建](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-closedoublecheck.png)

    在文本框输入`关闭基本设置`进行确认后，即可关闭多云互联功能：

    ![创建](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/ci-closed.png)

    !!! note

        - 关闭网络互联后，由于跨集群的服务地址信息已被缓存，会存在一定的生效延迟，一般在 1-2 分钟之内；特殊服务需手工重启网格组件才会生效
