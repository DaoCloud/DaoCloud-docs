# KubeEdge v1.15.0 Released

> Authors: [WillardHu](https://github.com/WillardHu) and [JiaweiGithub](https://github.com/JiaweiGithub)

KubeEdge is the core component of DCE 5.0 [Cloud Edge Collaboration](../kant/intro/index.md)
and DaoCloud has been actively following, promoting, and planning features of KubeEdge.

## What have been changed

KubeEdge v1.15.0 mainly adds support for Windows edge nodes, device management based on physical models, and DMI data plane support. The specific details are as follows:

### Support for Windows Edge Nodes

With the continuous expansion of edge computing application scenarios, there are also more types of devices involved, including many sensors, cameras, and industrial control devices based on the Windows operating system. Therefore, the new version of KubeEdge supports running edge nodes on Windows, covering more usage scenarios.

In version v1.15.0, KubeEdge supports edge nodes running on Windows Server 2019 and supports Windows containers running on edge nodes. This successfully expands the usage scenarios of KubeEdge to the Windows ecosystem. The Windows version of EdgeCore configuration adds a new field called `windowsPriorityClass`, which is set to `NORMAL_PRIORITY_CLASS` by default. Users can download the Windows version of the EdgeCore installation package on the Windows edge host, and after decompressing it, execute the following command to complete the registration and access of the Windows edge node. Users can use `kubectl get nodes` on the cloud side to confirm the status of the edge node and manage the edge Windows applications.

```sh
edgecore.exe --defaultconfig > edgecore.yaml
edgecore.exe --config edgecore.yaml
```

### Release of Device Management API v1beta1 based on Physical Models

In version v1.15.0, the device management API based on physical models, including Device Model and Device Instance, has been upgraded from v1alpha2 to v1beta1. It adds configurations related to edge device data processing, and combines the northbound device API with the southbound DMI interface to implement device data processing. The main updates of the API include:

- In Device Model, fields such as device property description, device property type, device property
  value range, and device property unit are added according to the physical model standard.
- All built-in protocol configurations in Device Instance are removed, including Modbus, Opc-UA, Bluetooth, etc.
  Users can use the extensible Protocol configuration to set their own protocols to achieve device access of
  any protocol. The mappers for built-in protocols such as Modbus, Opc-UA, Bluetooth will not be removed from
  the mappers-go repository, and will be updated to the latest version and maintained continuously.
- In the device properties of Device Instance, related configurations for data processing are added, including
  device reporting frequency, data collection frequency, whether the property is reported to the cloud, and
  whether it is pushed to the edge database. The data processing will be performed in the Mapper.

### Release of Mapper-Framework for DMI Data Plane Custom Development

In version v1.15.0, support for the DMI data plane is provided, mainly carried in the southbound Mapper development framework called Mapper-Framework. Mapper-Framework provides a brand-new Mapper automatic generation framework, which integrates DMI device data management (data plane) capabilities in the framework, allowing devices to process data at the edge or in the cloud, and improving the flexibility of device data management. Mapper-Framework can automatically generate the user's Mapper project, simplifying the complexity of designing and implementing the Mapper, and improving the development efficiency of the Mapper.

- Support for DMI device data plane management capabilities

    In version v1.15.0, DMI provides support for data plane capabilities, enhancing the ability of edge devices
    to process device data. Device data can be directly pushed to the user's database or application on the edge
    according to the configuration, or it can be reported to the cloud through the cloud-edge channel. Users can
    also actively pull device data through the API. The device data management methods are more diverse, solving
    the problem of frequent device data reporting to the cloud, which can easily cause communication blockage
    between the cloud and the edge. It can reduce the amount of data communicated between the cloud and the edge,
    and reduce the risk of communication blockage between the cloud and the edge. The DMI data plane system
    architecture is shown in the following figure:

    ![System Architecture](./images/edge01.png)

- Mapper Automatic Generation Framework Mapper-Framework

    In version v1.15.0, a brand-new Mapper automatic generation framework called Mapper-Framework is proposed.
    The framework has integrated functions such as Mapper registration to the cloud, cloud-side delivery of
    Device Model and Device Instance configuration information to the Mapper, and device data transmission
    and reporting. It greatly simplifies the development of the Mapper for users and facilitates the
    cloud native device management experience brought by the KubeEdge edge computing platform.

### Support for Running Kubernetes Static Pods on Edge Nodes

The new version of KubeEdge supports Kubernetes-native static Pod capability. Users can write Pod manifests
in JSON or YAML format in a specified directory on the edge host, similar to the operation method in Kubernetes.
Edged will monitor the files in this directory to create/delete edge static Pods and create mirrored Pods in the cluster.

The default directory for static Pods is `/etc/kubeedge/manifests`, and you can also specify
the directory by modifying the `staticPodPath` field in the EdgeCore configuration.

### Upgrade Kubernetes Dependency to v1.26

The new version upgrades the dependency on Kubernetes to v1.26.7, allowing you to use the new features in both the cloud and the edge.

For more detailed information about v1.15.0, please visit: https://bbs.huaweicloud.com/blogs/413613

## Contributions from DaoCloud to the KubeEdge Community

DaoCloud adheres to the concept of thriving and co-building the community, continuously encourages upstream contributions, and gives back to the community.

### Participated Features

- keadm compatibility with cloudcore, edgecore historical versions CI ([PR #5289](https://github.com/kubeedge/kubeedge/pull/5289)),
  keadm compatibility with k8s version CI ([PR #5006](https://github.com/kubeedge/kubeedge/pull/5006))
- Added Device CRD admission validation ([PR #5290](https://github.com/kubeedge/kubeedge/pull/5290)),
  proposal writing for the new version of device management API based on physical models v1beta1+ ([PR #4983](https://github.com/kubeedge/kubeedge/pull/4983)),
  added Mapper-Framework repository ([mapper-framework](https://github.com/kubeedge/mapper-framework)),
  refactored Mapper-Framework Config module ([PR #5219](https://github.com/kubeedge/kubeedge/pull/5219)),
  added lint check to Mapper-Framework ([PR #5292](https://github.com/kubeedge/kubeedge/pull/5292)),
  optimized device initialization module of Mapper-Framework ([PR #5247](https://github.com/kubeedge/kubeedge/pull/5247))
- Admission installation package support ([PR #5034](https://github.com/kubeedge/kubeedge/pull/5034)),
  upgrade of cloudcore on the cloud side ([PR #5229](https://github.com/kubeedge/kubeedge/pull/5229)),
  maintenance of mqtt using DaemonSet ([PR #5235](https://github.com/kubeedge/kubeedge/pull/5235))
- Provided more differentiated configuration fields for batch workloads (EdgeApplication) ([PR #5262](https://github.com/kubeedge/kubeedge/pull/5262))

### Bug Fixes

- Pulling pause image when deleting node access ([PR #5312](https://github.com/kubeedge/kubeedge/pull/5312)),
  node upgrade failure in historical versions ([PR #5085](https://github.com/kubeedge/kubeedge/pull/5085))
- Fixed sedna helm installation package bug ([PR #420](https://github.com/kubeedge/sedna/pull/420))
- Optimized rule admission validation ([PR #5225](https://github.com/kubeedge/kubeedge/pull/5225))
- Fixed synchronization issues when delivering and deleting device models ([PR #5065](https://github.com/kubeedge/kubeedge/pull/5065))
- Fixed pkg directory and related applications in Mapper-Framework ([PR #5070](https://github.com/kubeedge/kubeedge/pull/5070))
- Fixed timing issue with mutex unlock ([PR #5279](https://github.com/kubeedge/kubeedge/pull/5279))

### Community Seats

- Top-level kubeedge reviewer [@WillardHu](https://github.com/WillardHu)
- SIG release chairs + technical leads [@zhiyingfang2022](https://github.com/zhiyingfang2022)
- SIG network chairs (in review) + technical leads [@JiaweiGithub](https://github.com/JiaweiGithub)
- SIG device chairs + technical leads [@cl2017](https://github.com/cl2017)

### Other Matters

- Assisted the community in completing the planning for the second half of 2023 ([PR #172](https://github.com/kubeedge/community/pull/172))
- Added DaoCloud as a partner to KubeEdge ([PR #491](https://github.com/kubeedge/website/pull/491))
- Shared technical solutions for message routing support modification ([PR #5129](https://github.com/kubeedge/kubeedge/issues/5129)),
  message routing support for resumable transmission ([PR #4995](https://github.com/kubeedge/kubeedge/issues/4995)),
  optimization of message routing cloud-edge communication blockage ([PR #5332](https://github.com/kubeedge/kubeedge/issues/5332))
- Served as the rotating host of SIG-AI for Sedna in October and November
- Hosted SIG-DeviceIOT community meetings
- Guided the completion of the "Edge Device Multi-Node Migration Solution Based on KubeEdge Device Management Interface DMI" open-source summer project
- Participated in the design of EdgeMesh CNI features
- In Q4, the DaoCloud Edge Team submitted a total of 22 PRs to the KubeEdge community.
  See [Commit Details](https://kubeedge.devstats.cncf.io/d/56/company-commits-table?orgId=1&from=now-90d&to=now&var-repogroups=kubeedge&var-companies=DaoCloud%20Network%20Technology%20Co.%20Ltd.).

![Contributions](./images/edge02.png)
