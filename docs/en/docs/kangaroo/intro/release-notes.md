# Container Registry Release Notes

This page lists the release notes of the container registry, so that you can
understand the evolution path and feature changes of each version.

## 2023-11-03

### v0.12.0

- **New**: Support for quick deployment of middleware when creating a hosted Harbor in non-platinum versions
- **New**: Best practices for publishing Harbor Nginx configuration
- **New**: Best practices for resource planning when releasing container registries
- **Improvement**: Improved resource validation when creating a hosted Harbor
- **Improvement**: Prompt for installing cert manager as a dependency for Harbor operator

## 2023-09-06

### v0.11.0

- Added harbor hosting status verification
- Added deployment to download station
- Added best practices for Nginx proxy, resource capacity planning
- Optimized fix for the issue preventing updates to hosted Harbor description
- Optimized display of truncated registry space in bootstrap container registry
- Optimized frontend error for WS admin when creating recycle rules

## 2023-08-02

### v0.10

- Added a solution for migrating/backing up/restoring container registry, which has been verified through the migration of the release-ci repository
- Added best practices for logging into non-secure container registry
- Added support for using the internal middleware MINIO when creating hosted Harbor
- Added support for the PG mode of Renmin Jincang
- Improved the format validation for PG and Redis addresses when creating hosted Harbor
- Improved grayed-out and prompt optimization for unauthorized access
- Improved handling of special cases after unbinding clusters

## 2023-07-02

### v0.9

- **Added**: Added support for selecting the middleware `minio` instance when creating managed `harbor`.
- **Added**: Added support for key auditing functionality in `Ghippo`.
- **Improved**: Validated container registry resources under a workspace (WS) when deleting the WS.
- **Improved**: Handled abnormal states of managed `harbor` after unbinding clusters.
- **Fixed**: Fixed the issue where `Ghippo workspace` resources could not be unbound.
- **Fixed**: Fixed the issue with `Sidecar` injection.
- **Fixed**: Fixed the issue where images could not be pushed when selecting `minio` during `harbor` creation.

## 2023-06-05

### v0.8

#### New Features

- Added image description information to the `harbor` type repository.
- Added instance status to the registry space list.
- Added support for randomly generating `nodeport` port numbers when creating a `harbor`.
- Added validation for duplicate usage of `redis`, `postgresql`, and `s3` in the creation of `harbor`.
- Added image recycling feature to the `project`.

#### Fixes

- Fixed the concatenation error in the offline deployment of managed `harbor` image addresses.
- Fixed pagination issue in the `docker registry` type `project` list.
- Fixed search issue in the `docker registry` type `repository`.
- Fixed existing account problem when creating robot accounts.

#### Improvements

- Added job cleanup logic.
- Removed the `project` field from the interface for obtaining temporary login instructions.
- Improved login instructions.
- Optimized logic for image scanning judgment.

## 2023-05-08

### v0.7

#### Features

- Support page configuration image synchronization between multiple instances
- Support for associating `jfrog` type repositories in workspaces
- Support for creating managed `harbor` in offline `ARM` environment

#### Fixes

- Fixed the problem that the registry integration URL could not be updated after modification
- Fixed logical incompatibilities after `Project` was deleted from the native `Harbor` page

#### Optimization

- Optimize the performance of docking `jfrog` interface to within `2s`

## 2023-04-07

### v0.6.2

#### Features

- Support custom roles in global management, granting different role permissions to users
- Support for generating temporary login commands.
- Create managed `harbor` to support `cpu, memory` verification.
- Create hosted `harbor` support for editing image scanners.
- Create hosted `harbor` support for using `S3` storage.

#### Fixes

- Solve the problem that the installation byte of harbor-operator helm is too large

#### Optimization

- Optimize the performance of the image list feature page, and propose a separate `Project` list page

## 2023-03-15

### v0.5

#### Features

- Support creating managed `harbor`, support `NodePort` way to expose, and check whether the port is occupied
- Support creating managed `harbor` and support `https` way to expose
- Support for creating managed `harbor`, support for enabling `DCE 5.0 ODIC` access, and enable `DCE 5.0` users to log in to `Harboor`
- Support for creating managed `harbor` and support for verifying whether `harbor-operator` is installed in the deployed cluster
- Support for creating hosted `harbor` instances of `redis` that support deployment using middleware modules
- Support to create managed `harbor`, support to modify `Admin` password, resource quota, `Redis` instance, access type
- Support for creating hosted `harbor` Support for automatic creation of image scanners
- Support registry integration, integrate registrys to verify user passwords and user permissions
     - Support registry integration to verify that the username and password are correct, and ensure that the user has administrator privileges
     - Support integrated registrys to verify that the username and password are correct
- Add fuzzy query to support registry integration list
- Support page editing `Project` as public or private
- Support `harbor`, `docker registry` type registry multi-architecture image page display

#### Fixes

- Fixed `harbor`, `docker registry` repositories that support integrated repositories connected to `https`

## 2022-12-30

### v0.4

#### Features

- Support for creating managed registries based on Harbor
- Support multi-copy deployment
- Support full life cycle management of container registry
- Support deploying managed harbor instances in any namespace under any cluster of the platform
- Support platform access and management of external Harbor, Docker Registry container registry
- Support separate allocation of private registry space for platform workspace (tenant)
- Support for creating public/private registry spaces
- Support workspace (tenant) independent access to external Harbor, Docker Registry container registry
- Support for selecting images through the image selector when deploying applications
- Support image scanning
