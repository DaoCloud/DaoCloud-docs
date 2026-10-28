---
hide:
  - toc
---

# Manual Add Device

By configuring the device IP address and authentication credentials, servers, switches, and other devices can be manually onboarded to the platform for management.

This guide describes the process for a single device. For rapid batch onboarding, please refer to [Batch Add Device](./batch-access.md).

1. In the left navigation bar, click **Device Management** to enter the device list, then click the **Manual Add** button at the top right corner of the page.

    ![Device Management List](../images/access-device-01.png)

2. Fill in the configuration including device name, IP address, port, connection type, and username/password.

    ![Add Device](../images/add-device01.png)

    | Field | Required | Description |
    |-------|----------|-------------|
    | Name | Yes | Up to 253 characters; lowercase letters, numbers, dash (-), or dot (.) only; no consecutive symbols; must start and end with a letter or number. |
    | Device Group | No | Optional. Assign devices to specific groups based on device type or other criteria for easier management. |
    | IP Address | Yes | Management IP address of the device. |
    | Port | Yes | Port used to establish the connection with the device. |
    | Connection Type | Yes | Supports Redfish or SSH. If Redfish is selected, additional PXE boot and HTTPS settings are required. |
    | PXE Boot Configuration | Conditional | Required when using Redfish. Used to load the OS image over the network at startup; select Redfish or IPMI protocol based on your environment. |
    | Enable HTTPS | Conditional | Required when using Redfish. Specifies whether to use HTTPS for device communication. |
    | Authentication - Use default username/password | Optional | Automatically uses the credentials configured during Topohub Helm deployment. |
    | Authentication - Custom | Optional | Manually enter the username and password. |

3. After completing the configuration, click **OK** to finish onboarding the device. You will automatically return to the device list.

Next step: [Manage Devices](./manage-device.md)

[Download Center](https://docs.daocloud.io/en/download/){ .md-button .md-button--primary }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button .md-button--primary }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button .md-button--primary }
