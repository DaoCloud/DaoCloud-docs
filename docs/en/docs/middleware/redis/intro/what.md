---
hide:
  - toc
---

# What is Redis cache service

Redis cache service is an in-memory database cache service provided by DaoCloud. It is compatible with two in-memory database engines, Redis and Memcached. Business requirements for high concurrency and fast data access.

- out of the box

    Provides stand-alone, high-availability clusters, Cluster clusters, and read-write split cache instances, with rich memory specifications ranging from 128M to 1024G. You can directly create it through the UI console without preparing server resources separately.

    All Redis versions are deployed in containers, and can be created in seconds.

- Safe and reliable

    With the help of security management services such as DaoCloud global management and audit logs, the storage and access of instance data are fully protected.

    Flexible disaster recovery strategy, master/standby/cluster instances are deployed in a single cluster to support multicluster and multicloud deployment.

- Elastic expansion

    Provides online expansion and contraction services for instance memory specifications, helping you achieve cost control based on actual business volume and achieve the goal of on-demand usage.

- Convenient management

    Visualize the web management interface to complete operations such as instance restart and parameter modification online. A RESTful API is also provided to facilitate further automated instance management.

[Create a Redis instance](../user-guide/create.md){ .md-button .md-button--primary }