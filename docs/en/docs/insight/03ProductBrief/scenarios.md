# Application scenarios

## Unified collection and observation of multi-cluster data

**Pain points**

- On-cloud, off-cloud, and multicloud environment systems cannot be managed in a unified manner, and faults must be checked one by one, resulting in low operation and maintenance efficiency and high costs.
- Different data are collected separately, which leads to the inability to correlate and analyze the data, and it is difficult to troubleshoot.

**solution** 

- Supports one-click installation of Helm, supports graphical configuration management, does not limit the release version of Kubernetes, and realizes Insight on Any Kubernetes.
- Observability has one-stop collection and storage of logs, indicators, distributed link tracking, and event logs. Full-stack data observation realizes the integration of data collection, storage, analysis, visualization and alarm.
- Real-time monitoring of resources in various dimensions, including cluster monitoring, node monitoring, workload monitoring, service monitoring, etc.

![Install Collector](../images/scenerio01.png)

## Quick fault location and troubleshooting

**Pain points**

- In a complex microservice architecture, the maintenance cost of monitoring configuration increases, the cost of locating service failures increases, and the effective speed of monitoring faces huge challenges.
- The superposition of microservice architecture in the container environment makes troubleshooting complicated, and it is necessary to avoid judging the root cause based on a single exception for troubleshooting.

**solution**

- Draw a service topology map based on link data to quickly locate abnormal services.
- After an abnormal application is found in the topology map, the root cause of the fault can be clearly seen through one-click drill-down through the call chain.
- Query error logs by associating workloads to quickly resolve faults.

![Install Collector](../images/scenerio02.png)