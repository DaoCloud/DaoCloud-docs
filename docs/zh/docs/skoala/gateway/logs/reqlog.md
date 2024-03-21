---
hide:
  - toc
---

# 请求日志

微服务网关支持查看请求日志和实例日志。本页介绍如何查看实例日志以及查看日志时的相关操作。

## 查看方式

点击目标网关的名称，进入网关概览页面，然后在左侧导航栏点击 __日志查看__ -> __请求日志__ 。

![查看请求日志的路径](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/logs/images/reqlog-path.png)

## 相关操作

- 筛选日志：支持通过 Request ID、请求路径、域名、请求方法、HTTP、GRPC 等条件筛选日志，
  支持按照请求开始时间、请求耗时、请求服务耗时对日志进行排序。

    ![筛选日志](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/logs/images/log-filter1.png)

- 限定时间范围：可选择近 5 分钟、15 分钟、30 分钟的日志，或者自定义时间范围。

    ![限定时间](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/logs/images/logtime1.png)

- 导出日志：支持将日志文件导出到本地。

    ![导出日志](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/logs/images/log-export1.png)
