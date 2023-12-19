# 可观测性

## 任务和实例

在 Insight 里，可以从中抓取采样值的端点称为实例（Instance），为了性能扩展而复制出来的多个这样的实例形成了一个任务（Job）。例如，下面的 api-server 任务有四个相同的实例：

```css
job: api-server
instance 1: 1.2.3.4:5670
instance 2: 1.2.3.4:5671
instance 3: 5.6.7.8:5670
istance 4: 5.6.7.8:5671
```
  
Insight 抓取完采样值后，会自动给采样值添加下面的标签和值：

- job: 抓取所属任务
- instance: 抓取来源实例

另外每次抓取时，Insight 还会自动在以下时序里插入采样值：

- `up{job="[job-name]", instance="instance-id"}`：采样值为 1 表示实例健康，否则为不健康
- `scrape_duration_seconds{job="[job-name]", instance="[instance-id]"}`：采样值为本次抓取消耗时间
- `scrape_samples_post_metric_relabeling{job="<job-name>", instance="<instance-id>"}`：采样值为重新打标签后的采样值个数
- `scrape_samples_scraped{job="<job-name>", instance="<instance-id>"}`：采样值为本次抓取到的采样值个数

## 查询语言 PromQL

Insight 内置了一个强大的数据查询语言 PromQL。
Insight 是一个时间序列构成的数据库，所有保存在 Insight 里的数据都是按时间戳和值的序列顺序存放的，称为 Vector（向量）），因为是 NoSQL，相比关系型数据库 MySQL 能很好地支持大量数据写入。
从最新测试结果看，在硬件资源充足地情况下，Insight 单实例每秒可采集数十万条。每一次数据采集得到一个 Sample（样本），其由三部分组成：

- Metrics（指标）：包含了 Metrics name 以及 Labels。
- Timestamp（时间戳）：当前采样的时间，精确到毫秒。
- Value（采样值）：其类型为 float64 浮点数。

通过 PromQL 可以实现对监控数据的查询、聚合。同时 PromQL 也被应用于数据可视化（通过 Grafana）以及告警当中。通过 PromQL 可以轻松回答以下问题：

- 在过去一段时间中 95% 应用延迟时间的分布范围
- 预测在 4 小时后，磁盘空间占用大致会是什么情况
- CPU 占用率前 5 位的服务有哪些

## 数据模型

Insight 基本上将所有数据存储为[时间序列](https://en.wikipedia.org/wiki/Time_series)。
为同一指标和同一组标签维度的值加上时间戳形成数据流。除了存储的时间序列，Insight 还可以为查询生成临时的时间序列结果。

- 指标名称和标签

    每个时间序列数据通过 **指标名称** 和 **标签** 键值对进行唯一的标识。

- 指标名称
  
    指定了监测系统的常规功能（例如 `http_requests_total`- 收到的 HTTP 请求总数）。指标名称可以包含 ASCII 字母和数字以及下划线和英文冒号。它必须与正则表达式`[a-zA-Z_:][a-zA-Z0-9_:]*`匹配。

    !!! note

        英文冒号保留用于用户自定义的规则。不能用于 exporter 或 direct instrumentation。

Insight 采用标签实现多维度数据模型。相同指标名称的任何给定标签组合可以标识特定维度的指标（例如：所有使用 `POST` 方法到 `/api/tracks` 句柄的 HTTP 请求）。
这种查询语言允许根据这些维度进行过滤和聚合。更改任何标签值（包括添加或删除标签）将创建新的时间序列数据。

标签名称可以包含 ASCII 字母、数字以及下划线。必须与正则表达式 `[a-zA-Z\u][a-zA-Z0-9\u]*` 匹配。以 `__` 开头的标签名称保留供内部使用。

标签值可以包含任何 Unicode 字符。

标签值为空被视为等同于标签不存在。

- 样本

    样本构成实际的时间序列数据。每个样品包括：float64 值和毫秒精度的时间戳

- 标记法

    给定指标名称和一组标签，时间序列数据通常使用以下标记法进行标识：

    ```none
    <metric name>{<label name>=<label value>, ...}
    ```

    例如，指标名称为 `api_http_requests_total` 且标签为 `method="POST"` 和 `handler="/messages"` 的时间序列数据可以写为：

    ```none
    api_http_requests_total{method="POST", handler="/messages"}
    ```

    这与 [OpenTSDB](http://opentsdb.net/) 使用的标记法相同。

## 指标类型

Insight 的度量指标有以下几种类型。

- 计数器（Counter）

    计数器是一种累计型的度量指标，它是一个 **只能递增** 的数值。计数器主要用于统计类似于服务请求数、任务完成数和错误出现次数这样的数据。

- 计量器（Gauge）

    计量器是一个 **既可增又可减** 的度量指标值。计量器主要用于测量类似于温度、内存使用量这样的瞬时数据。

- 直方图（Histogram）

    直方图对观察结果（通常是请求持续时间或者响应大小这样的数据）进行采样，并在可配置的桶中对其进行统计。有以下几种方式来产生直方图（假设度量指标为 `<basename>`）：

    - 按桶计数，相当于 `<basename>_bucket{le="<upper inclusive bound>"}`
    - 采样值总和，相当于`<basename>_sum`
    - 采样值总数，相当于 `<basename>_count` ，也等同于把所有采样值放到一个桶里来计数 `<basename>_bucket{le="+Inf"}`

    Histogram 可以理解为柱状图，典型的应用如：请求持续时间，响应大小。可以对观察结果采样，分组及统计。

- 汇总（Summary）

    类似于直方图，汇总也对观察结果进行采样。除了可以统计采样值总和和总数，它还能够按分位数统计。有以下几种方式来产生汇总（假设度量指标为 `<basename>`）：

    - 按分位数，也就是采样值小于该分位数的个数占总数的比例小于 φ，相当于 `<basename>{quantile="<φ>"}`
    - 采样值总和，相当于 `<basename>_sum`
    - 采样值总数，相当于 `<basename>_count`
