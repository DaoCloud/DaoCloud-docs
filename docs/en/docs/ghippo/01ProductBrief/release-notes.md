# Global Management Release Notes

This page lists the Release Notes for global management of each version, so that you can understand the evolution path and feature changes of each version.

## 2022-11-30

### v0.12.1

#### Optimization

- Automatically build pure offline packages via CI
- Optimize GHippo upgrade document

## 2022-11-28

### v0.12.0

#### New features

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

#### New features

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
- Fix the zero value problem of user group creation time
- Fixed access key 'last used time' field returning null character when not used`

## v0.10

Release date: 2022-10-21

- **NEW** License -> Not Filled or Error Handling
- **NEW** audit log -> database automatically creates and merges partitions
- **NEW** Added support for ARM64 architecture
- **NEW** support https
- **NEW** Login -> background theme supports animation
- **New** Authorization Authentication -> Provide the front-end with the permission list of the currently logged-in user
- **NEW** Added About -> Software Version -> Module Support Chinese Name
- **Optimize** authorization authentication -> provide a job to ensure the synchronization of db and cr
- **Optimized** LDAP -> configuration error checking
- **Optimization** The operation feedback and prompts for each function support Chinese and English
- **Optimize** Workspace and Hierarchy -> Check whether there are sub-resources before deleting
- **Optimize** Optimize keycloak jvm parameters

## v0.9

Release date: 2022-9-25

- **NEW** Platform Settings -> Security Policy -> Session Timeout Policy
- **NEW** Audit Log -> Auto Cleanup
- **NEW** Platform Settings -> Security Policy-Account Lockout Policy
- **NEW** Platform Settings -> Top Navigation Appearance Customization-Restore Function
- **NEW** Platform Settings -> Login Page Appearance Customization-Restore Function
- **NEW** Product Navigation -> Homepage is only displayed for admin users
- **New** Workspace -> Users can only view the workspace & folder tree structure with permission
- **NEW** Keycloak High Availability
- **Add** mail server configuration -> support Insight and application workbench to send mail
- **NEW** Meet the Helm specification, support installer and offline
- **Added** [About Platform](../04UserGuide/04PlatformSetting/about.md), [Audit Log](../04UserGuide/03AuditLog.md), [Access Key](../04UserGuide/ 06PersonalCenter/Password.md), [Language Settings](../04UserGuide/06PersonalCenter/Language.md), [Security Settings](../04UserGuide/06PersonalCenter/SecuritySetting.md) and other documents

## v0.8

Release date: 2022-8-21

- **New** Personal Center -> Access Key (Create/Edit/Delete/View/List)
- **Add** audit log -> global management operation insert audit log
- **New** Audit Log -> connect to Insight to collect audit log
- **NEW** Platform Settings -> Security Policy -> Account Lockout Policy
- **NEW** Platform Settings -> Security Policy -> Browser Closing Policy
- **Add** Identity Provider -> Interconnect with IDP (OIDC protocol)
- **NEW** Workspace -> Shared Cluster Authority Management.
- **NEW** Workspace -> Shared Cluster Quota Management -> Storage
- **NEW** Platform Settings -> Top Navigation Appearance Customization -> Reset Function
- **NEW** Added new pages on the documentation site: [Identity Provider](../04UserGuide/01UserandAccess/idprovider.md), [Mail Server Settings](../04UserGuide/04PlatformSetting/MailServer.md), [ Appearance Customization](../04UserGuide/04PlatformSetting/Appearance.md), [LDAP](../04UserGuide/01UserandAccess/ldap.md), [OIDC](../04UserGuide/01UserandAccess/oidc.md)

## v0.7

Release date: 2022-7-23

- **NEW** Workspace -> Resource Quota Management (Create/Edit/Delete/View/List/Calculate Allocated)
- **NEW** Workspace -> GProduct resource quota registration
- **New** User and Access Control -> Authentication (APIServer/SDK)
- **NEW** Audit Log -> Display (View/List/Clean Settings/Export)
- **Add** audit log -> batch insert
- **New** Identity Provider -> LDAP Connection -> User/User Group Synchronization Settings (Create/Edit/Delete/View/Sync)
- **NEW** Platform Settings -> Security Policy -> Password Policy Settings
- **Optimize** workspace -> code structure adjustment
- **NEW** Added new pages on the document site: [Create User Group and Authorize](../04UserGuide/01UserandAccess/Group.md), [User Group](../04UserGuide/01UserandAccess/Group.md), [Login](../04UserGuide/00Login.md), [Password Reset](../04UserGuide/password.md), [Global Admin Roles](../04UserGuide/01UserandAccess/global.md), [Resources Management (by Workspace)](../04UserGuide/02Workspace/wsbp.md), [Resource Management (by Role)](../04UserGuide/02Workspace/quota.md)

## v0.6

Release date: 2022-6-21

- **NEW** Workspace -> Lifecycle Management (Create/Edit/Delete/View/List)
- **NEW** Workspace -> Hierarchical relationship management (binding/list)
- **NEW** Workspace -> Workspace and resource relationship management (bind/unbind/list)
- **NEW** Workspace -> Workspace and role and user (group) relationship management (binding/unbinding/list) (API/SDK)
- **New** Workspace -> Authentication (API/SDK)
- **NEW** Workspace -> GProduct resource name registration
- **NEW** About -> Product Versions (Create/Edit/Delete/View/List)
- **NEW** About -> Open Source Software (List/Initialize)
- **NEW** Added About -> Technical Team (List/Initialize)
- **NEW** License -> Lifecycle Management (Create/Edit/Delete/View/List)
- **Added** License -> Get ESN serial number
- **NEW** Added new pages in the documentation site: [Common Terminology](../01ProductBrief/glossary.md), [Function Overview](../01ProductBrief/Features.md), [Quick Start/Create User and Authorization](../04UserGuide/01UserandAccess/User.md), [What is User Access and Control](../04UserGuide/01UserandAccess/iam.md), [User](../04UserGuide/01UserandAccess/User.md )

## v0.5

Release date: 2022-5-23

- **Improved** Simplify mocking with mockery framework
- **NEW** e2e tests for users, groups and logins
- **Add** login page update configuration interface
- **NEW** Added support for login
- **NEW** Add support for forgotten password
- **NEW** Added support for adding, deleting, modifying and checking of messages in the station
- **NEW** Added support for OPA authority management
- **NEW** Added support for SMTP setting mail server
- **NEW** Added support for getting queries from the top navigation bar
- **NEW** Added support for updating the top navigation bar
- **Add** support for user role rights management CRUD
- Added Honkit based documentation station template
- Add overall bilingual document station structure and main content
- Completion of ROADMAP content
- merge document ROADMAP content into overall ROADMAP file
- Documentation site updated [What is Ghippo](WhatisGhippo.md)
