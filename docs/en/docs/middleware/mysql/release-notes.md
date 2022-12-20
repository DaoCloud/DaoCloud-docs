# MySQL Release Notes

This page lists the Release Notes of the MySQL database, so that you can understand the evolution path and feature changes of each version.

##v0.4

Release date: 2022-11-08

### APIs

- **NEW** Added MySQL lifecycle management interface function
- **NEW** Added MySQL details interface function
- **Add** docking insight based on grafana crd
- **NEW** Add interface with ghippo service
- **NEW** Add an interface with kpanda
- **NEW** Increased single-test coverage to 30%
- **NEW** Added backup and restore function
- **NEW** Added backup configuration interface
- **NEW** Added backup and restore source field in instance list interface
- **NEW** Add interface to get user list
- **Add** `mysql-operator` chart parameter to specify the metric exporter image
- **New** support arm64 architecture
- **NEW** Added arm64 operator image packaging
- **NEW** Added support for password desensitization
- **NEW** Added support for service exposure as nodeport
- **NEW** Added support for mtls
- **Fix** Fix fuzzy search of backup list interface invalid
- **FIX** Fix dependency bug
- **FIXED** After the backup job is deleted, the backup task list cannot be displayed
- **Optimize** uniformly adjust the timestamp api field to int64
- **IMPROVED** The problem that the image cannot be grabbed when it has uppercase and numbers

### Documentation

- **NEW** First release of documentation website
- **NEW** Basic concept
- **Added** Concepts
- **Added** First time using MySQL
- **NEW** Delete MySQL instance

## v0.3

Release date: 2022-10-18

### APIs

- **NEW** Added MySQL lifecycle management interface function
- **NEW** Added MySQL details interface function
- **Add** docking insight based on grafana crd
- **NEW** Add interface with ghippo service
- **NEW** Add an interface with kpanda
- **NEW** Increased single-test coverage to 30%
- **NEW** Added backup and restore function
- **NEW** Added backup configuration interface
- **NEW** Added backup and restore source field in instance list interface
- **Fix** Fix fuzzy search of backup list interface invalid
- **Optimize** uniformly adjust the timestamp api field to int64

### Documentation

- **NEW** First release of documentation website
- **NEW** Basic concept
- **Added** Concepts
- **Added** First time using MySQL
- **NEW** Delete MySQL instance