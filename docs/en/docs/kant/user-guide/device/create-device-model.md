---
MTPE: WANG0608GitHub
Date: 2024-07-30
---

# Create Device Model

A device model is a digital representation of an end device in the cloud, abstracting the common characteristics of the device into a data model, using attributes to define the device and the information it can provide externally.

This article introduces the steps to create a device model. The process is as follows:

1. Go to the edge unit details page and select __Edge Resources__ -> __Device Models__ from the left menu.

2. Click the __Create Device Model__ in the upper right corner of the end device list.

    <!--add image later-->

3. Fill in the basic information.

    - __Model Name__ : A combination of lowercase letters, numbers, hyphens (-), and dots (.), with no consecutive symbols,
    and it must start and end with a letter or number and contain up to 253 characters.
    - __Protocol__ : DCE 5.0 Cloud Edge Collaboration supports the connection of various protocol devices, including Modbus.
    - __Namespace__ : The resources in the namespace where the device is located are isolated from each other.
    - __Description__ : Description information of the device model.

    <!--add image later-->

4. Fill in the device configuration. You can add device __Twin Attributes__ and __Tag__ . Associated device instances can directly reference the model configuration.

    - __Twin Attributes__ : Optional. It refers to the dynamic data of the end device, including proprietary real-time data, such as the on or off state of a light, temperature and humidity of sensors.
    - __Tag__ : Optional. By tagging devices, different devices can be categorizes and managed.

    <!--add image later-->

    Adding Twin Attributes, Users can select the proper register type based on the device type and fill in the proper parameters. The parameter descriptions are as follows:

    - __Name__ : Required. The attribute name of the device.
    - __Type__ : Required. It includes string, int, float, boolean.
    - __Access Mode__ : The access permission for the twin attribute of the device includes Read/Write, Read Only.
    - __Unit__ : Optional. The attribute value unit.
    - __Value Range__ : Limits the range of the acquired raw data.

    <!--add image later-->

Next step: [Create End Devices](./create-device.md)
