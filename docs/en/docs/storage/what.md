# Cloud Native Storage

## Types of Cloud Native Storage

1. **Traditional storage cloud-native**: This type docks with the Kubernetes platform through the CSI standard and is relatively common. Users can use existing storage and, based on traditional storage, provide stable cloud-native storage with a strong SLA guarantee.

2. **Software-defined storage cloud-native**: Compatible with traditional applications and cloud-native applications, this type interfaces with Kubernetes based on the CSI standard. Software-defined storage uses the disk space on each machine in the enterprise through the network, forming scattered storage resources into a virtual storage device, with data scattered across different storage devices.

3. **Pure cloud-native storage**: This type of storage is naturally born for cloud-native and built on the cloud-native platform to better fit its characteristics. It can be migrated with the application Pod, has high scalability and high availability, but lower reliability than traditional storage accessed through the CSI standard.

## DCE Cloud Native Storage

DCE 5.0 cloud-native storage is based on the Kubernetes CSI standard and can be connected to CSI-compliant storage according to different SLA requirements and use cases. The cloud-native local storage launched by DaoCloud naturally has cloud-native features and meets the characteristics of high scalability and high availability in container use cases.
