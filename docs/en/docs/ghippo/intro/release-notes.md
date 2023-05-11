# Global Management Release Notes

This page lists the Release Notes for global management of each version, so that you can understand the evolution path and feature changes of each version.

## 2023-04-28

### v0.16.1

#### Fix

- Fix the problem of high CPU usage caused by infinite loop
- Fixed the problem of incomplete export of audit logs

## 2023-04-27

### v0.16.0

#### Features

- LDAP support for AD
- LDAP supports more parameters
- Support modifying the background image of the landing page
- Support the modification of filing information at the bottom of the home page and login page (update/display)
- Helm parameter format modification for database connection
- Access Management - Access Client API (Create/View/List/Update/Delete)
- Reverse generation URL supports adding Path in front
- The Audit Log SDK directly calls the AuditServer API
- Audit log user and system audits are divided into table storage and API access
- Remove the dependency of API Server accessing the external network

#### Optimization

- When creating a custom role, filter permissions that do not exist
- Simplified audit log database partition function

#### Fix

- Fixed the wrong display of custom character types

## 2023-03-29

### v0.15.0

#### Features

- Custom role function (create/edit/delete/view/list)
- Support GProduct permission point and custom role function docking
- Disconnected cluster resource processing
- GHippo OpenAPI documentation implementation
- Provide GProduct with insert audit log SDK

#### Fix

- Fixed the problem that the token can still be used after the key expires
- Fix the problem that the mirror warehouse is not controlled by the license

## 2023-02-27

### v0.14.0

#### Features

- Platform Settings->Appearance Customization->Advanced Customization->Login Page Customization and Post-Login Page Customization
- Support the keycloak quarkus architecture to run in a dual-stack environment
- A job is added to the CI process to detect whether there are non-compliant images in the helm chart package and whether the installation parameters are correct
- Set the switch in helm values, you can switch audit related functions with one click
- Audit log supports recording kpanda page operations

#### Optimization

- Optimization of OpenAPI calling method

#### Fix

- Fixed some wrong audit log names
- Modify the keycloak startup probe failureThreshold value to improve startup success rate
- Fix bind/unbind resource error i18n

## 2022-12-30

### v0.13.2

#### Fix

- The interface has supplemented the English copy that lacks permission instructions
- When updating the database table, an error may be reported due to the database encoding

## 2022-12-28

### v0.13.0

#### Features

- Support deploying a national secret gateway in front of DCE 5.0, and use a national secret browser to access DCE 5.0
- Set the switch in helm values, you can switch the istio sidecar function with one click
- Add Workspace and Folder Owner role to workspace and hierarchy
- Only users with Workspace/Folder Admin and Kpanda Owner permissions can perform resource binding
- Scan the open source license for the library used
- Added `Status` column to user list
- Provide offline installation documentation internally
- SDK unit testing up to 65%
- The interface supports sending test emails and email servers without account passwords
- The interface supports prompting for usernames that do not meet the system requirements

#### Optimization

- Ghippo authentication code optimization (reduce memory usage)
- Optimized the preloading mechanism when the front-end interface is low in network conditions

#### Fix

- Fixed the problem that OpenAPI cycle is a required parameter, and it is an optional parameter after the repair

## 2022-11-30

### v0.12.1

#### Optimization

- Automatically build pure offline packages via CI
- Optimize GHippo upgrade document

## 2022-11-28

### v0.12.0

#### Features

- Change `module` to `source` in resource group
- SDK provides Workspace and Resource binding change notification
- Complete docking Insight metrics and otel tracing (join keycloak and db links)
- Keycloak changed to Quarkus architecture
- Keycloak image upgraded to version 20.0.1

#### Optimization

- Refactored export audit log http interface to gprc stream interface
- SDK memory usage optimization, the peak value is reduced by 50%
- Audit log part code optimization
- e2e's kind image cut to 1.25
- Improve resource usage efficiency to over 40%

#### Bug fixes

- Fix the problem of strong binding cluster
- Fixed the problem that the option `Client secret sent as basic auth` in the configuration identity provider interface was not saved to keycloak

## 2022-11-01

### v0.11.2

#### Bug fixes

- Turn off the resource group binding cluster function
- Fixed the problem that the workspace cannot be created when there is no workspace

## 2022-10-28

### v0.11.0

#### Features

- Provide an interface for third-party applications to create an SSO docking Client in Keycloak
- Support Mysql8
- Docking Insight(metrics, log, otel tracing)
- License module name supports i18n
- Support multiple GProducts in one license
- The resource group is newly added to bind cluster type resources
- Added "Module" field to the resource group list
- The resource group list adds the bound identifier
- The resource binding interface supports the Registry resource type.

#### Optimization

- Change resource type to enumeration
- Whether the GProduct license needs to be filled with variables and changed to configurable
- Optimize CICD process

#### Bug fixes

- Repair deleted clusters still have problems
- Fixed istio cache not being reset after keycloak jwks change
- Fix the zero value problem of group creation time
- Fixed access key 'last used time' field returning null character when not used`

## v0.10

Release date: 2022-10-21

- **Added** License -> Not Filled or Error Handling
- **Added** audit log -> database automatically creates and merges partitions
- **Added** Added support for ARM64 architecture
- **Added** support https
- **Added** Login -> background theme supports animation
- **Added** Authorization Authentication -> Provide the front-end with the permission list of the currently logged-in user
- **Added** Added About -> Software Version -> Module Support Chinese Name
- **Optimize** authorization authentication -> provide a job to ensure the synchronization of db and cr
- **Optimized** LDAP -> configuration error checking
- **Optimization** The operation feedback and prompts for each function support Chinese and English
- **Optimize** Workspace and Hierarchy -> Check whether there are sub-resources before deleting
- **Optimize** Optimize keycloak jvm parameters

## v0.9

Release date: 2022-9-25

- **Added** Platform Settings -> Security Policy -> Session Timeout Policy
- **Added** Audit Log -> Auto Cleanup
- **Added** Platform Settings -> Security Policy-Account Lockout Policy
- **Added** Platform Settings -> Top Navigation Appearance Customization-Restore Function
- **Added** Platform Settings -> Login Page Appearance Customization-Restore Function
- **Added** Product Navigation -> Homepage is only displayed for admin users
- **Added** Workspace -> Users can only view the workspace & folder tree structure with permission
- **Added** Keycloak High Availability
- **Added** mail server configuration -> support Insight and App Workbench to send mail
- **Added** Meet the Helm specification, support installer and offline
- **Added** [About Platform](../user-guide/platform-setting/about.md), [Audit Log](../user-guide/audit-log.md), [Access Key](../04UserGuide/ 06PersonalCenter/Password.md), [Language Settings]../user-guide/06PersonalCenter/Language.mdd), [Security Settings]../user-guide/06PersonalCenter/SecuritySetting.mdd) and other documents

## v0.8

Release date: 2022-8-21

- **Added** Personal Center -> Access Key (Create/Edit/Delete/View/List)
- **Added** audit log -> global management operation insert audit log
- **Added** Audit Log -> connect to Insight to collect audit log
- **Added** Platform Settings -> Security Policy -> Account Lockout Policy
- **Added** Platform Settings -> Security Policy -> Browser Closing Policy
- **Added** Identity Provider -> Interconnect with IDP (OIDC protocol)
- **Added** Workspace -> Shared Cluster Authority Management.
- **Added** Workspace -> Shared Cluster Quota Management -> Storage
- **Added** Platform Settings -> Top Navigation Appearance Customization -> Reset Function
- **Added** Added new pages on the documentation site: [Identity Provider](../user-guide/access-control/idprovider.md), [Mail Server Settings](.../user-guide/platform-setting/MailServer.md, [ Appearance Customization](.../user-guide/platform-setting/Appearance.md, [LDAP](../user-guide/access-control/ldap.md), [OIDC](../user-guide/access-control/oidc.md)

## v0.7

Release date: 2022-7-23

- **Added** Workspace -> Resource Quota Management (Create/Edit/Delete/View/List/Calculate Allocated)
- **Added** Workspace -> GProduct resource quota registration
- **Added** Access Control -> Authentication (APIServer/SDK)
- **Added** Audit Log -> Display (View/List/Clean Settings/Export)
- **Added** audit log -> batch insert
- **Added** Identity Provider -> LDAP Connection -> User/group Synchronization Settings (Create/Edit/Delete/View/Sync)
- **Added** Platform Settings -> Security Policy -> Password Policy Settings
- **Optimize** workspace -> code structure adjustment
- **Added** Added new pages on the document site: [Create group and Authorize](../user-guide/access-control/Group.md), [group](../user-guide/access-control/Group.md), [Login](../user-guide/00Login.md), [Password Reset](../user-guide/password.md), [Global Admin Roles](../user-guide/access-control/global.md), [Resources Management (by Workspace)](../../user-guide/workspace/wsbp.md[Resource Management (by Role)](../../user-guide/workspace/quota.md

## v0.6

Release date: 2022-6-21

- **Added** Workspace -> Lifecycle Management (Create/Edit/Delete/View/List)
- **Added** Workspace -> Hierarchical relationship management (binding/list)
- **Added** Workspace -> Workspace and resource relationship management (bind/unbind/list)
- **Added** Workspace -> Workspace and role and user (group) relationship management (binding/unbinding/list) (API/SDK)
- **Added** Workspace -> Authentication (API/SDK)
- **Added** Workspace -> GProduct resource name registration
- **Added** About -> Product Versions (Create/Edit/Delete/View/List)
- **Added** About -> Open Source Software (List/Initialize)
- **Added** Added About -> Technical Team (List/Initialize)
- **Added** License -> Lifecycle Management (Create/Edit/Delete/View/List)
- **Added** License -> Get ESN serial number
- **Added** Added new pages in the documentation site: [Common Terminology](glossary.md), [Function Overview](feature.md), [Quick Start/Create User and Authorization](../user-guide/access-control/User.md), [What is User Access and Control](../user-guide/access-control/iam.md), [User](../04UserGuide/01UserandAccess/User.md )

## v0.5

Release date: 2022-5-23

- **Optimized** Simplify mocking with mockery framework
- **Added** e2e tests for users, groups and logins
- **Added** login page update configuration interface
- **Added** Added support for login
- **Added** Add support for forgotten password
- **Added** Added support for adding, deleting, modifying and checking of messages in the station
- **Added** Added support for OPA authority management
- **Added** Added support for SMTP setting mail server
- **Added** Added support for getting queries from the top navigation bar
- **Added** Added support for updating the top navigation bar
- **Added** support for user role rights management CRUD
- Added Honkit based documentation station template
- Add overall bilingual document station structure and main content
- Completion of ROADMAP content
- merge document ROADMAP content into overall ROADMAP file
- Documentation site updated [What is Ghippo](what.md)
