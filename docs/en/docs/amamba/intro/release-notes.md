# Releases Notes

This page lists the release notes for Application Workspace to help you understand the development and feature changes in each version.

## 2022-04-30

### v0.16.1

#### New Features

- Independent observability-related configurations when creating applications, including metrics, tracing, and JVM monitoring
- Toolchains support Jenkins integration
- Creation and management of multi-branch pipelines
- Toolchain integration capabilities from an administrator's view
- API support for blue/green release, including creation, deletion, rollback, upgrade, details, etc.

#### Fixes

- When an administrator binds a project to a specific workspace, the associated toolchain instance details cannot be obtained
- IMAGE_TAG is set to latest in the corresponding template file when it is empty during application creation based on a jar package or a git repo

#### Optimization

- Unified toolchain interface

## 2022-03-31

### v0.15.1

#### New Features

- More options for container configuration (lifecycle, environment variables, and data storage)
- Jira toolchain integration interface, including CRUD for Jira instances and the list of instance projects
- Fuzzy query of Defect List to query type, status, priority in Defect List
- List/watch mechanism for SMTP configuration for Ghippo, supporting email notification of Jenkins
- Creation of custom roles
- API support for Jenkins integration in toolchains, to get Jenkins list and details
- API support for multi-branch pipelines
- Test reports in the page of pipeline running record details
- SVN and Junit collection test report steps for the pipeline
- Creation of pipelines based on templates
- Creation of custom pipeline templates

#### Optimization

- Adjusted CPU and memory parameters for Jenkins

#### Fixes

- Cannot search toolchain data if page is less than 0

## 2022-02-22

### v0.14.0

#### New Features

- API support for creating pipelines using built-in templates
- API support for creating, updating, and deleting custom templates
- `apiserver` and `devopserver` can access Jenkins using the https protocol
- `event-proxy`component supports Jenkins event persistence
- Retry and rate limit when accessing Jenkins

#### Optimization

- The prompt message when rerunning a pipeline fails

#### Fixes

- Inconsistency between the credentials in the database and Jenkins
- Gray releases could be created successfully even with traffic ratios greater than 100%

## 2022-01-30

### v0.13.0

#### New Features

- Support for cascading delete, allowing you to select the resources you want to delete based on your actual needs
- Gray release supports editing YAML
- The Chart for deploying the Workbench no longer includes Jenkins. You can install Jenkins using a separate Helm Chart

#### Optimization

- Downloaded artifact reports are no longer fully cached in `apiserver`; they are partly cached through io chunking mode forwarding

#### Fixes

- Error when adding private repositories during continuous deployment.

## 2022-12-30

### v0.12.0

#### New Features

- Creating applications now supports enabling traditional microservices and service meshes at the same time
- Fuzzy search is supported for gray releases
- Fuzzy search and status retrievals are supported for continuous deployment
- Fuzzy search and status retrievals are supported for gitops repositories
- An interface to get json data based on GVR
- An interface to get helm information, which can deploy helm charts through argocd
- Hot reloading of Jenkins configuration files and syncer configuration files
- The return value of the ListRegistry interface adds a field indicating whether Nacos authentication is required
- API for pipeline artifact report list
- API for downloading artifact reports
- Pipeline step log supports obtaining the full log
- Interface for querying plugin information added caching
- Copy existing pipelines to generate new pipelines
- Customizable metric monitoring path when enabling the new application to be added into a registry in the Microservices module
- Integration with Jenkins trace
- The return value of the ListWorkload interface adds application-related resources

#### Fixes

- Accidental panic when rerunning the pipeline
- Errors related to instrumentation image offline used in microservice tracing
- Failure of analyzing monitoring statistics of gray releases
- Supports setting argo-rollouts controller replicas

## 2022-12-18

### v0.11.0

#### New Features

- Integration with Ghippo and Skoala trace
- Pipeline steps to check images when helm packages are offline
- A solution for invalid credentials after adding migration Jenkins
- Fuzzy search for credential list by name

#### Optimization

- Use jvm parameters to reduced Jenkins memory usage when without workloads
- Repository connectivity test when creating gitops modules
- Changed real-time synchronization of pipeline running status and other information to lazy loading
- Optimized the api release process to support separate release

#### Fixes

- Endless rollback if app creation fails when Microservice modules is enabled
- ArgoCD application deployment/deletion fails and invalid credentials due to changes in the kubeconfig of the cluster

## 2022-11-30

### v0.10.0

#### New Features

- Gitops repository, supporting import and delete
- Synchronization for gitops applications

#### Optimization

- The process of integrating an application into a service mesh

#### Fixes

- Admin users fail to authenticate deployment target (cluster/namespace)
- `Invalida date` error of the creation time, sync start time, and sync end time of gitops applications
- Error of getting data about the Nacos registry list
- Error that occurs when sorting workloads by name
- Loss of cluster and namespace in the destionation of ArgoCD after unbinding and then re-binding the cluster
- Loss of binding relationship between namespace and workspace due to update of namesapce label
- Error of trigger conversion when synching Jenkins config to a database after completing the pipeline
- Error that kubeconfig credentials in a ArgoCD cluster and in Jenkins are not synchronized due to changes in the kubeconfig of the cluster
- Out-of-order list and paging issues of the repository list
- Cannot upload a jar package larger than 32M

## 2022-11-18

### v0.9.0

#### New Features

- Continuous release of jenkins-agent image
- The option to use the mysql component from DCE 5.0 data service module as the database
- Upgrad Jenkins from 2.319.1 to 2.346.2, and kubernetes plugin to 3734.v562b_b_a_627ea_c, along with other related plugins

#### Improvements

- Improved performance for obtaining rollout image lists, application group lists, native application lists, etc.
- The image used in creating app from jar packages is provided by env variable, instead of being hardcoded in the source code. Also ensure that the whole DCE 5.0 install package can obtain that image

#### Fixes

- Rollout cannot be distinguished under different workspaces
- Unauthenticated gitops module
- Occasional incorrect status of pipeline steps
- Empty description of helm chart
- Storage is not verified during namespace creation
- Out-of-order and paging error of list argocd repository
- Cannot upload a jar package larger than 32M
- Cannot obtain the full log if the pipeline log is too large
