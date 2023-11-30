# Performance Test in Implementing Network Policies with eBPF Technology

[The tests](https://kinvolk.io/blog/2020/09/performance-benchmark-analysis-of-egress-filtering-on-linux/) indicate that implementing secure policies for inter-Pod communication using eBPF technology can improve performance. This improvement becomes more pronounced as the number of security policies increases. This page presents the results of performance test in network policy implemented with eBPF technology.

## Test objects

In the testing process, several implementations of security policies were compared:

- Packet filtering using iptables, which is commonly used by projects like Calico
- Packet filtering using ipset
- Packet filtering using eBPF technology

## Test approach

The test was conducted on two bare-metal nodes, simulating cross-node communication. Filtering policies were implemented in the egress on the client side. The objective was to evaluate the impact of different filtering approaches on packet access latency and throughput during the filtering policy matching process.

## Results

- In the TCP throughput test scenario, the results are shown in the following graph. It can be observed that when dealing with tens of thousands of filtering rules, the iptables approach significantly reduces packet throughput:

    ![throughput](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/ebpf-throughput.png)

- When dealing with thousands of filtering rules, the iptables approach incurs substantial CPU overhead on the host:

    ![cpu](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/ebpf-cpu.png)

- When dealing with thousands of filtering rules, the iptables approach imposes significant latency burden on the applications:

    ![latency](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/ebpf-latency.png)

## Conclusion

Implementing network security policies using eBPF technology has demonstrated superior performance compared to traditional iptables-based solutions. Even with the installation of tens of thousands of rules, it has minimal impact on application communication performance.
