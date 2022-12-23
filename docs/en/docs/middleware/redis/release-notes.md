# Redis Cache Service Release Notes

This page lists the Release Notes of the Redis cache service, so that you can understand the evolution path and feature changes of each version.

##v0.2.6

Release date: 2022-11-28

- **FIXED** Some field errors when updating Redis
- **IMPROVED** Password validation adjusted to MCamel low password strength
- **Improve** Improve the version dependency of sentinel mode, v1.1.1=>v1.2.2, the important change is to support k8s 1.25+
- **NEW** Support to install Redis cluster in active/standby mode in ARM environment
- **New** sc expansion prompt
- **Add** public field when returning list or details
- **NEW** Add return alarm list
- **Add** Validation Service annotation
- **Fix** service address display error

##v0.2.2

Release date: 2022-10-26

- **NEW** Add interface to get user list
- **New** support arm architecture
- **Add** Redis instance full lifecycle management
- **Add** monitoring deployment of redis instance
- **New** supports redis sentinel, singleton and cluster one-click deployment
- **NEW** Support ws permission isolation
- **New** supports online dynamic expansion
- **upgrade** release notes script