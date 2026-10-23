# Deployment Capacity Planning

By default, the observability module has resource limits set to prevent excessive resource consumption. Since the observability system needs to handle large volumes of data, improper capacity planning may result in high system load, affecting stability and reliability.

## Resource Planning for Observability Components

The observability module consists of **Insight** and **Insight Agent**. Among them, Insight is mainly responsible for the storage, analysis, and display of observability data. The Insight Agent includes functions such as data collection, data processing, and data uploading.

### Capacity Planning for Storage Components

The storage components of Insight mainly include Elasticsearch and VictoriaMetrics. Among them, Elasticsearch is mainly responsible for storing and querying log and trace data, and VictoriaMetrics is mainly responsible for storing and querying metrics data.

* **VictoriaMetrics**: Its disk usage is related to the stored metrics. After estimating the capacity according to the [vmstorage disk planning](./vms-res-plan.md), [adjust the vmstorage disk](./modify-vms-disk.md).

### Resource Planning for Collectors

The collector within Insight Agent includes **Prometheus**. Although Prometheus is typically a standalone component, in this case, it is embedded within Insight Agent for data collection. Therefore, it also requires resource planning.

* **Prometheus**: Its resource usage is related to the amount of metrics collected. You can refer to [Prometheus Resource Planning](./prometheus-res.md) for adjustment.

[Download Center](https://docs.daocloud.io/en/download/){ .md-button .md-button--primary }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button .md-button--primary }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button .md-button--primary }
