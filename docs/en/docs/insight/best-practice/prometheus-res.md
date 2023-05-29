# Prometheus resource planning

In the actual use of Prometheus, affected by the number of cluster containers and the opening of Istio,
the CPU, memory and other resource usage of Prometheus will exceed the set resources.

In order to ensure the normal operation of Prometheus in clusters of different sizes,
it is necessary to adjust the resources of Prometheus according to the actual size of the cluster.

## Reference Resource Planning

In the case that the mesh is not enabled, the test statistics show that the relationship
between the system Job index and Pod is: **Series number = 800\*Pod number**

When the service mesh is enabled, the magnitude of the Istio-related metrics generated
by the Pod after the function is enabled is: **Series number = 768\*Pod number**

### When the service mesh is not enabled

The following resource planning is recommended by Prometheus when the service mesh is not enabled:

| Cluster size (number of Pods) | Metrics (service mesh is not enabled) | CPU (core) | Memory (GB) |
| ---------------- | ---------------------- | --------- --------------- | ---------------------------- |
| 100 | 8w | Request: 0.5<br>Limit: 1 | Request: 2GB<br>Limit: 4GB |
| 200 | 16w | Request: 1<br>Limit: 1.5 | Request: 3GB<br>Limit: 6GB |
| 300 | 24w | Request: 1<br>Limit: 2 | Request: 3GB<br>Limit: 6GB |
| 400 | 32w | Request: 1<br>Limit: 2 | Request: 4GB<br>Limit: 8GB |
| 500 | 40w | Request: 1.5<br>Limit: 3 | Request: 5GB<br>Limit: 10GB |
| 800 | 64w | Request: 2<br>Limit: 4 | Request: 8GB<br>Limit: 16GB |
| 1000 | 80w | Request: 2.5<br>Limit: 5 | Request: 9GB<br>Limit: 18GB |
| 2000 | 160w | Request: 3.5<br>Limit: 7 | Request: 20GB<br>Limit: 40GB |
| 3000 | 240w | Request: 4<br>Limit: 8 | Request: 33GB<br>Limit: 66GB |

### When the service mesh function is enabled

The following resource planning is recommended by Prometheus in the scenario of **starting the service mesh**:

| Cluster size (Pod number) | metric volume (service mesh enabled) | CPU (core) | Memory (GB) |
| ---------------- | ---------------------- | --------- -------------- | ----------------------------- |
| 100 | 15w | Request: 1<br>Limit: 2 | Request: 3GB<br>Limit: 6GB |
| 200 | 31w | Request: 2<br>Limit: 3 | Request: 5GB<br>Limit: 10GB |
| 300 | 46w | Request: 2<br>Limit: 4 | Request: 6GB<br>Limit: 12GB |
| 400 | 62w | Request: 2<br>Limit: 4 | Request: 8GB<br>Limit: 16GB |
| 500 | 78w | Request: 3<br>Limit: 6 | Request: 10GB<br>Limit: 20GB |
| 800 | 125w | Request: 4<br>Limit: 8 | Request: 15GB<br>Limit: 30GB |
| 1000 | 156w | Request: 5<br>Limit: 10 | Request: 18GB<br>Limit: 36GB |
| 2000 | 312w | Request: 7<br>Limit: 14 | Request: 40GB<br>Limit: 80GB |
| 3000 | 468w | Request: 8<br>Limit: 16 | Request: 65GB<br>Limit: 130GB |

!!! note

    1. The number of Pods in the table refers to the number of Pods that are basically running stably in the cluster.
        If a large number of Pods are restarted, the index will increase sharply in a short period of time.
        At this time, resources need to be adjusted accordingly.
    2. Prometheus stores two hours of data by default in memory, and when the 
        [Remote Write function](https://prometheus.io/docs/practices/remote_write/#memory-usage) is enabled in the cluster,
        a certain amount of memory will be occupied, and resources surge ratio is recommended to be set to 2.
    3. The data in the table are recommended values, applicable to general situations.
        If the environment has precise resource requirements, it is recommended to check the resource usage of
        the corresponding Prometheus after the cluster has been running for a period of time for precise configuration.
