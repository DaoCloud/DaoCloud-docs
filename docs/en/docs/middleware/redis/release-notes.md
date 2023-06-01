# Redis Cache Service Release Notes

This page lists the Release Notes of the Redis cache service, so that you can understand the evolution path and feature changes of each version.

##v0.7.1

Release date: 2023-04-27

### new function

- **NEW** `mcamel-redis` details page displays related events
- **NEW** `mcamel-redis` list interface supports Cluster and Namespace field filtering
- **Added** `mcamel-redis` custom role

#### fix

- **Fix** `mcamel-redis` optimizes the scheduling strategy and adds a sliding button

## v0.6.2

Release date: 2023-03-29

### new function

- **NEW** `mcamel-redis` supports automatic backup and restore.

#### fix

- **FIXED** Offline mirrors not exported for backup restore.
- **Fix** `mcamel-redis` does not export offline mirror for backup restore.
- **Fix** `mcamel-redis` fixes several known issues, improves system stability and security.

### Documentation

- **NEW** Added backup function documentation.

## v0.5.0

Release date: 2023-02-23

### APIs

- **Added** `mcamel-redis` helm-docs template file.
- **Added** Operators in the `mcamel-redis` app store can only be installed on mcamel-system.
- **NEW** `mcamel-redis` supports cloud shell.
- **NEW** `mcamel-redis` supports separate registration of navigation bar.
- **NEW** `mcamel-redis` supports viewing logs.
- **NEW** `mcamel-redis` updated singleton/cluster mode Operator version.
- **NEW** `mcamel-redis` displays common Redis clusters.
- **Added** `mcamel-redis` Operator docking with chart-syncer.
- **Fix** the problem that `mcamel-redis` instance name is too long and the custom resource cannot be created.
- **FIXED** `mcamel-redis` workspace Editor user cannot see instance password.
- **Fix** `mcamel-redis` could not parse the correct Redis version number.
- **Fix** the problem that `mcamel-redis` cannot modify Port.
- **Upgrade** `mcamel-redis` upgrade offline mirror detection script.

### Documentation

- **Add** log view operation instructions, support custom query, export and other functions.

## v0.4.0

Release date: 2022-12-25

### APIs

- **NEW** `mcamel-redis` NodePort port conflict early detection.
- **NEW** `mcamel-redis` node affinity configuration.
- **Fix** `mcamel-redis` singleton and cluster setting nodeport invalid issue.
- **Fixed** the problem that the slave node cannot be set to 0 in `mcamel-redis` cluster mode.

##v0.2.6

Release date: 2022-11-28

### APIs

- **FIXED** Some field errors when updating Redis
- **IMPROVED** Password validation adjusted to MCamel low password strength
- **Improve** Improve the version dependency of sentinel mode, v1.1.1=>v1.2.2, the important change is to support k8s 1.25+
- **NEW** Support to install Redis cluster in active/standby mode in ARM environment
- **New** sc expansion prompt
- **Add** public field when returning list or details
- **NEW** Add return alert list
- **Add** Validation Service annotation
- **Fix** service address display error

##v0.2.2

Release date: 2022-10-26

### APIs

- **NEW** Add interface to get user list
- **New** support arm architecture
- **Add** Redis instance full life cycle management
- **Add** monitoring deployment of redis instance
- **New** supports redis sentinel, singleton and cluster one-click deployment
- **NEW** Support ws permission isolation
- **New** supports online dynamic expansion
- **upgrade** release notes script