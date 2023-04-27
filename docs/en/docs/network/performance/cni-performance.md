---
MTPE: TODO
Revised: Jeanine-tw
Pics: TODO
Date: 2023-03-29
---

# Network CNI Performance Test Report

This test report covers the performance testing of Cilium, Calico and Macvlan CNIs.

## Test Background

### Test Environment

|Model|CPU|Memory|NIC|System|Node IP|
|--|--|--|--|--|--|--|--|
|Dell PowerEdge R620|Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz * 2|4G 1333M * 4|Mellanox cx5 Physical NIC Bandwidth|Ubuntu 22.04|10.20.0.11|
|Dell PowerEdge R620|Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz * 2|4G 1333M * 4|Mellanox cx5|Ubuntu 22.04|10.20.0.12|

### Testing CNI Types

This test covers three main types of CNI: Cilium, Calico and Macvlan, and is based on the following model:

- Cilium
    - cilium (vxlan mode)
- Calico
    - calico (vxlan mode)
    - calico (underlay mode)
    - callico (ipip mode)
- Macvlan-Standalone

### Test cases

This test includes the following nine test cases:

- Between nodes
- Between a Pod and the node where the Pod resides
- Between a Pod and a node across nodes
- Between a Pod and a Pod on the same node
- Between a Pod and a Pod across nodes
- Node and Service communicate and the Endpoint corresponding to the Service is on this node
- Node and Service communicate and the Endpoint corresponding to the Service is on other nodes
- Pod and Service communicate, the Endpoint corresponding to the Service is on the same node as this Pod
- Pod and Service communicate, Service corresponding Endpoint and this Pod are on different nodes

### Test Metrics

- Pod throughput (between Pod and node)
- Service throughput (between Service and node)
- Latency - long connection (between Pod and node)
- Latency - short connection (between Pod and node)

### Testing tools and commands

This test uses the netperf tool for performance testing, and the test commands for different metrics are as follows

- Throughput

    ```shell
    netperf -t TCP_STREAM -H <serverIP> -p <serverPort> -l 60 -- -m 1024
    iperf3 -c <serverIP> -i 1 -t 60
    ```

- Time delay - long connection

    ```shell
    netperf -t TCP_RR -H <serverIP> -p <serverPort> -l 60 -- -r 1024 -O "MIN_LATENCY,MAX_LATENCY,P50_LATENCY,P90_LATENCY,P99_LATENCY,MEAN_LATENCY. STDDEV_LATENCY"
    ```

- Time delay - short link

    ```shell
    netperf -t TCP_CRR -H <serverIP> -p <serverPort> -l 60 -- -r 1024 -O "MIN_LATENCY,MAX_LATENCY,P50_LATENCY,P90_LATENCY,P99_LATENCY,MEAN_LATENCY. STDDEV_LATENCY"
    ```

## Test results

For the four test metrics, the test results for different CNI patterns in different test cases are shown below:

### Chart Conclusion

- Pod Throughput

    

    |test cases|conclusions|
    |----|----|
    |Pod and node, located on the same node| macvlan-standalone has the highest throughput, cilium vxlan has the lowest|
    |Pod and node, located on different nodes|caico-ipip, calico-underlay and macvlan-standalone have better performance, calico-vxlan, cilium-vxlan have worse|
    |Between Pod and Pod, located on the same node|macvlan has the best performance, cilium is second, calico has similar performance in all three modes, and all have worse performance|
    |Between Pod and Pod, on different nodes|macvlan is the best, cilium-vxlan is the second best, calico is worse|

- Service Throughput

    Service throughput 
    |test cases|conclusions|
    |----|----|
    |service and node, located in the same node|macvlan performance is the best, cilium second, calico three modes are similar, performance is worse|
    |Between Service and Node, located on different nodes|macvlan, calico-ipip, calico-underlay, cilium-vxlan have similar performance, calico-vxlan is worse|
    |Between Service and Pod, located on the same node|macvlan has the best performance, cilium is second, calico has similar performance in all three modes, and all have worse performance|
    |Between Service and Pod, on different nodes|macvlan and cilium perform better, calico worse|

- Pod long latency

    

    |test cases|conclusions|
    |----|----|
    |Pod and node, located at the same node|The five CNI modes perform similarly, with the lowest macvlan latency|
    |Pod and node, located on different nodes|macvlan has the best performance, cilium-vxlan is the second best, and calico-vxlan has the highest latency|
    |Pod and Pod, located on the same node|macvlan has the best performance, cilium is second, and calico has similar performance across all three modes, with relatively poor performance|
    |Between Pod and Pod, on different nodes|macvlan has the best performance, calico-underlay has the second best performance, and calico-vxlan has the worst performance|

- Pod short links

    

    |test cases|conclusions|
    |----|----|
    |Pod and node, located at the same node|The five cni modes do not differ much, macvlan and calico-underlay latency is the smallest|
    |Pod and node, located on different nodes|macvlan has the best performance, cilium-vxlan is second, and calico-vxlan has the highest latency|
    |Pod and Pod, located on the same node|macvlan has the best performance, cilium is second, and calico has similar performance across all three modes, with relatively poor performance|
    |Pod and Pod, located on different nodes|macvlan has the best performance, calico-underlay the second best, and calico-vxlan the worst|

### Detailed data

- Pod-related throughput (Gbits/sec)

    |test cases|cilium(vxlan)|calico(vxlan)|calico(ipip)|calico(underlay)|macvlan-standalone|sriov-standalone|
    |--|----|--|----|----|----|----|----|----|
    |-inter-node|9.16|9.16| 9.16| 9.16| 9.16| 9.16| 9.16|
    |Pod and node, located at the same node| 12.6| 13.8| 14.23| 14.2| 16.4| 15.8|
    |Pod and node, located at different nodes| 3.02| 1.57| 8.24| 9.2| 9.15| 9.09|
    |Pod and Pod at the same node| 15.3| 10.2| 10.33| 10.27| 22.2| 14.1|
    |Pod and Pod on different nodes| 8.30| 1.37| 4.51| 3.89| 9.18| 9.21|

- Service related throughput (Gbits/sec)

    |test cases|cilium(vxlan)|calico(vxlan)|calico(ipip)|calico(underlay)|macvlan-standalone|sriov-standalone|
    |--|----|--|----|----|----|----|----|
    |-Service and node, located on the same node| 8.30| 12| 11.77| 12.07| 16.6| 15.8|
    |Service and node, located on different nodes| 7.41| 1.23| 8.57| 9.037| 9.14| 9.10|
    |Service and Pod on the same node| 15.8| 10.2| 10| 10.17| 20.2| 15.6|
    |between Service and Pod on different nodes| 8.27| 1.3| 4.81| 3.49| 9.15| 16.3|

- netpref Time delay (long connection) (Microseconds)

    |test cases|cilium(vxlan)|calico(vxlan)|calico(ipip)|calico(underlay)|macvlan-standalone|sriov-standalone|
    |--|----|--|----|----|----|----|----|----|
    |internode| 113.27| 113.27| 113.27| 113.27| 113.27| 113.27| 113.27| 113.27|
    |Pod and node, located at the same node| 76.76| 76.81| 74.55| 62.27| 61.25| 74.34|
    |Pod and node, located at different nodes| 150.26| 241.46| 225.68| 170.23| 95.76| 109.77|
    |Pod and Pod, located at the same node| 65.62| 104.82| 91.44| 103.71| 45.47| 66.74|
    |Pod and Pod, on different nodes| 201.27| 275.22| 248.72| 195.61| 81.74| 78.83|

- netpref Time delay (short connection) (Microseconds)

    |test cases|cilium(vxlan)|calico(vxlan)|calico(ipip)|calico(underlay)|macvlan-standalone|sriov-standalone|
    |--|----|--|----|----|----|----|----|----|
    |-inter-node| 439.04| 439.04| 439.04| 439.04| 439.04| 439.04| 439.04|
    |Pod and node, located at the same node| 259.92| 230.65| 226.26| 203.63 |187.41 |225.66|
    |Pod and node, located at different nodes| 613.59| 803.80| 767.08| 587.53| 358.48| 413.77|
    |Pod and Pod, on the same node| 198.99| 982.92| 265.07| 277.75| 127.48| 275.52|
    |Pod and Pod, on different nodes| 789.32|
