# Workbench Release Notes

This page lists the Release Notes of the App Workbench, so that you can understand the evolution path and feature changes of each version.

## 2022-03-31

### v0.15.1

#### Features

- **Added** container configuration supports more options (lifecycle, environment variables and data storage)
- **Added** jira toolchain integration interface, including CRUD of jira instance and list of instance projects
- **Added** defect list supports fuzzy query, type, status, priority query
- **Added** The list/watch mechanism for ghippo's smtp configuration supports jenkins' email notification function
- **Added** Allows creation of custom roles
- **Added** API supports tool chain integration to add jenkins type, add to get jenkins list and details
- **Added** API supports multi-branch pipeline
- **Added** Added support for viewing test reports in details of pipeline running records
- **Added** Added SVN and Junint collection test report steps to the pipeline
- **Added** support for creating pipelines through templates
- **Added** support for creating custom pipeline templates
- **Added** API supports tool chain integration to add jenkins type, add to get jenkins list and details
- **Added** API supports tool chain integration to add jenkins type, add to get jenkins list and details

#### Optimization

**Optimize** Adjust the cpu and memory parameters of jenkins

#### Fix

**Fix** Fixed the problem that if the page is less than 0, the corresponding toolchain data cannot be searched, and some fields for front-end display have been added

## 2022-02-22

### v0.14.0

#### Features

- **Added** API supports using built-in templates to create pipelines
- **Added** API supports creating, updating, and deleting custom templates
- **Added** apiserver and devopserver support accessing Jenkins with https protocol
- **Added** event-proxy component supports Jenkins event persistence
- **Added** Added support for retry and throttling when accessing Jenkins

#### Optimization

**Optimization** Optimized the prompt when re-running a certain pipeline fails

#### Fix

- **Fixed** Fixed issue when credentials were inconsistent in database and Jenkins
- **Fixed** Fixed the problem that when the traffic ratio is greater than 100 when creating a grayscale release, the problem can be created successfully

## 2022-01-30

### v0.13.0

#### Features

- **Added** supports cascading deletion, and you can select resources to be deleted according to the actual situation
- **Added** Grayscale release supports editing YAML function
- **Added** Jenkins has been removed from the Chart package of the deployment App Workbench, and Jenkins can be installed using a separate Helm Chart

#### Optimization

**Optimization** Product report download, do not cache all in apiserver, use io block mode to partially cache and forward

#### Fix

**Fix** Fixed the problem of adding a private registry in continuous deployment and reporting an error

## 2022-12-30

### v0.12.0

#### Features

- **Added** Support to open traditional microservices and service mesh at the same time when creating an application
- **Added** Query gray release supports fuzzy query, query continuous deployment supports fuzzy query and state retrieval, query gitops registry supports fuzzy query and state retrieval
- **Added** Add an interface to get jso data according to GVR
- **Added** Add an interface to get helm information, you can deploy helm chart through argocd
- **Added** Hot reload of Jenkins configuration file and hot reload of syncer configuration file
- **Added** ListRegistry interface return value adds whether Nacos needs authentication field
- **Added** API for pipeline product report list and download product report interface
- **Added** Pipeline step logs support to get full logs
- **Added** Added cache to query plug-in information interface
- **Added** Copy the existing pipeline directly to generate a new pipeline
- **Added** Provides differentiated configuration for access metric monitoring when microservices are enabled, and the path can be customized
- **Added** Jenkins trace docking
- **Added** ListWorkload interface return value to add application-associated resources

#### Fix

- **Fixed** rerun pipeline, probabilistic panic fix
- **Fixed** The instrumentation image used in link tracking when creating microservices goes offline
- **Fixed** The monitoring and analysis of grayscale release failed
- **Fixed** support setting argo-rollouts controller replicas

## 2022-12-18

### v0.11.0

#### Features

- **Added** Ghippo and Skoala's trace docking, Ghippo itself only supports trace of some apis
- **Added** Added the pipeline for image checking when the helm package is offline
- **Added** Add a solution to the problem that the credential becomes invalid after adding and migrating jenkins
- **Added** The credential list supports fuzzy search by name

#### Optimization

- **Optimize** Reduce the memory usage of jenkins without workload by adjusting jvm parameters
- **Optimize** When the gitops module creates a registry, it adds a judgment on the connectivity of the registry
- **Optimization** Real-time synchronization of pipeline running status and other information causes too much pressure on jenkins, so change to lazy loading
- **Optimization** Optimized the api release process and supports separate release

#### Fix

- **Fixed** Unlimited rollback issue if creation fails when microservices are enabled
- **Fixed** argocd app deployment/deletion failure when cluster kubeconfig changed. And the problem of credential failure in jenkins

## 2022-11-30

### v0.10

#### Features

- **Added** Added the registry function in gitops, which supports import and deletion
- **Added** Added sync function for gitops app

#### Optimized

- **Optimized** Optimized the application access service mesh process

#### Fix

- **Fixed** Fixed the problem that the admin user was not authenticated to the deployment target (cluster/namespace)
- **Fixed** Fixed gitops app creation time, sync start time and sync end time with `Invalida date` bug
- **Fixed** Fixed the error of getting nacos registry list data
- **Fixed** Fixed listing workload interfaces sorted by name error
- **Fixed** Fixed cluster and namespace lost in destionation in ArgoCD after cluster unbind and rebind
- **Fixed** Fixed the problem that the binding relationship between namespace and workspace was lost when updating the label of namespace
- **Fixed** Fixed the error of trigger conversion when synchronizing the jenkins config to the database after completing the pipeline
- **Fixed** Fixed the problem that the credential of the kubeconfig type in the ArgoCD cluster and jenkins was out of sync due to the change of the cluster's kubeconfig
- **Fixed** Fixed unordered and paginated problems in registry list
- **Fixed** Fixed the problem that from-jar failed to upload more than 32M files

## 2022-11-18

### v0.9

#### Features

- **Added** The jenkins-agent image is continuously released
- **Added** Added option to use database from middleware
- **Upgrade** jenkins is upgraded from 2.319.1 to 2.346.2, kubernetes plugin is upgraded to 3734.v562b_b_a_627ea_c, related plugins are also upgraded

#### Optimized

- **Optimized** Obtain rollout mirror list, application group list, native application list and other performance optimization
- **Optimized** The image used by from-jar is no longer hard-coded in the source code, passed through env, and ensured that the installer can get it correctly

#### Fix

- **Fixed** the problem that rollout cannot be distinguished under different workspaces
- **Fixed** the problem that the gitops module is not authenticated
- **Fixed** the occasional pipeline step status is incorrect
- **Fixed** the problem that the description obtained from helmchart is empty
- **Fixed** The problem of creating a namespace without verifying storage
- **Fixed** fix for disorder and pagination problems in list argocd repository
- **Fixed** Fix the problem that from-jar failed to upload more than 32M files
- **Fixed** The problem that the full log cannot be obtained if the log volume is too large when obtaining the pipeline log