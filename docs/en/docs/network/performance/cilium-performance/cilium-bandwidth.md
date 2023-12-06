# Cilium Performance Test for eBPF-based Pod Bandwidth Management

Cilium improves the performance of Pod bandwidth based on eBPF technology. This page presents the performance test results of Cilium's eBPF-based Pod bandwidth management.

## Test objects

- In the traditional scenario, HTB/TBF qdisc is used to implement Pod traffic shaping control based on the same TC module in Linux.
- In Cilium, eBPF technology is used to implement Earlist Departure Time (EDT) , a rate limit model, which has excellent performance due to its lockless implementation.

## Testing tool and environment

- Testing tool: netperf

- Test environment: 256 concurrent sessions of request/response type streams (TCP_RR), and each stream rate is 100M.

## Test Results

- Cilium's EDT Pod bandwidth control has a very low impact on packet latency, while the traditional HTB qdisc-based TC scheme has a high impact on packet communication latency.

    ![latency](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/cilium-ebpf-latency.png)

- Cilium's EDT Pod bandwidth management has a limited impact on the TPS of application communication, while the traditional HTB qdisc-based TC scheme has a large impact on the TPS of application communication.

    ![tps](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/cilium-ebpf-tps.png)
