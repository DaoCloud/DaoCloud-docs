# 流量拓扑

在左侧导航栏中点击`流量拓扑`打开页面，该功能展示了网格下所有服务的拓扑关系。用户可以选择`视图方式`及`命名空间`对服务节点进行筛选展示。

![流量拓扑](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/monitor-topo.png)

## 显示设置

`命名空间边界`设置是否显示命名空间边界线框，选中将把同一命名空间下服务用边框框起，并标明命名空间名称.

![显示设置](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/monitor-displayConfig.png)

## 服务指标数据信息

点击任意服务，会弹出侧边栏基于协议类型分别展示服务相关指标：

- HTTP 服务：请求速率（RPM）、错误率（%）、平均时延（ms）

- TCP 服务：连接数（个）、接收吞吐量（B/S）、发送吞吐量（B/S）

![侧边栏信息](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/monitor-data.png)

## 健康状态

健康状态用于体现服务和连接的状态信息，分为正常、警告、异常和未知，通过比对错误率和延时指标数据判断。

- 正常（灰色）：错误率 = 0 并且 延时不超过 100 ms

- 警告（橙色）：0 < 错误率 <= 5% 或 100 ms < 延时 <= 200 ms

- 异常（红色）：错误率 > 5% 或延时 > 200 ms

- 未知（虚线）：未获得任何指标数据
