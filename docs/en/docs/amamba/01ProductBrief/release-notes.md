# Application Workbench Release Notes

This page lists the Release Notes of the application workbench, so that you can understand the evolution path and feature changes of each version.

## v0.10

Release date: 2022-11-30

- **NEW** Added the registry function in gitops, which supports import and deletion
- **NEW** Added sync function for gitops app
- **Fix** Fixed the problem that the admin user was not authenticated to the deployment target (cluster/namespace)
- **FIXED** Fixed gitops app creation time, sync start time and sync end time with `Invalida date` bug
- **Fix** Fixed the error of getting nacos registry list data
- **FIXED** Fixed listing workload interfaces sorted by name error
- **Fix** Fixed cluster and namespace lost in destionation in ArgoCD after cluster unbind and rebind
- **Fix** Fixed the problem that the binding relationship between namespace and workspace was lost when updating the label of namespace
- **Fix** Fixed the error of trigger conversion when synchronizing the jenkins config to the database after completing the pipeline
- **Fix** Fixed the problem that the credential of the kubeconfig type in the ArgoCD cluster and jenkins was out of sync due to the change of the cluster's kubeconfig
- **FIXED** Fixed unordered and paginated problems in registry list
- **Fix** Fixed the problem that from-jar failed to upload more than 32M files
- **Optimization** Optimized the application access service grid process

## v0.9

Release date: 2022-11-18

- **NEW** The jenkins-agent image is continuously released
- **NEW** Added option to use database from middleware
- **Fix** the problem that rollout cannot be distinguished under different workspaces
- **Fix** the problem that the gitops module is not authenticated
- **Fix** the occasional pipeline step status is incorrect
- **Fix** the problem that the description obtained from helmchart is empty
- **FIXED** The problem of creating a namespace without verifying storage
- **Fix** fix for disorder and pagination problems in list argocd repository
- **Fix** Fix the problem that from-jar failed to upload more than 32M files
- **Fix** The problem that the full log cannot be obtained if the log volume is too large when obtaining the pipeline log
- **Optimization** Obtain rollout image list, application group list, native application list and other performance optimization
- **Optimize** The image used by from-jar is no longer hard-coded in the source code, passed through env, and ensured that the installer can get it correctly
- **Upgrade** jenkins is upgraded from 2.319.1 to 2.346.2, kubernetes plugin is upgraded to 3734.v562b_b_a_627ea_c, related plugins are also upgraded

## v0.8

Release date: 2022-11-04

### APIs

- **NEW** API for getting and updating application json
- **Add** argocd application creation, list, query, modification and deletion interface
- **NEW** The interface to obtain the health status and synchronization status of continuous deployment
- **NEW** interface for synchronous argocd application
- **New** helm release interface
- **NEW** Synchronize resources under workspace to argocd, including workspace, cluster and namespace
- **NEW** Query Workload supports appgroup matching && workload name fuzzy matching
- **NEW** Supports docking microservice-related functions when creating and updating applications, including service registration, service governance, indicator monitoring and link tracking
- **NEW** List the namespace interfaces bound to the workspace to support searching and sorting
- **FIXED** Added a rollback function after failing to create an Application
- **Fix** from-git, from-jar can not pass the imageTag field in the front end
- **FIXED** Credential creation failed in new workspace
- **Fix** the problem that the dag graphs of from-jar and from-git cannot be displayed partially without registry credential
- **FIX** Null pointer error when pipeline contains empty cron string
- **Fix** After creating the Application, go to the pipeline module to update, if the name exceeds the limit, an error will be reported
- **FIXED** Create namespace failed but no rollback delete
- **Fix** Obtain the log of a step after running, in some special cases, the step_id is not shaped
- **Fix** When modifying the name of the pipeline, when the old name is the same as the new name, the page displays the processing of modification failure
- **Fix** When the image contains a port number, the verification is mistakenly regarded as an image-tag fix
- **Optimize** argocd initial authentication and connection

### Infrastructure

- **NEW** The basic image of the arm architecture is continuously released
- **Fix** Change the number of pods that jenkins agent can pull up to 100, change connectTimeout and readTimeout 2 timeout parameters
- **NEW** Added documentation for jenkins deployment in non-Global clusters
- **NEW** Add solution documentation for non-docker runtimes

## v0.7

Release date: 2022-9-28

### APIs

- **NEW** Support for running pipelines on clusters with containerd runtime
- **Add** worksapce role operation authentication
- **NEW** Added interface for listing application groups
- **NEW** Add interface for creating ResourceQuota
- **NEW** Add an interface to obtain cluster plug-in installation information
- **NEW** Added an interface to get the container image of rollout
- **NEW** Added the metircs interface, providing go gc and prometheus default indicators, as well as the counter of jenkins event
- **NEW** Support grayscale publishing for workloads containing multiple ports
- **NEW** When creating an application, svc supports NodePort and Loadbalance
- **FIXED** When creating a namespace, the Namespace does not exist, and the error of ResourceQuota does not exist, resulting in the failure to create the Namespace
- **Fix** select workspace associated cluster and namespace error

### Infrastructure

- **NEW** Add workspace authentication and cluster and namespace authentication where resources are deployed
- **Fix** The image field only checks the length, not as required
- **NEW** Install argo cd when deploying
- **Optimization** amamba charts installation completion prompt optimization
- **Optimization** amamba charts offline installation optimization

## v0.6

Release date: 2022-9-21

### APIs

- **New** Canary release list, update and delete interface
- **NEW** Canary Details Page
- **NEW** Added core apigroup, and moved workspace and namespace-related interfaces to this group
- **Add** helm creation and related interfaces (get the registry of the cluster, specify the details and version information of the chart)
- **NEW** Pipeline, pipeline running record search
- **FIXED** Quota check error reported when modifying namespace label

### API Services

- **NEW** CR such as GProductNavigator and GProductPorxy will be installed when installing via chart
- **Optimize** Optimize XML serialization and deserialization, gorm query syntax, pageutil model unification

### Infrastructure

- **NEW** E2E for credential CRUD and pipeline running CRUD interface
- **Optimize** Optimize the implementation of the workload list, and the performance has been greatly improved
- **NEW** Update the introduction of the application workbench, quickly create pipelines, use graphical editing pipelines and function overview product documentation

## v0.5

Release date: 2022-8-21

- **NEW** Add interface for deleting native applications
- **NEW** Get the secretReference list, verify the secret, whether the container registry is correct, and get the image tag list
- **NEW** List the names of deployments with grayscale release enabled
- **NEW** Add namespace-related interfaces, including listing namespaces, creating, updating, and deleting namespaces
- **Add** bind namespace to workspace
- **NEW** List all non-grpc-gateway URLs
- **NEW** The http interface for running the pipeline supports all build parameters, including file parameters
- **REMOVED** The gprc-gateway interface for running the pipeline is removed because of the new http interface for running the pipeline
- **NEW** Automatically install when a rollout is created without a specified built-in analysis template
- **NEW** The trigger method of adding webhook to the pipeline
- **Added** workload jump kpanda
- **Fix** Pipeline running records are not modified when renaming pipeline
- **Fix** Modify the default time zone of mysql to East Eighth District

## v0.4

Release date: 2022-7-25

- **NEW** Create applications and generate pipelines based on git
- **NEW** Create applications and generate pipelines based on jar packages
- **NEW** When running to a step that needs to be reviewed, the specified user can review: Approve/Cancel
- **NEW** Added verification of pipeline creation fields
- **New** Get jenkinsjson on the front-end page, save it to db after modifying jenkinsjson, and synchronize the modification of jenkinsfile and jenkinsjson
- **NEW** Added an API interface for listing workloads
- **Add** Enter the pipeline running record details page, click the `Run Report` tab page to view the task status
- **Optimization** Return error when pipeline settings do not allow concurrent builds and there are pipelines running
- **Optimization** The performance of the interface for obtaining pipeline parameters is optimized to the ms level
- **Optimization** Use the `Generic Event Plugin` plug-in to realize real-time synchronization of pipeline configuration and pipeline running status

## v0.3

Release date: 2022-7-08

- **NEW** API interface for creating applications based on images and listing all native workloads
- **Add** support for kubeconfig, access token key creation
- **NEW** Provide API for creating visible workspace list, creating ns and ns list
- **NEW** Pipeline creation supports build settings, trigger settings (timing trigger and code source trigger), single-branch pipeline based on git registry jenkinsfile, Jenkinsfile verification
- **Add** Pipeline running record details, full and step-by-step logs, support for delete, replay and cancel operations
- **New** E2E test coverage automatic calculation, continuous performance test report, automatic update dependency