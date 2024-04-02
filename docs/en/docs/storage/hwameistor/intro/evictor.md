---
hide:
  - toc
---

# Evictor

The Evictor is an important component for the operation and maintenance of the HwameiStor system, ensuring the continuous and normal operation of HwameiStor in production environments. When system nodes or application Pods are evicted for various reasons, the Evictor automatically discovers the HwameiStor volumes associated with the nodes or Pods and migrates them to other nodes, ensuring that the evicted Pods can be scheduled to other nodes and run normally.

In a production environment, it is recommended to deploy the Evictor in a highly available manner.

## How to Use

Refer to [Volume Eviction](../resources/volume-eviction.md) for more information.
