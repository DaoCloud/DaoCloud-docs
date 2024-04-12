# Microservice Engine (Skoala) Releases Notes

This page lists the release notes of Microservices to help you learn its feature development and bug fixing progress.

## 2024-04-11

### v0.35.2

#### Fixes

- **Fixed** the issue of inaccurate permissions in the microservice engine module in the global management
- **Fixed** abnormal saving of global rate limiting in the gateway
- **Fixed** abnormal memory configuration when creating a gateway
- **Fixed** abnormal maximum heap memory configuration at runtime in the gateway
- **Fixed** abnormal time display in relation to Eureka in the registration center
- **Fixed** abnormal creation of Seata with custom password in Nacos
- **Fixed** database initialization exception in Seata

!!! note

    Important: In version 0.35.x, Gateway API related custom resources (CRD) have been updated. Since the chart update does not automatically apply CRD changes,
    please manually apply the CRD: skoala-init/charts/contour-provisioner-prereq/crds/gateway-api.yaml

## 2024-04-03

### v0.35.1

#### Fixes

- **Fixed** error when creating a domain in the gateway
- **Fixed** mismatch in managed Nacos resource checks
- **Fixed** abnormal API status after enabling health check port for domain in the gateway and adding health check configuration in API
- **Fixed** incorrect API statistics overview in the gateway
- **Fixed** abnormal registration center status
- **Fixed** abnormal resource annotations when creating traffic lanes
- **Fixed** gateway custom plugin functionality issues

!!! note

    Important: In version 0.35.x, Gateway API related custom resources (CRD) have been updated. Since the chart update does not automatically apply CRD changes,
    please manually apply the CRD: skoala-init/charts/contour-provisioner-prereq/crds/gateway-api.yaml

## 2024-03-23

### v0.35.0

#### New Features

- **Added** ability for cloud-native gateway API to match routes based on request parameters
- **Added** ability for distributed transaction Seata to use custom passwords
- **Added** time filtering capability for Grafana panels in distributed transactions
- **Added** ability to filter cloud-native microservice traffic lanes by namespace

#### Fixes

- **Fixed** issues related to registration center types
- **Fixed** inaccurate prompt when gateway instance count is zero
- **Fixed** logic related to cloud-native microservices
- **Fixed** issue of traffic lanes list not refreshing on initial load
- **Fixed** incorrect display of Sentinel password
- **Fixed** NullPointerException when creating new API with Envoy as xdsServer
- **Fixed** pagination issue when mesh instance has no services
- **Fixed** issues resulting from changes in the service mesh module API

#### Improvements

- **Improved** compatibility with distributed transaction Seata 2.0
- **Improved** default version to Nacos 2.3.0 for managed registration center
- **Improved** gateway API statistics chart algorithm to incremental statistics mode

## 2024-03-06

### v0.33.4

#### Fixes

- **Fixed** logic related to native microservices
- **Fixed** issue where traffic swim lane list does not refresh on initial load
- **Fixed** incorrect display of Sentinel password
- **Fixed** integration issues caused by changes in grid module API

## 2024-03-01

### v0.33.3

#### Fixes

- **Fixed** logic related to cloud-native microservices
- **Fixed** issues caused by changes in grid module API

## 2024-02-02

### v0.34.0

#### New Features

- **Added** namespace information deployed by the gateway in gateway query port based on application workspace requirements

#### Improvements

- **Improved** total number of gateway log pagination queries, limited to a maximum display of 10000 list log data
- **Improved** error prompts for gateway log queries

## 2024-02-01

### v0.33.2

#### Fixes

- **Fixed** an issue with abnormal restart of gateway service component
- **Fixed** an issue with abnormal export of gateway logs
- **Fixed** an issue with incorrect display of status when the replica count of gateway workload is 0
- **Fixed** an issue with gateway control plane not restarting application configuration when injecting sidecars to gateway
- **Fixed** an issue with inconsistency between returned sidecar injection status and actual status in gateway list

#### Improvements

- **Improved** the latest SDK in the mesh module to fix logic related to cloud-native microservices interfaces

## 2024-01-30

### v0.33.1

#### Fixes

- **Fixed** a logic related to cascading deletion in Nacos

## 2024-01-18

### v0.32.0

#### New Features

- **Added** cloud native microservice monitoring resources
- **Added** support for connecting to a registry center with authentication mode enabled
- **Added** ARM architecture offline installation package release process

#### Fixes

- **Fixed** an issuein updating plugin references when updating domain names
- **Fixed** an issue with incorrect service port in service list query
- **Fixed** an issue with incorrect display of log protocol fields
- **Fixed** an issue with unsorted results in service list API of traffic lanes
- **Fixed** an issue with incorrect number of instances in service list of traffic lanes
- **Fixed** an issue in refreshing namespace when cloud native gateway is already created
- **Fixed** an issue with mismatched instance status in connected Kubernetes clusters
- **Fixed** an issue with incorrect instance list results in connected meshes
- **Fixed** an issue with incorrect stop address for NodePort services in gateway
- **Fixed** an issue with abnormal display of Nacos services in non-default groups in registry center

#### Improvements

- **Improved** Routing weight optimization to meet application workspace requirements
- **Improved** Weight validation logic for services in gateway API
- **Improved** Handling of resource initial operations caused by changes in cluster access addresses

## 2024-01-03

### v0.31.2

#### Fixes

- **Fixed** an issue of missing protocol field display in the gateway API
- **Fixed** an issue of abnormal managed resources due to address changes after cluster reconnection
- **Fixed** an issue of incorrect statistics for abnormal gateway access
- **Fixed** an issue of NodePort ports being set to 0 for cluster services
- **Fixed** an issue of inaccurate status prompts for automatic population of cluster services and mesh services
- **Fixed** an issue of installation failure for Init Chart when the insight-system namespace does not exist

## 2023-12-26

### v0.31.1

#### Fixes

- **Fixed** an issue of missing log files for gateway management components

## 2023-12-26

### v0.31.0

#### New Features

- **Added** support for managed Nacos version 2.3.0
- **Added** support for service and API gateway services as traffic entry points
- **Added** outlier instance detection
- **Added** details for traffic swimlane topology (traffic direction, versions, etc.)
- **Added** advanced configuration for heap memory in gateway runtime

#### Fixes

- **Fixed** an issue of missing connection addresses in gateway service lists and service details
- **Fixed** an issue of missing labels after updating gateway APIs
- **Fixed** an issue of duplicate gateway API routing rules
- **Fixed** an issue of empty value for maximum heap memory in gateway runtime
- **Fixed** an issue of service integration when managing Nacos and mesh services
- **Fixed** an issue of incorrect Istio sidecar annotations injection in the gateway
- **Fixed** an issue of abnormal Nacos service query in the gateway
- **Fixed** an issue of inability to create drainage rules due to long service names in traffic swimlanes
- **Fixed** an issue of abnormal service port update in the gateway
- **Fixed** an issue of abnormal resource quota calculation when creating managed resources
- **Fixed** a logical issue in filtering gateway API lists based on domain names
- **Fixed** an issue of duplicate ports in cloud native microservice governance
- **Fixed** an issue of repeated judgment and duplicate conditions when multiple routes exist for an API
- **Fixed** an issue of abnormal error in API testing for HTTPS domain names
- **Fixed** an issue of abnormality when deleting Sentinel functionality
- **Fixed** an issue of component restart when exporting logs with empty gateway logs
- **Fixed** an issue of empty console address in the response of managed Nacos resource information API
- **Fixed** an issue of failed Seata plugin activation when the managed Nacos name has the suffix `-seata`
- **Fixed** an issue of MySQL viewing permissions in managed Nacos middleware management
- **Fixed** an issue of labels in gateway interface v1alpha2 version

#### Improvements

- **Improved** Skoala Agent component and added logging functionality
- **Improved** the gateway control plane (Contour) to v1.27.0 private branch version
- **Improved** the gateway runtime (Envoy) to v1.28.0 official version
- **Improved** the gateway dependency on Gateway API custom resources to v1.0 official version
- **Improved** the gateway log query index (compatible with previous versions)

## 2023-12-11

### v0.30.2

#### Fixes

- **Fixed** an issue of multiple duplicate route records in the gateway API

## 2023-12-01

### v0.30.0

#### Fixes

- **Fixed** an issue with incorrect running status of gateway
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

- **Fixed** logic for mesh instance list in mesh mode governance
- **Fixed** synchronization issues with managed Nacos controllers

#### Improvements

- **Improved** gateway service list API and added access address display feature
- **Improved** logic for synchronizing API updates after modifying services
- **Improved** loading speed of gateway resource list
- **Improved** configuration details for gateway timeout settings

### 2023-11-07

#### v0.28.1

##### Fixes

- **Fixed** sorting issue in the gateway service list
- **Fixed** multiple line break issue when importing gateway APIs
- **Fixed** the problem where Seata Operator image does not support offline repository
- **Fixed** the issue with abnormal offline release process

## 2023-10-26

### v0.28.0

#### New Features

- **Added** support for regular expression and exact match for gateway API request headers.
- **Added** support for bulk import and export of gateway APIs.
- **Added** support for managing multiple versions of Nacos (currently supports versions 2.0.4, 2.1.1, and 2.2.3).
- **Added** support for complex password requirements in Sentinel console.
- **Added** support for targeted gray release of Nacos configuration files.
- **Added** support for distributed transactions (including TCC mode, FMT mode, SAGA mode, XA mode).
- **Added** support for importing interfaces using Swagger standard through visual form interface.

#### Fixes

- **Fixed** an issue of supporting different versions of managed Nacos.
- **Fixed** an issue of duplicate request methods in the gateway interface list.
- **Fixed** the problem of Zookeeper registry not being able to connect to instances with TLS protocol.
- **Fixed** an issue of domain deletion and update failure after enabling global authentication in the gateway.
- **Fixed** an issue of incorrect CPU usage at the namespace level in managed Nacos.
- **Fixed** an issue of abnormal service change when switching from NodePod mode to ClusterIP mode in managed Nacos.
- **Fixed** an issue of abnormal Seata interface verification.
- **Fixed** an issue of abnormal workspace access when switching registry center.
- **Fixed** the permission issue with related interfaces of managed Nacos.
- **Fixed** the issue with Grafana monitoring panel for managed Nacos.
- **Fixed** the issue with Sentinel Grafana monitoring panel.
- **Fixed** the accuracy issue with overall permissions.

#### Improvements

- **Improved** the update logic of the gateway, which does not allow disabling HTTPS at the gateway level when the domain has enabled HTTPS.
- **Improved** the accuracy of audit log events.
- **Improved** Optimized the logic of cloud native microservice WebAssembly plugins.
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

- **Fixed** an issue of duplicate details in batch deletion response
- **Fixed** Problem with sorting plugin information in cloud native microservices port list
- **Fixed** an issue with abnormal display of traffic swimlane list
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

### v0.27.0

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
- **Fixed** an issuein service instance list in managed Nacos
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

- **Fixed** an issue with detection of `Consul` registry connectivity
- **Fixed** an issue with gateway restarting due to abnormal application of plugins
- **Fixed** an issue with abnormal configuration of gateway verification plugins
- **Fixed** an issue with abnormal editing of cluster flow control rules in `Sentinel`

!!! note "Important Note"

    Starting from Microservice Engine version `v0.24.2`, there is an incompatible update for versions `v0.24.2` and earlier. This is because the gateway involves a change in the address of the open-source component repository. Therefore, before updating, you need to manually delete the existing `gateway-api-admission-xxxxx` Job and then proceed with the normal upgrade process.

## 2023-07-26

### v0.26.1

#### Fixes

- **Fixed** an issue of incorrect version of the Agent component.

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

- **Fixed** an issue of Nacos port not being updated.
- **Fixed** an issue of cluster flow control rules in Sentinel not being saved.
- **Fixed** an issue of API exception when deleting non-empty services in Nacos.
- **Fixed** an issue of duplicate data in gateway monitoring data.
- **Fixed** the issue with the use of plugins in cloud native microservices related APIs.
- **Fixed** the issues with gateway domain naming rules.
- **Fixed** an issue of incorrect version in cloud native microservice traffic lanes.

#### Improvements

- **Improved** the driver name of the People's Congress Golden Warehouse database from "kb_v8r6" to "kingbase".

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

- **Fixed** an issue of incorrect external image scanning address in the pipeline.
- **Fixed** an issue of missing directory-level dependency for permissions associated with middleware.

#### Improvements

- **Improved** the chain validation of gateway and related resource changes.
- **Improved** the gateway listening port from cluster IP to container port.

## 2023-07-06

### v0.24.2

#### Fixes

- **Fixed** page experience optimization and bug fixes.

## 2023-07-05

### v0.24.1

#### Fixes

- **Fixed** an issue of outdated versions in Skoala-init Chart form
- **Fixed** page experience improvements and issues

## 2023-06-30

### v0.24.0

#### New Features

- **Added** API for cloud native microservices plugins
- **Added** cascading selection capability for permissions associated with middleware operations

#### Fixes

- **Fixed** data exception in Insight integration
- **Fixed** abnormal filtering results for gateway status

#### Improvements

- **Improved** chain validation for gateway and related resource changes

## 2023-06-26

### v0.23.0

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
- **Fixed** an issue where gateway can enable HTTPS even if it is disabled
- **Fixed** default value issue in Skoala-init Chart form data

#### Improvements

- **Improved** user experience and issues with Sentinel Grafana
- **Improved** display of relevant resource alerts in managed resource alarms
- **Refactored** configuration structure of global management module
- **Improved** reading of managed Nacos information through Clusterpedia
- **Upgraded** Insight integration to version 0.17.3
- **Improved** flexibility of database-related configuration

## 2023-05-31

### v0.22.2

#### Fixes

- **Fixed** an issues with Sentinel cluster flow control API
- **Fixed** an issues with fuzzy query API for Sentinel rules

#### Improvements

- **Improved** default values for connecting to the database to increase fault tolerance

## 2023-05-29

### v0.22.1

#### Fixes

- Positions of plugin CRDs are not correc.
- Issue related to OpenAPI publishing process.

#### Improvements

- Set default values for database of Hive component.

## 2023-05-26

### v0.22.0

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

#### Improvements

- Sentinel monitoring panel structure and data logic.
- Remove virtualhost CR from Gateway domain management.
- Sentinel cluster flow control API logic.
- Upgrade Ghippo to 0.17.0-rc2.
- Database initialization component "sweet has been deprecated since version 0.22.0 and will be completely removed in versions 0.23.0 and later. The data table will be automatically synchronized and updated starting from version 0.22.0, with no manual intervention required.

## 2023-05-07

### v0.21.2

#### Fixes

- Sentinel monitoring dashboard.
- Gateway being injected a service mesh sidecar.
- Format of registry address for traditional microservices with service mesh enabled.
- Data service instance is not filtered according to the cluster when selecting the hosted registry.
- Incorrect registry statistics.

#### Improvements

- Update the Gateway component to the latest community test version.

## 2023-04-26

### v0.21.1

#### Fixes

- Cloud native microservice pagination

#### Improvements

- "disable Istio sidecar injection" for Nacos
- Insight version to official v0.16.0
- Retry mechanism of components accessing database
- Nacos port 9848 to GRPC to work with service mesh

## 2023-04-25

### v0.21.0

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

#### Improvements

- Version of Insight integrated to 0.16.0
- Add a prefix to the module name for template end service
- Virtualhost crd
- Httpproxy crd
- Skoala plugin crd

## 2023-04-21

### v0.20.0

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

#### Improvements

- Plugins related API
- Configuration file structure
- Configuration parameter is implemented in the configuration package instead of being read directly
- Overall package structure of management components
- Management component
- Contour version to 1.24.3-ipfilter-tracing
- Envoy version to v1.25.4

## 2023-04-10

### v0.19.4

#### Fixes

- Startup issues of managed Nacos

## 2023-04-10

### v0.19.3

#### Fixes

- Front-end problems

## 2023-04-04

### v0.19.2

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

#### Improvements

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
- Error in editing Nacos persistent storage
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

#### Improvements

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

#### Improvements

- Details in Sentinel application monitor panel

## 2022-12-29

### v0.16.0

#### Fixes

- Error in Sentinel invoking Nacos interface with authentication enabled
- Error of nacos-operator frequently modifying service resources

#### Improvements

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

#### Improvements

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

#### Improvements

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

#### Improvements

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

*[Skoala]: The development name for the microservices in DaoCloud
