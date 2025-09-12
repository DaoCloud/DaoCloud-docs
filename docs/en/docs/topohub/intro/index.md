---
hide:
  - toc
---

# What is Device Management

The Device Management module is a Kubernetes-native infrastructure management component designed for AI computing centers. It provides unified management of hardware resources such as hosts and switches. It comes with a built-in multi-instance DHCP service that supports automatic allocation and fixed assignment of IP and MAC addresses, covering both in-band and out-of-band networks, simplifying BMC management and operating system deployment. With PXE boot, it enables automated provisioning and offers a WebUI management interface for centralized management of IOS, TFTP, ZTP, and related configuration files. The Device Management module helps AI computing centers achieve integrated management of networks, hosts, and file services, significantly improving operational efficiency and automation.

**Key Features**

- Device Discovery and Onboarding

    - Automatically detect new physical devices such as servers and switches
    - DHCP automatically assigns in-band and out-of-band network addresses
    - Support batch onboarding of devices, enabling quick provisioning within minutes

- Full Lifecycle Management

    - Remote power control: one-click power on/off, reboot, force shutdown
    - PXE boot provisioning: automated operating system deployment
    - Hardware health monitoring: real-time monitoring of accessibility, power, and other key metrics

- Multi-Subnet DHCP Service

    - Launch independent DHCP server instances in different VLANs or subnets
    - Support automatic or manual binding of IP and MAC addresses to ensure stable IP allocation
    - Enable multi-tenant network security isolation through VLANs

- Unified Operations Management

    - Manage devices by cluster or business group for easier operations
    - Collect metrics, logs, and event data for rapid issue diagnosis
    - Dynamically scale device management capacity as business grows

**Product Logical Architecture**

<!-- ![Logical Architecture Diagram](../images/index-01.png) -->
