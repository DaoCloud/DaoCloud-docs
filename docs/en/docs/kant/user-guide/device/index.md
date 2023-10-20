# Terminal Device Overview

## Terminal Devices

Terminal devices can range from sensors and controllers to smart cameras or industrial computers.

Terminal devices can be connected to edge nodes, supporting access through the Modbus protocol and unified management.

## Device Twin

Device twin refers to the dynamic data of terminal devices, including proprietary real-time data such as the on/off status of a light. This data can also be referred to as the twin properties of the terminal device.

Device twin has the same characteristics as physical devices, facilitating better communication between terminal devices and applications. Commands sent by applications first reach the device twin, which updates its state based on the expected state set by the application. Additionally, the terminal device provides real-time feedback on its actual state, and the device twin simultaneously records the expected and actual values of the terminal device. When the terminal device comes online again after being offline, its state is synchronized with the device twin.


In the CloudEdge Collaboration module, terminal devices can be created and associated with edge nodes. Once associated, the twin property information of the associated devices is stored on the edge node. Applications running on the edge node can access the actual values of the device twin properties and modify the desired values to change the device's state.

## Workflow

The typical steps for managing and controlling terminal devices are as follows:

1. Create terminal devices.
2. Associate terminal devices with edge nodes.
3. Manage and control terminal devices, monitor their statuses.

Next step: [Create Terminal Devices](create-device.md)
