# 实例监控、日志查看与配置参数

## 实例监控

MinIO 内置了 Prometheus 和 Grafana 监控模块。

1. 在实例列表页面中，找到想要查看监控信息的实例，点击该实例的名称。

    ![点击某个名称](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/view01.png)

2. 在左侧导航栏点击 __实例监控__ 。

    ![点击实例监控](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/insight01.png)

    !!! note

        如果提示监控组件异常，请按提示[安装 insight-agent 插件](../../../insight/quickstart/install/install-agent.md)。

3. 查看实例的监控信息。点击红框里的信息符号可查看每个指标的含义说明。

    ![点击实例监控](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/insight02.png)

## 日志查看

通过访问每个 MinIO 的实例详情页面；可以支持查看 MinIO 的日志。

1. 在 MinIO 实例列表中，找到想要查看日志的实例，点击实例名称进入详情页面。

    ![image](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/log01.png)

2. 在左侧菜单栏点击 __日志查看__ 。

    ![image](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/log02.png)

3. 根据需要调整日志查询的时间范围和刷新周期，具体可参考[日志查询](../../../insight/user-guide/data-query/log.md)。

    ![image](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/log04.png)

!!! note "常用操作"

    * 自定义日志查询时间范围：在日志页面右上角可以切换日志的查询时间范围
    * 通过关键字检索日志：在左侧 __搜索框__ 下输入关键字即可查询带有特定内容的日志
    * 查看日志的时间分布情况：通过柱状图查看在某一时间范围内的日志数量
    * 查看日志的上下文：在日志最右侧点击 __查看上下文__  即可
    * 导出日志：在柱状图下方点击 __下载__ 即可

    ![image](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/log03.png)

## 配置参数

MinIO 内置了参数配置 UI 界面。

1. 在 MinIO 实例列表中，找到想要配置参数的 MinIO 实例，点击实例名称。

    ![点击某个名称](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/view01.png)

2. 在左侧导航栏，点击 __配置参数__ 。

    ![点击配置参数](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/view02.png)

3. 打开 __编辑配置__ ，对 MinIO 的各项参数进行添加、删除、修改。

    ![配置参数](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/view03.png)

4. 点击 __保存__ ，会导致 MinIO 重启。

