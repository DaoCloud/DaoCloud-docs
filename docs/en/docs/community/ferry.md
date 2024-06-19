---
MTPE: windsonsea
date: 2024-06-19
---

# Ferry

Ferry is a Kubernetes multicluster communication component that eliminates communication differences between clusters
as if they were in a single cluster, regardless of their network environments.

### Why ferry

- Avoid Cloud Lock-in
    - Open up inter-access between different clouds
    - Migration of Service to different clouds is seamless
- Out of the Box
    - Command line tools are provided for easy installation and use
    - Centrally defined rules
- No Intrusion
    - No dependency on Kubernetes version
    - No dependency on any CNI or network environment
    - No need to modify existing environment
- Intranet Traversal
    - Only one public IP is required

[Go to ferry repo](https://github.com/ferryproxy/ferry){ .md-button }
