# Device Management Release Notes

This page lists the release notes for Device Management, helping you understand the evolution and feature changes across versions.

## 2025-12-31

### v0.6.0

- **Fixed** permission validation issue for batch device and subnet import interface

## 2025-10-31

### v0.5.0

- **Added** support for SSH device shutdown and reboot operations
- **Added** support for permission configuration
- **Optimized** subnet deletion logic by removing restrictions

## 2025-08-31

### v0.4.1

- **Added** support for connecting in-band/out-of-band servers, switches, and other devices via Redfish or SSH
- **Added** support for batch device onboarding
- **Added** access to BMC console of Redfish devices
- **Added** support for device power on, power off, reboot, and forced reboot operations
- **Added** PXE provisioning for devices accessed via Redfish
- **Added** support for updating basic device information and device credentials
- **Added** support for deleting devices
- **Added** support for creating subnets, where subnet instances launch DHCP services on node NICs to dynamically assign IP addresses to hosts
- **Added** support for batch subnet creation
- **Added** support for managing subnets, including updating subnet information and deleting subnets
- **Added** support for viewing subnet DHCP IP pools and IP allocation status
- **Added** support for binding device IP addresses to MAC addresses
