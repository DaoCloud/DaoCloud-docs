---
MTPE: windsonsea
date: 2024-06-03
---

# Container Registry Release Notes

This page lists the release notes of the container registry, so that you can
understand the evolution path and feature changes of each version.

*[Kangaroo]: Internal dev codename for the container registry
*[Kpanda]: Internal dev codename for container management
*[Harbor]: An open-source container registry tool and a CNCF graduated project

## 2023-05-31

### v0.18.1

- **Optimized** the accuracy of login command prompts after integrating Harbor administrator into the container registry
- **Fixed** pagination issue in the image selector interface on the application workbench

## 2023-04-30

### v0.17.0

- **Optimized** deletion prompts for Docker/Jfrog registry
- **Optimized** image download counts
- **Optimized** the registry space list view for Docker/Jfrog registry from the administrator's perspective

## 2023-03-29

### v0.16.1

- **Added** best practice documentation for deploying Harbor via LoadBalancer mode
- **Added** support for upgrading Kangaroo through Kpanda Helm application updates
- **Fixed** an issue with failed image deletion in Docker Registry
- **Fixed** an issue with failed creation of image recycling rules for regular tenants (with wsadmin permissions)
- **Fixed** dependency issue in creating and deleting Harbor with custom role management
- **Fixed** an error occurred when creating a container registry with Chinese characters in the description

## 2023-01-31

### v0.15.0

- **Fixed** an error when querying registry space for associated JFrog container registry
- **Fixed** a failure to generate login command

## 2023-12-29

### v0.14.0

- **Optimized** compatibility for supporting illegal k8s usernames
- **Fixed** an issue with consuming excessive bandwidth during large-scale image synchronization
- **Fixed** an issue with high latency in querying large-scale images in a single registry space

## 2023-11-30

### v0.13.1

- **Fixed** an issue with binding workspace to registry space
- **Fixed** an issue with granting authorization to all public registry spaces when generating login instructions

## 2023-10-31

### v0.12.0

- **Added** support for quick deployment of middleware when creating a managed Harbor in non-platinum versions
- **Added** best practices for publishing Harbor Nginx configuration
- **Added** best practices for resource planning when releasing container registries
- **Optimized** resource validation when creating a managed Harbor
- **Optimized** prompt for installing cert manager as a dependency for Harbor operator

## 2023-09-06

### v0.11.0

- **Added** harbor hosting status verification
- **Added** deployment to download station
- **Added** best practices for Nginx proxy, resource capacity planning
- **Fixed** an issue preventing updates to managed Harbor description
- **Optimized** display of truncated registry space in bootstrap container registry
- **Optimized** a frontend error for WS admin when creating recycle rules

## 2023-08-02

### v0.10.0

- **Added** a solution for migrating/backing up/restoring container registry,
  which has been verified through the migration of the release-ci repository
- **Added** best practices for logging into non-secure container registry
- **Added** support for using the internal middleware MINIO when creating managed Harbor
- **Added** support for the PG mode of Renmin Jincang
- **Optimized** the format validation for PG and Redis addresses when creating managed Harbor
- **Optimized** grayed-out and prompt optimization for unauthorized access
- **Optimized** handling of special cases after unbinding clusters

## 2023-07-02

### v0.9.0

- **Added** support for selecting the middleware `minio` instance when creating managed harbor
- **Added** support for key auditing functionality in `Ghippo`
- **Optimized** validation for container registry resources under a workspace (WS) when deleting the workspace
- **Optimized** state info of managed harbor after unbinding clusters
- **Fixed** an issue where `Ghippo workspace` resources could not be unbound
- **Fixed** an issue with `Sidecar` injection
- **Fixed** an issue where images could not be pushed when selecting `minio` during harbor creation

## 2023-06-05

### v0.8.0

#### New Features

- **Added** image description information to the harbor type repository
- **Added** instance status to the registry space list
- **Added** support for randomly generating `nodeport` port numbers when creating a harbor
- **Added** validation for duplicate usage of `redis`, `postgresql`, and `s3` in the creation of harbor
- **Added** image recycling feature to the `project`

#### Fixes

- **Fixed** the concatenation error in the offline deployment of managed harbor image addresses
- **Fixed** pagination issue in the docker registry type `project` list
- **Fixed** search issue in the docker registry type `repository`
- **Fixed** existing account problem when creating robot accounts

#### Optimization

- **Added** job cleanup logic
- **Removed** the `project` field from the interface for obtaining temporary login instructions
- **Optimized** login instructions
- **Optimized** logic for image scanning judgment

## 2023-05-08

### v0.7.0

#### New features

- **Added** support page configuration image synchronization between multiple instances
- **Added** support for associating `jfrog` registry in workspaces
- **Added** support for creating managed harbor in offline `ARM` environment

#### Fixes

- **Fixed** the problem that the registry integration URL could not be updated after modification
- **Fixed** logical incompatibilities after `Project` was deleted from the native harbor page

#### Optimization

- **Optimized** the performance of docking `jfrog` interface to within `2s`

## 2023-04-07

### v0.6.2

#### New features

- **Added** support custom roles in global management, granting different role permissions to users
- **Added** support for generating temporary login commands
- **Added** managed harbor to support `cpu, memory` verification
- **Added** managed harbor support for editing image scanners
- **Added** managed harbor support for using `S3` storage

#### Fixes

- **Fixed** an issue that the installation byte of harbor-operator helm is too large

#### Optimization

- **Optimized** the performance of the image list feature page, and propose a separate `Project` list page

## 2023-03-15

### v0.5.0

#### New features

- **Added** support for creating managed Harbor instances with `NodePort` exposure and validation of port availability.
- **Added** support for creating managed Harbor instances with `https` exposure.
- **Added** support for creating managed Harbor instances with `DCE 5.0 ODIC` integration, allowing users to log in to Harbor using `DCE 5.0` credentials.
- **Added** support for validating the installation of `harbor-operator` in the deployed cluster when creating managed Harbor instances.
- **Added** support for deploying `redis` instances using the middleware module in managed Harbor instances.
- **Added** support for modifying `Admin` password, resource quotas, `Redis` instances, and access types in managed Harbor instances.
- **Added** support for automatically creating image scanners in managed Harbor instances.
- **Added** support for repository integration, including validation of user passwords and permissions.
    - **Added** support for validating the correctness of username and password in repository integration and ensuring that the user has administrator privileges.
    - **Added** support for validating the correctness of username and password in repository integration.
- **Added** support for fuzzy searching in the repository integration list.
- **Added** support for editing the visibility of projects as public or private.
- **Added** support for displaying multi-architecture images in the pages of Harbor and Docker Registry repositories.

#### Fixes

- **Fixed** support for accessing Harbor and Docker Registry repositories via `https` integration.

## 2022-12-30

### v0.4.0

#### New features

- **Added** support for creating managed registries based on Harbor
- **Added** support multi-copy deployment
- **Added** support full life cycle management of container registry
- **Added** support deploying managed harbor instances in any namespace under any cluster of the platform
- **Added** support platform access and management of external Harbor, Docker Registry container registry
- **Added** support separate allocation of private registry space for platform workspace (tenant)
- **Added** support for creating public/private registry spaces
- **Added** support workspace (tenant) independent access to external Harbor, Docker Registry container registry
- **Added** support for selecting images through the image selector when deploying applications
- **Added** support image scanning
