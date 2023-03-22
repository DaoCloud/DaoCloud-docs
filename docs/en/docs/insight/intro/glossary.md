# Glossary

- Alert

    An alert is the outcome of an alerting rule in Insight that is actively firing. Alerts are sent from Insight to the Alertmanager.

- Alert rules

    Alert rules is a PromQL expression whose return value is a Boolean value. It describes whether the metrics or user-defined metrics are within the threshold range. If not, an alert event will be generated.

- Alertmanager

    Alertmanager takes in alerts, aggregates them into groups, de-duplicates, applies silences, throttles, and then sends out notifications to email, WeChat, Dingding etc.

- Client Library

    A client library is a library in some language (e.g. Go, Java, Python, Ruby) that makes it easy to directly instrument your code, write custom collectors to pull metrics from other systems and expose the metrics to Insight server.

- Collector

    A collector is a part of an exporter that represents a set of metrics. It may be a single metric if it is part of direct instrumentation, or many metrics if it is pulling metrics from another system.

- Dashboard

    Dashboard is a form of visual management, that is, a clear representation of data, intelligence and other conditions. It displays information through a variety of visual perceptions that are intuitive and colorful. You can see the real-time situation on the platform and all performance metrics in DCE.

- Endpoint

    A source of metrics that can be scraped, usually corresponding to a single process.

- Event

    Event is the record information, which records the alert rules, trigger time and the system status. At the same time, corresponding actions will be triggered, such as sending mail.

- Exporter

    An exporter is a binary running alongside the application you want to obtain metrics from. The exporter exposes Insight metrics, commonly by converting metrics that are exposed in a non-Insight format into a format that Insight supports.

- Metrics

    Metrics use  [open-metric](https://openmetrics.io/) format. It is a standard to measure the degree of certain feature in software or hardware systems. The metrics consists of namespace, dimension, indicator name and unit, which  descrips the status and resource performance. More information, refer to[metric type](../../reference/basic-knowledge/insight.md#data-modle)。

- Log

    Log is an abstract data that changes during system operation. Its contents specify an ordered collection of object operations and their results to be sorted by time.

- Trace

    Trace can record the processing information within the scope of a single request, including service calls and processing duration data.

- Instance

    An instance is a label that uniquely identifies a target in a job.
  
- Job

    A collection of targets with the same purpose, for example monitoring a group of like processes replicated for scalability or reliability, is called a job. More information, refer to [job and instance](../../reference/basic-knowledge/insight.md#job and instance)

- Notification

    A notification represents a group of one or more alerts, and is sent by the Alertmanager to email, WeChat, Dingding etc.

- PromQL

    PromQL is the Insight Query Language. It allows for a wide range of operations, including aggregation, slicing and dicing, prediction and joins. More information, refer to[query data](../../reference/basic-knowledge/insight.md#query data-promql)

- Pushgateway

    The Pushgateway persists the most recent push of metrics from batch jobs. This allows Insight  to scrape their metrics after they have terminated.

- Recording Rule

    Recording Rule is named PromQL expression, which is a new metric obtained by calculating multiple indicators, and described more complete and complex system states.

- Sample

    A sample is a single value at a point in time in a time series.In Insight, each sample consists of a float64 value and a millisecond-precision timestamp.

- Service Discovery

    Service Discovery is a configuration for the Kubernetes environment, which is used for batch and automatic access to monitor on Kubernetes.

- Target

    A target is the definition of an object to scrape. For example, what labels to apply, any authentication required to connect, or other information that defines how the scrape will occur.
