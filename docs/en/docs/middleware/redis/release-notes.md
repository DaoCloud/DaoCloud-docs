# Redis Cache Service Release Notes

This page lists the Release Notes of the Redis cache service, so that you can understand the evolution path and feature changes of each version.

## v0.6.2

Release date: 2023-03-29

### new function

- **Added** `mcamel-redis` supports automatic backup and restore.

#### Fix

- **Fixed** Offline mirrors not exported for backup restore.
- **Fixed** `mcamel-redis` does not export offline mirror for backup restore.
- **Fixed** `mcamel-redis` fixes several known issues, improves system stability and security.

### Documentation

- **Added** Added backup function documentation.

## v0.5.0

Release date: 2023-02-23

### APIs

- **Added** `mcamel-redis` helm-docs template file.
- **Added** Operators in the `mcamel-redis` app store can only be installed on mcamel-system.
- **Added** `mcamel-redis` supports cloud shell.
- **Added** `mcamel-redis` supports separate registration of navigation bar.
- **Added** `mcamel-redis` supports viewing logs.
- **Added** `mcamel-redis` updated singleton/cluster mode Operator version.
- **Added** `mcamel-redis` displays common Redis clusters.
- **Added** `mcamel-redis` Operator docking with chart-syncer.
- **Fixed** the problem that `mcamel-redis` instance name is too long and the custom resource cannot be created.
- **Fixed** `mcamel-redis` workspace Editor user cannot see instance password.
- **Fixed** `mcamel-redis` could not parse the correct Redis version number.
- **Fixed** the problem that `mcamel-redis` cannot modify Port.
- **Upgrade** `mcamel-redis` upgrade offline mirror detection script.

### Documentation

- **Added** log view operation instructions, support custom query, export and other functions.

## v0.4.0

Release date: 2022-12-25

### APIs

- **Added** `mcamel-redis` NodePort port conflict early detection.
- **Added** `mcamel-redis` node affinity configuration.
- **Fixed** `mcamel-redis` singleton and cluster setting nodeport invalid issue.
- **Fixed** the problem that the slave node cannot be set to 0 in `mcamel-redis` cluster mode.

## v0.2.6

Release date: 2022-11-28

### APIs

- **Fixed** Some field errors when updating Redis
- **Optimized** Password validation adjusted to MCamel low password strength
- **Improve** Improve the version dependency of sentinel mode, v1.1.1=>v1.2.2, the important change is to support k8s 1.25+
- **Added** Support to install Redis cluster in active/standby mode in ARM environment
- **Added** sc expansion prompt
- **Added** public field when returning list or details
- **Added** Add return alarm list
- **Added** Validation Service annotation
- **Fixed** service address display error

## v0.2.2

Release date: 2022-10-26

### APIs

- **Added** Add interface to get user list
- **Added** support arm architecture
- **Added** Redis instance full life cycle management
- **Added** monitoring deployment of redis instance
- **Added** supports redis sentinel, singleton and cluster one-click deployment
- **Added** Support ws permission isolation
- **Added** supports online dynamic expansion
- **upgrade** release notes script