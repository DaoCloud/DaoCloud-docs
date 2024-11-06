---
MTPE: windsonsea
date: 2024-08-21
---

# Virtual Machine Features

The virtual machine module provides management capabilities for the full lifecycle of virtual machines.
Virtual Machine supports the following operations:

| Operation | Description | Virtual Machine State |
| --- | ---- | -------- |
| Create Virtual Machine | Create one or multiple virtual machines. | / |
| Edit/Update Virtual Machine with YAML | Modify the virtual machine. | Running/Stopped/Processing/Error |
| Start Virtual Machine | Start a virtual machine that is in a stopped state. | Stopped |
| Shut Down Virtual Machine | Shut down the virtual machine. | Running/Processing |
| Restart Virtual Machine | Restart a virtual machine that is in a running state. | Running/Error |
| Access Console | Open the virtual machine console and log into the virtual machine system (VNC, terminal). | Running |
| Modify Compute Specifications | Modify the CPU and memory of the virtual machine. Supports online/stopped modification of compute specifications. | Running/Stopped |
| Create Snapshot | Create a snapshot for the virtual machine. | Running/Stopped |
| Clone Virtual Machine | Clone the current virtual machine. | Running/Stopped/Error |
| Live Migration | Migrate the virtual machine to another virtual machine node; currently only supports live migration. | Running |
| Data Disk Expansion | Expand the data disk for the virtual machine. | Running/Stopped/Processing |
| Load Disk | Load an available data disk for the virtual machine. | Running/Stopped |
| Unload Disk | Unload a loaded disk from the virtual machine. | Running/Stopped |
| Load Network Card | Load a network card for the virtual machine. | Stopped |
| Unload Network Card | Unload a loaded network card from the virtual machine. | Stopped |
| Convert Virtual Machine to Template | Convert the current virtual machine into a template. | Running/Stopped |
| View Virtual Machine Details | Access the virtual machine details page to view basic information, monitoring, events, snapshots, and configuration information. | Running/Stopped/Processing |
| Delete Virtual Machine | Immediately release the resources such as CPU, memory, IP address, etc., and permanently delete the virtual machine. Please proceed with caution. | Running/Stopped/Processing/Error |
