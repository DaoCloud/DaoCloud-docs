# Install F5network

This page describes how to install F5network.

## Installation notes

The [AS3](https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/userguide/) is a plug-in on the F5 device that provides a configurable interface to the remote network of the F5 device. There is a version matching requirement between the AS3 version and the software version of the F5 device.

[k8s bigip ctlr](https://github.com/F5Networks/k8s-bigip-ctlr) is an F5 control plane component on a K8S cluster that has version matching requirements with K8S, and [k8s bigip ctlr](https://github.com/) F5Networks/k8s-bigip-ctlr) also has version matching requirements with AS3.

Therefore, it is important to know the versions of both the F5 device and the K8S cluster in order to know what versions of AS3 and k8s-bigip-ctlr to be installed correctly.

![f5network version](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/f5-version.png)

To get the latest version matching relationships, please refer to the [F5 official documentation on Controller/Platform compatibility](https://clouddocs.f5.com/containers/latest/userguide/what-is.html#container-ingress-service-compatibility)

## F5 installs AS3 service

1. Login to the management Web UI of F5, click `Statics -> Dashboard` in the navigation bar, and get the version number of the F5 device.

    ![f5 bigip version](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/F5-bigipversion.png)

2. Download the AS3 RPM package of the matching version to your local computer <https://github.com/F5Networks/f5-appsvcs-extension/releases> according to the version matching relationship in the `Installation Requirements`.

3. Login to the management web UI of F5, go to `iApps -> Package Management Lx`, and click `import` in the upper right corner.

    ![f5 as3](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/f5-as3.png)

4. In the `import package`, click `browse`, select the AS3 on your local computer, and finish `upload`.

5. After completing the installation, you can view the installation result.

    ![f5 as3](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/f5-as3-1.png)

## F5 creates partition

A separate partition can be created on the F5 device for [k8s bigip ctlr](https://github.com/F5Networks/k8s-bigip-ctlr) to manage the store and forward rules. The steps are as follows:

1. Login to the management web UI of F5, go to `System` -> `Users` -> `Partition List`, and click `create` in the upper right corner.

    ![f5 partition1](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/f5-partiton1.png)

2. In the creation screen, fill in `Partion Name` and you don't need to change the other default values, then click `Finished` to finish the creation.

    ![f5 partition2](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/f5-partiton-create.png)

## Install a storage component in your cluster (optional)

If you want a storage component to be installed in Layer 4 load balancing mode, you need to install [f5 ipam controller](https://github.com/F5Networks/f5-ipam-controller).
And [f5 ipam controller](https://github.com/F5Networks/f5-ipam-controller) requires the cluster to have the storage component to provide PVC services. You can refer to the relevant storage component installation manual for details.

If you want a storage component to be installed in Layer 7 load balancing mode, you can skip the steps of installing the componanet as it doesn't require the [f5 ipam controller](https://github.com/F5Networks/f5-ipam-controller) to be installed.

## Install F5network in a cluster

1. Prepare a DCE cluster, and login to the Web UI of the global cluster. Go to `Container Management` -> `Cluster List`, login to the cluster where you want to install F5network.

2. In `Helm Apps` -> `Helm Charts`, find and click install `f5network`.

    ![f5network helm](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/f5network1.png)

3. In `Version selection`, select the version you want to install, and click `Install`.

4. In the Installation Parameters screen, fill in the following information：

    ![f5network install1](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/f5network2.png)

    In the screen as above, fill in `Name`, `Namespace`, and `Version`.

    ![f5network install2](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/f5network3.png)

    Parameters description in the screen as above:

    - `f5-bigip-ctlr Settings -> Registry`: the repository address of the f5-bigip-ctlr mirror. the default has been filled with available online repositories. If it is a private environment, you can change it to a private repository address.

    - `f5-bigip-ctlr Settings -> repository`: the f5-bigip-ctlr mirror name.

    - `f5-bigip-ctlr version`: the mirror version of f5-bigip-ctlr. The default value is already set to the latest version number. If you modify it, pay attention to the version compatibility mentioned in `Installation requirements`.

    - `Install ingressClass`: install ingressClass. Enable it if you want to use 7-layer forwarding mode, and disable it if you want to use 4-layer forwarding mode.

    - `IngressClass Name`: the name of the ingressClass. Enable it if you want to use Layer 7 forwarding mode, and disable it if you want to use Layer 4 forwarding mode.

    - `Default ingressClass`: set the installed ingressClass as the default ingressClass for the cluster. Enable it if you want to use Layer 7 forwarding mode, and disable it if you want to use Layer 4 forwarding mode.

    - `BigIP Management Addr`: the WEB UI login address of F5.

    - `BigIP Partition`: the name of the Partition on the F5 device, i.e. the Partition created in the `F5 Device Create Partition` step.

        > If multiple clusters share the same F5 device, it is better to use separate Partitions for different clusters.

    - `Default Ingress IP`: when this component is installed in Layer 7 load balancing mode, this value sets the ingress ingress VIP on F5, note that the IP should be the IP address of F5 external interface subnet.
      When this component is installed in Layer 4 load balancing mode, this value is ignored.

        > If multiple clusters share the same F5 device, separate IPs should be used for different clusters.

    - `Only Watch F5 CRD`: when this option is turned on, the component will only monitor its own CRD, for working in Layer 4 load balancing mode; otherwise, it will monitor all K8S resources, for working in Layer 7 load balancing mode.

    - `Node Label Selector`: set node label selector. The selected node will be used as the entry node in nodePort forwarding mode. If this value is not set, F5 will forward the traffic to the nodePort of all nodes in the cluster.

    - `Forward Method`:set the mode for F5 to forward traffic, `nodePort` and `cluster` mode. For explanation of the mode, refer to [introduction](index.md).
   
    ![f5network install2](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/f5network4.png)

    Parameters description in the screen as above:

    - `BigIP Username`: the login account of the F5 device.
    
    - `BigIP Password`: the login password of the F5 device.

    - `install f5-ipam-controller`: install the f5-ipam-controller component. Disable it when you want to work in Layer 7 load balancing mode, and enable it when you want to work in Layer 4 load balancing mode.

    - `F5-ipam-controller Settings -> Registry`: set the repository address of the f5-ipam-controller image. The default has been filled with available online repositories. If it is a private environment, you can change it to a private repository address.
      This option can be ignored when `install f5-ipam-controller` is turned off.

    - `f5-ipam-controller Settings -> repository`: the f5-ipam-controller image name.
      This option can be ignored when `install f5-ipam-controller` is turned off.

    - `F5-ipam-controller version`: the version of the mirror of the F5-ipam-controller. The default value is already set to the latest version number.
      This option can be ignored when `install f5-ipam-controller` is turned off.

    - `BIGIP L4 IP Pool`: the VIP address pool for F5's Layer 4 load balancing. These IPs should be the IP addresses of the F5 external interface subnet.
      The format of this value is similar to `{ LabelName: 172.16.1.1-172.16.1.5}`, where LabelName will be used in the annotation when creating the application service.
      
        !!! Note

            When creating the application service, as long as the annotation `cis.f5.com/ipamLabel: LabelName` is given to the service, the VIP will be assigned by this component and will eventually take effect on the F5 device.
            This option can be ignored when `install f5-ipam-controller` is turned off.

            If multiple clusters share the same F5 device, different clusters should use separate IP pools.

    - `storageClassName`: the storageClass Name, which will be used by the f5-ipam-controller component for common PVC objects.
      When `install f5-ipam-controller` is turned off, this option can be ignored.

    - `storageSize`: the storage pool size, which will be used by the f5-ipam-controller component for common PVC objects.
      This option can be ignored when `install f5-ipam-controller` is turned off.

## Configuration in cluster forwarding mode (optional)

When the component is installed in cluster forwarding mode, it is necessary to configure VXLAN tunnels between the F5 and K8S clusters, or to configure BGP neighbors.

The CNI component of the K8S can often be configured with BGP and BPG neighbors of the F5 component to enable network connectivity.
For Calico scenario, please refer to the [F5 official documentation](https://clouddocs.f5.com/containers/latest/userguide/calico-config.html).

For more information about this component, please refer to the [F5 Official Document](https://clouddocs.f5.com/containers/latest/userguide/).
