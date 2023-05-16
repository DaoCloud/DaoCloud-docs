# Image Registry Release Notes

This page lists the release notes of the image registry, so that you can understand the evolution path and feature changes of each version.

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

- Optimize the performance of the image list function page, and propose a separate `Project` list page

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
- Support registry integration, associate registrys to verify user passwords and user permissions
     - Support registry integration to verify that the user name and password are correct, and ensure that the user has administrator privileges
     - Support associated registrys to verify that the username and password are correct
- Add fuzzy query to support registry integration list
- Support page editing `Project` as public or private
- Support `harbor`, `docker registry` type registry multi-architecture image page display


#### Fixes

- Fixed `harbor`, `docker registry` repositories that support associated repositories connected to `https`

## 2022-12-30

### v0.4

#### Features

- Support for creating managed image registries based on Harbor
- Support multi-copy deployment
- Support full life cycle management of image registry
- Support deploying managed harbor instances in any namespace under any cluster of the platform
- Support platform access and management of external Harbor, Docker Registry image registry
- Support separate allocation of private image space for platform workspace (tenant)
- Support for creating public/private image spaces
- Support workspace (tenant) independent access to external Harbor, Docker Registry image registry
- Support for selecting images through the image selector when deploying applications
- Support image scanning
