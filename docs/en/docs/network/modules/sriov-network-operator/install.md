# Installing sriov-network-operator

This page describes how to install sriov-network-operator.

## Prerequisites

To use sriov-network-operator within a DCE 5.0 cluster, it is recommended to install `Spiderpool`. Please refer to the [Install Spiderpool](../spiderpool/install.md) guide.

## Installation Steps

Ensure that your cluster is successfully connected to the `Container Management` platform, then follow these steps to install sriov-network-operator.

1. In the left navigation pane, click `Container Management` -> `Clusters` and locate the name of the cluster where you want to install sriov-network-operator.

2. In the left navigation pane, select `Helm App` -> `Helm Charts` and find the `sriov-network-operator` chart.

3. Select the desired version in the `Version Selection` and click `Install`.

4. On the installation page, fill in the required installation parameters.


    Parameter explanations for the above screenshots:

    - `Namespace`: The namespace in which to deploy the sriov-network-operator components. The default value is `kube-system`.
    - `Images` -> `Registry`: Set the repository address for all images. The default online registry is already provided. If you are using a private environment, you can modify it with your own registry.
    - `Images` -> `Operator` -> `Repository`: Set the image name for the Operator. The default value can be kept.
    - `Images` -> `Operator` -> `Tag`: Set the image version for the Operator. The default value can be kept.
    - `Images` -> `SriovCni` -> `Repository`: Set the image name for SriovCni. The default value can be kept.
    - `Images` -> `SriovCni` -> `Tag`: Set the image version for SriovCni. The default value can be kept.

    Parameter explanations for the above screenshot:

    - `Images` -> `SriovConfigDaemon` -> `Repository`: Set the image name for SriovConfigDaemon. The default value can be kept.
    - `Images` -> `SriovConfigDaemon` -> `Tag`: Set the image version for SriovConfigDaemon. The default value can be kept.
    - `Images` -> `SriovDevicePlugin` -> `Repository`: Set the image name for SriovDevicePlugin. The default value can be kept.
    - `Images` -> `SriovDevicePlugin` -> `Tag`: Set the image version for SriovDevicePlugin. The default value can be kept.
    - `Operator` -> `Resource Prefix`: SRIOV network device plugin endpoint resource prefix.
    - `SriovNetworkNodePolicy` -> `Name`: Name of the SRIOV network node policy.

    Parameter explanations for the above screenshot:

    - `pfNames`: List of Physical Function (PF) names for SR-IOV.
    - `pfNames` -> `numVfs`: Number of Virtual Functions (VFs) per Physical Function (PF).
    - `pfNames` -> `resourceName`: Resource name of the SRIOV network device plugin endpoint.
    - `NodeSelector` -> `labelKey`: Key of the NodeSelector label.
    - `NodeSelector` -> `labelValue`: Value of the NodeSelector label.

5. Click the `OK` button at the bottom right to complete the installation.
