---
hide:
  - toc
---

# Install the Device Management Component

The Device Management module requires installing both the frontend UI component and the backend service component.  
Starting from DCE 5.0 installer v0.33.0 and above, installation of the Device Management frontend UI component is supported and **does not require manual installation**.  
Please contact the delivery support team to obtain the commercial installation package.

The installation process is as follows:

1. Install the frontend UI component `topohub-dashboard`

    For the commercial version installation process, please refer to the [installation guide](../../install/index.md).

    By default, the `topohub-dashboard` component is not installed. Please update the **manifest** configuration file first.

    Example manifest:

    ```diff
    apiVersion: manifest.daocloud.io/v1alpha1
    kind: DCEManifest
    metadata:
      ...
    global:
      helmRepo: https://release.daocloud.io/chartrepo
      imageRepo: release.daocloud.io
    infrastructures:
      ...
      # Device Management UI component
      topohub-dashboard:
    -  enable: false # Default is false, not installed
    +  enable: true  # Set to true if you need to install the Device Management module
        helmVersion: 0.3.0
    ```

2. Install the backend service component `topohub`

    > The backend service component only needs to be installed in the [global service cluster](../../kpanda/user-guide/clusters/cluster-role.md#global-service-cluster).

    Open the global service cluster, then navigate to __Helm Applications__ -> __Helm Templates__, locate `topohub`, and proceed with the installation.

    - **BMC username and password**: Default credentials for connecting to the host BMC.
    - **DHCP Server**: The name of the NIC on the node that can access all managed device networks. It should be connected to the switch in trunk mode (e.g., `eth1`).
    - **Topohub working node**: The node where the `topohub` component will be deployed and running.

## Conclusion

After completing the above steps, you can fully experience all the features of Device Management in DCE 5.0.  
Enjoy your usage!
