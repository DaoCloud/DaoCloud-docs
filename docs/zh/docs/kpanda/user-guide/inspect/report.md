---
hide:
  - toc
---

# 查看巡检报告

[巡检执行](inspect.md)完成后，可以查看巡检记录和详细的巡检报告。

## 前提条件

- 已经[创建了巡检配置](config.md)
- 已经[执行过至少一次巡检](inspect.md)

## 操作步骤

1. 进入集群巡检页面，点击目标巡检集群的名称。

    ![start](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/inspect07.png)

2. 点击想要查看的巡检记录名称。

    - 每执行一次巡检，就会生成一条巡检记录。
    - 当巡检记录超过[巡检配置](config.md)中设置的最大保留条数时，从执行时间最早的记录开始删除。

        ![start](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/inspect08.png)

3. 查看巡检的详细信息，根据巡检配置可能包括集群资源概览、系统组件的运行情况等。
  
    在页面右上角可以下载巡检报告或删除该项巡检报告。

    ![start](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/inspect09.png)
