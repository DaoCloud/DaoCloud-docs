---
hide:
  - toc
---

# Manage Devices

After devices are successfully onboarded, DCE 5.0 allows you to perform operations such as power on/off, reboot, and PXE provisioning.

## Prerequisites

- Devices have been onboarded. See [Manual Device Onboarding](index.md) or [Batch Device Onboarding](./batch-access.md).
- Your account has permissions to view and operate the devices.

## Device Operations

Follow these steps:

1. In the left navigation bar, click **Device Management** -> **Devices** to enter the device list page. Locate the target device and click the __┇__ on the right to expand the action menu.

    <!-- ![Device List and Action Menu](../images/manage-device-00.png) -->

2. Select the desired function:

    - **BMC Console**: Redirects to the device vendor's BMC Web console.
    - **Power On / Power Off / Reboot**: Perform standard power on, off, or reboot operations.
    - **Forced Reboot**: Immediately power off and on. This may cause unsaved data loss and is recommended only if the device is unresponsive.
    - **PXE Provisioning**: Start the provisioning process. Ensure PXE boot and image sources are correctly configured.
    - **Update**: Modify device management IP, port, device group, and other configurations.
    - **Modify Authentication**: Update the credentials used to connect to the device or its BMC.
    - **Delete**: Remove the device from the platform. After deletion, the device will no longer be managed, and related history may be unrecoverable.

        !!! note

            If the device was automatically onboarded via DHCP, deleting it will only temporarily remove the configuration. The device may reappear in the list due to DHCP auto-discovery.  
            To permanently remove the device, it is recommended to:

            1. Disable DHCP server address assignment in the BMC manager
            2. Contact the administrator to stop the DHCP service and manually onboard the device
