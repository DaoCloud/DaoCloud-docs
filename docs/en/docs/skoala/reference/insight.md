# Observability

## Jobs and Instances

In Insight, the endpoints from which sample values are collected are referred to as instances. Multiple instances of the same type are replicated to form a job for performance scaling. For example, the "api-server" job has four identical instances:

```css
job: api-server
instance 1: 1.2.3.4:5670
instance 2: 1.2.3.4:5671
instance 3: 5.6.7.8:5670
instance 4: 5.6.7.8:5671
```

After collecting sample values, Insight automatically adds the following labels and values to the samples:

- job: the job to which the sample belongs
- instance: the source instance of the sample

Additionally, during each collection, Insight automatically inserts sample values into the following time series:

- `up{job="[job-name]", instance="instance-id"}`: a sample value of 1 indicates that the instance is healthy; otherwise, it is considered unhealthy.
- `scrape_duration_seconds{job="[job-name]", instance="[instance-id]"}`: the sample value represents the time taken for the current collection.
- `scrape_samples_post_metric_relabeling{job="<job-name>", instance="<instance-id>"}`: the sample value represents the number of samples after relabeling.
- `scrape_samples_scraped{job="<job-name>", instance="<instance-id>"}`: the sample value represents the number of samples collected during the current collection.

## PromQL Query Language

Insight comes with a powerful data query language called PromQL. Insight is a database composed of time series, where all data stored in Insight is organized in sequences of timestamps and values, known as vectors. Being a NoSQL database, it is well-suited for handling large amounts of data writes compared to relational databases like MySQL. Based on recent tests, a single instance of Insight can handle hundreds of thousands of data points per second when sufficient hardware resources are available. Each data collection results in a sample, which consists of three parts:

- Metrics: It includes the metric name and labels.
- Timestamp: The current time at which the sample is taken, accurate to milliseconds.
- Value: It is a float64 floating-point value representing the sample.

PromQL enables querying and aggregation of monitoring data. It is also used for data visualization (via Grafana) and alerting. PromQL allows you to easily answer questions such as:

- The distribution range of the 95th percentile application latency over a certain period of time.
- Predicting the approximate disk space usage after 4 hours.
- The top 5 services with the highest CPU utilization.

## Data Model

Insight essentially stores all data as [time series](https://en.wikipedia.org/wiki/Time_series). A data stream is formed by adding timestamps to the values of the same metric and label dimensions. In addition to storing time series, Insight can generate temporary time series results for queries.

- Metric Name and Labels

    Each time series data is uniquely identified by a combination of the **metric name** and **labels** key-value pairs.

- Metric Name
  
    Specifies the general functionality of the monitoring system (e.g., `http_requests_total` - the total number of received HTTP requests). The metric name can contain ASCII letters, numbers, underscores, and colons. It must match the regular expression `[a-zA-Z_:][a-zA-Z0-9_:]*`.

    !!! note

        The colon character is reserved for user-defined rules and cannot be used for exporters or direct instrumentation.

Insight uses labels to implement a multidimensional data model. Any given combination of labels for the same metric name can identify metrics for specific dimensions (e.g., all HTTP requests that use the `POST` method to the `/api/tracks` endpoint). This query language allows filtering and aggregation based on these dimensions. Changing any label value (including adding or removing labels) will create new time series data.

Label names can contain ASCII letters, numbers, and underscores. They must match the regular expression `[a-zA-Z\u][a-zA-Z0-9\u]*`. Label names starting with `__` are reserved for internal use.

Label values can contain any Unicode characters.

An empty label value is considered equivalent to the label not existing.

- Samples

    Samples constitute actual time series data. Each sample includes a float64 value and a timestamp with millisecond precision.

- Notation

    Time series data is typically identified using the following notation, given the metric name and a set of labels:

    ```none
    <metric name>{<label name>=<label value>, ...}
    ```

    For example, a time series data with a metric name of `api_http_requests_total` and labels `method="POST"` and `handler="/messages"` can be written as:

    ```none
    api_http_requests_total{method="POST", handler="/messages"}
    ```

    This notation is similar to the one used by [OpenTSDB](http://opentsdb.net/).

## Metric Types

Insight has several types of metrics:

- Counter

    A counter is an accumulating metric that can only be incremented. Counters are primarily used for counting events such as service requests, task completions, or occurrences of errors.

- Gauge

    A gauge is a metric that can both increase and decrease. Gauges are used to measure instantaneous values such as temperature or memory usage.

- Histogram

    A histogram samples observations (usually data like request durations or response sizes) and counts them in configurable buckets. There are several ways to generate a histogram (assuming the metric name is `<basename>`):

    - By bucket count, represented as `<basename>_bucket{le="<upper inclusive bound>"}`
    - By sum of observed values, represented as `<basename>_sum`
    - By count of observed values, represented as `<basename>_count`, which is also equivalent to counting all observed values in a single bucket `<basename>_bucket{le="+Inf"}`

    Histograms can be understood as bar charts and are typically used for data such as request durations or response sizes. They allow sampling, grouping, and statistical analysis of observations.

- Summary

    Similar to histograms, summaries sample observations. In addition to summing observed values and counting them, summaries can also provide statistics based on quantiles. There are several ways to generate a summary (assuming the metric name is `<basename>`):

    - By quantile, representing the percentage of observed values smaller than the quantile, represented as `<basename>{quantile="<φ>"}`
    - By sum of observed values, represented as `<basename>_sum`
    - By count of observed values, represented as `<basename>_count`
