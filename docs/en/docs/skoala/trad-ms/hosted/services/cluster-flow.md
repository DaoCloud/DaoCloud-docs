---
hide:
  -toc
---

# Create Cluster Flow Control Rules

[Flow control rules](flow-control.md), [circuit breaking rules](circuit-breaker.md), [authorization rules](auth.md), [hotspot rules](hotspot.md), and [system rules](system.md) can only collect local resource invocation information and are suitable for single-node applications. However, in the current era of cloud native applications, many applications are deployed in clusters and distributed across multiple machines. In distributed scenarios, the above rules have some limitations. For example, if the traffic routed to each machine in the cluster is unbalanced, one machine may stop serving requests due to exceeding its threshold before reaching the overall threshold sum of the entire cluster.

Cluster flow control mode is designed to solve this problem. In cluster flow control mode, two concepts need to be understood:

- TokenServer: It collects and sums up the QPS (Queries Per Second) of all instances in the cluster, compares the total value with the overall threshold of the cluster (single-machine threshold ✖️ number of machines). If the overall cluster threshold has not been reached, it sends tokens to clients.
- TokenClient: These are the application instances distributed across different machines. The client requests tokens from the TokenServer. If a token is successfully obtained, it means the overall threshold has not been reached, and the instance can continue processing requests. If a token cannot be obtained, it means the overall threshold has been reached, and the requests from that instance will fail directly.

!!! note

    - The TokenServer needs to be configured in the `public` namespace of Nacos, with the group set to `SENTINEL_GROUP`.
    - The TokenServer is a single point of failure. If the TokenServer goes down, the cluster flow control mode will degrade to single-machine flow control mode.

Follow the steps below to create a cluster flow control rule:

1. Click the name of the target managed registry, then click `Microservices` in the left sidebar and click the `Governance` option on the right side.

    > Note that the microservice you want to govern should have the "Can be governed" status set to "Yes" in order to proceed with the following steps.


2. Select `Cluster Flow Control Rules`, then click `Create Cluster Flow Control Rule` on the right side.


3. Fill in the rule configuration based on the instructions below and click `OK` in the bottom right corner.

    - Server Name: The name of the TokenServer.
    - TokenServer IP: The IP address of the TokenServer.
    - TokenServer Port: The port number of the TokenServer.
    - Client Selection: The cluster flow control client used to communicate with the associated TokenServer and request tokens.


4. After creating the rule, you can view it in the list of system rules. Click the more options button on the right side to update or delete the rule.

