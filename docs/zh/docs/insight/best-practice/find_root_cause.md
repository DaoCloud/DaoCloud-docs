# 使用 Insight 定位应用异常

本文将以 DCE 5.0 中举例，讲解如何通过 Insight 发现 DCE 5.0 中异常的组件并分析出组件异常的根因。

本文假设你已经了解 Insight 的产品功能或愿景。

## 拓扑图 —— 从宏观察觉异常

随着企业对微服务架构的实践，企业中的服务数量可能会面临着数量多、调用复杂的情况，开发或运维人员很难理清服务之间的关系，因此，我们提供了拓扑图监控的功能，我们可以通过拓扑图对当前系统中运行的微服务状况进行初步诊断。

如下图所示，我们通过拓扑图发现其中 __Insight-Server__ 这个节点的颜色为 __红色__ ，并将鼠标移到该节点上，发现该节点的错误率为 __2.11%__ 。因此，我们希望查看更多细节去找到造成该服务错误率不为 __0__ 的原因:

![01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/find_root_cause/01.png)

当然，我们也可以点击最顶部的服务名，进入到该服务的总览界面：

![02](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/find_root_cause/02.png)

## 服务总览 —— 具体分析的开始

当你需要根据服务的入口和出口流量分别分析的时候，你可以在右上角进行筛选切换，筛选数据之后，我们发现该服务有很多 __操作__ 对应的错误率都不为 0. 此时，我们可以通过点击 __查看链路__ 对该 __操作__ 在这段时间产生的并记录下来的链路进行分析：

![03](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/find_root_cause/03.png)

![04](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/find_root_cause/04.png)

## 链路详情 —— 找到错误根因，消灭它们

在链路列表中，我们可以通过界面直观地发现链路列表中存在着 __错误__ 的链路（上图中红框圈起来的），我们可以点击错误的链路查看链路详情，如下图所示：

![05](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/find_root_cause/05.png)

在链路图中我们也可以一眼就发现链路的最后一条数据是处于 __错误__ 状态，将其右边 __Logs__ 展开，我们定位到了造成这次请求错误的原因：

![06](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/find_root_cause/06.png)

根据上面的分析方法，我们也可以定位到其他 __操作__ 错误的链路：

![07](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/find_root_cause/07.png)
![08](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/find_root_cause/08.png)
![09](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/find_root_cause/09.png)

## 接下来 —— 你来分析！
