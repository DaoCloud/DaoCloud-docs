# vmstorage disk capacity planning

vmstorage is responsible for storing multicluster metrics for observability.
In order to ensure the stability of vmstorage, it is necessary to adjust the disk capacity
of vmstorage according to the number of clusters and the size of the cluster.
For more information, please refer to [vmstorage retention period and disk space](https://docs.victoriametrics.com/guides/understand-your-setup-size.html?highlight=datapoint#retention-perioddisk-space).

## Test Results

After 14 days of disk observation of vmstorage of clusters of different sizes,
We found that the disk usage of vmstorage was positively correlated with the
amount of metrics it stored and the disk usage of individual data points.

1. The amount of metrics stored instantaneously `increase(vm_rows{ type != "indexdb"}[30s])`
    to obtain the increased amount of metrics within 30s
2. Disk usage of a single data point: `sum(vm_data_size_bytes{type!="indexdb"}) / sum(vm_rows{type != "indexdb"})`

## calculation method

**Disk usage** = Instantaneous metrics x 2 x disk usage for a single data point x 60 x 24 x storage time (days)

**Parameter Description:**

1. The unit of disk usage is `Byte`.
2. `Storage duration (days) x 60 x 24` converts time (days) into minutes to calculate disk usage.
3. The default collection time of Prometheus in Insight Agent is 30s, so twice the amount of metrics
    will be generated within 1 minute.
4. The default storage duration in vmstorage is 1 month, please refer to
    [Modify System Configuration](../../user-guide/system-config/modify-config.md) to modify the configuration.

!!! warning

     This formula is a general solution, and it is recommended to reserve redundant disk
     capacity on the calculation result to ensure the normal operation of vmstorage.

## reference capacity

The data in the table is calculated based on the default storage time of one month (30 days),
and the disk usage of a single data point (datapoint) is calculated as 0.9.
In a multicluster scenario, the number of Pods represents the sum of the number of Pods in the multicluster.

### When the service mesh is not enabled

| Cluster size (number of Pods) | Metrics | Disk capacity |
| ----------------- | ------ | -------- |
| 100 | 8W | 6 GiB |
| 200 | 16W | 12 GiB |
| 300 | 24w | 18 GiB |
| 400 | 32w | 24 GiB |
| 500 | 40w | 30 GiB |
| 800 | 64w | 48 GiB |
| 1000 | 80W | 60 GiB |
| 2000 | 160w | 120 GiB |
| 3000 | 240w | 180 GiB |

### When the service mesh is enabled

| Cluster size (number of Pods) | Metrics | Disk capacity |
| ----------------- | ------ | -------- |
| 100 | 15W | 12 GiB |
| 200 | 31w | 24 GiB |
| 300 | 46w | 36 GiB |
| 400 | 62w | 48 GiB |
| 500 | 78w | 60 GiB |
| 800 | 125w | 94 GiB |
| 1000 | 156w | 120 GiB |
| 2000 | 312w | 235 GiB |
| 3000 | 468w | 350 GiB |

### Example

There are two clusters in the DCE 5.0 platform, of which 500 Pods are running in the global management cluster
(service mesh is turned on), and 1000 Pods are running in the working cluster (service mesh is not turned on), and the expected metrics are stored for 30 days.

- The number of metrics in the global management cluster is 800x500 + 768x500 = 784000
- Worker cluster metrics are 800x1000 = 800000

Then the current vmstorage disk usage should be set to (784000+80000)x2x0.9x60x24x31 =124384896000 byte = 116 GiB

!!! note

    For the relationship between the number of metrics and the number of Pods in the cluster,
    please refer to [Prometheus Resource Planning](./prometheus-res.md).
