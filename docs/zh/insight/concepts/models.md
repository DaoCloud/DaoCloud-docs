# 数据模型

Insight 基本上将所有数据存储为[时间序列](https://en.wikipedia.org/wiki/Time_series)。
为同一指标和同一组标签维度的值加上时间戳形成数据流。除了存储的时间序列，Insight 还可以为查询生成临时的时间序列结果。

## 指标名称和标签

每个时间序列数据通过**指标名称**和**标签**键值对进行唯一的标识。

**指标名称** 指定了监测系统的常规功能（例如 `http_requests_total`- 收到的 HTTP 请求总数）。
指标名称可以包含 ASCII 字母和数字以及下划线和英文冒号。它必须与正则表达式`[a-zA-Z_:][a-zA-Z0-9_:]*`匹配。

!!! note

    英文冒号保留用于用户自定义的规则。不能用于 exporter 或 direct instrumentation。

Insight 采用标签实现多维度数据模型。相同指标名称的任何给定标签组合可以标识特定维度的指标（例如：所有使用 `POST` 方法到 `/api/tracks` 句柄的 HTTP 请求）。
这种查询语言允许根据这些维度进行过滤和聚合。更改任何标签值（包括添加或删除标签）将创建新的时间序列数据。

标签名称可以包含 ASCII 字母、数字以及下划线。必须与正则表达式 `[a-zA-Z\u][a-zA-Z0-9\u]*` 匹配。以 `__` 开头的标签名称保留供内部使用。

标签值可以包含任何 Unicode 字符。

标签值为空被视为等同于标签不存在。

## 样本

样本构成实际的时间序列数据。每个样品包括：

- float64 值

- 毫秒精度的时间戳

## 标记法

给定指标名称和一组标签，时间序列数据通常使用以下标记法进行标识：

```none
<metric name>{<label name>=<label value>, ...}
```

例如，指标名称为 `api_http_requests_total` 且标签为 `method="POST"` 和 `handler="/messages"` 的时间序列数据可以写为：

```none
api_http_requests_total{method="POST", handler="/messages"}
```

这与 [OpenTSDB](http://opentsdb.net/) 使用的标记法相同。
