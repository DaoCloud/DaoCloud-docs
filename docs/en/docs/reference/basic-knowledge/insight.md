# Observability

## Tasks and instances

In Insight, the endpoint from which sampled values ​​can be grabbed is called an instance (Instance), and multiple such instances replicated for performance expansion form a task (Job). For example, the api-server task below has four identical instances:

```css
job: api-server
instance 1: 1.2.3.4:5670
instance 2: 1.2.3.4:5671
instance 3: 5.6.7.8:5670
istance 4: 5.6.7.8:5671
```
  
After Insight grabs the sampled value, it will automatically add the following labels and values ​​to the sampled value:

- job: grab the task to which it belongs
- instance: crawl source instance

In addition, Insight also automatically inserts sampled values ​​at the following timings each time it is captured:

- `up{job="[job-name]", instance="instance-id"}`: The sampling value is 1, which means the instance is healthy, otherwise it is unhealthy
- `scrape_duration_seconds{job="[job-name]", instance="[instance-id]"}`: The sampling value is the time consumed by this crawl
- `scrape_samples_post_metric_relabeling{job="<job-name>", instance="<instance-id>"}`: The sample value is the number of sample values ​​after relabeling
- `scrape_samples_scraped{job="<job-name>", instance="<instance-id>"}`: The sampling value is the number of sampling values ​​captured this time

## Query language PromQL

Insight has built-in a powerful data query language PromQL.
Insight is a database composed of time series. All the data stored in Insight are stored in the order of timestamp and value sequence, called Vector (vector). Because it is NoSQL, it can perform well compared to the relational database MySQL. Supports large amounts of data writing.
According to the latest test results, with sufficient hardware resources, a single instance of Insight can collect hundreds of thousands of records per second. Each data acquisition gets a Sample (sample), which consists of three parts:

- Metrics: Contains Metrics name and Labels.
- Timestamp: The current sampling time, accurate to milliseconds.
- Value (sample value): Its type is float64 floating point number.

The query and aggregation of monitoring data can be realized through PromQL. At the same time, PromQL is also used in data visualization (via Grafana) and alerting. The following questions can be answered easily with PromQL:

- Distribution of 95% app latency over time
- Predict what disk space usage will look like in 4 hours
- What are the top 5 services by CPU utilization

## Data Model

Insight basically stores all data as [time series](https://en.wikipedia.org/wiki/Time_series).
Timestamp values ​​for the same metric and the same set of labeled dimensions to form a stream. In addition to stored time series, Insight can also generate ad hoc time series results for queries.

- Metric name and label

    Each time series data is uniquely identified by key-value pairs of **index name** and **label**.

- metric name
  
    Specifies general capabilities of the monitoring system (e.g. `http_requests_total` - total number of HTTP requests received). Metric names can contain ASCII letters and numbers as well as underscores and colons. It must match the regular expression `[a-zA-Z_:][a-zA-Z0-9_:]*`.

    !!! note

        English colons are reserved for user-defined rules. Cannot be used with exporter or direct instrumentation.

Insight uses tags to implement a multidimensional data model. Any given label combination of the same metric name can identify a metric for a particular dimension (for example: all HTTP requests using the `POST` method to the `/api/tracks` handle).
This query language allows filtering and aggregation based on these dimensions. Changing any label value, including adding or removing labels, will create new time series data.

Tag names can contain ASCII letters, numbers, and underscores. Must match the regular expression `[a-zA-Z\u][a-zA-Z0-9\u]*`. Tag names starting with `__` are reserved for internal use.

Tag values ​​can contain any Unicode characters.

A tag value of null is considered equivalent to no tag being present.

- sample

    The samples constitute the actual time series data. Each sample includes: float64 value and timestamp with millisecond precision

- notation

    Given a metric name and a set of labels, time series data is typically identified using the following notation:

    ```none
    <metric name>{<label name>=<label value>, ...}
    ```

    For example, time series data with metric name `api_http_requests_total` and tags `method="POST"` and `handler="/messages"` can be written as:

    ```none
    api_http_requests_total{method="POST", handler="/messages"}
    ```

    This is the same notation used by [OpenTSDB](http://opentsdb.net/).

## metric type

Insight has the following types of metrics.

- Counter

    A counter is a cumulative metric that is a value that can only be incremented. Counters are mainly used to count data such as the number of service requests, the number of task completions, and the number of errors.

- Gauge

    A gauge is a metric value that can both increase and decrease. Meters are mainly used to measure instantaneous data like temperature, memory usage, etc.

- Histogram

    A histogram samples observations (typically data like request duration or response size) and counts them in configurable buckets. There are several ways to generate a histogram (assuming the metric is `<basename>`):

    - Count by bucket, equivalent to `<basename>_bucket{le="<upper inclusive bound>"}`
    - The sum of sampled values, equivalent to `<basename>_sum`
    - The total number of sampled values, which is equivalent to `<basename>_count`, and is also equivalent to putting all sampled values ​​in a bucket to count `<basename>_bucket{le="+Inf"}`

    Histogram can be understood as a histogram, typical applications such as: request duration, response size. Observations can be sampled, grouped and counted.

- Summary

    Similar to histograms, summaries also sample observations. In addition to counting the sum and total of sampled values, it can also count by quantile. There are several ways to generate summaries (assuming the metric is `<basename>`):

    - By quantile, that is, the proportion of the number of sampled values ​​​​less than the quantile to the total is less than φ, which is equivalent to `<basename>{quantile="<φ>"}`
    - the sum of samples, equivalent to `<basename>_sum`
    - total number of sampled values, equivalent to `<basename>_count`