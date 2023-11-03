# Effectively improve resource utilization and let idle computing power run

> Author of this article: Product Manager of Cloud Native Research Institute [Stella](https://github.com/Stella0621)

![Improve resource utilization](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/640.png)

## Resource Utilization Status

According to Gartner's latest forecast: "In 2023, global enterprise spending on cloud services is expected to grow by 20.7% to $600 billion,
This is higher than the US$490 billion and 18.8% growth forecast in 2022, and the PaaS growth rate will reach 23.2%.
By 2025, more than 85% of enterprises will adopt the principle of prioritizing the cloud. "
At the same time, many businesses stated that “the full execution of a digital strategy will not be possible without cloud native technologies.”

For enterprises that have embraced cloud native, cloud technology has created substantial value for them.
Since most modern enterprises want to build applications that are highly scalable, elastic, and flexible,
And it can quickly update and iterate to meet the needs of itself and customers. At present, no technology can help enterprises achieve these goals like cloud technology.
Especially in terms of improving resource utilization and saving costs, cloud native has been ranked first for many years, and has become the best path for enterprises to reduce costs and increase efficiency.

However, as the scale of many enterprises continues to expand and the volume of business continues to grow, the problems of high cost of cloud infrastructure services and low resource utilization are becoming more and more prominent.
Not all computing resources can be fully utilized, and wasteful spending on the cloud is still a headache for many enterprises.
According to Flexera's State of the Cloud 2022 report:
“Optimizing existing cloud usage has been the top issue for surveyed organizations for the sixth year in a row, with cloud spending projected to increase by 29%, with an estimated 32% of cloud spending going to waste.”
In addition, the China Academy of Communications pointed out in a white paper on cloud native cost management published last year: "Kubernetes resources are reserved too much, and more than 50% of them are generally wasted."
In the past 2022 North American KubeCon conference, "cost" was also mentioned as many as 15 times. Although cloud native is excellent in improving enterprise resource utilization,
But there is still a lot of room for improvement. Therefore, no matter in the past or now, how to further help enterprises to effectively improve resource utilization and give full play to the value of going to the cloud is the unshirkable responsibility of cloud native practitioners.

## How to optimize resources

What resources are being wasted?

In order to optimize resources, it is necessary to identify which businesses allocate excess resources.
Resource usage is usually measured by metrics such as CPU, memory, disk, and incoming and outgoing bandwidth.
General public cloud or private cloud vendors will provide ready-made solutions for the collection and viewing of these metrics.

By viewing historical metrics, you can quickly understand the actual utilization rate and periodicity of resources. On this basis, fine-grained resource utilization optimization can be carried out.

### 1. Reasonably set Request and Limit

![Request and Limit](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/usage01.png)

When creating a Pod in Kubernetes, you can specify the container's request for CPU and memory resources (request), as well as the resource limit (limit).
The Request field represents the minimum resource requirement of the Pod, and each Kubernetes node can allocate a certain amount of CPU and memory to the Pod.
The scheduler will only consider those nodes that have not allocated resources and satisfied the Pod's requested amount when scheduling. If the amount of unallocated resources of the node is less than the resource request amount of the Pod,
Then the scheduler will not schedule the Pod on this node.

In practice, a cluster may be used by multiple teams. In order to cope with the peak hours of traffic and ensure the service quality of their workloads, each team must
Usually, more resources are applied for the Pod, that is, the Request is set larger. In this way, the difference between the Request and the actual use will be wasted,
And the resources with this difference cannot be used by other workloads. Therefore, in order to meet the resource needs of all teams, more nodes need to be added to the cluster.
At the same time, more nodes also bring more waste of resources.

Therefore, it is very important to properly set the Request and Limit values for the container to optimize resource utilization, and setting the Request and Limit of the Pod is also an art.
The workload of the application, the size of the cluster, and other factors need to be considered. In order to properly set resource requests and limits for Pods, it is recommended to consider the following:

1. The container workload and resource requirements running in the Pod. If the container has a high workload, more CPU and memory are required.

2. The resource limits set for Pods should be large enough so that containers can use resources as needed. If the resource limit is set too small, the container may be killed prematurely.

3. The resource request set for the Pod should be as close as possible to the actual resource requirements of the container to help Kubernetes make scheduling decisions.
    If the resource request is too high, the Pod may not be scheduled to the node; if it is too low, the resources on the node may be wasted.

To determine resource requests and limits for Pods, use Kubernetes resource monitoring tools such as the kubectl top command or Prometheus and Grafana.
These tools can help enterprises understand the resource usage of pods and nodes, and adjust resource requests and limits according to actual needs.

In addition, you can also use the auto-scaling feature to dynamically adjust the number of replicas according to the resource usage of Pods, which can ensure that the resources in the cluster are effectively used.

### 2. Automatic expansion and contraction

Kubernetes provides three automatic expansion and contraction methods by default, namely:

- Horizontal Pod Autoscaler (HPA): Horizontal automatic expansion and contraction
- Vertical Pod Autoscaler (VPA): vertical automatic scaling
- Cluster Autoscaler (CA): automatic expansion and contraction of cluster nodes

#### HPA

HPA is an auto-scaling feature that dynamically adjusts the number of Pod replicas based on actual load.
HPA regularly monitors the resource usage of Pods in Deployment, ReplicationController, ReplicaSet or StatefulSet,
Dynamically adjust the number of replicas according to the set rules. For example, you can set that when the CPU usage exceeds 80%, HPA will increase the number of copies;
When CPU usage falls below 50%, HPA reduces the number of replicas.

HPA can effectively improve the resource utilization of Pods in Deployment, ReplicationController, ReplicaSet, or StatefulSet.

#### VPA

Unlike HPA, VPA means that more resources (for example: memory or CPU) are allocated to running Pods.
VPA monitors the resource usage of Pods and automatically adjusts the resource requests and limits of containers according to the set target usage.
For example, if the Pod's CPU usage is low, the VPA reduces the container's CPU requests and limits;
If the Pod's CPU usage is high, VPA increases the container's CPU requests and limits.

Using VPA has the following advantages:

- Pod resources are used as needed to improve the efficiency of cluster nodes
- It is not necessary to run benchmark tasks to determine appropriate values for CPU and memory requests
- VPA can adjust CPU and memory requests at any time without manual operation, thus reducing maintenance time.

It should be noted that: VPA is not yet ready for production, and you need to understand the impact of resource adjustment on applications before using it.

#### CA

CA is also an automatic scaling feature in Kubernetes, which can dynamically adjust the number of nodes according to the resource usage of the cluster.
CA monitors the resource usage of the cluster and automatically adjusts the number of nodes according to the set threshold.
For example, if the CPU usage of the cluster exceeds a threshold, the CA will increase the number of nodes;
If the CPU usage of the cluster falls below a threshold, the CA reduces the number of nodes.
CA can effectively improve the resource utilization of Kubernetes cluster.
When the resource usage of the cluster changes, CA can automatically adjust the number of nodes so that the cluster can better utilize the available resources.

#### Summary

By using elastic expansion and contraction, the business can automatically adjust server resources and use resources efficiently through the high and low peaks of daily requests.
This is also the essential ability of going to the cloud. In addition, in containers, elastic expansion and contraction are generally divided into container layer and node node layer. When changes in business load trigger expansion and contraction of the container layer,
The expansion and contraction of the container will change the amount of allocatable resources of the node cluster, and the expansion and contraction of the node node will occur.
Not only does it not need to apply for too many resources in advance to launch the business, but the redundant resources applied for can also be used on demand.

### 3. Off-peak scheduling

Kubernetes staggered peak scheduling is a policy that can be implemented by setting a Pod scheduling policy to control the number of jobs that run at the same time.
The goal is to avoid running a large number of jobs when the system load is too high, and to allow more jobs to run during times when the system load is lower.
This approach makes efficient use of computing resources and balances the load among the nodes in the cluster.
You can use the Kubernetes scheduler or a third-party scheduler to implement off-peak scheduling. Peak shift scheduling is usually used in the following cases:

- Run more jobs during times of low system load to improve resource utilization.
- Avoid running a large number of jobs when the system load is too high, so as not to cause system paralysis.
- Balance the load among the nodes in the cluster to improve system reliability.

As an example, suppose you have a scheduled job that runs once a day, starting at 8:00 AM.
If you use a staggered scheduling policy, you can adjust the start time of the job so that it starts running at 6:00 or 10:00 a.m.
And not at 8am. In this way, the problem of excessive system load caused by running a large number of jobs at 8 o'clock in the morning can be avoided.
These Pods are scheduled during times when the cluster's resource usage is low, thereby reducing the cluster's resource usage peaks.

### 4. Online and offline mixing

Hybrid deployment of online and offline services refers to running offline and online services simultaneously in a Kubernetes cluster:

- Online business: business that requires real-time processing, such as websites, games, mobile applications, etc. This type of business usually has lower latency requirements, but higher resource requirements.
- Offline business: business that does not require real-time processing, such as batch jobs, data analysis, and backup. This type of business usually consumes more resources, but can allow longer delays.

For example, a company may have a website that provides online shopping and shipping services. This service has high requirements on stability,
Because the fluency of an online website is related to the user experience. To ensure the availability and responsiveness of the website,
Such services have a higher QoS level during deployment and enjoy higher priority when allocating resources.
At the same time, the resource utilization rate of the website is directly proportional to the website traffic, with a peak during the day and a low peak at night, which has obvious traffic tidal characteristics.

At the same time, the company may need to regularly back up its customer database and analyze the sales data of the past year to determine the next marketing strategy.
To achieve this goal, companies can use a Kubernetes cluster to run two offline business jobs:
One for data backup and one for data analysis. The data backup job can be run once every morning,
Backup customer database data to cloud storage. A data analysis job can be run every weekend to analyze sales data for the past year and generate a report.

It can be seen that the traffic of online services is periodic, sensitive to delay, low in resource usage, and has high requirements on stability, service resources and load;
Offline jobs can usually tolerate high latency, and failed tasks can be restarted. These two types of service loads have great room for optimization in terms of time-segmented use and complementary resources.
For example, you can set lower resource requests and limits for offline services, and use lower priority scheduling policies.
In this way, when the online business needs resources, the offline business will automatically give up the resources. Through hybrid deployment of offline services,
It can effectively utilize the resources in the cluster while ensuring the availability and response speed of online services.

## Summarize

Kubernetes can improve resource utilization in several ways. By setting resource requests and limits for Pods, using auto-scaling, staggered peak scheduling strategies, and hybrid deployment techniques,
It can effectively optimize the computing resources of the Kubernetes cluster, better meet business needs and save costs.
Of course, in practical applications, we can also perform more optimizations according to specific business cases.
In general, to improve the resource utilization of Kubernetes, it is only necessary to conduct a comprehensive analysis of the running mode and resource usage of the application.
And using appropriate tools and methods to improve resource utilization can make the Kubernetes cluster run more efficiently.

[Download DCE 5.0](../download/index.md){ .md-button .md-button--primary }
[Install DCE5.0](../install/index.md){ .md-button .md-button--primary }
[Free Trial](../dce/license0.md){ .md-button .md-button--primary }
