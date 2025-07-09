# NUMA Affinity Scheduling

A NUMA node is a fundamental unit in a Non-Uniform Memory Access (NUMA) architecture. A Kubernetes Node consists of multiple NUMA nodes. Accessing memory across different NUMA nodes introduces latency. Developers can optimize task scheduling and memory allocation strategies to improve memory access efficiency and overall performance.

## Use Cases

NUMA affinity scheduling is commonly used for compute-intensive jobs sensitive to CPU parameters or scheduling latency, such as scientific computing, video decoding, animation rendering, and big data offline processing.

## Scheduling Policies

Pod scheduling can adopt the following NUMA placement policies. See the Pod scheduling behavior documentation for details on each policy’s effect:

* **single-numa-node**: Pods are scheduled only on nodes whose topology manager policy is set to `single-numa-node`, with CPUs allocated within the same NUMA node. If no node meets this condition, the Pod will not be scheduled.
* **restricted**: Pods are scheduled on nodes with topology manager policy `restricted`, with CPUs allocated within the same set of NUMA nodes. If no node satisfies this, scheduling fails.
* **best-effort**: Pods are scheduled on nodes with topology manager policy `best-effort`, attempting to place CPUs within the same NUMA node if possible. If no node fully meets this, the best available node is chosen.

## Scheduling Principle

When a Pod specifies a topology policy, Volcano filters nodes according to the policy and CPU topology:

1. Filter nodes based on the Pod’s Volcano topology policy.
2. Further filter nodes whose CPU topology meets the policy requirements for scheduling.

| Pod Topology Policy | Step 1: Filter Nodes by Topology Policy | Step 2: CPU Topology Filter and Scheduling Behavior |
| ------------------- | -------------- | -------------- |
| none | All nodes allowed: none, best-effort, restricted, single-numa-node | No CPU topology filtering |
| best-effort | Only nodes with `best-effort` policy allowed | Prefer single NUMA node allocation; if unavailable, allow multiple NUMA nodes to satisfy CPU request |
| restricted | Only nodes with `restricted` policy allowed | Strict: If a single NUMA node has enough CPUs to satisfy the request, allocate within that NUMA node only. If insufficient, Pod is unschedulable. If no single NUMA node fits, multiple NUMA nodes allowed |
| single-numa-node | Only nodes with `single-numa-node` policy allowed | CPU allocation strictly within a single NUMA node |

## Configuring NUMA Affinity Scheduling

1. Set policies in the Job spec:

    ```yaml
    task:
       - replicas: 1
         name: "test-1"
         topologyPolicy: single-numa-node
       - replicas: 1
         name: "test-2"
         topologyPolicy: best-effort
    ```

2. Configure kubelet’s topology manager policy by setting the `--topology-manager-policy` parameter. Supported values are:

    * `none` (default)
    * `best-effort`
    * `restricted`
    * `single-numa-node`

## Usage Examples

1. Example 1: Configure NUMA affinity in a stateless workload.

    ```yaml
    kind: Deployment
    apiVersion: apps/v1
    metadata:
      name: numa-test
    spec:
      replicas: 1
      selector:
        matchLabels:
           app: numa-test
      template:
        metadata:
          labels:
             app: numa-test
         annotations:
            volcano.sh/numa-topology-policy: single-numa-node  # set topology policy
        spec:
          containers:
            - name: container-1
              image: nginx:alpine
              resources:
                requests:
                  cpu: 2           # must be an integer and match limits
                  memory: 2048Mi
                limits:
                  cpu: 2           # must be an integer and match requests
                  memory: 2048Mi
          imagePullSecrets:
          - name: default-secret
    ```

2. Example 2: Create a Volcano Job using NUMA affinity.

    ```yaml
    apiVersion: batch.volcano.sh/v1alpha1
    kind: Job
    metadata:
      name: vj-test
    spec:
      schedulerName: volcano
      minAvailable: 1
      tasks:
        - replicas: 1
          name: "test"
          topologyPolicy: best-effort    # set topology policy
          template:
            spec:
              containers:
                - image: alpine
                  command: ["/bin/sh", "-c", "sleep 1000"]
                  imagePullPolicy: IfNotPresent
                  name: running
                  resources:
                    limits:
                      cpu: 20
                      memory: "100Mi"
              restartPolicy: OnFailure
    ```

### NUMA Scheduling Analysis

Assuming the following NUMA node setup:

| Node | Node Topology Manager Policy | Allocatable CPUs on NUMA node 0 | Allocatable CPUs on NUMA node 1 |
| ------ | --------------- | ------------------------------- | ------------------------------- |
| node-1 | single-numa-node | 16 CPUs | 16 CPUs |
| node-2 | best-effort | 16 CPUs | 16 CPUs |
| node-3 | best-effort | 20 CPUs | 20 CPUs |

* In Example 1, the Pod requests 2 CPUs and sets the policy to `single-numa-node`, so it will be scheduled on `node-1`.
* In Example 2, the Pod requests 20 CPUs and sets the policy to `best-effort`. It will be scheduled on `node-3` because `node-3` can fulfill the CPU request on a single NUMA node, while `node-2` would need to allocate across multiple NUMA nodes.

### Check Current Node CPU Info

Use `lscpu` to view CPU and NUMA node information:

```sh
lscpu
...
CPU(s): 32
NUMA node(s): 2
NUMA node0 CPU(s): 0-15
NUMA node1 CPU(s): 16-31
```

### Check Current CPU Allocation

Check CPU allocation on the node:

```sh
cat /var/lib/kubelet/cpu_manager_state
{"policyName":"static","defaultCpuSet":"0,10-15,25-31","entries":{"777870b5-c64f-42f5-9296-688b9dc212ba":{"container-1":"16-24"},"fb15e10a-b6a5-4aaa-8fcd-76c1aa64e6fd":{"container-1":"1-9"}},"checksum":318470969}
```

In this example, two containers are running on the node: one using CPUs 1-9 on NUMA node 0, and the other using CPUs 16-24 on NUMA node 1.
