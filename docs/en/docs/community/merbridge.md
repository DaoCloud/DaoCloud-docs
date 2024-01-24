# Merbridge

Merbridge is designed to make traffic interception and forwarding more efficient for service mesh. It replaced iptables with eBPF.

eBPF (extended Berkeley Packet Filter) can run user's programs in the Linux kernel without modifying the kernel code or loading kernel modules. It is widely used in networking, security, monitoring and other relevant fields. Compared with iptables, Merbridge can shorten the data path between sidecars and services and therefore accelerate networking. Meanwhile, using Merbridge will not change the original architecture of Istio. The original logic is still valid. This means that if you don't want Merbridge anymore, just delete the DaemonSet. The original iptables will function again without any troubles.

## What does Merbridge provide

Merbridge has following core features:

- Processing outbound traffic

    Merbridge uses eBPF’s `connect` program to modify `user_ip` and `user_port`, so as to change the destination address of a connection and ensure traffic can be sent to the new interface. In order to help Envoy identify the original destination, the application (incl. Envoy) will call the `get_sockopt` function to get `ORIGINAL_DST` when receiving a connection.

- Processing inbound traffic

    Inbound traffic is processed similarly to outbound traffic. Note that eBPF cannot take effect in a specified namespace like iptables, so changes will be global. It means that if we apply eBPF to Pods that are not originally managed by Istio, or an external IP, serious problems will occur, e.g., cannot establish a connection.

    To address this issue, we designed a tiny control plane, deployed as a DaemonSet. It can help watch and get a list of all pods on the node, similar to kubelet. Then, Pod IPs injected into the sidecar will be written into the `local_pod_ips` map. For traffic with a destination address not in the map, Merbridge will not intercept it.

- Accelerating networking

    In Istio, Envoy visits the application by the current podIP and port number. Because the podIP exists in the `local_pod_ips` map, traffic will be redirected to the podIP on port 15006, producing an infinite loop. Are there any ways for eBPF to get the IP address in the current namespace? Yes! We have designed a feedback mechanism: When Envoy tries to establish a connection, we redirect it to port 15006. When it moves to sockops, we will check if the source IP and the destination IP are the same. If yes, it means the wrong request is sent, and we will discard it in the sockops process. Meanwhile, the current ProcessID and IP will be written into the `process_ip map`, allowing eBPF to support corresponding relationship between processes and IPs. When the next request is sent, we will check directly from the `process_ip map` if the destination is the same as the current IP. Envoy will retry when the request fails. This retry process will only occur once, and subsequent connections will go very fast.

[Go to Merbridge repo](https://github.com/merbridge/merbridge){ .md-button }

[Go to Merbridge website](https://merbridge.io/){ .md-button }

![cncf logo](./images/cncf.png)

<p align="center">
Merbridge is <a href="https://landscape.cncf.io/?selected=merbridge">a CNCF sandbox project</a>.
</p>
