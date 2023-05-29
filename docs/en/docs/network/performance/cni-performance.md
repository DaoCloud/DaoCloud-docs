---
MTPE: Jeanine-tw
Revised: Jeanine-tw
Pics: TODO
Done: 2023-05-17
---

# CNI Performance Test Report

This test report covers the performance testing of CNIs including Cilium, Calico and Macvlan.

## Test background

### Test environment

|Model|CPU|Memory|NIC|System|Node IP|
|--|--|--|--|--|--|--|--|
|Dell PowerEdge R620|Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz * 2|4G 1333M * 4|Mellanox cx5 Physical NIC Bandwidth|Ubuntu 22.04|10.20.0.11|
|Dell PowerEdge R620|Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz * 2|4G 1333M * 4|Mellanox cx5|Ubuntu 22.04|10.20.0.12|

### Tested CNI types

This test covers three CNIs including Cilium, Calico and Macvlanis and is based on the following models:

- Cilium
    - cilium (vxlan mode)
- Calico
    - calico (vxlan mode)
    - calico (underlay mode)
    - callico (ipip mode)
- Macvlan-Standalone

### Test cases

This test includes the following nine Test cases:

- Node to node
- Pod to node where the Pod resides
- Pod to node across nodes
- Pod to Pod on the same node
- Pod to Pod across nodes
- Node to Service, and the Endpoint corresponding to the Service is on this node
- Node to Service, and the Endpoint corresponding to the Service is on other nodes
- Pod to Service, the Endpoint corresponding to the Service is on the same node as this Pod
- Pod to Service, and Service corresponding Endpoint and this Pod are on different nodes

### Test metrics

- Pod throughput (Pod to node)
- Service throughput (Service to node)
- Latency - long connection (Pod to node)
- Latency - short connection (Pod to node)

### Testing tools and commands

This test uses the netperf tool for performance testing, and the test commands for different metrics are as follows:

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

- Pod throughput

    |Test cases|Conclusions|
    |----|----|
    |Pod to node（the same node）| Macvlan-standalone has the highest throughput, while cilium vxlan has the lowest|
    |Pod to node（different nodes）|Calico-ipip, calico-underlay and Macvlan-standalone outperform than calico-vxlan and cilium-vxlan|
    |Pod to Pod（the same node）|Macvlan outperforms cilium, and calico has similarly worse performance in all three modes|
    |Pod to Pod（different nodes）|Macvlan is the best, followed by cilium-vxlan and then calico|

- Service throughput

    |Test cases|Conclusions|
    |----|----|
    |Service to node, both  on the same node|Macvlan is the best and followed by cilium, and calico has similarly worse performance in three modes|
    |Service to node, both  on different nodes|Macvlan, calico-ipip, calico-underlay, cilium-vxlan have similar performance, and calico-vxlan is the worst|
    |Service to Pod, both  on the same node|Macvlan has the best performance and is followed by cilium.  Calico has similarly worse performance in all three modes|
    |Service to Pod（different nodes）|Both macvlan and cilium perform better than calico|

- Pod latency


    |Test cases|Conclusions|
    |----|----|
    |Pod to node（the same node）|The five CNI modes perform similarly, with the lowest macvlan latency|
    |Pod to node（different nodes）|Macvlan has the best performance, cilium-vxlan is the second best, and calico-vxlan has the highest latency|
    |Pod to Pod（the same node）|Macvlan outperforms cilium, and calico has similarly worse performance in all three modes|
    |Pod to Pod（different nodes）|Macvlan has the best performance, followed by calico-underlay and then calico-vxlan|

- Pod short traces

    

    |Test cases|Conclusions|
    |----|----|
    |Pod to node（the same node）|The five cni modes has similar latencies, macvlan and calico-underlay has the smallest one|
    |Pod to node（different nodes）|Macvlan outperforms cilium-vxlan, and calico-vxlan has the highest latency|
    |Pod to Pod（the same node）|Macvlan outperforms cilium, and calico has similarly worse performance in all three modes|
    |Pod to Pod（different nodes）|Macvlan has the best performance, followed by calico-underlay and then calico-vxlan|

### Detailed data

- Pod-related throughput (Gbits/sec)

    |Test cases|Cilium(vxlan)|Calico(vxlan)|Calico(ipip)|Calico(underlay)|Macvlan-standalone|Sriov-standalone|
    |--|----|--|----|----|----|----|----|----|
    |Node to node|9.16|9.16| 9.16| 9.16| 9.16| 9.16| 9.16|
    |Pod to node（the same node）| 12.6| 13.8| 14.23| 14.2| 16.4| 15.8|
    |Pod to node（different nodes）| 3.02| 1.57| 8.24| 9.2| 9.15| 9.09|
    |Pod to Pod（the same node）| 15.3| 10.2| 10.33| 10.27| 22.2| 14.1|
    |Pod to Pod（different nodes）| 8.30| 1.37| 4.51| 3.89| 9.18| 9.21|

- Service related throughput (Gbits/sec)

    |Test cases|Cilium(vxlan)|Calico(vxlan)|Calico(ipip)|Calico(underlay)|Macvlan-standalone|Sriov-standalone|
    |--|----|--|----|----|----|----|----|
    |Service to node（the same node）| 8.30| 12| 11.77| 12.07| 16.6| 15.8|
    |Service to node（different nodes）| 7.41| 1.23| 8.57| 9.037| 9.14| 9.10|
    |Service to Pod（the same node）| 15.8| 10.2| 10| 10.17| 20.2| 15.6|
    |Service to Pod（different nodes）| 8.27| 1.3| 4.81| 3.49| 9.15| 16.3|

- netpref latency (long connection) (Microseconds)

    |Test cases|Cilium(vxlan)|Calico(vxlan)|Calico(ipip)|Calico(underlay)|Macvlan-standalone|Sriov-standalone|
    |--|----|--|----|----|----|----|----|----|
    |Node to node| 113.27| 113.27| 113.27| 113.27| 113.27| 113.27| 113.27| 113.27|
    |Pod to node（the same node）| 76.76| 76.81| 74.55| 62.27| 61.25| 74.34|
    |Pod to node（different nodes）| 150.26| 241.46| 225.68| 170.23| 95.76| 109.77|
    |Pod to Pod（the same node）| 65.62| 104.82| 91.44| 103.71| 45.47| 66.74|
    |Pod to Pod（different nodes）| 201.27| 275.22| 248.72| 195.61| 81.74| 78.83|

- netpref latency (short connection) (Microseconds)

    |Test cases|Cilium(vxlan)|Calico(vxlan)|Calico(ipip)|Calico(underlay)|Macvlan-standalone|Sriov-standalone|
    |--|----|--|----|----|----|----|----|----|
    |Node to node| 439.04| 439.04| 439.04| 439.04| 439.04| 439.04| 439.04|
    |Pod to node（the same node）| 259.92| 230.65| 226.26| 203.63 |187.41 |225.66|
    |Pod to node（different nodes）| 613.59| 803.80| 767.08| 587.53| 358.48| 413.77|
    |Pod to Pod（the same node）| 198.99| 982.92| 265.07| 277.75| 127.48| 275.52|
    |Pod to Pod（different nodes）| 789.32|
