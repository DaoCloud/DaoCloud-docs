# Device Management Release Notes

This page lists the release notes for Device Management, helping you understand the evolution and feature changes across versions.

## 2025-08-31

### v0.4.1

- **New** Support for connecting in-band/out-of-band servers, switches, and other devices via Redfish or SSH
- **New** Support for batch device onboarding
- **New** Access to BMC console of Redfish devices
- **New** Support for device power on, power off, reboot, and forced reboot operations
- **New** PXE provisioning for devices accessed via Redfish
- **New** Support for updating basic device information and device credentials
- **New** Support for deleting devices
- **New** Support for creating subnets, where subnet instances launch DHCP services on node NICs to dynamically assign IP addresses to hosts
- **New** Support for batch subnet creation
- **New** Support for managing subnets, including updating subnet information and deleting subnets
- **New** Support for viewing subnet DHCP IP pools and IP allocation status
- **New** Support for binding device IP addresses to MAC addresses
