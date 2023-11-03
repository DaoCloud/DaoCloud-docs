---
hide:
  - toc
---

# What is MinIO

[MinIO](https://www.minio.org.cn/) is a popular, lightweight, and open-source object storage solution that is perfectly compatible with the AWS S3 protocol and supports K8s friendly. MinIO is specially designed for cloud native workloads such as AI, and can provide data workloads for high-performance cloud native data machine learning, big data analysis, and massive storage infrastructure.

DCE's MinIO module is an object storage middleware built on the open source MinIO, which is plug-and-play. DaoCloud has developed an easy-to-use graphical interface for it, providing users with exclusive MinIO instances for computing, storage, and bandwidth resources.

MinIO is popular because of the following features:

1. High performance.

    MinIO is the world's leading pioneer in object storage services and currently has millions of users around the world. Read/write speeds of up to several hundred GB per second on standard hardware.

2. Scalability.

    MinIO borrows from web scalers to bring a simple scaling model to object storage. When deploying MinIO, scaling starts with a single cluster.

3. Cloud native support.

    MinIO is a storage solution built from scratch in the past few years. It conforms to all cloud native computing architectures and construction processes, and includes the latest cloud computing technologies and concepts.

4. Pure open source.

    MinIO is 100% open source based on the Apache V2 license. This means that MinIO's customers can use and integrate MinIO automatically, without restrictions, freely and freely, freely innovate and create, freely modify and improve, freely redistribute new versions and combine software.

5. Compatible with S3 storage.

    AWS's S3 API (Interface Protocol) is an object storage protocol that has reached consensus on a global scale, and is a standard recognized by everyone around the world.

6. Minimalist.
   
    Minimalism is the guiding design principle of MinIO. Simplicity reduces the chance of error, increases uptime, provides reliability, and is fundamental to performance.

7. Support multicloud.

    Millions of instances can be created and deployed in private cloud, public cloud and edge computing environments.

Designed to be cloud native, MinIO can run as lightweight containers managed by external orchestration services such as Kubernetes. The entire server is about tens of MB of static binary files, which can efficiently utilize CPU and memory resources even under high load, allowing enterprises to co-host a large number of tenants on shared hardware.

<!--screenshot-->

[Create a MinIO instance](../user-guide/create.md){ .md-button .md-button--primary }