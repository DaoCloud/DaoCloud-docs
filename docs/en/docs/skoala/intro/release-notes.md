# Releases Notes

This page lists the release notes of DME to help you learn its feature development and bug fixing progress.

## 2023-04-26

### V0.21.1

#### Bug Fixes

- Cloud-native microservice pagination

#### Enhancement

- "disable Istio sidecar injection" for Nacos
- Insight version to official v0.16.0
- Retry mechanism of components accessing database
- Nacos port 9848 to GRPC to work with service mesh

## 2023-04-25

### V0.21.0

#### New Features

- Separate display of gateway access internal and external addresses
- API related to cloud-native microservice governance capability
- Alert message list API
- API related to gateway using plugins
- Gateway logical API of various plugins

#### Bug Fixes

- Envoy configuration is not updated when the gateway is updated
- Only a single port can be added to the gateway
- Insight problems of integrating JVM queries
- Cloud-native microservice governance API
- Sentinel rule cannot be stored or pulled
- Some API calls cause the program to crash when the database is not connected
- Resource state API
- Cloud-native microservice governance API time unit
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

#### Bug Fixes

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

#### Bug Fixes

- Startup issues of managed Nacos

## 2023-04-10

### V0.19.3

#### Bug Fixes

- Front-end problems

## 2023-04-04

### V0.19.2

#### Bug Fixes

- Nacos and Sentinel verify account by default
- Gateway API sorting in overview page

## 2023-04-04

### v0.19.1

#### Bug Fixes

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
- Cloud-native microservice list API
- APIs related to importing cloud-native microservices
- Custom resource design of plugins
- APIs related to plugin management
- API to intercept gateway front-end traffic
- Package of how cascade resource operation adding transaction
- Resource restart

#### Bug Fixes

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

#### Bug Fixes

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

#### Bug Fixes

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

#### Bug Fixes

- Repetitive builder creation when building an image

#### Enhancement

- Details in Sentinel application monitor panel

## 2022-12-29

### v0.16.0

#### Bug Fixes

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

#### Bug Fixes

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

#### Bug Fixes

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

#### Bug Fixes

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

#### Bug Fixes

- Status error of Insight after added into microservices
- Status error of Mesh plugin after enabled in managed registries
- Error in gateway log index
- Error in pre-dependency check interface
- Logical error of Sentinel matching Nacos default namespace
- Logic error in handling port connected to the container management module is wrong
