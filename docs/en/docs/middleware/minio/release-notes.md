# MinIO object storage Release Notes

This page lists the Release Notes of MinIO object storage, so that you can understand the evolution path and feature changes of each version.

## v0.4.1

Release date: 2023-03-28

### APIs

- **Fixed** `mcamel-minio` page showing wrong LoadBalancer address.
- **Fixed** `mcamel-minio` should not verify wild storage configuration when removing MinIO.
- **FIX** `mcamel-minio` fixed to create Bucket occasionally failed.

### other

- **Upgrade** `mcamel-minio` golang.org/x/net to v0.7.0.

## v0.3.0

Release date: 2023-02-23

### APIs

- **Added** `mcamel-minio` helm-docs template file.
- **Added** Operators from the `mcamel-minio` app store can only be installed on mcamel-system.
- **NEW** `mcamel-minio` supports cloud shell.
- **NEW** `mcamel-minio` supports separate registration of navigation bar.
- **NEW** `mcamel-minio` supports viewing logs.
- **Added** `mcamel-minio` Operator docking with chart-syncer.
- **Fix** the problem that `mcamel-minio` instance name is too long and the custom resource cannot be created.
- **Fix** `mcamel-minio` workspace Editor users cannot view instance password.
- **Upgrade** `mcamel-minio` upgrades the offline mirror detection script.

### Documentation

- **Add** log view operation instructions, support custom query, export and other functions.

## v0.2.0

Release date: 2022-12-25

### APIs

- **NEW** `mcamel-minio` NodePort port conflict early detection.
- **NEW** `mcamel-minio` node affinity configuration.
- **Fix** `mcamel-minio` fixes the problem that the status display is abnormal when a single instance is used.
- **FIXED** `mcamel-minio` did not verify name when creating instance.

### UI

- **Optimize** `mcamel-minio` cancels the authentication information input box.

## v0.1.4

Release date: 2022-11-28

- **Improve** Update the front-end interface, whether the sc list can be expanded
- **IMPROVED** Password validation adjusted to MCamel medium password strength
- **NEW** Configure Bucket when creating MinIO cluster
- **Add** public field when returning list or details
- **NEW** Return to alarm list
- **Add** Validation Service annotation
- **Fix** When creating MinIO, the password check is adjusted from between to length
- **Improved** Improve and optimize the copy function
- **IMPROVED** instance details - access settings, remove cluster IPv4
- **Improved** Middleware password verification difficulty adjustment
- **New** minio supports built-in BUCKET creation when creating
- **NEW** Docking alarm capability
- **New** Added the function of judging whether sc supports capacity expansion and prompting in advance
- **Optimize** Optimize the prompt logic of installation environment detection & adjust its style
- **Optimize** middleware style walkthrough optimization

## v0.1.2

Release date: 2022-11-08

- **NEW** Add interface to get user list
- **New** minio instance creation
- **Add** modification of minio instance
- **Add** delete of minio instance
- **Add** configuration modification of minio instance
- **New** minio instances support nodeport's svc
- **Added** monitoring data export of minio instance
- **Add** monitoring and viewing of minio instances
- **Add** Multi-tenant global management docking
- **Add** mcamel-minio-ui create/list/modify/delete/view
- **NEW** APIServer/UI supports mtls
- **Fix** In singleton mode, there is only one pod, fix the problem that grafana cannot obtain data
- **Optimization** Improve the function of the calculator
