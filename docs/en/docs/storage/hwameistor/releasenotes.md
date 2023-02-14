# Hwameistor Release Notes

This page lists the Release Notes related to Hwameistor, so that you can understand the evolution path and feature changes of each version.

## 2022-12-30

### v0.7.1

#### new function

- **Added** Hwameistor DashBoard UI, which can display the usage status of storage resources and storage nodes.

- **New** interface to manage Hwameistor storage nodes, local disks, and migration records.

- **Added** storage pool management function, which supports the interface to display the basic information of the storage pool and the corresponding node information of the storage pool.

- **Added** local volume management function, which supports the interface to perform data volume migration and high availability conversion.

#### Optimization

- **Optimize** Unnecessary logs before data migration, and avoid the impact of Job execution under other Namespaces.
