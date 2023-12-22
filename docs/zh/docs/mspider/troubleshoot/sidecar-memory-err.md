# 边车占用大量内存

造成这种问题的情况有几种：

### 情况 1

未开启边车发现范围的命名空间隔离功能。sidecar缓存了网格所有服务的信息，当网格集群规模较大，服务发现规则较多，就会占用大量内存，建议开启，在创建网格时或网格概览-编辑边车信息里面选择。针对跨命名空间访问的情况，在边车管理-命名空间，对单个命名空间进行配置。

    ![边车发现范围](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/sidecar-find-flag-01.png)

    ![边车发现范围](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/sidecar-find-flag-02.png)

### 情况 2

经过边车的流量规模较大，请求延迟高，响应体文本大，都会占用更多的内存，可以通过监控拓扑查看确认情况。

    ![边车发现范围](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/mspider-topology-01.png)

### 情况3

边车内存泄漏。通过监控组件查看，比如dce5组件insight等，若集群规模流量未变化，边车内存占用不断上升，则可能是内存泄漏，联系我们以定位问题。

    ![内存占用查看](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/sidecar-memory-query-01.png)