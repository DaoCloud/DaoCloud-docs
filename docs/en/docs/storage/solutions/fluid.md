# Fluid

[Fluid](http://pasa-bigdata.nju.edu.cn/fluid/zh/) is an open-source Kubernetes-native distributed dataset orchestration and acceleration engine,
mainly serving data-intensive applications in cloud-native scenarios, such as big data applications, AI applications, etc.

Through the data layer abstraction provided by Kubernetes services, data can be flexibly and efficiently moved, copied, evicted, transformed, and managed between storage sources like HDFS, OSS, Ceph and upper-layer cloud-native applications in Kubernetes. Specific data operations are transparent to users, users no longer need to worry about efficiency of accessing remote data, convenience of managing data sources, and how to help Kubernetes make operation and maintenance scheduling decisions. Users only need to directly access abstracted data in the most natural Kubernetes native data volume way, and the remaining tasks and underlying details are all handled by Fluid.

## Core Concepts

- Dataset: Simply put, it's the data collection that applications need to access. Different applications correspond to different dataset types.

- Runtime Distributed Cache System Runtime: Runtime is a standard framework for Fluid to deploy distributed cache systems. The specific deployed distributed cache system is the specific Runtime.

    - AlluxioRuntime
    - JuiceFSRuntime
    - JinboFSRuntime
    - GooseFSRuntime
    - EFCRuntime
    - ThinRuntime

- Data Access: Fluid provides a unified Fuse interface to user applications, which is fully POSIX compliant. User applications can access remote datasets just like accessing local data.

## Deploy Fluid via Helm Template

DCE 5.0 supports Fluid and has integrated it into the App Store as an Addon.

1. Enter the `Container Management` module and find the cluster where you need to install Fluid in the `Cluster List`. Click the cluster name.
