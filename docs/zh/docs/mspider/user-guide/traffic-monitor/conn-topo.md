# 流量拓扑

DCE 5.0 服务网格提供给了动态流转的流量拓扑功能。

在左侧导航栏中，点击 __流量监控__ -> __流量拓扑__ ，您可以选择 __视图方式__ 、 __命名空间__ 、采集源、时间来查看服务的拓扑关系。

![流量拓扑](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/user-guide/images/topo01.png)

## 显示设置

共有 3 个选项：

- 命名空间边界：按命名空间分区显示服务
- 显示空闲节点
- 开启动画：展示流量流转的动态方向

![显示设置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/user-guide/images/topo02.png)

服务拓扑图支持平移、缩放等操作。

## 图例

点击左下角的 __图例__ 按钮，可以查看当前线条、圆圈、颜色所代表的含义。

![图例](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/user-guide/images/topo03.png)

服务用圆圈表示，圆圈的颜色表示了该服务的健康状态：

- 健康（灰色）：错误率 = 0 并且 延时不超过 100 ms
- 警告（橙色）：0 < 错误率 <= 5% 或 100 ms < 延时 <= 200 ms
- 异常（红色）：错误率 > 5% 或延时 > 200 ms
- 未知（虚线）：未获得任何指标数据

## 服务指标数据信息

点击任意服务，会弹出一个侧边栏，基于协议类型展示服务相关指标：

- HTTP 协议：错误率（%）、请求速率（RPM）、平均延时（ms）
- TCP 协议：连接数（个）、接收吞吐量（B/S）、发送吞吐量（B/S）
- 治理信息：查看治理的虚拟服务、目标服务、网关等

![侧边栏](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/user-guide/images/topo04.png)
