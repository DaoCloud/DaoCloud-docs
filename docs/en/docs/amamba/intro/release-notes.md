---
MTPE: windsonsea
date: 2024-05-08
---

# Releases Notes

This page lists the release notes for Workbench to help you understand
the development and feature changes in each version.

## 2024-06-30

### v0.28.0

#### New Features

- **Added** a feature of running pipelines from a specified stage.

#### Improvements

- **Improved** pipeline DAG, allowing for switching between old and new versions. Note: Saving pipelines across 
  different versions is prohibited as it may cause compatibility issues.
- **Improved** auto-completion in the Jenkinsfile editor.
- **Improved** support for integrating with older versions of SonarQube.
- **Improved** the API to support embedding ArgoCD UI in the GitOps details page.
- **Improved** the API to support creating, deleting, updating, and retrieving custom pipeline steps.

#### Fixes

- **Fixed** incorrect audit log names.

#### Known Issues

- In v0.28.2, once pipeline webhooks are enabled, they cannot be disabled. An upgrade to v0.28.3 
  is required to resolve this issue.

## 2024-05-30

### v0.27.0

#### New Features

- **Added** support for creating SSH credentials.

#### Improvements

- **Improved** error messages for namespace creation.
- **Improved** information returned by the Sonarqube code scan results API.
- **Improved** support for operations related to rollouts created natively.
- **Improved** the API to now support rerunning pipelines from a specified stage.
- **Improved** support for enabling both pipeline webhooks and code source triggers simultaneously.

#### Fixes

- **Fixed** an error when updating SSH credentials.
- **Fixed** an issue with incorrect pagination offset calculation.

## 2024-04-30

### v0.26.0

#### New Features

- **Added** support management of integrated code repositories
- **Added** support cloning code repositories
- **Added** support creating branches/tags

#### Improvements

- **Improved** Support searching across all namespaces for helm, olm, native applications, and canary release applications
- **Improved** Add running status to workload list and when retrieving resources for workload types
- **Improved** Support installation status of kube-app-manager
- **Improved** Remove credentials when creating applications from Git/Jar

#### Bug Fixes

- **Fixed** failure to retrieve multi-branch pipeline logs
- **Fixed** incorrect start time for pipeline runs
- **Fixed** error in fuzzy search for namespaces
- **Fixed** incomplete pipeline logs
- **Fixed** creation of native applications after failed creation from Git/Jar

## 2024-03-30

### v0.25.0

#### New Features

- **Added** the creation interface and logic for native applications, support creating workload resources separately

#### Improvements

- **Improved** webhook callback logic for SonarQube
- **Improved** Automatically fill in container names when enabling specific container steps after defining labels for pipelines

#### Bug Fixes

- **Fixed** rendering of pipeline DAG failed for built-in pipeline templates
- **Fixed** empty configuration in casc when removing SonarQube integration
- **Fixed** casc configuration not being updated when integrating SonarQube in workspace
- **Fixed** loss of credentials, SonarQube configurations, email configurations, etc. after switching Jenkins instances

## 2024-01-31

### v0.24.0

#### Added

- **Added** Pipeline support for CI Kanban overview
- **Added** Ability to terminate GitOps application synchronization
- **Added** Ability to view events for GitOps applications
- **Added** Support for canary release based on Contour

#### Improvements

- **Improved** Added health status for GitOps applications: paused, missing, and unknown
- **Improved** Provided commit, comment, and author information for synced and latest git repository, and version information for helm repository
- **Improved** Canary release based on ContourPlugin no longer depends on a specific version of Contour SDK

#### Fixed

- **Fixed** Fixed the issue where creating an application with dryRun option still creates the application

## 2023-12-31

### v0.23.0

#### New Features

- **Added** support for integration with Nexus and related operations
- **Added** support for integration with Testlink and related operations

#### Improvements

- **Improved** token creation method when creating applications based on Git/Jar
- **Improved** unification of fields related to cpu and memory in OAM application UI

#### Bug Fixes

- **Fixed** image address for the contour plugin
- **Fixed** an error when adding a resource type trait to an OAM application
- **Fixed** incorrect return value when rolling back a native application
- **Fixed** an issue where an OAM application is not reconciled by the controller after rolling back
- **Fixed** an error in modifying casc file when removing integration with SonarQube
- **Fixed** an issue where instances can be queried across different workspaces
- **Fixed** an issue of incorrect resource count displayed in the native application topology

## 2023-11-30

### v0.22.0

#### New Features

- **Added** sensitive operations to audit log
- **Added** support for adding global environment variables to pipelines
- **Added** support for deploying applications and updating application images in pipelines
- **Added** support for deploying SonarQube toolchain

#### Improvements

- **Improved** API to support searching Jenkins node labels
- **Improved** API to support integrating Jenkins across clusters
- **Improved** pipeline templates with parameter validation
- **Improved** each component service to expose golang metrics and pprof pages
- **Improved** API to support rolling back native application versions
- **Improved** deployment of applications from git/jar using serviceAccountToken to avoid permission escape

#### Fixes

- **Fixed** error when exporting application template and creating version for native applications without istio installed in the target cluster
- **Fixed** failure to fetch git/tag when ArgoCD is installed in a specified namespace
- **Fixed** an issue with content changing after saving pipeline templates.

## 2023-10-31

### v0.21.0

#### New Features

- **Added** support for creating OLM applications
- **Added** support for editing OLM application YAML
- **Added** support for deleting OLM applications
- **Added** support for request-based feature rollout with Istio
- **Added** native application version management (create, delete, update, retrieve)
- **Added** export template for native applications

#### Improvements

- **Improved** API now supports returning the installation status of argocd/kubevela components
- **Improved** git remote branches and tags can now be searched
- **Improved** regular expression validation for multi-branch pipelines input
- **Improved** an interface to check feature gate status (frontend only displays when enabled)
- **Improved** an interface to create kube-app-manager
- **Improved** Upgraded argo-rollout chart version to v2.32.0

#### Fixes

- **Fixed** bug causing errors in checking project binding relationships for kangaroo
- **Fixed** issues related to control plane namespace when creating OAM applications
- **Fixed** error in form git/jar deployment caused by Kubernetes CD plugin
- **Fixed** an issue where non-listed users were able to approve pipelines issue
- **Fixed** pipeline configuration errors caused by sync pipelines
- **Fixed** an issue where type reset occurred during rollout updates

## 2023-08-31

### v0.20.0

#### New Features

- **Added** integration with GitLab using access token
- **Added** status field for native applications
- **Added** API integration with kolm
- **Added** CRUD APIs for multi-cloud applications
- **Added** ability to add triggers in pipelines, automatically adding webhooks in GitLab, and triggering pipelines based on related events

#### Improvements

- **Improved** Retrieval of SonaQube scan results is no longer bound to specific run records, rather it retrieves from the latest run record
- **Improved** alignment between recent pipeline records and last run records
- **Improved** handling logic for resources bound to the workspace in event listeners
- **Improved** error message prompt when unable to connect to KubeVela

#### Bug Fixes

- **Fixed** creation failure of control plane namespace when resource quotas were set for Global clusters
- **Fixed** ability to bind control plane namespace to multiple workspaces
- **Fixed** successful creation of control plane namespace even if the namespace is already deleted
- **Fixed** an issue with incorrect comparison of multi-branch pipeline configurations
- **Fixed** an issue with missing dbName in link queries

## 2023-07-31

### v0.19.2

#### New Features

- **Added** support for navigating to Jira to view details in the Issues interface
- **Added** status indicators for clusters
- **Added** editing YAML, adding components, editing components, editing operational features, and other functionalities for OAM applications
- **Added** support for sorting pipelines based on recent run time
- **Added** support for Sonarqube configuration and code quality result steps in pipelines
- **Added** integration of Sonarqube instances in the toolchain
- **Added** default binding of native applications when creating applications based on git, jar, and container images in the wizard

#### Improvements

- **Improved** steps to integrate gitlab with jenkins credentials
- **Improved** display of binding time and added a division for sonarqube instances with bound workspaces in the administrator view
- **Improved** the issue of the cache not expiring in apiserver

## 2022-06-30

### v0.18.1

#### New Features

- **Added** permission support for running pipelines in the pipeline module.
- **Added** support for updating and deleting native applications and their subresources.
- **Added** basic functionality for creating and managing OAM (Open Application Model) applications.
- **Added** installed Kubevela open-source components.
- **Added** support for automatic and manual synchronization of toolchain resources, along with corresponding metric indicators.
- **Added** version information to pipeline templates.
- **Added** support for creating native applications and viewing their resource information.
- **Added** cluster-wide check for nginx ingress-class.

#### Fixes

- **Fixed** an issue where an error occurred on the native application list page when the target cluster did not have the CRD (Custom Resource Definition) for native applications installed.
- **Fixed** an issue where no values were modified when updating pipeline credentials, resulting in a null return when password information was not returned.
- **Fixed** the problem where the orphan strategy for multi-branch pipelines showed as -1 when it was empty.

#### Improvements

- **Improved** API handling for exceptional scenarios in pipelines.
- **Improved** a status field to display the runtime status of clusters in the API.
- **Improved** hardcoding to support deployment in different namespaces.
- **Improved** When integrating with GitLab, returning the GitLab address.
- **Improved** Returning toolchainID when integrating GitLab with Jenkinsfile-based pipelines and multi-branch pipelines.

## 2023-6-15

### v0.17.4

#### Fixes

- **Fixed** an issue with abnormal operations in the canary release tasks.

## 2022-05-31

### v0.17.3

#### New Features

- **Added** API now supports selecting integrated code repositories using code selectors.
- **Added** support for nginx-ingress based canary release strategy.
- **Added** API now supports resource topology for applications.
- **Added** API unified credentials.
- **Added** version information to pipeline templates.
- **Added** support for creating native applications and viewing their resource information.

#### Fixes

- **Fixed** the issue where containers in container images didn't support underscores.
- **Fixed** the error with replica numbers in blue-green deployments.
- **Fixed** the problem where the orphan strategy for multi-branch pipelines showed as -1 when it was empty.

#### Improvements

- **Improved** retry functionality to the http-client of the jira-provider, improving the handling speed of pipeline events.
- **Improved** the handling speed of pipeline events.
- **Improved** pipeline templates for from-git and from-jar.
- **Improved** the URL for requesting Jenkins, for both regular pipelines and multi-branch pipelines.

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

#### Improvements

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

#### Improvements

- Adjusted CPU and memory parameters for Jenkins

#### Fixes

- Cannot search toolchain data if page is less than 0

## 2022-02-22

### v0.14.0

#### New Features

- API support for creating pipelines using built-in templates
- API support for creating, updating, and deleting custom templates
- __apiserver__ and __devopserver__ can access Jenkins using the https protocol
- __event-proxy__ component supports Jenkins event persistence
- Retry and rate limit when accessing Jenkins

#### Improvements

- The prompt message when rerunning a pipeline fails

#### Fixes

- Inconsistency between the credentials in the database and Jenkins
- Gray releases could be created successfully even with traffic ratios greater than 100%

## 2022-01-30

### v0.13.0

#### New Features

- Support for cascading delete, allowing you to select the resources you want to delete based on your actual needs
- Gray release supports editing YAML
- The Chart for deploying Workbench no longer includes Jenkins. You can install Jenkins using a separate Helm Chart

#### Improvements

- Downloaded artifact reports are no longer fully cached in __apiserver__ ; they are partly cached through io chunking mode forwarding

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

#### Improvements

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

#### Improvements

- The process of integrating an application into a service mesh

#### Fixes

- Admin users fail to authenticate deployment target (cluster/namespace)
- __Invalida date__ error of the creation time, sync start time, and sync end time of gitops applications
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
