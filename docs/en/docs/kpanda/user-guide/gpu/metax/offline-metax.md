# Offline Installation and Usage of Metax GPU Components

This section provides guidance on the offline installation of Metax components such as `metax-gpu-extensions` and `metax-operator`, as well as instructions for using Metax GPU cards.

## Prerequisites

- [DCE 5.0](../../../../install/index.md) container management platform has been deployed and is functioning properly.
- The container management module has either [joined an existing Kubernetes cluster](../../clusters/integrate-cluster.md) or [created a new one](../../clusters/create-cluster.md), and the UI interface of the cluster is accessible.
- The GPU cards in the current cluster are not virtualized and are not in use by other applications.
- The image registry has imported the [Addon offline installation package](https://docs.daocloud.io/download/addon/history/). For usage, refer to [Using the Addon offline installation package](https://docs.daocloud.io/download/addon/v0.40.0/#_3).

## Component Overview

DCE 5.0 ships with two built-in Helm chart packages: `metax-gpu-extensions` and `metax-operator`. Choose which to install based on your usage scenario.

1. **metax-gpu-extensions**: Contains the `gpu-device` and `gpu-label` components. When using the Metax-extensions solution, application container images must be built based on the MXMACA® base image. This solution only supports the full GPU usage scenario.
2. **metax-operator**: Contains the `gpu-device`, `gpu-label`, `driver-manager`, `container-runtime`, and `operator-controller` components.
   With this approach, you can build application container images that do not include the MXMACA® SDK. It supports both full GPU and vGPU scenarios.

## Procedure

1. In the left navigation bar, go to __Container Management__ -> __Cluster Management__, and click the name of the target cluster.
2. From the left navigation bar, click __Helm Apps__ -> __Helm Templates__, then search for __metax__.
3. The following two components will appear. Install them selectively as needed.

![Two Components](../images/metax1.png)

!!! bug "📢📢📢 Installation Notes"

    The current `metax-operator` chart already includes `metax-exporter` by default, so you do not need to install it separately.
