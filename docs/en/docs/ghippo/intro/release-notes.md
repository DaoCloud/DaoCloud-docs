# Global Management Release Notes

This page lists the Release Notes for global management of each version, so that you can understand the evolution path and feature changes of each version.

## 2023-11-30

### v0.22.0

#### Features

- Automatically expand the active navigation bar
- Support for underscores in usernames in the SDK
- DCE 4.0 to DCE 5.0 migration scheme validation support
- Added precise search to `Operations Management` list

#### Improvements

- Added Chinese language support to the `About Platform` - `Product Versions` submodule for kcoral, dowl, kcollie, and virtnest

#### Fixes

- Fixed issue with adding user groups for synchronized LDAP users
- Fixed issue with incomplete display of workspace reports in `Operations Management`

## 2023-11-1

### v0.21.0

#### Features

- Support for integrating with multiple AD/LDAP servers
- Support for integrating with multiple OIDC providers
- Differentiate users based on their LDAP/OIDC source
- Dependencies for permissions cannot be cancelled
- Backend customization of the primary navigation bar
- Support for redirecting to English documentation site in non-Chinese languages

#### Improvements

- Improved handling of interface error 400 without specific cause
- Enhanced display of empty data in `Operational Management` reports
- Improved functionality of jumping from cluster billing list to node billing list in `Operational Management`

#### Fixes

- Fixed potential deadlock issue during startup of Ghippo APIServer
- Fixed calculation error in cluster billing for `Operational Management`

## 2023-09-04

### v0.20.1

#### Bug Fix

- Fixed issue causing unnecessary 400 error in the interface

## 2023-08-30

### v0.20.0

#### Features

- Added support for integrating with WeCom.
- Passwords now support 8-32 characters.
- Added support for Cloud-Edge Collaboration Kant integration with a license.
- `Operations Management` Added support for PostgreSQL/Kingbase databases.

#### Improvements

- Added primary keys to some database tables that were missing them.

## 2023-07-28

### v0.19.0

#### Features

- Support automatic login for IDP integration with project groups.
- Resource group binding for mesh/mesh-namespace.
- Add tips to custom role permissions.
- Platform settings - Security policies - Restrict multiple concurrent sessions for individual users.
- Platform settings - Security policies - Limit maximum concurrent session connections for the system.

#### Improvements

- Custom parameters support for Webhook URL.

#### Fixes

- Fixed error when filling in email server details.
- Fixed issue with LDAP users failing to join user groups.

## 2023-07-06

### v0.18.1

#### Fixes

- Fixed the issue where workspace cluster names could be empty.
- Fixed the permission issue with Folder Admin role workspace authorization list.
- Fixed the upgrade failure from GHippo 0.17 to 0.18.
- Fixed the issue where the options for selecting cluster types were the same when adding shared resources.
- Fixed the issue in the resource group list where grid-type resources could not be unbound.

## 2023-06-29

### v0.18.0

##### Features

- Workspace migration
- Access management - Webhook (create/edit/delete/list/view)
- Automatic cleanup of Webhook records in the background
- Reminder before license expiration
- Disabled functionality after license expiration
- Users need to enter old password when changing their password
- Resource groups can be bound to service mesh resources
- Support for external Postgres database
- Operational management - Reports support more types of currencies
- High availability support for istio-ingressgateway and istiod

#### Improvements

- Backend configuration passwords are stored in secrets

#### Fixes

- Fixed timezone issue in audit logs
- Fixed role list display issue during workspace authorization

## 2023-06-02

### v0.17.1

#### Fixes

- Fixed migration failure caused by incorrect file migration
- Fixed issue where only the Workspace Admin role could be selected when creating a workspace

## 2023-05-30

### v0.17.0

#### Features

- Access Control： Access Clients (Create/View/List/Update/Delete)
- Access Control： Webhook API (Create/Edit/Delete/List/View)
- User CRUD/Login/Logout event triggers webhook
- Access Control provides permission points
- Username/group name supports `.` and `@`
- The default language of the platform is changed to automatically detect browser preferences.
- Audit logs can be downloaded in Excel and CSV formats
- Audit log: Two types of logs (system and user) are displayed separately
- Prevent removing the admin role of the admin user or editing admin permissions
- Workspace authorization displays the details of the role's permissions
- Unit test coverage can only rise, not fall.
- OpenAPI supports versions, and OpenAPI documents support deprecation (other GProduct modules must be updated synchronously to the corresponding version in installer v0.8.0)
- Operations Management: GMagpie uses database configuration specifications (Helm parameters, DSN) to dock with the installer.
- Operations Management: Reports can be downloaded in Excel and CSV formats.
- Operations Management: Supports Workspace reports.
- Operations Management: Supports Workspace billing reports.
- Operations Management: Supports pod reports.
- Operations Management: Supports pod billing reports.
- Operations Management: Supports Namespace billing reports.

#### Optimize

- Optimize the default sorting of the role list.
- Modify Workspace Editor permission points.

#### Fix

- Fixed the synchronization time issue of LDAP synchronized groups.

## 2023-04-28

### v0.16.1

#### Fixes

- Fixed the issue of high CPU usage caused by infinite loop
- Fixed the issue of incomplete export of audit logs

## 2023-04-27

### v0.16.0

#### Features

- LDAP support for AD
- LDAP supports more parameters
- Support modifying the background image of the landing page
- Support the modification of filing information at the bottom of the home page and login page (update/display)
- Helm parameter format modification for database connection
- Access Control - Access Client API (Create/View/List/Update/Delete)
- Reverse generation URL supports adding Path in front
- The Audit Log SDK directly calls the AuditServer API
- Audit log user and system audits are divided into table storage and API access
- Remove the dependency of API Server accessing the external network

#### Optimization

- When creating a custom role, filter permissions that do not exist
- Simplified audit log database partition function

#### Fixes

- Fixed the wrong display of custom character types

## 2023-03-29

### v0.15.0

#### Features

- Custom role feature (create/edit/delete/view/list)
- Support GProduct permission point and custom role feature docking
- Disconnected cluster resource processing
- GHippo OpenAPI documentation implementation
- Provide GProduct with insert audit log SDK

#### Fixes

- Fixed the issue that the token can still be used after the key expires
- Fixed the issue that the container registry is not controlled by the license

## 2023-02-27

### v0.14.0

#### Features

- Platform Settings->Appearance Customization->Advanced Customization->Login Page Customization and Post-Login Page Customization
- Support the keycloak quarkus architecture to run in a dual-stack environment
- A job is added to the CI process to detect whether there are non-compliant images in the helm chart package and whether the installation parameters are correct
- Set the switch in helm values, you can switch audit related features with one click
- Audit log supports recording kpanda page operations

#### Optimization

- Optimization of OpenAPI calling method

#### Fixes

- Fixed some wrong audit log names
- Modify the keycloak startup probe failureThreshold value to improve startup success rate
- Fixed bind/unbind resource error i18n

## 2022-12-30

### v0.13.2

#### Fixes

- The interface has supplemented the English copy that lacks permission instructions
- When updating the database table, an error may be reported due to the database encoding

## 2022-12-28

### v0.13.0

#### Features

- Support deploying a national secret gateway in front of DCE 5.0, and use a national secret browser to access DCE 5.0
- Set the switch in helm values, you can switch the istio sidecar feature with one click
- Add Workspace and Folder Owner role to Workspace and Folder
- Only users with `Workspace Admin`, `Folder Admin`, and `Kpanda Owner` permissions can perform resource binding
- Scan the open source license for the library used
- Added `Status` column to user list
- Provide offline installation documentation internally
- SDK unit testing up to 65%
- The interface supports sending test emails and email servers without account passwords
- The interface supports prompting for usernames that do not meet the system requirements

#### Optimization

- Ghippo authentication code optimization (reduce memory usage)
- Optimized the preloading mechanism when the front-end interface is low in network conditions

#### Fixes

- Fixed the issue that OpenAPI cycle is a required parameter, and it is an optional parameter after the repair

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
- Complete docking Insight metrics and otel tracing (join keycloak and db traces)
- Keycloak changed to Quarkus architecture
- Keycloak image upgraded to version 20.0.1

#### Optimization

- Refactored export audit log http interface to gprc stream interface
- SDK memory usage optimization, the peak value is reduced by 50%
- Audit log part code optimization
- e2e's kind image cut to 1.25
- Improve resource usage efficiency to over 40%

#### Fixes

- Fixed the issue of strong binding cluster
- Fixed the issue that the option `Client secret sent as basic auth` in the configuration identity provider interface was not saved to keycloak

## 2022-11-01

### v0.11.2

#### Fixes

- Turn off the resource group binding cluster function
- Fixed the issue that the workspace cannot be created when there is no workspace

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

#### Fixes

- Fixed deleted clusters still have issues
- Fixed istio cache not being reset after keycloak jwks change
- Fixed the zero value issue of group creation time
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
- **Optimized** authorization authentication -> provide a job to ensure the synchronization of db and cr
- **Optimized** LDAP -> configuration error checking
- **Optimized** The operation feedback and prompts for each feature support Chinese and English
- **Optimized** Workspace and Folder -> Check whether there are sub-resources before deleting
- **Optimized** Optimize keycloak jvm parameters

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
- **Added** mail server configuration -> support Insight and Workbench to send mail
- **Added** Meet the Helm specification, support installer and offline

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

## v0.7

Release date: 2022-7-23

- **Added** Workspace -> Resource Quota Management (Create/Edit/Delete/View/List/Calculate Allocated)
- **Added** Workspace -> GProduct resource quota registration
- **Added** Access Control -> Authentication (APIServer/SDK)
- **Added** Audit Log -> Display (View/List/Clean Settings/Export)
- **Added** audit log -> batch insert
- **Added** Identity Provider -> LDAP Connection -> User/group Synchronization Settings (Create/Edit/Delete/View/Sync)
- **Added** Platform Settings -> Security Policy -> Password Policy Settings
- **Optimized** workspace -> code structure adjustment

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
- Added overall bilingual document station structure and main content
- Completion of ROADMAP content
- merge document ROADMAP content into overall ROADMAP file
- Documentation site updated [What is Ghippo](index.md)
