# Cilium Performance Test for Cross-Node Communication between Pods

This page describes the performance test results of Cilium in the scenario of cross-node communication between Pods.

The official [test report](https://docs.cilium.io/en/v1.13/operations/performance/benchmark/) provided by Cilium shows that Cilium leverages eBPF technology to improve the accessibility performance between pods across nodes. The test is based on a bare metal machine and 100G network connection, with Cilium's configuration adjusted for maximum network performance.
The adjustment of Cilium including:

- Using host routing to forward pod data between nodes without any tunneling mode configured.

- Disabled iptables connection tracking on the host.

## Test objects

![cilium](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/cilium-cross-target.png)

## Test environment

![env](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/cilium-cross-env.png)

## Testing tool and metrics

The tests use netperf to generate workloads and collect metrics. The test metrics are as follows:

- Throughput

    Maximum transfer rate over a single TCP connection and total transfer rate over 32 concurrent TCP connections.

- Request/Response Rate (TCP_RR)

    The number of request/response messages that can be transmitted per second over a single TCP connection and 32 concurrent TCP connections.

## Test one

For TCP Single Stream, test TCP throughput between two cross-node Pods:

![single1](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/cilium-singlestream01.png)

CPU overhead for client and server:

![single2](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/cilium-singlestream02.png)

## Test two

For 32-core CPU, 32 concurrent TCP connections, test TCP throughput between two cross-node Pods

![multi](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/cilium-multistream01.png)

CPU overhead for client and server:

![multi2](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/cilium-multistream02.png)

## Test three

Simulate the test of Layer 7 access based on the TCP_RR mode to repeat the behavior of "sending 1 request, and then waiting for 1 reply" over and over again over the same TCP connection.

The TCP_RR performance between two cross-node Pods is tested with the Pod having only 1 core CPU:

![tcprr1](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/cilium-tcprr01.png)

CPU overhead of the client and server:

![tcprr2](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/cilium-tcprr02.png)

## Test four

Test TCP_RR performance between two cross-node Pods when the Pod has only 32 cores of CPU:

![tcprr3](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/cilium-tcprr03.png)

CPU overhead of the client and server:

![tcprr4](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/cilium-tcprr04.png)
