# Releases Notes

This page lists the release notes of Microservices to help you learn its feature development and bug fixing progress.

## 2023-12-01

### v0.30.0

#### Fixes

- **Fixed** issue with incorrect running status of gateway
- **Fixed** status check issue with Nacos Operator
- **Fixed** status check issue with edge instance of mesh service

#### Improvements

- **Improved** gateway-related APIs
- **Improved** query logic for gateway logs to support custom field queries

## 2023-11-26

### v0.29.0

#### New Features

- **Added** API documentation management and API querying
- **Added** visualization of traffic swimlane for gray release, displaying the internal gray release swimlane division and data flow through views

#### Fixes

- **Fixed** logic for grid instance list in grid mode governance
- **Fixed** synchronization issues with managed Nacos controllers

#### Improvements

- **Improved** gateway service list API and added access address display feature
- **Improved** logic for synchronizing API updates after modifying services
- **Improved** loading speed of gateway resource list
- **Improved** configuration details for gateway timeout settings

### 2023-11-07

#### V0.28.1

##### Fixes

- **Fixed** sorting issue in the gateway service list
- **Fixed** multiple line break issue when importing gateway APIs
- **Fixed** the problem where Seata Operator image does not support offline repository
- **Fixed** the issue with abnormal offline release process

## 2023-10-26

### V0.28.0

#### New Features

- **New** Added support for regular expression and exact match for gateway API request headers.
- **New** Added support for bulk import and export of gateway APIs.
- **New** Added support for managing multiple versions of Nacos (currently supports versions 2.0.4, 2.1.1, and 2.2.3).
- **New** Added support for complex password requirements in Sentinel console.
- **New** Added support for targeted gray release of Nacos configuration files.
- **New** Added support for distributed transactions (including TCC mode, FMT mode, SAGA mode, XA mode).
- **New** Added support for importing interfaces using Swagger standard through visual form interface.

#### Fixes

- **Fixed** the issue of supporting different versions of managed Nacos.
- **Fixed** the issue of duplicate request methods in the gateway interface list.
- **Fixed** the problem of Zookeeper registry not being able to connect to instances with TLS protocol.
- **Fixed** the issue of domain deletion and update failure after enabling global authentication in the gateway.
- **Fixed** the issue of incorrect CPU usage at the namespace level in managed Nacos.
- **Fixed** the issue of abnormal service change when switching from NodePod mode to ClusterIP mode in managed Nacos.
- **Fixed** the issue of abnormal Seata interface verification.
- **Fixed** the issue of abnormal workspace access when switching registry center.
- **Fixed** the permission issue with related interfaces of managed Nacos.
- **Fixed** the issue with Grafana monitoring panel for managed Nacos.
- **Fixed** the issue with Sentinel Grafana monitoring panel.
- **Fixed** the accuracy issue with overall permissions.

#### Improvements

- **Improved** the update logic of the gateway, which does not allow disabling HTTPS at the gateway level when the domain has enabled HTTPS.
- **Improved** the accuracy of audit log events.
- **Improved** Optimized the logic of cloud-native microservice WebAssembly plugins.
- **Improved** the gateway health query logic on the overview page (changed from Rate to Increase).
- **Improved** the Swagger path by removing version information from the URL and supporting multiple versions of APIs.
- **Improved** Skoala Init Helm Chart to support distributed transaction controller (Seata Operator).
- **Improved** Skoala Agent certificate.
- **Improved** interface descriptions and details in all Swagger documentation.
- **Improved** audit log format and automatic generation mechanism.
- **Improved:** When releasing production versions, the Skoala Helm Chart will be published to the official image repository's System project.

## 2023-09-01

### v0.27.2

#### Fixes

- **Fixed** Frontend updated to version 0.18.1, resolving UI issues

### v0.27.1

#### Fixes

- **Fixed** Issue of duplicate details in batch deletion response
- **Fixed** Problem with sorting plugin information in cloud native microservices port list
- **Fixed** Issue with abnormal display of traffic swimlane list
- **Fixed** Inconsistent container names for frontend components
- **Fixed** Some errors in Sentinel business application monitoring reports

#### Improvements

- **Improved** Upgraded Insight version to 0.19.2
- **Improved** Upgraded Ghippo version to 0.20.0

!!! note "Important Note"

    If your Microservice Engine version is greater than `v0.24.2`,
    it is important to note that there are incompatible updates for versions `v0.24.2`
    and earlier. This is due to changes in the open-source component repository address
    related to the gateway. To ensure a smooth upgrade process, make sure to manually
    delete the old `gateway-api-admission-xxxxx` Job before proceeding with the update.

## 2023-08-25

### V0.27.0

#### New Features

- **Added** Permission dependencies for various module functionalities
- **Added** Exception details API field for managed resources
- **Added** API interface to retrieve user permission points
- **Added** Duplicate check API for gateway domain creation
- **Added** Failure reason API information for service addition in traffic swimlane
- **Added** API interfaces for managed Nacos gray release
- **Added** Support for multiple Envoy instances in a single machine for the gateway, resolving
  injection failure issues for edge cars in the mesh as gateways
- **Added** API interface to retrieve port rate limiting rules list
- **Added** Regular expression and exact path matching modes for API matching in the gateway
- **Added** Authentication-related API interfaces for Sentinel console
- **Added** Export and import interfaces for API configuration in the gateway
- **Added** API interfaces for relevant statistics data in the gateway overview

#### Fixes

- **Fixed** Inconsistent permissions between gateway service access and predefined permissions
- **Fixed** Incorrect representation of service governance status
- **Fixed** Exceptional return issue in managed Nacos configuration gray release
- **Fixed** Error in service instance list in managed Nacos
- **Fixed** Duplicated service versions in traffic swimlane
- **Fixed** Abnormal service list issue in traffic swimlane
- **Fixed** Service deletion issue in traffic swimlane
- **Fixed** Null pointer exception in swimlane list when error reason is empty
- **Fixed** Non-functional Skoala-init Chart form mode configuration

#### Improvements

- **Improved** Changed the deletion of swimlane services from delete method to put method as required.
- **Improved** Removed redundant permission dependencies and improved internal permission dependencies
- **Improved** Adapted interface display requirements for traffic swimlane
- **Improved** Cloud native microservice plugin interface
- **Improved** Changed the method of adding swimlane services from batch to single entry
- **Improved** Front-end component Deployment port from 80 to 8080
- **Improved** Upgraded Ghippo SDK to v0.20.0-dev2

!!! note "Important Note"

    When the Microservice Engine version is greater than `v0.24.2`, there are incompatible updates
    for versions `v0.24.2` and earlier. Since the gateway involves changes in the open-source component
    repository addresses, it is necessary to manually delete the old `gateway-api-admission-xxxxx` Job
    before performing the upgrade. Then proceed with the normal upgrade process.

## 2023-08-03

### v0.26.2

#### Fixed

- **Fixed** Issue with detection of `Consul` registry connectivity
- **Fixed** Issue with gateway restarting due to abnormal application of plugins
- **Fixed** Issue with abnormal configuration of gateway verification plugins
- **Fixed** Issue with abnormal editing of cluster flow control rules in `Sentinel`

!!! note "Important Note"

    Starting from Microservice Engine version `v0.24.2`, there is an incompatible update for versions `v0.24.2` and earlier. This is because the gateway involves a change in the address of the open-source component repository. Therefore, before updating, you need to manually delete the existing `gateway-api-admission-xxxxx` Job and then proceed with the normal upgrade process.

## 2023-07-26

### v0.26.1

#### Fixes

- **Fixed** the issue of incorrect version of the Agent component.

## 2023-07-25

### v0.26.0

#### New Features

- **Added** interface for viewing Sentinel flow control rules.
- **Added** APIs for cloud native microservice governance.
- **Added** APIs for cloud native microservice traffic lanes.
- **Added** support for version 0.19 of the observability module.
- **Added** API for displaying audit log in the overall overview.
- **Added** API for displaying resources in the gateway overview page.
- **Added** APIs for global validation plugin capabilities at the gateway level.

#### Fixes

- **Fixed** the issue of Nacos port not being updated.
- **Fixed** the issue of cluster flow control rules in Sentinel not being saved.
- **Fixed** the issue of API exception when deleting non-empty services in Nacos.
- **Fixed** the issue of duplicate data in gateway monitoring data.
- **Fixed** the issue with the use of plugins in cloud native microservices related APIs.
- **Fixed** the issues with gateway domain naming rules.
- **Fixed** the issue of incorrect version in cloud native microservice traffic lanes.

#### Optimizations

- **Optimized** the driver name of the People's Congress Golden Warehouse database from "kb_v8r6" to "kingbase".

## 2023-07-19

### v0.25.0

#### New Features

- **Added** tagging of gateway runtime mesh injection.
- **Added** cascading selection capability for permissions associated with middleware.
- **Added** API for viewing cloud native microservice flow control rules.
- **Added** APIs for cloud native microservice governance.
- **Added** component version information for cluster readiness check during managed resource installation.
- **Added** fuzzy search capability for various search APIs.

#### Fixes

- **Fixed** the issue of incorrect external image scanning address in the pipeline.
- **Fixed** the issue of missing directory-level dependency for permissions associated with middleware.

#### Optimizations

- **Optimized** the chain validation of gateway and related resource changes.
- **Optimized** the gateway listening port from cluster IP to container port.

## 2023-07-06

### v0.24.2

#### Fixes

- **Fixed** page experience optimization and bug fixes.

## 2023-07-05

### V0.24.1

#### Fixes

- **Fixed** the issue of outdated versions in Skoala-init Chart form
- **Fixed** page experience improvements and issues

## 2023-06-30

### V0.24.0

#### New Features

- **Added** API for cloud native microservices plugins
- **Added** cascading selection capability for permissions associated with middleware operations

#### Fixes

- **Fixed** data exception in Insight integration
- **Fixed** abnormal filtering results for gateway status

#### Improvements

- **Improved** chain validation for gateway and related resource changes

## 2023-06-26

### V0.23.0

#### New Features

- **Added** batch online/offline interface for gateway API
- **Added** enhanced health check configuration for engine components
- **Added** support for tag caching in cache logic
- **Added** mandatory injection option for mesh sidecar during gateway creation and update
- **Added** support for filtering gateway list by status
- **Added** integration of audit logs
- **Added** license check in continuous integration
- **Added** storage of sensitive information in Secret in Charts
- **Upgraded** managed Nacos version to 2.2.3
- **Upgraded** Sentinel version to 0.10.5

#### Fixes

- **Fixed** alignment of Insight integration data metrics with raw data
- **Fixed** permission inheritance issue when integrating with mSpider module
- **Fixed** missing governance status in Nacos instance list
- **Fixed** cluster flow control name issue in Sentinel
- **Fixed** query data not being aggregated by workspace in overall overview
- **Fixed** issue where gateway can enable HTTPS even if it is disabled
- **Fixed** default value issue in Skoala-init Chart form data

#### Improvements

- **Improved** user experience and issues with Sentinel Grafana
- **Improved** display of relevant resource alerts in managed resource alarms
- **Refactored** configuration structure of global management module
- **Improved** reading of managed Nacos information through Clusterpedia
- **Upgraded** Insight integration to version 0.17.3
- **Improved** flexibility of database-related configuration

## 2023-05-31

### V0.22.2

#### Fixes

- **Fixed** issues with Sentinel cluster flow control API
- **Fixed** issues with fuzzy query API for Sentinel rules

#### Improvements

- **Improved** default values for connecting to the database to increase fault tolerance

## 2023-05-29

### V0.22.1

#### Fixes

- Positions of plugin CRDs are not correc.
- Issue related to OpenAPI publishing process.

#### Enhancement

- Set default values for database of Hive component.

## 2023-05-26

### V0.22.0

#### New Features

- Support for Nacos v2.2.x.
- Gateway tracing.
- Cloud native microservice path rewrite API.
- Cloud native microservice timeout API.
- Cloud native microservice fault injection API.
- Cloud native microservice retry and other APIs.
- WASM plugin for Cloud native microservices.
- Skoala-init Chart adds JSON Schema.
- OpenAPI document publishing process.
- Hive supports database neutrality.

#### Fixes

- NullPointerException in the Nacos related API.
- Displayed port of Nacos was incorrect.
- HTTPProxy spelling error in Grafana.
- SQL scripts in Nacos database initialization.
- Custom permissions of gateway.
- NullPointerException when calling Ghippo.
- Nacos service metadata interface exception.
- Error in updating domain.
- Issues when frequently calling Kpanda API.
- Inaccurate data acquisition through Insight access.
- Error occurred when querying WASM plugin.
- Error occurred after updating API routing service.
- Sentinel Token server resources.
- ZooKeeper tracing is not closed.

#### Enhancement

- Sentinel monitoring panel structure and data logic.
- Remove virtualhost CR from Gateway domain management.
- Sentinel cluster flow control API logic.
- Upgrade Ghippo to 0.17.0-rc2.
- Database initialization component "sweet has been deprecated since version 0.22.0 and will be completely removed in versions 0.23.0 and later. The data table will be automatically synchronized and updated starting from version 0.22.0, with no manual intervention required.

## 2023-05-07

### V0.21.2

#### Fixes

- Sentinel monitoring dashboard.
- Gateway being injected a service mesh sidecar.
- Format of registry address for traditional microservices with service mesh enabled.
- Data service instance is not filtered according to the cluster when selecting the hosted registry.
- Incorrect registry statistics.

#### Enhancement

- Update the Gateway component to the latest community test version.

## 2023-04-26

### V0.21.1

#### Fixes

- Cloud native microservice pagination

#### Enhancement

- "disable Istio sidecar injection" for Nacos
- Insight version to official v0.16.0
- Retry mechanism of components accessing database
- Nacos port 9848 to GRPC to work with service mesh

## 2023-04-25

### V0.21.0

#### New Features

- Separate display of gateway access internal and external addresses
- API related to cloud native microservice governance capability
- Alert message list API
- API related to gateway using plugins
- Gateway logical API of various plugins

#### Fixes

- Envoy configuration is not updated when the gateway is updated
- Only a single port can be added to the gateway
- Insight problems of integrating JVM queries
- Cloud native microservice governance API
- Sentinel rule cannot be stored or pulled
- Some API calls cause the program to crash when the database is not connected
- Resource state API
- Cloud native microservice governance API time unit
- Domain format verification
- Some fields of plugins are named incorrectly

#### Enhancement

- Version of Insight integrated to 0.16.0
- Add a prefix to the module name for template end service
- Virtualhost crd
- Httpproxy crd
- Skoalaplugin crd

## 2023-04-21

### V0.20.0

#### New Features

- Sentinel portal version
- Gateway domain-level whitelist
- Native service governance list API
- Native service governance editing API
- Observable JVM monitoring integration
- Visualized status of the gateway resource workload
- Gateway workload policy selection

#### Fixes

- Contour image version
- User-defined role and API mappings
- API sort and entry in gateway overview page

#### Enhancement

- Plugins related API
- Configuration file structure
- Configuration parameter is implemented in the configuration package instead of being read directly
- Overall package structure of management components
- Management component
- Contour version to 1.24.3-ipfilter-tracing
- Envoy version to v1.25.4

## 2023-04-10

### V0.19.4

#### Fixes

- Startup issues of managed Nacos

## 2023-04-10

### V0.19.3

#### Fixes

- Front-end problems

## 2023-04-04

### V0.19.2

#### Fixes

- Nacos and Sentinel verify account by default
- Gateway API sorting in overview page

## 2023-04-04

### v0.19.1

#### Fixes

- CVE-2022-31045
- Plugin API
- Gateway restart
- Version cannot be updated when the plugin is updated
- Nacos and Sentinel verify account by default
- Gateway API sorting in overview page

## 2023-03-24

### v0.19.0

#### New Features

- Custom permissions and API implementation
- APIs related to registry overview
- APIs related to gateway whitelist
- APIs related to gateway health status in overview page
- Supported Nacos versions of 2.1.2
- API for obtaining Nacos and gateway version information
- Registry statistics collector in overview page
- Registry statistics API in overview page
- Cloud native microservice list API
- APIs related to importing cloud native microservices
- Custom resource design of plugins
- APIs related to plugin management
- API to intercept gateway front-end traffic
- Package of how cascade resource operation adding transaction
- Resource restart

#### Fixes

- Database script for initializing Nacos in Nacos Operator
- APIs related to overview Sentinel data
- APIs related to overview gateway data
- Gateway abnormal restart in gateway lifecycle management
- Capitalization of overview API path
- Nacos 2.1.2 cannot create cluster
- Traffic interception modification does not take effect
- Gateway whitelist API
- Nacos GRPC port name affect integrating Istio
- External mirror security scan in daily builds

#### Enhancement

- Streamline CI actions
- Use retry mechanism to update all resources
- Reconstruct gateway features

## 2023-02-25

### v0.18.0

#### New Features

- APIs to separate registries and configuration centers
- APIs related to overview

#### Fixes

- Image version of gateway-api
- IP pool loading issues of gateways under load balancer mode
- Health check issues

## 2023-02-22

### v0.17.1

#### New Features

- Gateway NodePort
- Gateway LoadBalancer
- Statistics API of Sentinel rules
- List API of services governed by Sentinel
- Cookie rewriting policy for gateway API
- Cronjobs in overview page
- Regular collection of abnormal Sentinel jobs
- API about Sentinel cluster flow control details
- Service options to be added into gateway
- Health check policy of gateway
- Health policies in the gateway API
- API related to Sentinel statistics
- CI process with offline chart
- Security scanning for external images in daily builds
- Automatic update of image version in the chart

#### Fixes

- Error in creating Nacos namespace
- Error in editing  Nacos persistent storage
- Resource verification of Nacos life cycle management
- Data display of gateway monitoring panel
- Ghippo link GRPC address missing
- Error of Sentinel cannot acquire cluster flow control API
- Status of managed Nacos resource is not updated
- Sentinel adaption to Nacos public strings
- Error of Sentinel resource collection API cannot aggregate instances
- Invalid Sentinel system rules
- Paging error of gateway service registries
- Error in creating service port
- Error in database initialization setup
- Use Helm commands instead of Argocd to deploy Alpha environment
- Base image CVE and upgrade to v3.17.2
- Error of chat update in release process

#### Enhancement

- Gateway-api version to v0.6.0
- Use client-go instead of clusterpedia to get to-be-updated resources
- Sentinel application monitoring template
- CI steps of building offline chart as independent
- Contour version to v1.24.1
- Envoy version to v1.25.1
- Use Chart to fix the namespace when installing skoala init

## 2022-12-30

### v0.16.1

#### Fixes

- Repetitive builder creation when building an image

#### Enhancement

- Details in Sentinel application monitor panel

## 2022-12-29

### v0.16.0

#### Fixes

- Error in Sentinel invoking Nacos interface with authentication enabled
- Error of nacos-operator frequently modifying service resources

#### Enhancement

- Add Grafana monitor panel for Sentinel service
- Insight to the latest version to support querying monitoring data by cluster name

## 2022-12-28

### v0.15.2

#### New Features

- Gateway API support for authentication servers
- API to integrate services in managed registries
- API about Sentinel cluster flow control

#### Fixes

- Sentinel rule concatenation error
- Error in Sentinel dashboard name
- Error in management component Chart when Service IPs are changed in production environment
- Error in Nacos controller logic
- Error in integrating egress with cluster management

#### Enhancement

- Error in dashboard of managed Nacos
- File obtain address for nacos-operator database initialization
- Sentinel image to v0.6.0

## 2022-12-22

### v0.14.0

#### New Features

- Offline images required by init Chart
- Token to get managed Nacos

#### Fixes

- Error in naming values in Skoala Chart
- Mirroring errors in CI flows

#### Enhancement

- Output logs to console by default
- Nacos-operator to the community version
- Enable for authentication of Nacos custom resources
- Log level of default components

## 2022-12-21

### v0.13.0

#### New Features

- Connectivity with APIs of MySQL and Redis components
- API to support gateway JWT verification
- Logic of gateway domain verification
- API of Sentinel resource listing
- API for gateway to query services in registries
- Push Init Chart to addon helm repo after release
- Complete gitlab release operations after version release
- Dynamically change log level

#### Fixes

- Global flow rules do not take effect after update
- Envoy log level was not set
- Error in updated gateways are not classified
- Error in database initialization of managed Nacos

#### Enhancement

- Registries are listed in descending order by update time
- Unified field name of gateway JWT
- Add "whether to enable JWT" field in gateway domain list
- Logic for Sentinel service name connector
- Upgrade Contour to version 1.23
- Upgrade Envoy to version 1.24
- Upgrade k8s.io/ related components to version 0.25
- Revert `go-replayers` component to community version
- Revert `go-helm-client` component to community version
- Upgrade Contour to version 1.23.1
- Modified Agent component as **Must** not inject sidecar
- Revert default configuration of Nacos image to community version
- Remove CI flows associated with Nacos image

## 2022-12-13

### v0.12.2

#### New Features

- Add Grafana template for Sentinel"s own monitoring
- Add configuration information of the customized gateway index

#### Fixes

- Status error of Insight after added into microservices
- Status error of Mesh plugin after enabled in managed registries
- Error in gateway log index
- Error in pre-dependency check interface
- Logical error of Sentinel matching Nacos default namespace
- Logic error in handling port connected to the container management module is wrong
