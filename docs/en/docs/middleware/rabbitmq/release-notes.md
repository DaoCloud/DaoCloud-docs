# RabbitMQ Release Notes

This page lists the Release Notes of the RabbitMQ message queue, so that you can understand the evolution path and feature changes of each version.

## v0.6.4

Release date: 2022-11-28

- **NEW** Add interface to get user list
- **IMPROVED** Password validation adjusted to MCamel medium password strength
- **New** supports multi-architecture images, the configuration method is `depend.arm64-img.rabbitClusterImageFormat: xxxx`
- **New** supports sc expansion interception, when sc does not support expansion, directly intercept it
- **Add** public field when returning list or details
- **Added** return alerts
- **Add** Validation Service annotation
- **FIXED** page console may access wrong port

## v0.6.1

Release date: 2022-10-27

### APIs

- **NEW** Added to increase coverage
- **Add** front-end UI registration function
- **NEW** Performance enhancements
- **NEW** Added pagination function to the list page
- **NEW** Added the function of modifying the configuration
- **NEW** Added the ability to return modifiable ConfigMaps
- **NEW** Change the limitation of creating instances to the cluster level instead of the namespace level
- **NEW** Added splicing function of monitoring address
- **NEW** Added the ability to modify the version number
- **NEW** Modify the underlying update logic to patch logic
- **NEW** RabbitMQ e2e test coverage is about 17.24%
- **NEW** Added RabbitMQ performance pressure test report
- **NEW** Added RabbitMQ bug spot check
- **NEW** Docking ghippo adds workspace interface
- **NEW** Docking insight injected into dashboard through crd
- **Add** uniformly adjust the timestamp api field to int64
- **NEW** Increased single-test coverage to 53%
- **Optimize** Update the release note script and execute the release-process specification

### Documentation

- **NEW** New function description
- **NEW** Create RabbitMQ
- **NEW** RabbitMQ data migration
- **New** instance monitoring
- **NEW** Enter RabbitMQ for the first time
- **Added** Applicable scenarios