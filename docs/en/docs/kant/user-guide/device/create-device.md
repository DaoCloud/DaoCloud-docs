# Creating End Device

End device can be connected to edge nodes and support access via the Modbus protocol.
Once an end device is connected, it can be managed centrally in the cloud management plane.

This article describes the steps to create end device and bind them to edge nodes.

## Creating End Device

The steps are as follows:

1. Go to the edge unit details page and select the left menu `Edge Resources` -> `End Device`.

2. Click the `Create Device` button at the top right corner of the end device list.

3. Fill in the basic information.

    - Device Name: A combination of lowercase letters, numbers, hyphens (-), and dots (.), and it should not have consecutive separators. It should start and end with a letter or number. contains a maximum of 253 characters.
    - Access Protocol: The current platform supports Modbus protocol for device access.
    - Namespace: The namespace where the device is located. Namespaces isolate resources from each other.
    - Description: Device description information.

4. Fill in the device configuration, and you can add device twin properties and tags.

    - Device Twin Properties: Optional. Refers to the dynamic data of the end device, including proprietary real-time data such as the on/off state of a light, temperature, and humidity readings from a sensor, etc.
    - Tags: Optional. Classify and manage different device by assigning tags to them.

    To add a device twin property, you can select the corresponding register type based on the
    device type and fill in the corresponding parameters. The parameter descriptions are as follows:

    - Register Type: Modbus protocol device register types include Coil Registers, Discrete Input Registers, Holding Registers, and Input Registers.
    - Property Name: Required. The name of the device property.
    - Property Value: Required. The desired value of the property, based on the data type of the register type.
    - Access Method: Default value. Varies based on the default access method for the register type.
    - Register Address: Required. The starting data bit corresponding to the property.
    - Collection Interval: Optional. Specifies the interval at which the device collects and reports data.
    - Swap High/Low Bytes: Swap the two-byte contents in each register obtained.
    - Reverse Register Order: Reverse the order of all registers obtained from high to low.
    - Property Value Range: Limit the range of the original data obtained.
    - Scaling Factor: Scale the original data obtained.

5. Fill in the device access configuration.

    The Modbus protocol has two transmission modes: RTU and TCP. The access configuration differs between the two modes.

    - Slave ID: The identification field when accessing register values.

    **RTU Transmission Mode:**

    - Serial Port: The serial port to which the end device is connected. Different values can be selected depending on the operating system of the edge node.
    - Baud Rate: The number of symbol elements transmitted per second, which measures the data transfer rate.
    - Data Bits: A parameter that measures the actual data bits in communication.
    - Parity: A simple error-checking mechanism used to determine if there is noise interference during communication or if there is a synchronization issue between transmitting and receiving data.
    - Stop Bits: Represents the last bit of a single data packet.

    **TCP Transmission Mode:**

    - IP Address: The IP address of the end device.
    - Port: The port of the end device.

6. Confirm the information and click `Create` if the configured information is correct to complete the device creation.

## Binding End Device to Edge Nodes

An end device can only be bound to one edge node. After the device is bound to a node, applications deployed on the node can retrieve real-time data from the device using the device twin created in the cloud.

The steps are as follows:

1. Go to the edge unit details page and select the left menu `Edge Resources` -> `End Device`.

2. On the right side of the end device list, click the `⋮` button and select `Bind Node` from the popup menu.

3. In the dialog box, select the node to bind and click `OK` to complete the binding of the edge node.

Next step: [Managing End Device](manage-device.md)
