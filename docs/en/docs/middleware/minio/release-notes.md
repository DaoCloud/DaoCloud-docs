# MinIO object storage Release Notes

This page lists the Release Notes of MinIO object storage, so that you can understand the evolution path and feature changes of each version.

## 2023-11-30

### v0.10.0

#### Improvements

- **Added** support for recording operation audit logs
- **Improved** prompt when instance list information is not obtained

## 2023-10-31

### v0.9.0

#### Improvements

- **New** Added offline upgrade functionality.
- **New** Added restart functionality for instances.
- **New** Added PVC resizing.
- **New** Added support for managing external instances.
- **Bug Fix** Fixed Pod list display to show Host IP.
- **Bug Fix** Fixed cloudshell permissions issue.

## 2023-09-30

### v0.8.1

#### Improvements

- **Optimization:** Added relok8s file.

#### Upgrade

- **Upgrade:** Upgraded Operator image to v5.0.6.

## 2023-08-31

### v0.8.0

#### Improvements

- **Improved** Syntax compatibility for KindBase.
- **Improved** Page display during operator creation process.

#### Upgrade

- **Upgraded** Operator image to v5.0.6.

## 2023-07-31

### v0.7.3

#### New Features

- **Added** Access restrictions for UI interface.

## 2023-06-30

### v0.7.0

#### New Features

- **Added**: Integrated with the global management audit log module.

#### Improvements

- **Improved**: Removed interfering elements and added time range selection to monitoring charts.

## 2023-04-27

### v0.5.1

#### New features

- **Added** `mcamel-minio` details page displays related events
- **Added** `mcamel-minio` supports custom roles

#### Optimization

- **Optimized** `mcamel-minio` scheduling strategy adds a sliding button

## v0.4.1

Release date: 2023-03-28

### APIs

- **Fixed** `mcamel-minio` page showing wrong LoadBalancer address.
- **Fixed** `mcamel-minio` should not verify wild storage configuration when removing MinIO.
- **Fixed** `mcamel-minio` fixed to create Bucket occasionally failed.

### Other

- **Upgraded** `mcamel-minio` golang.org/x/net to v0.7.0.

## v0.3.0

Release date: 2023-02-23

### APIs

- **Added** `mcamel-minio` helm-docs template file.
- **Added** Operators from the `mcamel-minio` app store can only be installed on mcamel-system.
- **Added** `mcamel-minio` supports cloud shell.
- **Added** `mcamel-minio` supports separate registration of navigation bar.
- **Added** `mcamel-minio` supports viewing logs.
- **Added** `mcamel-minio` Operator docking with chart-syncer.
- **Fixed** the problem that `mcamel-minio` instance name is too long and the custom resource cannot be created.
- **Fixed** `mcamel-minio` workspace Editor users cannot view instance password.
- **Upgraded** `mcamel-minio` upgrades the offline mirror detection script.

### Documentation

- **Added** log view operation instructions, support custom query, export and other features.

## v0.2.0

Release date: 2022-12-25

### APIs

- **Added** `mcamel-minio` NodePort port conflict early detection.
- **Added** `mcamel-minio` node affinity configuration.
- **Fixed** `mcamel-minio` fixes the problem that the status display is abnormal when a single instance is used.
- **Fixed** `mcamel-minio` did not verify name when creating instance.

### UI

- **Optimized** `mcamel-minio` cancels the authentication information input box.

## v0.1.4

Release date: 2022-11-28

- **Optimized** Update the front-end interface, whether the sc list can be expanded
- **Optimized** Password validation adjusted to MCamel medium password strength
- **Added** Configure Bucket when creating MinIO cluster
- **Added** public field when returning list or details
- **Added** Return to alert list
- **Added** Validation Service annotation
- **Fixed** When creating MinIO, the password check is adjusted from between to length
- **Optimized** Improve and optimize the copy function
- **Optimized** instance details - access settings, remove cluster IPv4
- **Optimized** Middleware password verification difficulty adjustment
- **Added** minio supports built-in BUCKET creation when creating
- **Added** Docking alert capability
- **Added** Added the feature of judging whether sc supports capacity expansion and prompting in advance
- **Optimized** Optimize the prompt logic of installation environment check & adjust its style
- **Optimized** middleware style walkthrough optimization

## v0.1.2

Release date: 2022-11-08

- **Added** Add interface to get user list
- **Added** minio instance creation
- **Added** modification of minio instance
- **Added** delete of minio instance
- **Added** configuration modification of minio instance
- **Added** minio instances support nodeport's svc
- **Added** monitoring data export of minio instance
- **Added** monitoring and viewing of minio instances
- **Added** Multi-tenant global management docking
- **Added** mcamel-minio-ui create/list/modify/delete/view
- **Added** APIServer/UI supports mtls
- **Fixed** In singleton mode, there is only one pod, fix the problem that grafana cannot obtain data
- **Optimized** Improve the feature of the calculator