# Cloud native storage

## Several types of cloud native storage

1. **Traditional storage cloud-native**, docking with the Kubernetes platform through the CSI standard, this type is relatively common, users can use existing storage, and based on traditional storage, the ability to provide cloud-native storage is stable and SLA strong guarantee.
2. **Software-defined storage cloud-native**, software-defined storage, compatible with traditional applications and cloud-native applications. It also interfaces with Kubernetes based on the CSI standard. Software-defined storage uses the disk space on each machine in the enterprise through the network, and forms these scattered storage resources into a virtual storage device, and the data is scattered in different storage devices.
3. **Pure cloud-native storage**, this type of storage is naturally born for cloud-native. It is built on the cloud-native platform, which can better fit the characteristics of cloud-native, and can be migrated with the application Pod. Migration has the following characteristics: high scalability and high availability, but lower reliability than traditional storage accessed through the CSI standard.

## DCE cloud native storage

DCE 5.0 cloud-native storage is based on the Kubernetes CSI standard, and can be connected to CSI-compliant storage according to different SLA requirements and user scenarios.
The cloud-native local storage launched by DaoCloud naturally has cloud-native features and meets the characteristics of high scalability and high availability in container scenarios.

