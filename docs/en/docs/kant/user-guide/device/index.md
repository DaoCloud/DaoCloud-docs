# End Device Overview

## End Device

End device can range from sensors and controllers to smart cameras or industrial computers.

End device can be connected to edge nodes, supporting access through the Modbus protocol and unified management.

## Device Twin

Device twin refers to the dynamic data of end device, including proprietary real-time data such as
the on/off status of a light. This data can also be referred to as the twin properties of the end device.

Device twin has the same characteristics as physical device, facilitating better communication between
end device and applications. Commands sent by applications first reach the device twin, which updates
its state based on the expected state set by the application. Additionally, the end device provides
real-time feedback on its actual state, and the device twin simultaneously records the expected and
actual values of the end device. When the end device comes online again after being offline, its state
is synchronized with the device twin.

In the CloudEdge Collaboration module, end device can be created and associated with edge nodes.
Once associated, the twin property information of the associated device is stored on the edge node.
Applications running on the edge node can access the actual values of the device twin properties and
modify the desired values to change the device's state.

## Workflow

The typical steps for managing and controlling end device are as follows:

1. Create an end device.
2. Associate the end device with an edge node.
3. Manage and control the end device, monitor its status.

Next step: [Create End Device](create-device.md)
