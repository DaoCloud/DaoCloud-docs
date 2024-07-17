---
MTPE: windsonsea
Date: 2024-07-17
hide:
  - toc
---

# Network Connectivity Check

In modern cloud native architectures, enterprises are increasingly adopting multi-cluster,
multi-network deployment models to enhance the resilience and availability of applications.
However, this complex architecture also brings about network connectivity issues.
In a hosted mesh mode, especially in a multi-network mode, ensuring network connectivity
between clusters becomes particularly important. To address this issue, the platform provides
a lightweight and easy-to-operate method to help users quickly check connectivity between clusters.

!!! note

    If it is multi-network in the hosted mesh mode, you need to enable
    [multicloud interconnect configuration](cluster-interconnect.md).

The main features are as follows:

- Lightweight detection agents:

    Deploy lightweight detection agents in each cluster. These agents
    can communicate with each other and verify connections through HTTP/HTTPS requests.

- Automated detection process:

    By clicking a button, users can initiate a detection request.
    The tool will automatically traverse all clusters and perform connectivity checks.

- Detailed results:
  
    Detailed detection results will be generated, including the connectivity status between each cluster.
    If issues are detected, the results will provide possible reasons and suggested solutions.
