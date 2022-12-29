# Workbench Release Notes

This page lists the Release Notes of the application workbench, so that you can understand the evolution path and feature changes of each version.

## 2022-11-30

### v0.10

#### New features

- **NEW** Added the warehouse function in gitops, which supports import and deletion
- **NEW** Added sync function for gitops app

#### Optimized

- **Optimized** Optimized the application access service grid process

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