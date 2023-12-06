# Cilium's Access Acceleration Test in the nodePort Mode

This page describes the results of Cilium's access acceleration test in the nodePort mode.

## Test objects

In this test, the performance of forwarding for Kubernetes nodePort was compared among the following solutions:

- Solution 1: Cilium's eBPF XDP accelerates nodePort

    In eBPF's XDP mode, nodePort's forwarding rules can be offloaded to run on a physical NIC. This feature needs to run on bare metal machines and requires the functional support of the physical hardware NIC, which is currently supported by the mainstream NICs of the major vendors. This function has excellent acceleration effect, low hardware cost and no software adaptation cost, which is the best choice besides DPDK technology.

- Solution 2: Cilium's eBPF TC accelerates nodePort

    In eBPF TC mode, the forwarding rules of nodePort are completed at the lowest layer of the linux kernel network stack. The acceleration effect is not as good as eBPF XDP acceleration, but the effect is much better than the traditional iptables-based forwarding scheme.
    The program can run on any machine, including bare metal machines and virtual machines, there is no requirement for hardware.

- Solution 3: Kubernetes kube-proxy forwards nodePort

    Kube-proxy is a component of the Kubernetes platform that accomplishes service forwarding (including nodePort forwarding) based on iptables rules or ipvs rules, and its forwarding performance is average.

## Test one: testing nodePort forwarding throughput

In a bare metal machine testing environment, the pktgen packet generation tool was used to generate 10Mpps (million packets per second) of request traffic. The throughput of nodePort forwarding was observed for different solutions:

![throughput1](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/cilium-nodeport01.png)

From the above graph, the following can be observed:

- Cilium's eBPF XDP accelerates nodePort

    It can handle the entire 10Mpps of request traffic and forward it at the same rate after nodePort resolution.

- Cilium's eBPF TC accelerates nodePort

    For the 10Mpps of request traffic, it can only handle approximately 3.5Mpps of requests.

- kube-proxy using iptables for nodePort forwarding

    For the 10Mpps of request traffic, it can only handle approximately 2.3Mpps of requests.

- kube-proxy using ipvs for nodePort forwarding

    For the 10Mpps of request traffic, it can only handle approximately 1.9Mpps of requests. Note: Its advantage over iptables becomes prominent when there are a large number of backends.

### Conclusion

Both Cilium's eBPF TC and eBPF XDP accelerate nodePort, delivering significantly better performance than the traditional kube-proxy in Kubernetes. This ensures excellent network forwarding performance for the northbound access entry of the cluster.

## Test 2: testing resource overhead of nodePort forwarding

In a bare metal machine testing environment, the pktgen packet generation tool was used to conveniently generate request traffic of 1Mpps, 2Mpps, and 4Mpps. The following solutions were tested to measure the CPU overhead on the host for implementing nodePort forwarding:

![throughput2](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/cilium-nodeport02.png)

From the above graph, the following can be observed:

- Cilium's eBPF XDP accelerates nodePort

    The host's CPU idle rate is the highest, indicating minimal CPU overhead for forwarding nodePort requests. Even under 4Mpps request traffic pressure, the host still has a significant amount of unused CPU resources.

- Cilium's eBPF TC accelerated nodePort

    The host's CPU idle rate is relatively high, implying relatively low CPU overhead for forwarding nodePort requests. Under 4Mpps request traffic pressure, the host's CPU is already fully utilized.

- kube-proxy using iptables for nodePort forwarding

    The host's CPU idle rate is relatively low, indicating higher CPU overhead for forwarding nodePort requests. Under 2Mpps and 4Mpps request traffic pressure, the host's CPU is fully exhausted.

- kube-proxy using ipvs for nodePort forwarding

    The host's CPU idle rate is relatively low, indicating higher CPU overhead for forwarding nodePort requests. Under 2Mpps and 4Mpps request traffic pressure, the host's CPU is fully exhausted.

### Conclusion

Cilium's eBPF TC and eBPF XDP acceleration for nodePort consume fewer host CPU resources, allowing these CPU resources to be utilized for other tasks on the host, ensuring the availability of resources for other business operations.
