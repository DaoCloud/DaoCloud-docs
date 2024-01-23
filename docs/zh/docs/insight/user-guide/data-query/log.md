# 日志查询

Insight 默认采集节点日志、容器日志以及 kubernetes 审计日志。在日志查询页面中，可查询登录账号权限内的标准输出 (stdout) 日志，包括节点日志、产品日志、Kubenetes 审计日志等，快速在大量日志中查询到所需的日志，同时结合日志的来源信息和上下文原始数据辅助定位问题。

## 操作步骤

1. 点击一级导航栏进入 __可观测性__ 。
2. 左侧导航栏中，选择 __日志__ 。

    - 默认查询最近 24 小时；
    - 第一次进入时，默认根据登录账号权限查询有权限的集群或命名空间的容器日志；
  
    ![log](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/log00.png)

3. 顶部 Tab 默认进入 __普通查询__ 。

    1. 点击 __筛选__ 展开过滤面板，可切换日志搜索条件和类型。
    2. 日志类型：

        - __容器日志__ ：记录集群中容器内部的活动和事件，包括应用程序的输出、错误消息、警告和调试信息等。支持通过集群、命名空间、容器组、容器过滤日志。
        - __节点日志__ ：记录集群中每个节点的系统级别日志。这些日志包含节点的操作系统、内核、服务和组件的相关信息。支持通过集群、节点、文件路径过滤日志。

    3. 支持对单个关键字进行模糊搜索。

        ![log](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/log03.png)

4. 顶部切换 Tab 选择 __Lucene 语法查询__ 。

    第一次进入时，默认选择登录账号权限查询有权限的集群或命名空间的容器日志。

    ![log](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/log01.png)

    **Lucene 语法说明：**

    1. 使用 逻辑操作符（AND、OR、NOT、"" ）符查询多个关键字，例如：keyword1 AND (keyword2 OR keyword3) NOT keyword4。
    2. 使用波浪号 (~) 实现模糊查询，在 "~" 后可指定可选的参数，用于控制模糊查询的相似度，不指定则默认使用 0.5。例如：error~。
    3. 使用通配符 (*、?) 用作单字符通配符，表示匹配任意一个字符。
    4. 使用方括号 [ ] 或花括号 { } 来查询范围，方括号 [ ] 表示闭区间，包含边界值。花括号 { } 表示开区间，排除边界值。范围查询只适用于能够进行排序的字段类型，如数字、日期等。例如：timestamp:[2022-01-01 TO 2022-01-31]。
    5. 更多用法请查看：[Lucene 语法说明](../../faq/lucene.md)。

### 其他操作

#### 查看日志上下文

点击日志后的按钮，在右侧划出面板中可查看该条日志的默认 100 条上下文。可切换 __显示行数__ 查看更多上下文内容。

![log](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/logcontext.png)

#### 导出日志数据

点击列表右上侧的下载按钮。

- 支持配置导出的日志字段，根据日志类型可配置的字段不同，其中 __日志内容__ 字段为必选。
- 支持将日志查询结果导出为 **.txt** 或 **.csv** 格式。

![log](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/logexport.png){ width="500"}
