# Hwameistor Release Notes

This page lists the Release Notes related to Hwameistor, so that you can understand the evolution path and feature changes of each version.

## 2023-3-30

### v0.9.2

#### Optimization

- **ADD** UI relok8s

### v0.9.1

#### Optimization

- **Added** Volume Status monitoring [Issue#741](https://github.com/hwameistor/hwameistor/pull/741)
- **Fix** Local Storage deployment parameter [Issue #742](https://github.com/hwameistor/hwameistor/pull/742)

### v0.9.0

#### Features

- **NEW** Disk Owner [Issue #681](https://github.com/hwameistor/hwameistor/pull/681)
- **Added** Grafana DashBoard [Issue #733](https://github.com/hwameistor/hwameistor/pull/733)
- **Add** Operator installation method, automatically pull UI when installing [Issue #679](https://github.com/hwameistor/hwameistor/pull/679)
- **Added** UI application Label [Issue #710](https://github.com/hwameistor/hwameistor/pull/710)

#### Optimization

- **Added** disk used capacity [Issue #681](https://github.com/hwameistor/hwameistor/pull/681)
- **Optimize** Skip scoring mechanism when no available disk is found [Issue #724](https://github.com/hwameistor/hwameistor/pull/724)
- **SET** DRDB port defaults to 43001 [Issue #723](https://github.com/hwameistor/hwameistor/pull/723)

## 2023-1-30

### v0.8.0

#### Optimization

- **Optimized** Chinese documentation
- **optimized** value.yaml file
- **UPDATE** Roadmap
- **Optimization** When the installation fails, set the default failure policy

## 2022-12-30

### v0.7.1

#### Features

- **Added** Hwameistor DashBoard UI, which can display the usage status of storage resources and storage nodes.

- **New** interface to manage Hwameistor storage nodes, local disks, and migration records.

- **Added** storage pool management function, which supports the interface to display the basic information of the storage pool and the corresponding node information of the storage pool.

- **Added** local volume management function, which supports the interface to perform data volume migration and high availability conversion.

#### Optimization

- **Optimize** Unnecessary logs before data migration, and avoid the impact of Job execution under other Namespaces.
