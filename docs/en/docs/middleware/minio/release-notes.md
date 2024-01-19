---
MTPE: windsonsea
date: 2024-01-05
---

# MinIO object storage Release Notes

This page lists the Release Notes of MinIO object storage, so that you can understand the evolution path and feature changes of each version.

*[mcamel-minio]: "mcamel" is the dev name for DaoCloud's middlewares, and "minio" is a light-weight middleware that provides object storage services

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

- **Added** `mcamel-minio` details page displays related events
- **Added** `mcamel-minio` supports custom roles
- **Improved** `mcamel-minio` scheduling strategy adds a sliding button

## 2023-03-28

### v0.4.1

- **Fixed** `mcamel-minio` page showing wrong LoadBalancer address.
- **Fixed** `mcamel-minio` should not verify wild storage configuration when removing MinIO.
- **Fixed** `mcamel-minio` fixed to create Bucket occasionally failed.
- **Upgraded** `mcamel-minio` golang.org/x/net to v0.7.0.

## 2023-02-23

### v0.3.0

- **Added** `mcamel-minio` helm-docs template file.
- **Added** Operators from the `mcamel-minio` app store can only be installed on mcamel-system.
- **Added** `mcamel-minio` supports cloud shell.
- **Added** `mcamel-minio` supports separate registration of navigation bar.
- **Added** `mcamel-minio` supports viewing logs.
- **Added** `mcamel-minio` Operator docking with chart-syncer.
- **Fixed** an issue that `mcamel-minio` instance name is too long and the custom resource cannot be created.
- **Fixed** `mcamel-minio` workspace Editor users cannot view instance password.
- **Upgraded** `mcamel-minio` upgrades the offline mirror detection script.
- **Added** log view operation instructions, support custom query, export and other features.

## 2022-12-25

### v0.2.0

- **Added** `mcamel-minio` NodePort port conflict early detection.
- **Added** `mcamel-minio` node affinity configuration.
- **Fixed** `mcamel-minio` fixes the problem that the status display is abnormal when a single instance is used.
- **Fixed** `mcamel-minio` did not verify name when creating instance.
- **Improved** `mcamel-minio` cancels the authentication information input box.

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
