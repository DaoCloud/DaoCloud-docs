# The application workbench releases Notes

This page lists the Release Notes of the application Workbench so that you can understand the evolution path and feature changes of each version.

## 2022-04-30

### v0.16.1

#### New function

- ** add ** Create applications independently of observability-related configurations, including metrics monitoring, link tracking, and JVM monitoring
- ** add ** Integrated Toolchain supports Jenkins
- ** add ** Supports the creation and management of multi-branch pipeline
- ** add ** Supports tool chain integration from an administrator perspective
- ** add ** API supports blue-green publishing, including create, delete, rollback, upgrade, details, etc

#### repair

- ** repair ** The bug cannot be obtained when the administrator binds the project to the specified workspace and obtains the details of the associated tool chain instance
- ** repair ** If IMAGE_TAG is empty when creating an application based on from-jar and from-git, set it to latest in the corresponding template file

#### optimization

- ** optimization ** Unified integration tool link interface

## 2022-03-31

### v0.15.1

#### New function

- ** add ** Container configuration supports more options (lifecycle, environment variables, and data storage)
- ** add ** jira Toolchain integration interface, including a list of CRUDs for jira instances and instance projects
- ** add ** Defect list supports fuzzy query, query of type, status, and priority
- ** add ** list/watch mechanism for ghippo smtp configuration, support jenkins email notification function
- ** add ** Allows the creation of custom roles
- ** add ** API supports toolchain integration Add jenkins type, add get jenkins list and details
- ** add ** The API supports a multi-branch pipeline
- ** add ** Support the test report for pipeline running record details
- ** add ** Pipeline Added the procedure for collecting test reports from SVN and Junit
- ** add ** Support pipeline-creating through templates
- ** add ** Supports the creation of custom pipeline templates
- ** add ** API supports toolchain integration Add jenkins type, add get jenkins list and details
- ** add ** API supports toolchain integration Add jenkins type, add get jenkins list and details

#### optimization

** optimization ** Adjust jenkins cpu, memory parameters

#### repair

** repair ** Fixes the problem of not being able to search for the corresponding toolchain data if page is less than 0, and adds some fields for the front end to display

## 2022-02-22

### v0.14.0

#### New function

- ** add ** The API supports pipelining using built-in templates
- ** add ** The API supports creating, updating, and deleting user-defined templates
- ** add ** apiserver and devopserver support Jenkins for accessing https
- ** add ** The event-proxy component supports Jenkins event persistence
- ** add ** Support retry and limiting traffic when accessing Jenkins

#### optimization

** optimization ** Improved prompt for failure to rerun a pipeline

#### repair

- ** repair ** Fixed an issue where the credentials were inconsistent between the database and Jenkins
- ** repair ** Fixed an issue where the traffic ratio was greater than 100 when creating grayscale publications

## 2022-01-30

### v0.13.0

#### New function

- ** add ** Cascading deletion is supported. You can select resources to be deleted based on site requirements
- ** add ** Grayscale publishing supports editing YAML functionality
- ** add ** Jenkins has been removed from the Chart package of the deployment application Workbench, supporting installation of Jenkins using a separate Helm Chart

#### optimization

** optimization ** Product report download, not all cache in apiserver, using io block mode partial cache forwarding

#### repair

** repair ** Fixed an error when adding private repository in continuous deployment

## 2022-12-30

### v0.12.0

#### New function

- ** add ** Both traditional micro services and service grids can be enabled during application creation
- ** add ** Query gray scale publication supports fuzzy query, query continuous deployment supports fuzzy query and search by status, query gitops warehouse supports fuzzy query and status search
- ** add ** Adds an interface to get jso data according to GVR
- ** add ** Add interface to get helm information, you can deploy helm chart via argocd
- ** add ** Hot loading of the Jenkins configuration file and hot loading of the syncer configuration file
- ** add ** Return Value of ListRegistry interface Added Whether Nacos requires the authentication field
- ** add ** Pipeline artifact report list interface and download artifact report interface
- ** add ** Pipeline step logs Full logs can be obtained
- ** add ** Query plug-in information interface added cache
- ** add ** Directly copy the existing pipeline to generate a new pipeline
- ** add ** Monitoring access counters when the micro-service is enabled Provides differentiated configurations and customized paths
- ** add ** Jenkins trace docking
- ** add ** ListWorkload interface Returned Value Add resources associated with an application

#### repair

- ** repair ** Restart pipeline, probability panic fix
- ** repair ** The instrumentation mirror used in link tracing when creating the microservice is offline
- ** repair ** Monitoring analysis of gray release failed
- ** repair ** Setting the argo-rollouts controller replicas is supported

## 2022-12-18

### v0.11.0

#### New function

- ** add ** trace connection between Ghippo and Skoala. Ghippo supports only trace of some apis
- ** add ** helm package image check pipeline under off-line condition
- ** add ** Add a solution to the problem of credential invalidation after the jenkins migration is added
- ** add ** The list of credentials supports fuzzy search by name

#### optimization

- ** optimization ** Reduced jenkins memory footprint when there was no workload by adjusting jvm parameters
- ** optimization ** gitops module adds judgment on warehouse connectivity when creating a warehouse
- ** optimization ** Real-time synchronization of pipeline running status and other information caused excessive pressure on jenkins, so it was changed to lazy loading mode
- ** optimization ** Optimized api release process, support separate release

#### repair

- ** repair ** If the micro-service creation fails, the micro-service can be rolled back without limit
- ** repair ** argocd application deployment/removal failed when cluster kubeconfig changed. And the invalidation of jenkins credential

## 2022-11-30

### v0.10.0

#### New function

- ** add ** Added the warehouse function in gitops, supporting import and deletion
- ** add ** Added the synchronization function for gitops

#### optimization

** optimization ** Optimized the application access service grid flow

#### repair

- ** repair ** Fixed the problem that the admin user does not authenticate the cluster/namespace deployment target
- ** repair ** Fixed the gitops application creation time, synchronization start time, and synchronization end time being `Invalida date`
- ** repair ** Fixed an error in getting nacos registry list data
- ** repair ** Fixed an error listing workload interfaces sorted by name
- ** repair ** Fixed cluster and namespace loss in destionation in ArgoCD after cluster unbundling and rebinding
- ** repair ** Fixed the problem that the namespace and workspace binding relationship was lost when the namespace label was updated
- ** repair ** Fixed trigger conversion when synchronizing jenkins config to database after pipelining
- ** repair ** Fixed an issue with kubeconfig type credential in the ArgoCD cluster and jenkins being out of sync due to a kubeconfig change in the cluster
- ** repair ** Fixes unordered and paging issues with warehouse lists
- ** repair ** Fixed the failure to upload more than 32M files from-jar

## 2022-11-18

### v0.9.0

#### New function

- ** add ** jenkins-agent Image is published continuously
- ** add ** Added the option to use the middleware database
- ** upgrade ** jenkins was upgraded from 2.319.1 to 2.346.2,kubernetes plugin was upgraded to 3734.v562b_b_a_627ea_c, and plugins were also updated

#### optimization

- ** optimization ** Obtain the rollout image list, application group list, native application list and other performance optimization
- ** optimization ** The image used by from-jar is no longer written in the source code. It is passed as env and guaranteed to be obtained correctly by the installer

#### repair

- ** repair ** rollout indistinguishable problem in different workspace
- ** repair ** The gitops module is not authenticated
- ** repair ** Occasionally the pipeline step status is not correct
- ** repair ** Gets an empty description for helmchart
- ** repair ** The namespace fails to verify the storage
- ** repair ** list argocd Fix for unordered and paging issues in repository
- ** repair ** from-jar failed to upload more than 32M files
- ** repair ** If too many pipeline logs are obtained, all pipeline logs cannot be obtained
