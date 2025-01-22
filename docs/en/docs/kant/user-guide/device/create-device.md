---
MTPE: FanLin
Date: 2024-01-05
---

# Create End Device

End device can be connected to edge nodes and support access via the Modbus protocol.
Once an end device is connected, it can be managed centrally in the cloud management plane.

This article describes the steps to create end device and bind them to edge nodes.

## Create an End Device

Follow these steps to create an end device:

1. Navigate to the edge unit details page and select __Edge Resources__ -> __End Devices__ from the left menu.

2. Click the __Create Device__ button located at the top right corner of the end device list.

    <!--add image later-->

3. Fill in __Basic Information__ .

    - __Device Name__ : Use a combination of lowercase letters, numbers, hyphens (-), and periods (.). Avoid consecutive symbols and ensure the name starts and ends with a letter or number. It can have a maximum of 253 characters.
    - __Namespace__ : Specify the namespace where the device resides. Namespaces help isolate resources from each other.
    - __Device Model__ : The associated device model.
    - __Protocol__ : The protocol of the associated device model will be automatically filled in and cannot be modified here.
    - __Description__ : Provide a brief description of the device.

    <!--add image later-->

4. Fill in __Device Settings__ , and you can click __Add Twins__ and __Tag__ .

    - __Twin Attributes__ : Optional. Refers to the dynamic data of the end device, including proprietary real-time data such as the on/off state of a light, temperature, and humidity readings from a sensor.
    - __Tag__ : Optional. Classify and manage different device by assigning labels to them.

    ![Basic Info](../images/create-device-03.png)

    To add twins attributes, you can select the corresponding register type based on the
    device type and fill in the corresponding parameters. The parameter descriptions are as follows:

    - __Attribute Name__ : Required. The device attribute name.
    - __Desired Value__ : Optional. The desired value of the attribute, which can be filled when the access permission is Read or Write.
    - __Collection Interval__ : Optional. The interval at which data is collected from the device.
    - __Report Cycle__ : Optional. The interval at which data is reported from the device.
    - __Visitors__ : The method used to access the device attribute must be consistent with the mapper's access method when the platform is connected to the device.

    <!--add image later-->

5. Fill in __Access Settings__ .

    The access parameters for the platform to connect to the device should be provided in YAML format as follows:

    <!--add image later-->

6. Verify that the configured information is correct, then click __OK__ to complete the device creation.

    ![Confirm Creation](../images/create-device-07.png)

## Binding End Device to Edge Nodes

An end device can be associated with only one edge node. Once the device is bound to a node, applications deployed on that node can access real-time data from the device using the device twin created in the cloud.

The steps are as follows:

1. Go to the edge unit details page and select the left menu __Edge Resources__ -> __End Devices__ .

2. On the right side of the end device list, click the __┇__ button and select __Bind Node__ from the popup menu.

3. In the dialog box, select the node to bind and click __OK__ to complete the binding of the edge node.

    ![Bind Node](../images/create-device-08.png)

Next step: [Manage End Device](manage-device.md)
