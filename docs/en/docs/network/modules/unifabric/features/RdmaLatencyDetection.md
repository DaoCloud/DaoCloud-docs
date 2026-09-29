# RDMA Latency Monitoring Guide

## Background

### What Is RDMA Latency Monitoring

RDMA latency monitoring is a network performance monitoring feature provided by Unifabric. It
continuously monitors the latency performance of the RDMA network in a Kubernetes cluster. By
automatically running RDMA latency tests between cluster nodes, it helps operators:

- **Detect network performance issues early:** Continuously monitor latency changes and quickly
  identify network performance degradation.
- **Validate network topology:** Verify that the network topology is configured correctly through
  latency tests.
- **Locate faulty nodes:** Pinpoint the nodes and NICs that show abnormal latency.
- **Optimize network configuration:** Provide data support for network optimization.

### How It Works

The unifabric-agent on each node contains a standalone `rdma-latency` container, which is
responsible for:

1. **Starting the RDMA test server:** Starting the `ib_write_lat` and `ib_read_lat` server
   processes on each RDMA NIC.
2. **Generating test tasks:** Automatically generating latency test tasks between nodes based on
   the configured policy (`none`/`topo`).
3. **Running latency tests:** Acting as a client to connect to the server on other nodes and
   running RDMA Write/Read latency tests.
4. **Exporting monitoring metrics:** Exposing test results in Prometheus metric format for
   collection by the monitoring system.

### Key Features

- **Automated testing:** Automatically generates test tasks based on ScaleoutLeafGroup topology
  information.
- **Multiple test policies:** Supports the `none` (simple pairing) and `topo` (topology-based)
  policies.
- **Full coverage:** Covers multiple network paths such as intra-group same-rail, intra-group
  cross-rail, and cross-group same-rail.
- **Bidirectional testing:** Tests both RDMA Write and RDMA Read latency.
- **Prometheus integration:** Test results are exposed as Prometheus metrics for easy monitoring
  and alerting.
- **Continuous monitoring:** Runs tests periodically to detect performance degradation in time.

## Test Plan

### Test Policy Overview

RDMA latency monitoring supports two test policies:

| Policy   | Applicable scenario                     | Prerequisites                                                     | Test complexity |
| -------- | --------------------------------------- | ----------------------------------------------------------------- | --------------- |
| **none** | Small clusters, simple network topology | None                                                              | Low             |
| **topo** | Large clusters, fine-grained monitoring | Requires the RDMA neighbor discovery feature (ScaleoutLeafGroup resource) | High       |

### None Policy (Simple Pairing)

#### Test Logic

- Sort all nodes in lexicographical order.
- Pair nodes for testing (0-1, 2-3, 4-5...).
- If the total number of nodes is odd:
    - 3 nodes: node 0 tests nodes 1 and 2.
    - More than 3 nodes: the first node additionally tests the last node.

#### Client and Server Roles

Under the `none` policy, within each node pair:

- **Server:** The node that comes later in lexicographical order (for example, node-2, node-4).
- **Client:** The node that comes earlier in lexicographical order (for example, node-1, node-3).

#### Example (4 Nodes)

```
Client node-1 -> Server node-2 (tests all RDMA NIC pairs on the same subnet)
Client node-3 -> Server node-4 (tests all RDMA NIC pairs on the same subnet)
```

### Topo Policy (Topology-Based)

#### Prerequisites

The `ScaleoutLeafGroup` resource must exist in the cluster. This resource is created automatically
through LLDP neighbor discovery and defines the grouping and topology relationship of nodes.

#### Test Scenarios

The `topo` policy contains three test scenarios covering different network paths:

##### Scenario 1: Intra-Group Same-Rail Test

**Test goal:** Verify the latency between nodes on the same subnet (rail) under the same Leaf
switch.

**Rail definition:** NICs with the same IP subnet belong to the same rail, or NICs with the same
name belong to the same rail.

- For example: the 172.17.3.0/24 subnet is rail 1, and the 172.17.4.0/24 subnet is rail 2.

**Test scope:** All nodes in the group are paired with each other to test NICs on the same rail.

**Client and server:**

- Each node acts as both client and server.
- Node A acts as the client to test node B.
- Node B acts as the client to test node A.

**Network path:** Traffic passes through the same Leaf switch.

**Example:**

```
ScaleoutLeafGroup: group-1 (connected to Leaf-1)
  Nodes: node-1, node-2, node-3, node-4

Test pairs (rail 1: 172.17.3.0/24):
  Client node-1 (172.17.3.141) -> Server node-2 (172.17.3.142)
  Client node-3 (172.17.3.143) -> Server node-4 (172.17.3.144)
```

**Metric label:** `latency_type="sameleaf_samerail"`

##### Scenario 2: Intra-Group Cross-Rail Test

**Test goal:** Verify the latency between nodes on different subnets (rails) under the same Leaf
switch.

**Test scope:** For each group, select the first and the last node in lexicographical order for
cross-rail testing.

**Client and server:**

- **Client:** The first node (for example, node-1).
- **Server:** The last node (for example, node-4).

**Network path:** Traffic may pass through the Spine switch (depending on the Leaf switch
configuration).

**Example:**

```
ScaleoutLeafGroup: group-1
  Nodes: node-1, node-2, node-3, node-4

Test pairs (cross-rail):
  Client node-1 (rail 1: 172.17.1.141) -> Server node-4 (rail 2: 172.17.2.144)
  Client node-1 (rail 1: 172.17.1.141) -> Server node-4 (rail 3: 172.17.3.144)
  Client node-1 (rail 1: 172.17.1.141) -> Server node-4 (rail 4: 172.17.4.144)
  Client node-1 (rail 2: 172.17.2.142) -> Server node-4 (rail 1: 172.17.1.144)
  Client node-1 (rail 2: 172.17.2.142) -> Server node-4 (rail 3: 172.17.3.144)
  Client node-1 (rail 2: 172.17.2.142) -> Server node-4 (rail 4: 172.17.4.144)
  ...
```

**Metric label:** `latency_type="sameleaf_crossrail"`

##### Scenario 3: Cross-Group Same-Rail Test

**Test goal:** Verify the latency between nodes on the same subnet (rail) across different Leaf
switches.

**Prerequisites:** At least 2 ScaleoutLeafGroups.

**Test scope:** Select the first node in lexicographical order from each group, and test it
against the first node of the other groups.

**Client and server:**

- The first node in lexicographical order of each group is the client.
- The first node of other groups is the server.
- Nodes in different groups test each other.

**Network path:** Traffic passes through the Spine switch.

**Example:**

```
ScaleoutLeafGroup: group-1 (connected to Leaf-1)
  Nodes: node-1, node-2, node-3, node-4
  Test node: node-1

ScaleoutLeafGroup: group-2 (connected to Leaf-2)
  Nodes: node-5, node-6, node-7, node-8
  Test node: node-5

Test pairs:

Rail 1: 172.17.1.0/24:
  Client node-1 (172.17.1.141) -> Server node-5 (172.17.1.145)
Rail 2: 172.17.2.0/24:
  Client node-1 (172.17.2.142) -> Server node-5 (172.17.2.145)
Rail 3: 172.17.3.0/24:
  Client node-1 (172.17.3.143) -> Server node-5 (172.17.3.145)
Rail 4: 172.17.4.0/24:
  Client node-1 (172.17.4.144) -> Server node-5 (172.17.4.145)
```

**Metric label:** `latency_type="crossgroup_samerail"`

### Monitoring Metric Format

All test results are exposed as Prometheus metrics:

#### Metric Name

```
unifaric_rdma_latency_us
```

#### Metric Type

**Gauge** - the average latency (in microseconds) of the most recent test.

#### Metric Labels

| Label                | Description                          | Example value                                                      |
| -------------------- | ------------------------------------ | ------------------------------------------------------------------ |
| `source_node`        | Source node (client) name            | `node-1`                                                           |
| `source_rdma_device` | Source node RDMA device name         | `mlx5_0`                                                           |
| `source_ifname`      | Source node NIC interface name       | `ens841np0`                                                        |
| `source_ip`          | Source node IP address               | `172.17.3.141`                                                     |
| `target_node`        | Target node (server) name            | `node-2`                                                           |
| `target_rdma_device` | Target node RDMA device name         | `mlx5_0`                                                           |
| `target_ifname`      | Target node NIC interface name       | `ens841np0`                                                        |
| `target_ip`          | Target node IP address               | `172.17.3.142`                                                     |
| `source_group`       | ScaleoutLeafGroup of the source node | `group-1`                                                          |
| `target_group`       | ScaleoutLeafGroup of the target node | `group-1`                                                          |
| `latency_type`       | Latency test type                    | `sameleaf_samerail` / `sameleaf_crossrail` / `crossgroup_samerail` |
| `test_strategy`      | Test policy                          | `pairwise` / `topo`                                                |
| `state`              | Test state                           | `success` / `failed`                                               |
| `error_msg`          | Error message (only on failure)      | `connection timeout`                                               |

#### Metric Examples

**Successful same-rail test:**

```prometheus
unifaric_rdma_latency_us{
  source_node="node-1",
  source_rdma_device="mlx5_0",
  source_ifname="ens841np0",
  source_ip="172.17.3.141",
  target_node="node-2",
  target_rdma_device="mlx5_0",
  target_ifname="ens841np0",
  target_ip="172.17.3.142",
  source_group="group-1",
  target_group="group-1",
  latency_type="sameleaf_samerail",
  test_strategy="topo",
  state="success",
  error_msg=""
} 2.45
```

**Failed cross-rail test:**

```prometheus
unifaric_rdma_latency_us{
  source_node="node-3",
  source_rdma_device="mlx5_0",
  source_ifname="ens841np0",
  source_ip="172.17.3.143",
  target_node="node-4",
  target_rdma_device="mlx5_1",
  target_ifname="ens842np0",
  target_ip="172.17.4.144",
  source_group="group-1",
  target_group="group-1",
  latency_type="sameleaf_crossrail",
  test_strategy="topo",
  state="failed",
  error_msg="connection timeout"
} 0
```

## Configuration and Installation

### Configuration Examples

#### Small-Scale Cluster (`none` Policy)

```yaml
features:
  rdmaLatencyDetection:
    interval: 3m
    workers: 3
    gpuNetwork:
      enabled: true
      strategy: pairwise
    testServerPorts: "20000-20017"
```

#### Large-Scale Cluster (`topo` Policy)

```yaml
features:
  rdmaNeighbor:
    enabled: true
    enableScaleOutLeafGroup: true
    gpuRdmaNicFilter: "interface=ens*"

  rdmaLatencyDetection:
    interval: 5m
    workers: 10
    gpuNetwork:
      enabled: true
      strategy: topo
    testServerPorts: "20000-20017"
```

Helm configuration parameters:

| Parameter                | Type   | Default value   | Description                                                                        |
| ------------------------ | ------ | --------------- | ---------------------------------------------------------------------------------- |
| `interval`               | string | `"5m"`          | Test interval, supports the s/m/h units                                            |
| `workers`                | int    | `5`             | Number of workers that run tests concurrently                                      |
| `gpuNetwork.enabled`     | bool   | `true`          | Whether to enable GPU RDMA network latency detection                               |
| `gpuNetwork.strategy`    | string | `"topo"`        | GPU network test policy: `pairwise` (pairwise pairing) or `topo` (topology-based)   |
| `storageNetwork.enabled` | bool   | `true`          | Whether to enable storage RDMA network latency detection                           |
| `testServerPorts`        | string | `"20000-20010"` | Port range of the RDMA test server                                                 |
| `metrics.port`           | int    | `5027`          | Port that exposes Prometheus metrics                                               |

!!! note

    - If `strategy` is set to `topo`, make sure `features.rdmaNeighbor.enableScaleOutLeafGroup` is
      set to `true`.
    - To start the RDMA latency test server properly, make sure `testServerPorts` reserves a
      sufficient port range and avoids port conflicts. Reserve at least two ports for each RDMA
      NIC: one for `ib_write_lat` and one for `ib_read_lat`. For example, if there are 9 RDMA
      NICs, at least 18 ports are required.

### Installation Steps

#### Install or Upgrade the Helm Chart

```bash
# Or upgrade an existing installation
helm upgrade unifabric ./chart \
  --namespace unifabric-system \
  -f values.yaml
```

> By default, RDMA latency detection is based on the `topo` policy. Make sure
> `features.rdmaNeighbor.enableScaleOutLeafGroup` is set to `true`.

## Verification

### Container Architecture

The unifabric-agent Pod contains **3 containers:**

```
unifabric-agent Pod
├── lldpd (container)         # LLDP neighbor discovery service
├── agent (container)         # Main business logic, manages FabricNode and other resources
└── rdma-latency (container)  # RDMA latency detection service (standalone container)
```

**Responsibilities of the rdma-latency container:**

- Starts the RDMA test servers (`ib_write_lat`, `ib_read_lat`).
- Runs latency test tasks.
- Exposes Prometheus metrics (port 5027).

### Check Pod Status

```bash
# Check Pod status
kubectl get pods -n unifabric-system -l app=unifabric-agent

# Expected output:
NAME                      READY   STATUS    RESTARTS   AGE
unifabric-agent-xxxxx     3/3     Running   0          5m
```

**Note:** The `READY` column should show `3/3`, meaning all 3 containers are ready.

### Check Whether the ScaleoutLeafGroup CRD Is Working

A ScaleoutLeafGroup object represents a group of nodes that share the same GPU network topology.

```bash
~# kubectl get scaleoutleafgroups.unifabric.io
NAME              healthyNodes   totalNodes   healthy   AGE
409bf491f7136a8a  4              4            true      6h1m
```

Check whether `healthy` of the scaleoutleafgroups is `true`. This indicates that Unifabric has
correctly collected the GPU network topology information of all nodes.

### View Metrics

#### Method 1: View Through Port-Forward

```bash
# Forward the metrics port
kubectl port-forward -n unifabric-system <pod-name> 5027:5027

# View metrics in another terminal
curl http://localhost:5027/metrics | grep unifaric_rdma_latency_us
...
unifabric_rdma_latency_us{error_msg="",latency_type="sameleaf_samerail",source_group="409bf491f7136a8a",source_ifname="ens834np0",source_ip="172.17.1.141",source_node="sh-cube-master-1",source_rdma_device="mlx5_4",state="success",target_group="409bf491f7136a8a",target_ifname="ens834np0",target_ip="172.17.1.142",target_node="sh-cube-master-2",target_rdma_device="mlx5_4",test_strategy="topo"} 2.994644
unifabric_rdma_latency_us{error_msg="",latency_type="sameleaf_samerail",source_group="409bf491f7136a8a",source_ifname="ens834np0",source_ip="172.17.1.142",source_node="sh-cube-master-2",source_rdma_device="mlx5_4",state="success",target_group="409bf491f7136a8a",target_ifname="ens834np0",target_ip="172.17.1.141",target_node="sh-cube-master-1",target_rdma_device="mlx5_4",test_strategy="topo"} 5.515484
...
```

The output above shows:

- `unifaric_rdma_latency_us`: the RDMA latency metric is 2.994644 us.
- `error_msg`: error message (only on failure).
- `latency_type`: test type.
- `source_group`: source node group.
- `source_ifname`: source NIC interface name.
- `source_ip`: source node IP.
- `source_node`: source node name.
- `source_rdma_device`: source RDMA device name.
- `state`: test state.
- `target_group`: target node group.
- `target_ifname`: target NIC interface name.
- `target_ip`: target node IP.
- `target_node`: target node name.
- `target_rdma_device`: target RDMA device name.
- `test_strategy`: test policy.
- `latency_type`: test type.

#### Method 2: View Through Prometheus

Run the following queries in the Prometheus UI:

```promql
# View all metrics
unifaric_rdma_latency_us

# View successful tests
unifaric_rdma_latency_us{state="success"}

# View failed tests
unifaric_rdma_latency_us{state="failed"}
```

### Verify Same-Rail Metrics

**Same-rail test** metric characteristics:

- `latency_type="sameleaf_samerail"`.
- `source_ip` and `target_ip` are on the same subnet.
- The latency value is usually low (< 5 microseconds).

```promql
# Query same-rail tests
unifaric_rdma_latency_us{latency_type="sameleaf_samerail", state="success"}
```

**Example output:**

```
unifaric_rdma_latency_us{
  source_node="node-1",
  source_ip="172.17.3.141",
  target_node="node-2",
  target_ip="172.17.3.142",
  latency_type="sameleaf_samerail",
  state="success"
} 2.3
```

### Verify Cross-Rail Metrics

**Cross-rail test** metric characteristics:

- `latency_type="sameleaf_crossrail"`.
- `source_ip` and `target_ip` are on different subnets.
- The latency value is usually higher (5-15 microseconds).

```promql
# Query cross-rail tests
unifaric_rdma_latency_us{latency_type="sameleaf_crossrail", state="success"}
```

**Example output:**

```
unifaric_rdma_latency_us{
  source_node="node-3",
  source_ip="172.17.3.143",
  target_node="node-4",
  target_ip="172.17.4.144",
  latency_type="sameleaf_crossrail",
  state="success"
} 8.7
```

## Troubleshooting

### PromQL Query Examples

1. View all successful latency tests

    ```promql
    unifaric_rdma_latency_us{state="success"}
    ```

1. View the latency of a specific node

    ```promql
    unifaric_rdma_latency_us{source_node="node-1", state="success"}
    ```

1. View intra-group same-rail latency

    ```promql
    unifaric_rdma_latency_us{latency_type="sameleaf_samerail", state="success"}
    ```

1. View cross-rail latency (may be higher)

    ```promql
    unifaric_rdma_latency_us{latency_type="sameleaf_crossrail", state="success"}
    ```

1. View failed tests

    ```promql
    unifaric_rdma_latency_us{state="failed"}
    ```

1. Calculate the average latency

    ```promql
    avg(unifabric_rdma_latency_us{state="success", latency_type="sameleaf_samerail"})
    ```

1. Find paths with abnormally high latency (>10 microseconds)

    ```promql
    unifaric_rdma_latency_us{state="success"} > 10
    ```

### The Container Fails to Start

#### Symptoms

```bash
kubectl get pods -n unifabric-system -l app=unifabric-agent
# Output shows: READY 2/3 or CrashLoopBackOff
```

#### Troubleshooting Steps

**Step 1: Check the container status**

```bash
# View Pod details
kubectl describe pod -n unifabric-system <pod-name>

# View the logs of the rdma-latency container
kubectl logs -n unifabric-system <pod-name> -c rdmalatency --tail=100
```

**Step 2: Common errors and solutions**

##### Error 1: Port conflict

**Error message:**

```
failed to start RDMA test servers: failed to start server on mlx5_0:
address already in use
```

**Cause:** The configured port range conflicts with other services.

**Solution:**

```yaml
# Modify values.yaml and adjust the port range
features:
  rdmaLatencyDetection:
    testServerPorts: "21000-22000" # Use a different port range
```

```bash
# Update the configuration
helm upgrade unifabric ./chart -n unifabric-system -f values.yaml
```

##### Error 2: The RDMA device does not exist

**Error message:**

```
failed to start RDMA test servers: no RDMA devices found
```

**Cause:** The node has no RDMA NIC or the NIC is not properly recognized.

**Troubleshooting:**

```bash
# Check the RDMA devices on the node
kubectl exec -n unifabric-system <pod-name> -c rdmalatency -- ibv_devices

# Check the FabricNode resource
kubectl get fabricnode <node-name> -o yaml | grep -A 20 gpuNics
```

##### Error 3: Insufficient permissions

**Error message:**

```
failed to start RDMA test servers: permission denied
```

**Cause:** The Pod does not have sufficient permissions to access the RDMA devices.

**Solution:** Make sure the DaemonSet is configured with `hostNetwork: true` and an appropriate
securityContext.

### Adjust the Log Level

If you need more detailed logs for troubleshooting:

```yaml
# Modify values.yaml
agent:
  config:
    logLevel: 7 # 0=info, 3=debug, 7=trace
```

```bash
# Update the configuration
helm upgrade unifabric ./chart -n unifabric-system -f values.yaml

# View detailed logs
kubectl logs -n unifabric-system <pod-name> -c rdma-latency -f
```

### No Metrics Are Generated

**Possible causes:**

1. RDMA latency detection is not enabled.
2. No RDMA NIC is found.
3. The `topo` policy is used but no ScaleoutLeafGroup exists.

**Troubleshooting steps:**

```bash
# 1. Check the configuration
kubectl get cm -n unifabric-system unifabric -o yaml

# 2. Check whether FabricNode contains RDMA NIC information
kubectl get fabricnode <node-name> -o yaml

# 3. View the logs and check whether the Metrics Server started properly
kubectl logs -n unifabric-system daemonset/unifabric-agent -c rdmalatency
```

### Metrics Show Failed Tests (state=failed)

#### Symptoms

```promql
unifaric_rdma_latency_us{state="failed"} > 0
```

#### Troubleshooting Steps

**Step 1: View the error message**

```promql
# View the error_msg label of failed metrics
unifaric_rdma_latency_us{state="failed"}
```

**Common error messages:**

##### Error 1: connection timeout

**Cause:** The server on the target node is not started, or the network is unreachable.

**Troubleshooting:**

```bash
# 1. Check the status of the rdma-latency container on the target node
kubectl get pods -n unifabric-system -l app=unifabric-agent -o wide | grep <target-node>

# 2. Check the server process on the target node
kubectl exec -n unifabric-system <target-pod-name> -c rdma-latency -- \
  ps aux | grep ib_write_lat

# 3. Check port listening
kubectl exec -n unifabric-system <target-pod-name> -c rdma-latency -- \
  netstat -tlnp | grep 20000

# 4. Manually test the RDMA connection
kubectl exec -n unifabric-system <source-pod-name> -c rdma-latency -- \
  ib_write_lat -d mlx5_0 -p 20000 <target-ip>
```

##### Error 2: no route to host

**Cause:** The network is unreachable or blocked by a firewall.

**Troubleshooting:**

```bash
# 1. Test network connectivity
kubectl exec -n unifabric-system <source-pod-name> -c rdma-latency -- \
  ping -c 3 <target-ip>

# 2. Check firewall rules
kubectl exec -n unifabric-system <source-pod-name> -c rdma-latency -- \
  iptables -L -n | grep 20000

# 3. Check the route
kubectl exec -n unifabric-system <source-pod-name> -c rdma-latency -- \
  ip route get <target-ip>
```
