# Global Management Release Notes

This page lists the Release Notes for global management of each version,
so that you can understand the evolution path and feature changes of each version.

## 2025-08-15

### v0.40.3

- **Fixed** an issue where login page icons and background were not displayed correctly.  
- **Fixed** an issue where customized login page charts were missing.  

## 2025-07-31

### v0.40.0

- **Added** sub-account support in SaaS mode.  
- **Added** CRUD operations for sub-accounts in SaaS mode.  
- **Added** new login and registration pages in SaaS mode.  
- **Improved** login `Token` to include `domain` information.  
- **Improved** Helm Chart `Values` configuration for `sidecar` resources by consolidating
  `sidecar.istio.io/proxyResources` from `apiserver`, `audit-server`, `ghippo-ui`, `anakin`,
  and `controller-manager` into `global.istioSidecar.resources` for centralized control.  
- **Fixed** an issue where selecting both `SSL` and `starTLS` when testing the mail server did not raise an error.  
- **Fixed** an issue where inserting a sub-product into the primary menu failed.  
- **Fixed** an issue where disabling two-factor authentication caused password reset to show `OTP` reset.  
- **Fixed** an issue where the frontend failed to fetch information from identity providers
  via the `OIDC` protocol in one click.  

## 2025-06-30

### v0.38.1

* **Added** support to display the most recent login time of `LDAP` users.
* **Added** quota management UI adaptation for `Ascend 910 VIR` type `GPU`.
* **Fixed** issue where some permission points were empty when viewing role details.

## 2025-05-31

### v0.37.0

* **Added** customizable support for the `gproductresourcepermissionses` CR controlling menu display based on permissions.
* **Optimized** SDK by adding the `RegisterDeltaGlobalAuthzPermissionHandler` method.
* **Fixed** issue where clearing CSS in advanced customization was unsuccessful.

## 2025-04-30

### v0.36.0

- **Added** service topology view into observability module.
- **Fixed** an issue where user `OpenAPI` tokens were missing assigned user group permissions.
- **Fixed** an issue preventing `LDAP` users from changing their language settings.

## 2025-02-28

### v0.35.0

- **Added** real-name authentication for individual public cloud users.
- **Added** audit logging for creating, updating, and deleting custom roles.
- **Fixed** login state validation issues in the `ListGProducts API`.
- **Fixed** an issue where audit logs were not recorded when saving `SMTP` settings.
- **Fixed** inconsistent search rules between the user authorization list and the group authorization list.
- **Fixed** inconsistent styling between global management and namespace quota management pages.
- **Fixed** incorrect display of allocated `vGPU` memory in the workspace.

## 2025-01-31

### v0.34.0

- **Added** support for global management to use cert-manager for generating and managing SSL certificates.
- **Added** disabled SSH keys and access credentials when a user is deleted or disabled.
- **Added** a feature gate for public cloud.
- **Added** public cloud user registration.
- **Added** phone number information to the public cloud user profile page.
- **Added** dual sidebars for public cloud (admin/user sidebar).
- **Fixed** an issue with vGPU allocated quota calculation in workspaces.
- **Fixed** an issue where searching for usernames containing `_` in the user list returned no results.
- **Fixed** an issue where some audit log resource names were empty.
- **Fixed** an issue with abnormal username display in audit logs.

## 2024-11-30

### v0.33.0

- **Upgraded** Istio to 1.22.3
- **Added** virtual machine module license
- **Added** metering and billing support for Muxi GPU in Operational Management
- **Fixed** an issue with resource name display anomaly for Create-User in audit logs

## 2024-10-31

### v0.32.0

- **Added** sidecar version role permission SDK
- **Added** cloud-native AI related permission points in Workspace Editor
- **Added** encryption implementation for username and password in session-limit interface
- **Fixed** an issue where the corresponding field was not cleared after re-setting
  user LDAP filter to empty during synchronization

## 2024-9-30

### v0.31.0

- **Added** support for username encryption when creating users
- **Added** custom roles that support Container Management folders and workspace roles, and allow their permission points to be mapped to predefined roles in Container Management
- **Fixed** an error related to excessively long license expiration periods.
- **Fixed** an error encountered when a resource is unbound from a workspace.
- **Fixed** an issue where the query methods for reports of the same type are inconsistent in __Global Management__ -> __Operations Management__ .

## 2024-8-31

### v0.30.0

- **Added** configuration and display of system information
- **Added** the SDK RegisterDeltaResourcePermissionHandler method
- **Added** tenant perspective and related permissions in __Global Management__ -> __Operations Management__
- **Improved** the scanning for hardcoded certificates using trivy and gosec
- **Improved** the development guide in __Global Management__ -> __Operations Management__
- **Fixed** an issue where the report would not display proper namespace information if there are no pods in the namespace under __Global Management__ -> __Operations Management__

## 2024-07-31

### v0.29.0

#### Features

- **Added** LDAP server to support LDAPS
- **Added** installer versions to __Global Management__ -> __Settings__ -> __About__

#### Improvements

- **Improved** login and password change functions to support username and password encryption
- **Improved** prompt text about binding resources on __Global Management__ -> __Workspace and Folder__ -> __Resource Group__

#### Fixes

- **Fixed** SMTP server settings
- **Fixed** an issue where installation fails when OEM is configured `enable`
- **Fixed** the inconsistency issue of English column names in exported reports in __Operations Management__

## 2024-06-30

### v0.28.0

#### Features

- **Added** OAuth2 Identity Provider generic plugin
- **Added** username and userLdapFilter fields to LDAP configuration
- **Added** installation insight-angent prompt in __Global Management__ -> __Operations Management__ -> __Billing Config__

#### Improvements

- **Improved** user creation to automatically remove spaces around the username text (if any) before saving
- **Improved** the search mechanism of binding resources
- **Improved** a SDK method `ListWorkspaceUsersByPermission()`

#### Fixes

- **Fixed** an issue that authorized users with a custom role can see all workspaces
- **Fixed** an issue that the RBAC Access Denied page will appear on the Insight page after closing the browser and reopening it
- **Fixed** an issue that the exported report has inconsistent fields with those shown on the page in __Global Management__ -> __Operations Management__

## 2024-5-31

### v0.27.0

- **Added** an option in Settings to show/hide the background video on the login page
- **Added** features to view/add/update/delete SSH certificate information in Personal Center
- **Added** features of creating user and changing password:
  encryption for username and password parameters when passed to API
- **Added** MySQL MGR mode
- **Improved** Keycloak component to version 22.0.4
- **Fixed** an issue with GPU count statistics after licensing by GPU

## 2024-4-30

### v0.26.0

- **Added** support for license by GPU
- **Added** a summary link in Audit Logs
- **Improved** unit tests for the Audit Logs SDK
- **Fixed** an issue with the user-agent field in Audit Logs
- **Fixed** an issue where Audit Logs login records often show one failure followed by one success
- **Fixed** an issue in __Operations Management__ where validation prompts were not removed
  after clicking cancel on billing configuration changes
- **Fixed** an issue in __Operations Management__ with GPU billing duration calculation in pod reports

## 2024-4-1

### v0.25.1

- **Fixed** an issue with resource quota check while workspace resource group is binding to a namespace

## 2024-3-31

### v0.25.0

#### Features

- **Added** a feature where top-level navigation bar is displayed based on permissions
- **Added** a feature where Workspace/Folder Editor does not support changing Workspace/Folder and names
- **Added** Ghippo support for ARM offline installation packages
- **Added** a method provided by SDK to find Alias using Workspace ID GetWorkspaceById()
- **Added** __Operations Management__ -> Report Management -> Pod Report: GPU statistics
- **Added** __Operations Management__ -> Accounting and Billing -> Pod Billing: GPU billing

#### Fixes

- **Fixed** an issue with front-end CSS errors on global management login
- **Fixed** an issue where the Refresh Token API in the observability interface could not update the Token

## 2024-1-31

### v0.24.0

- **Added** resource quotas limiting GPU
- **Added** support for DCE5 logged-in users to access Insight's Grafana and other components
- **Improved** rate limiting with single flight mechanism when triggering FoldersAuthz CR
- **Improved** to filter out duplicate authorizations
- **Improved** the condition where Workspace authorization information is not stored in FoldersAuthz CR
- **Improved** a full update of FoldersAuthz CR upon ghippo-controller-manager restart
- **Fixed** an issue where a large number of authorization requests caused FoldersAuthz CR updates to overwhelm k8s

## 2023-12-29

### v0.23.0

- **Added** a feature to automatically log out from the identity provider page when logging out of DCE 5.0
- **Added** support for usernames with underscores and other special characters
- **Added** removal of the restriction on authorizing usernames with special characters
- **Added** a user isolation mode between Folders
- **Added** support for authorizing multiple roles to Folder/Workspace users
- **Improved** initial username and password (admin/changeme) to be stored in Secret instead of ConfigMap
- **Fixed** an issue with the redirection of offline environment documentation site
- **Fixed** an issue with installer version 0.13 upgrade failure
- **Fixed** an issue with workspace large-scale test performance

## 2023-12-05

### v0.22.1

- **Fixed** an issue with incomplete display of middleware in the navigation bar

## 2023-11-30

### v0.22.0

#### Features

- **Added** auto-expanding active navigation bar
- **Added** SDK support for usernames with underscores
- **Added** support for DCE 4.0 to DCE 5.0 migration validation
- **Added** __Operations Management__ precise search in list
- **Improved** Chinese language support to the __About__ - __Product Versions__ submodule
  for kcoral, dowl, kcollie, and virtnest
- **Fixed** an issue where LDAP users synchronized over could not be added to groups
- **Fixed** an issue in Operations Management where workspace reports were not fully displayed

## 2023-11-01

### v0.21.0

#### Features

- **Added** a feature of integrating multiple ADs/LDAPs
- **Added** a feature of integrating multiple OIDCs
- **Added** a feature to distinguish users from different LDAP/OIDC
- **Added** a feature to prevent the removal of permission dependencies
- **Added** backend customization of the top-level navigation bar
- **Added** support for redirecting to the English documentation site in non-Chinese languages

#### Improvements

- **Improved** an issue with random 400 errors in the interface
- **Improved** Operations Management display of empty data in reports
- **Improved** Operations Management function to jump from the cluster billing list to the node billing list by 
  node count

#### Fixes

- **Fixed** an issue where Ghippo APIServer might deadlock on startup
- **Fixed** an issue in Operations Management with incorrect cluster billing calculations

## 2023-09-04

### v0.20.1

- **Fixed** an issue with random 400 errors in the interface

## 2023-08-30

### v0.20.0

- **Added** connection with Enterprise WeChat
- **Added** support for 8-32 character passwords
- **Added** support for integrating Kant license for cloud-edge collaboration
- **Added** Operations Management support for postgres/kingbase databases
- **Improved** added primary keys to some database tables without primary keys

## 2023-07-28

### v0.19.0

- **Added** support for integrating project group IDP login without clicking
- **Added** resource group binding to mesh / mesh-namespace
- **Added** tips for custom role permission points
- **Added** Settings -> Security Policies -> limiting multiple concurrent sessions for a single user
- **Added** Settings -> Security Policies -> limiting the maximum number of concurrent session connections
  for the system
- **Improved** support for customized parameters in Webhook URL
- **Fixed** an issue with errors when filling in the mail server
- **Fixed** an issue where LDAP users could not join groups

## 2023-07-06

### v0.18.1

- **Fixed** an issue where workspace cluster names could be empty
- **Fixed** an issue with Folder Admin role permissions in the workspace authorization list
- **Fixed** an issue with Ghippo upgrade from 0.17 to 0.18
- **Fixed** an issue where options for selecting cluster types were the same when adding shared resources
- **Fixed** an issue where mesh-type resources in the resource group list could not be unbound

## 2023-06-29

### v0.18.0

#### Features

- **Added** the feature of workspace migration
- **Added** features to create/edit/delete/list/view Webhook in Access Control
- **Added** a feature to automaticlly cleanup Webhook record in Access Control
- **Added** License expiration reminder
- **Added** License function unavailable after expiration
- **Added** the setting where users must enter the old password when changing passwords
- **Added** resource group support for binding service mesh resources
- **Added** support for external Postgres database
- **Added** more types of currencies which are supported by reports in Operations Management
- **Added** istio-ingressgateway and istiod supporting high availability

#### Improvements

- **Improved** backend configuration of passwords stored in secret

#### Fixes

- **Fixed** an issue with Audit Logs time zones
- **Fixed** an issue with role list not displaying during workspace authorization

## 2023-06-02

### v0.17.1

- **Fixed** an issue where migration files caused migration failures
- **Fixed** an issue where only Workspace Admin could be selected when creating a workspace

## 2023-05-30

### v0.17.0

#### Features

- **Added** features to access clients (create/view/list/update/delete)in Access Control
- **Added** features to create/edit/delete/list/view Webhook API in Access Control
- **Added** user CRUD/Login/Logout events triggering Webhook
- **Added** Access Control permission
- **Added** support for `.` and `@` in usernames/group names
- **Added** a feature where platform default language changes to auto-detected browser preference
- **Added** a feature of downloading audit logs as Excel and CSV formats
- **Added** a feature to separate display for system and user logs in Audit Logs 
- **Added** prohibition on removing admin user's admin role or editing admin's permissions
- **Added** display of role permission details in workspace authorization 
- **Added** unit test coverage which can only increase
- **Added** OpenAPI supporting version, OpenAPI documentation  deprecation (other GProduct modules 
  must be updated to the corresponding version in installer v0.8.0)
- **Added** a feature where GMagpie uses database configuration specifications (Helm parameters, DSN) to interface 
  with the installer in Operations Management
- **Added** Excel and CSV formats when downloading reports in Operations Management
- **Added** support for Workspace reports in Operations Management
- **Added** support for Workspace billing reports in Operations Management
- **Added** support for pod group reports in Operations Management
- **Added** support for pod group billing reports in Operations Management
- **Added** support for Namespace billing reports in Operations Management

#### Improvements

- **Improved** default sorting of the role list
- **Improved** Workspace Editor permission

#### Fixes

- **Fixed** an issue with the synchronization time of LDAP group synchronization

## 2023-04-28

### v0.16.1

- **Fixed** an issue where an infinite loop caused excessive CPU usage
- **Fixed** an issue where audit logs export was incomplete

## 2023-04-27

### v0.16.0

#### Features

- **Added** LDAP support for AD
- **Added** LDAP support for more parameters
- **Added** support for changing the login page background image
- **Added** support for modifying the ICP information at the bottom of the homepage and login page (update/display)
- **Added** support for modifying database connection Helm parameter format
- **Added** access management: access client API (create/view/list/update/delete)
- **Added** support for adding Path prefix to proxy URL
- **Added** Audit Logs SDK to directly call AuditServer API
- **Added** separate storage for user and system audit logs, with separate API access
- **Added** removal of API Server's dependency on accessing the external network

#### Improvements

- **Improved** filtering out non-existent permissions when creating customized roles
- **Improved** Audit Logs database partitioning functionality

#### Fixes

- **Fixed** an issue with displaying customized role types

## 2023-03-29

### v0.15.0

#### Features

- **Added** custom role function (create/edit/delete/view/list)
- **Added** support for GProduct permission and integration with custom role functionality
- **Added** handling of disconnected cluster resources
- **Added** Ghippo OpenAPI documentation implementation
- **Added** Audit Logs SDK for GProduct

#### Fixes

- **Fixed** an issue where tokens could still be used after the key expired
- **Fixed** an issue where the container registry was not controlled by the license

## 2023-02-27

### v0.14.0

#### Features

- **Added** Settings -> appearance -> advanced customization -> login page customization and post-login 
  page customization
- **Added** support for keycloak quarkus architecture in dual-stack environments
- **Added** JOB in CI process to check for non-compliant images in Helm chart packages and validate installation parameters
- **Added** an option in Helm values to enable/disable audit-related functionality with one click
- **Added** support for recording kpanda page operations in Audit Logs

#### Improvements

- **Improved** OpenAPI call method

#### Fixes

- **Fixed** some incorrect audit log names
- **Fixed** keycloak startup probe failureThreshold value to improve startup success rate
- **Fixed** binding/unbinding resource errors in i18n

## 2022-12-30

### v0.13.2

- **Fixed** the missing English explanations for interface permission descriptions
- **Fixed** an issue where database table updates might fail due to database encoding

## 2022-12-28

### v0.13.0

#### Features

- **Added** support for deploying a GM (Guomi) gateway in front of DCE 5.0 and accessing DCE 5.0 using a GM browser
- **Added** an option in Helm values to enable/disable Istio Sidecar functionality with one click
- **Added** Workspace and Folder Owner roles 
- **Added** setting where only users with Workspace/Folder Admin and Kpanda Owner permissions can bind resources
- **Added** open-source license scanning for all used libraries
- **Added** a __status__ column in the user list
- **Added** internal offline installation documentation
- **Added** SDK unit test coverage to 65%
- **Added** support for sending test emails and using mail servers without account credentials
- **Added** prompts for usernames that do not meet system requirements

#### Improvements

- **Improved** Ghippo authentication code to reduce memory usage
- **Improved** preloading mechanism of the frontend interface under low network conditions

#### Fixes

- **Fixed** an issue where OpenAPI cycle was a required parameter; it is now optional

## 2022-11-30

### v0.12.1

- **Improved** automatic construction of pure offline packages through CI
- **Improved** Ghippo upgrade documentation

## 2022-11-28

### v0.12.0

#### Features

- **Added** changed the __module__ in the resource group to __source__
- **Added** SDK provides notifications for changes in Workspace and Resource bindings
- **Added** complete integration with Insight metrics and otel tracing (including keycloak and db links)
- **Added** Keycloak changed to Quarkus architecture
- **Added** Keycloak image upgraded to version 20.0.1

#### Improvements

- **Improved** refactored the export audit logs http interface to a grpc stream interface
- **Improved** SDK memory usage, peak reduced by 50%
- **Improved** some audit logs code
- **Improved** e2e kind image switched to 1.25
- **Improved** resource usage efficiency increased to over 40%

#### Fixes

- **Fixed** an issue with strong binding of clusters
- **Fixed** an issue where selecting __Client secret sent as basic auth__ in the identity provider configuration 
  interface was not saved in keycloak

## 2022-11-01

### v0.11.2

- **Fixed** an issue with resource group binding to clusters
- **Fixed** an issue where workspaces could not be created when there were no workspaces

## 2022-10-28

### v0.11.0

#### Features

- **Added** interface for third-party applications to create SSO clients in Keycloak
- **Added** support for Mysql8
- **Added** integration with Insight (metrics, log, otel tracing)
- **Added** support for i18n in License module names
- **Added** support for multiple GProducts in a single License
- **Added** resource group support for binding cluster-type resources
- **Added** a "module" field to the resource group list
- **Added** a bound identifier to the resource group list
- **Added** resource binding interface support for Registry resource types

#### Improvements

- **Improved** resource types changed to enumeration
- **Improved** whether GProduct licenses need to be injected with variables is now configurable
- **Improved** CICD process

#### Fixes

- **Fixed** an issue where deleted clusters still existed
- **Fixed** an issue where keycloak jwks changes did not reset the Istio cache
- **Fixed** an issue with zero-value creation time for groups
- **Fixed** an issue where the __last used time__ field for access keys returned an empty string when not used

## 2022-09-28

### v0.10.0

#### Features

- **Added** support for login
- **Added** support for forgotten password
- **Added** support for CRUD functionality for internal messages
- **Added** support for SMTP mail server settings
- **Added** support for retrieving the top navigation bar
- **Added** support for updating the top navigation bar
- **Added** support for CRUD of user role permissions
- **Added** workspace -> lifecycle management (create/edit/delete/view/list)
- **Added** workspace -> hierarchy management (bind/list)
- **Added** workspace -> workspace and resource relationship management (bind/unbind/list)
- **Added** workspace -> workspace and role and user (group) relationship management (bind/unbind/list) (API/SDK)
- **Added** workspace -> authorization (API/SDK)
- **Added** workspace -> GProduct resource name registration
- **Added** About -> product version (create/edit/delete/view/list)
- **Added** About -> open-source software (list/initialize)
- **Added** About -> technical team (list/initialize)
- **Added** Licenses -> lifecycle management (create/edit/delete/view/list)
- **Added** Licenses -> retrieve ESN serial number
- **Added** Licenses -> handling of un-injected or erroneous situations
- **Added** workspace -> resource quota management (create/edit/delete/view/list/calculate allocated)
- **Added** workspace -> GProduct resource quota registration
- **Added** User and Access Control -> authorization (APIServer/SDK)
- **Added** Audit Logs -> display (view/list/cleanup settings/export)
- **Added** Audit Logs -> batch insertion
- **Added** Identity provider -> integrate LDAP -> user/group synchronization settings (create/edit/delete/view/sync)
- **Added** Settings -> Security Policies -> password policy settings
- **Added** personal center -> access keys (create/edit/delete/view/list)
- **Added** Audit Logs -> insertion of global management operations into Audit Logs
- **Added** Audit Logs -> integration with Insight to collect audit logs
- **Added** Settings -> Security Policies -> account lockout policy
- **Added** Settings -> Security Policies -> browser close policy
- **Added** identity provider -> integrate IDP (OIDC protocol)
- **Added** workspace -> shared cluster permission management
- **Added** workspace -> shared cluster quota management -> storage
- **Added** Settings -> top navigation appearance customization -> reset functionality
- **Added** Settings -> Security Policies -> session timeout policy
- **Added** Audit Logs -> automatic cleanup functionality
- **Added** Settings -> Security Policies -> account lockout policy
- **Added** Settings -> top navigation appearance customization -> restore functionality
- **Added** Settings -> login page appearance customization -> restore functionality
- **Added** product navigation -> homepage only displayed for admin users
- **Added** workspace -> users can only view the tree structure of workspaces and folders they have permissions for
- **Added** Keycloak high availability
- **Added** mail server configuration -> support for sending emails from Insight and Workbench
- **Added** compliance with Helm specifications, supporting installers and offline deployment
- **Added** Audit Logs -> automatic creation and merging of database partitions
- **Added** support for ARM64 architecture
- **Added** support for https
- **Added** login -> background theme supports animation
- **Added** authorization and authentication -> provide the current logged-in user's permission list to the frontend
- **Added** About -> software version -> module supports Chinese names
- **Added** overall bilingual documentation site structure and main content

#### Improvements

- **Improved** authorization and authentication -> provide a JOB to ensure synchronization of database and custom resources
- **Improved** LDAP -> configuration error checks
- **Improved** feedback and error messages for operations in various functions support both Chinese and English
- **Improved** workspace and folder -> check for existing sub-resources before deletion
- **Improved** keycloak jvm parameters
- **Improved** simplified mock using the mockery framework
