# Topology-Aware Scheduling for Training Jobs

In the fields of artificial intelligence and machine learning, model training jobs—such as distributed training for large language models (LLMs)—place extremely high demands on compute resources and network performance. These jobs often involve frequent communication between multiple Pods, such as gradient aggregation and data exchange, where network latency and bandwidth utilization directly impact training efficiency.

In modern data centers, complex network topologies (e.g., nodes, racks, zones) make the physical placement of Pods critical to communication performance. The default Kubernetes scheduler primarily allocates resources based on CPU and memory, lacking awareness of network topology. This can result in Pods being scheduled across distant nodes, increasing communication overhead and extending training time.

**Kueue** is a native Kubernetes job queueing system that optimizes resource allocation for batch jobs through quotas and queue mechanisms. **Baize**, leveraging its **Topology-Aware Scheduling (TAS)** capability, utilizes data center topology information to intelligently schedule Pods onto network-proximate nodes. This minimizes network hops and improves communication throughput. TAS is particularly suitable for model training scenarios, as it significantly reduces network latency in distributed training, accelerates gradient synchronization and data transfer, and provides efficient and reliable scheduling support for AI/ML workloads.

This article explains how to use topology-aware scheduling with detailed steps below:

### 1. Manually Create a Topology CR

As mentioned earlier, data center organizational units are hierarchical, and Pods running within the same unit enjoy better network bandwidth than those running across different units.

We can represent the hierarchy of nodes in the data center using node labels. Nodes at the same level can form a **super node**, which represents a **network topology performance domain**. Multiple super nodes are connected hierarchically to form a tree structure.

Currently, Baize does not support creating node topologies via UI, so users must manually create the Topology Custom Resource (CR) in a GPU cluster.

Sample YAML:

```yaml
apiVersion: kueue.x-k8s.io/v1alpha1
kind: Topology
metadata:
  name: default
spec:
  levels:
    - nodeLabel: shanghai-cube/super-node # A super node represents a network performance domain. Multiple super nodes form a tree structure.

---
apiVersion: kueue.x-k8s.io/v1beta1
kind: ResourceFlavor
metadata:
  name: tas-flavor
spec:
  nodeLabels:
    metax-tech.com/driver.ready: 'true'
  topologyName: default
```

### 2. Create a Resource Pool

Follow the steps in [Creating a Resource Pool](../oam/resource/create.md). Select the target nodes and the previously created node topology.

<!-- ![Create Resource Pool](../best-practice/images/train-with-tas-02.png) -->

### 3. Create a Queue

Follow the steps in [Creating a Queue](../oam/queue/create.md). Choose the resource pool created in the previous step.

<!-- ![Create Queue](../best-practice/images/train-with-tas-03.png) -->

### 4. Create a Training Job

With the TAS configuration in place, you can now create a training job using a PodTemplate that includes TAS settings. Refer to [Creating a Training Job](../developer/jobs/create.md) for guidance.

The queue specified in the training job references a resource pool with topology information. Based on the TAS configuration, scheduling is automated. Scheduling all related Pods within the same topology domain is a **preference**, not a **requirement**. By default, TAS matches the lowest level in the topology; if a `PodSet` cannot be scheduled within a given topology domain, the scheduler will attempt the next higher level.

With these steps completed, you have successfully configured topology-aware scheduling for your training job.
