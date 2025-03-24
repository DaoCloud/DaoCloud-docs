# Deployment Capacity Planning

By default, the observability module has resource limits set to prevent excessive resource consumption. Since the observability system needs to handle large volumes of data, improper capacity planning may result in high system load, affecting stability and reliability.

## Resource Planning for Observability Components

The observability module consists of **Insight** and **Insight Agent**.  
- **Insight** is mainly responsible for the storage, analysis, and visualization of observability data.  
- **Insight Agent** handles data collection, processing, and uploading.

### Capacity Planning for Storage Components

The storage components of Insight primarily include **Elasticsearch** and **VictoriaMetrics**:  
- **Elasticsearch** is mainly used for storing and querying log and trace data.  
- **VictoriaMetrics** is used for storing and querying metrics data.  

> **VictoriaMetrics**: Disk usage is related to the volume of stored metrics. After estimating capacity according to the [vmstorage disk planning guide](./vms-res-plan.md), adjust the [vmstorage disk size accordingly](./modify-vms-disk.md).

### Resource Planning for Collectors

The collector within Insight Agent includes **Prometheus**. Although Prometheus is typically a standalone component, in this case, it is embedded within Insight Agent for data collection. Therefore, it also requires resource planning.

> **Prometheus**: Resource consumption depends on the volume of metrics collected. You can refer to the [Prometheus resource planning guide](./prometheus-res.md) for adjustment recommendations.
