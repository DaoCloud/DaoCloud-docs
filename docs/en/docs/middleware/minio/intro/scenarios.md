---
hide:
  - toc
---

# scenes to be used

MinIO is an object storage service based on the Apache License v2.0 open source protocol.
It is compatible with the AWS S3 cloud storage service interface and is very suitable for storing large-capacity unstructured data.
Examples include pictures, videos, log files, backup data, and container/virtual machine images, while an object file can be of any size, ranging from KB to a maximum of TB.

Common usage scenarios are:

- Network disk: massive files
- Social networking sites: massive pictures
- E-commerce website: Massive product images
- Video website: massive video files

Each MinIO cluster is a collection of distributed MinIO servers, one process per node.
MinIO runs as a single process in user space and uses lightweight coroutines to achieve high concurrency.
Drives are grouped into Scratch Sets (by default, 16 drives per group), and objects are placed on those Scratch Sets using a deterministic hashing algorithm.

MinIO is designed for large-scale, multi-datacenter cloud storage services.
Each tenant runs its own MinIO cluster that is completely isolated from other tenants, allowing tenants to be immune to any disruptions from upgrades, updates, and security incidents.
Each tenant scales independently by federating clusters across geographic regions.