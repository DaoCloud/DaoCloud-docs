# End Device Overview

## End Device

End device can range from sensors and controllers to smart cameras or industrial computers.

End device can be connected to edge nodes. You can connect them through the Modbus protocol and manage them centrally.

## Device Model

A device model is a digital representation of an end device in the cloud. It abstracts the common characteristics
of the device into a data model, using attributes to define the device and the information it can provide externally.

## Device Twin

Device twin refers to the dynamic data of end device, including proprietary real-time data such as
the on/off status of a light. This data can also be referred to as the twin attributes of the end device.

Device twin has the same characteristics as physical device, facilitating better communication between
end device and applications. Commands sent by applications first reach the device twin, which updates
its state based on the expected state set by the application. Additionally, the end device provides
real-time feedback on its actual state, and the device twin simultaneously records the expected and
actual values of the end device. When the end device comes online again after being offline, its state
is synchronized with the device twin.

In DCE 5.0 Cloud Edge Collaboration module, end device can be created and associated with edge nodes.
Once associated, the twin attribute information of the associated device is stored on the edge node.
Applications running on the edge node can access the actual values of the device twin attributes and
modify the desired values to change the device's state.

## Workflow

The typical steps for managing and controlling end device are as follows:

1. Create device models
2. Create end devices
3. Associate end devices with edge nodes
4. Manage and control end devices, and monitor device status

Next step: [Create End Device](create-device.md)
