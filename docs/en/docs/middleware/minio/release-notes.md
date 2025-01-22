---
MTPE: windsonsea
date: 2024-01-05
---

# MinIO object storage Release Notes

This page lists the Release Notes of MinIO object storage, so that you can understand the evolution path and feature changes of each version.

*[mcamel-minio]: "mcamel" is the dev name for DaoCloud's middlewares, and "minio" is a light-weight middleware that provides object storage services

## 2024-09-30

### v0.19.0

- **Fixed** an issue with permission leakage when querying the MinIO list by selecting a workspace
- **Fixed** an issue with missing audit logs for certain operations

## 2024-08-31

### v0.18.1

- **Improved** the process so that abnormal clusters cannot be selected when creating instances
- **Fixed** the error in the `minio operator` multi-replica exit mechanism, adjusting it to single-replica mode.

## 2024-07-31

### v0.17.0

- **Fixed** incorrect MinIO image address after cluster restart

## 2024-04-30

### v0.14.0

- **Added** a prompt for namespace quota

## 2024-03-31

### v0.13.0

- **Improved** Prevent reading MySQL password when user permissions are insufficient

## 2024-01-31

### v0.12.0

- **Improved** Support for Chinese Dashboard in MinIO instances
- **Improved** Added display of MinIO version in global management

## 2023-12-31

### v0.11.0

- **Updated** MinIO Operator version to v5.0.11
- **Fixed** an issue where validation for special characters in input fields was not working when creating instances.

## 2023-11-30

### v0.10.0

- **Added** support for recording operation audit logs
- **Improved** prompt when instance list information is not obtained

## 2023-10-31

### v0.9.0

- **Added** offline upgrade functionality
- **Added** restart functionality for instances
- **Added** PVC resizing
- **Added** support for managing external instances
- **Fixed** Pod list display to show Host IP
- **Fixed** cloudshell permissions issue

## 2023-09-30

### v0.8.1

- **Improved** relok8s file
- **Upgraded** Operator image to v5.0.6

## 2023-08-31

### v0.8.0

- **Improved** syntax compatibility for KindBase
- **Improved** page display during operator creation process
- **Upgraded** Operator image to v5.0.6

## 2023-07-31

### v0.7.3

- **Added** access restrictions for UI interface

## 2023-06-30

### v0.7.0

- **Added** integration with the global management audit log module
- **Improved** interfering elements and added time range selection to monitoring charts

## 2023-04-27

### v0.5.1

- **Added** __mcamel-minio__ details page displays related events
- **Added** __mcamel-minio__ supports custom roles
- **Improved** __mcamel-minio__ scheduling strategy adds a sliding button

## 2023-03-28

### v0.4.1

- **Fixed** __mcamel-minio__ page showing wrong LoadBalancer address.
- **Fixed** __mcamel-minio__ should not verify wild storage configuration when removing MinIO.
- **Fixed** __mcamel-minio__ fixed to create Bucket occasionally failed.
- **Upgraded** __mcamel-minio__ golang.org/x/net to v0.7.0.

## 2023-02-23

### v0.3.0

- **Added** __mcamel-minio__ helm-docs template file.
- **Added** Operators from the __mcamel-minio__ app store can only be installed on mcamel-system.
- **Added** __mcamel-minio__ supports cloud shell.
- **Added** __mcamel-minio__ supports separate registration of navigation bar.
- **Added** __mcamel-minio__ supports viewing logs.
- **Added** __mcamel-minio__ Operator docking with chart-syncer.
- **Fixed** an issue that __mcamel-minio__ instance name is too long and the custom resource cannot be created.
- **Fixed** __mcamel-minio__ workspace Editor users cannot view instance password.
- **Upgraded** __mcamel-minio__ upgrades the offline mirror detection script.
- **Added** log view operation instructions, support custom query, export and other features.

## 2022-12-25

### v0.2.0

- **Added** __mcamel-minio__ NodePort port conflict early detection.
- **Added** __mcamel-minio__ node affinity configuration.
- **Fixed** __mcamel-minio__ fixes the problem that the status display is abnormal when a single instance is used.
- **Fixed** __mcamel-minio__ did not verify name when creating instance.
- **Improved** __mcamel-minio__ cancels the authentication information input box.

## 2022-11-28

### v0.1.4

- **Improved** the front-end interface, whether the sc list can be expanded
- **Improved** password validation adjusted to MCamel medium password strength
- **Added** Configure Bucket when creating MinIO cluster
- **Added** public field when returning list or details
- **Added** Return to alert list
- **Added** Validation Service annotation
- **Fixed** When creating MinIO, the password check is adjusted from between to length
- **Improved** the copy function
- **Improved** instance details - access settings, remove cluster IPv4
- **Improved** Middleware password verification difficulty adjustment
- **Added** minio supports built-in BUCKET creation when creating
- **Added** Docking alert capability
- **Added** the feature of judging whether sc supports capacity expansion and prompting in advance
- **Improved** the prompt logic of installation environment check & adjust its style
- **Improved** middleware style walkthrough optimization

## 2022-11-08

### v0.1.2

- **Added** interface to get user list
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
- **Improved** Improve the feature of the calculator
