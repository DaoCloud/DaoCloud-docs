# Workbench Release Notes

This page lists the Release Notes of the application workbench, so that you can understand the evolution path and feature changes of each version.

## 2022-03-31

### v0.15.1

#### New features

- **New** container configuration supports more options (lifecycle, environment variables and data storage)
- **New** jira toolchain integration interface, including CRUD of jira instance and list of instance projects
- **New** defect list supports fuzzy query, type, status, priority query
- **New** The list/watch mechanism for ghippo's smtp configuration supports jenkins' email notification function
- **NEW** Allows creation of custom roles
- **NEW** API supports tool chain integration to add jenkins type, add to get jenkins list and details
- **NEW** API supports multi-branch pipeline
- **NEW** Added support for viewing test reports in details of pipeline running records
- **NEW** Added SVN and Junint collection test report steps to the pipeline
- **Add** support for creating pipelines through templates
- **Add** support for creating custom pipeline templates
- **NEW** API supports tool chain integration to add jenkins type, add to get jenkins list and details
- **NEW** API supports tool chain integration to add jenkins type, add to get jenkins list and details

#### Optimization

**Optimize** Adjust the cpu and memory parameters of jenkins

#### Fix

**Fix** Fixed the problem that if the page is less than 0, the corresponding toolchain data cannot be searched, and some fields for front-end display have been added

## 2022-02-22

### v0.14.0

#### New features

- **New** API supports using built-in templates to create pipelines
- **NEW** API supports creating, updating, and deleting custom templates
- **New** apiserver and devopserver support accessing Jenkins with https protocol
- **New** event-proxy component supports Jenkins event persistence
- **NEW** Added support for retry and throttling when accessing Jenkins

#### Optimization

**Optimization** Optimized the prompt when re-running a certain pipeline fails

#### Fix

- **FIXED** Fixed issue when credentials were inconsistent in database and Jenkins
- **Fix** Fixed the problem that when the traffic ratio is greater than 100 when creating a grayscale release, the problem can be created successfully

## 2022-01-30

### v0.13.0

#### New features

- **NEW** supports cascading deletion, and you can select resources to be deleted according to the actual situation
- **NEW** Grayscale release supports editing YAML function
- **NEW** Jenkins has been removed from the Chart package of the deployment application workbench, and Jenkins can be installed using a separate Helm Chart

#### Optimization

**Optimization** Product report download, do not cache all in apiserver, use io block mode to partially cache and forward

#### Fix

**Fix** Fixed the problem of adding a private warehouse in continuous deployment and reporting an error

## 2022-12-30

### v0.12.0

#### New features

- **NEW** Support to open traditional microservices and service grid at the same time when creating an application
- **NEW** Query gray release supports fuzzy query, query continuous deployment supports fuzzy query and state retrieval, query gitops warehouse supports fuzzy query and state retrieval
- **NEW** Add an interface to get jso data according to GVR
- **NEW** Add an interface to get helm information, you can deploy helm chart through argocd
- **NEW** Hot reload of Jenkins configuration file and hot reload of syncer configuration file
- **New** ListRegistry interface return value adds whether Nacos needs authentication field
- **New** API for pipeline product report list and download product report interface
- **NEW** Pipeline step logs support to get full logs
- **NEW** Added cache to query plug-in information interface
- **NEW** Copy the existing pipeline directly to generate a new pipeline
- **Add** Provides differentiated configuration for access indicator monitoring when microservices are enabled, and the path can be customized
- **Added** Jenkins trace docking
- **Add** ListWorkload interface return value to add application-associated resources

#### Fix

- **Fix** rerun pipeline, probabilistic panic fix
- **FIXED** The instrumentation image used in link tracking when creating microservices goes offline
- **Fix** The monitoring and analysis of grayscale release failed
- **FIX** support setting argo-rollouts controller replicas

## 2022-12-18

### v0.11.0

#### New features

- **Added** Ghippo and Skoala's trace docking, Ghippo itself only supports trace of some apis
- **NEW** Added the pipeline for image checking when the helm package is offline
- **NEW** Add a solution to the problem that the credential becomes invalid after adding and migrating jenkins
- **NEW** The credential list supports fuzzy search by name

#### Optimization

- **Optimize** Reduce the memory usage of jenkins without workload by adjusting jvm parameters
- **Optimize** When the gitops module creates a warehouse, it adds a judgment on the connectivity of the warehouse
- **Optimization** Real-time synchronization of pipeline running status and other information causes too much pressure on jenkins, so change to lazy loading
- **Optimization** Optimized the api release process and supports separate release

#### Fix

- **Fix** Unlimited rollback issue if creation fails when microservices are enabled
- **FIXED** argocd app deployment/deletion failure when cluster kubeconfig changed. And the problem of credential failure in jenkins

## 2022-11-30

### v0.10

#### New features

- **NEW** Added the warehouse function in gitops, which supports import and deletion
- **NEW** Added sync function for gitops app

#### Optimized

- **Optimized** Optimized the application access service mesh process

#### Fixed

- **Fixed** Fixed the problem that the admin user was not authenticated to the deployment target (cluster/namespace)
- **FIXED** Fixed gitops app creation time, sync start time and sync end time with `Invalida date` bug
- **Fixed** Fixed the error of getting nacos registry list data
- **FIXED** Fixed listing workload interfaces sorted by name error
- **Fixed** Fixed cluster and namespace lost in destionation in ArgoCD after cluster unbind and rebind
- **Fixed** Fixed the problem that the binding relationship between namespace and workspace was lost when updating the label of namespace
- **Fixed** Fixed the error of trigger conversion when synchronizing the jenkins config to the database after completing the pipeline
- **Fixed** Fixed the problem that the credential of the kubeconfig type in the ArgoCD cluster and jenkins was out of sync due to the change of the cluster's kubeconfig
- **FIXED** Fixed unordered and paginated problems in warehouse list
- **Fixed** Fixed the problem that from-jar failed to upload more than 32M files

## 2022-11-18

### v0.9

#### New features

- **NEW** The jenkins-agent image is continuously released
- **NEW** Added option to use database from middleware
- **Upgrade** jenkins is upgraded from 2.319.1 to 2.346.2, kubernetes plugin is upgraded to 3734.v562b_b_a_627ea_c, related plugins are also upgraded

#### Optimized

- **Optimized** Obtain rollout mirror list, application group list, native application list and other performance optimization
- **Optimized** The image used by from-jar is no longer hard-coded in the source code, passed through env, and ensured that the installer can get it correctly

#### Fixed

- **Fixed** the problem that rollout cannot be distinguished under different workspaces
- **Fixed** the problem that the gitops module is not authenticated
- **Fixed** the occasional pipeline step status is incorrect
- **Fixed** the problem that the description obtained from helmchart is empty
- **FIXED** The problem of creating a namespace without verifying storage
- **Fixed** fix for disorder and pagination problems in list argocd repository
- **Fixed** Fix the problem that from-jar failed to upload more than 32M files
- **Fixed** The problem that the full log cannot be obtained if the log volume is too large when obtaining the pipeline log