---
MTPE: windsonsea
date: 2024-08-21
---

# Virtual Machine Features

The virtual machine module provides management capabilities for the lifecycle of virtual machines.
Virtual Machine supports the following operations:

| Operation | Description | Virtual Machine State |
| --- | ---- | -------- |
| [Create Virtual Machine](../quickstart/index.md) | Create one or multiple virtual machines. | / |
| [Edit/Update Virtual Machine](../quickstart/update.md) | Modify the virtual machine. | Running/Stopped/Processing/Error |
| Start Virtual Machine | Start a virtual machine that is in a stopped state. | Stopped |
| Shut Down Virtual Machine | Shut down the virtual machine. | Running/Processing |
| Restart Virtual Machine | Restart a virtual machine that is in a running state. | Running/Error |
| [Access Console](../quickstart/access.md) | Open the virtual machine console and log into the virtual machine system (VNC, terminal). | Running |
| Modify Compute Specifications | Modify the CPU and memory of the virtual machine. Supports online/stopped modification of compute specifications. | Running/Stopped |
| [Create Snapshot](../vm/snapshot.md) | Create a snapshot for the virtual machine. | Running/Stopped |
| [Clone Virtual Machine](../vm/clone.md) | Clone the current virtual machine. | Running/Stopped/Error |
| [Live Migration](../vm/live-migration.md) | Seamlessly migrate a running virtual machine to another node. | Running |
| [Cold Migration](../vm/migratiom.md) | Migrate a powered-off virtual machine to another node. | Stopped |
| Data Disk Expansion | Expand the data disk for the virtual machine. | Running/Stopped/Processing |
| Load Disk | Load an available data disk for the virtual machine. | Running/Stopped |
| Unload Disk | Unload a loaded disk from the virtual machine. | Running/Stopped |
| [Switch Network Mode](../vm/vm-network.md) | Switch the network mode when updating the virtual machine. | Running/Stopped/Processing/Error |
| Load Network Card | Load a network card for the virtual machine. | Stopped |
| Unload Network Card | Unload a loaded network card from the virtual machine. | Stopped |
| [Virtual Machine Template](../template/index.md) | Convert the current virtual machine into a template. | Running/Stopped |
| [View Virtual Machine Details](../quickstart/detail.md) | Access the virtual machine details page to view basic information, monitoring, events, snapshots, and configuration information. | Running/Stopped/Processing |
| Delete Virtual Machine | Immediately release the resources such as CPU, memory, IP address, etc., and permanently delete the virtual machine. Please proceed with caution. | Running/Stopped/Processing/Error |
