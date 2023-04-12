# Microservice Engine Release Notes

This page lists the Release Notes of the microservice engine, so that you can understand the evolution path and feature changes of each version.

## 2023-04-04

### v0.19.1

#### fix

- **FIXED** CVE-2022-31045 vulnerability
- **Fix** plugin center API issue
- **FIX** Gateway restart issue
- **Fix** The problem that the version cannot be successfully updated when the plugin is updated
- **Fix** Nacos and Sentinel default authentication account problem
- **Fixed** microservice gateway gateway API ordering issue in overview

## 2023-03-24

### v0.19.0

#### Features

- **Add** custom permission point and API implementation
- **NEW** Added API related to registry overview
- **NEW** API related to gateway blacklist and whitelist
- **NEW** API related to gateway health in the overview
- **Add** Nacos support version to 2.1.2
- **New** API to get Nacos and gateway version information
- **NEW** Register configuration center statistics collector in the overview
- **NEW** Register configuration center statistics API in the overview
- **Add** cloud native microservice service list API
- **Add** cloud native microservice service import related API
- **NEW** Custom resource design in plugin center
- **NEW** Added APIs related to plug-in management in plug-in center
- **NEW** Added gateway front-end traffic interception configuration API
- **NEW** Cascading resource operations add transaction (similar) mechanism processing package
- **Add** resource restart function

#### fix

- **Fix** Nacos Operator's database script problem of initializing Nacos
- **FIXED** issues with Sentinel related data overview API
- **FIXED** issues with overview API for gateway related data
- **Fix** Gateway life cycle management reduces abnormal restart of the gateway
- **FIX** Overview API path case problem
- **Fix** Nacos 2.1.2 cannot create a cluster
- **Fix** the problem that the modification of gateway pre-traffic interception does not take effect
- **Fix** gateway blacklist API issue
- **Fix** Nacos GRPC port name for integration with Istio
- **FIX** external mirror security scan in daily build

#### Optimization

- **Optimize** CI process and simplify unnecessary tasks
- **Optimization** The update operation of all resources adopts the retry mechanism
- **Optimization** Refactoring of gateway-related functions

## 2023-02-25

### v0.18.0

#### Features

- **NEW** Add registration center configuration center separation API
- **NEW** Add overview related logic and API

#### fix

- **Fix** gateway-api image version issue
- **Fix** IP pool loading issue for gateway in load balancing mode
- **Fix** health check related issues

## 2023-02-22

### v0.17.1

#### Features

**NEW** Gateway NodePort support

- **Added** Gateway LoadBalancer support
- **Add** Sentinel rule statistics API
- **NEW** Added service list API for Sentinel governance
- **NEW** Cookie rewrite strategy for Gateway API
- **Add** overview data timing task
- **Add** Timed collection of abnormal Sentinel tasks
- **Add** Sentinel cluster flow control details API
- **Add** Gateway access service list port selection
- **Add** Gateway Service Health Check Policy
- **NEW** Support for Health Policies in Gateway API
- **Add** Sentinel statistics related API
- **Add** CI process that supports chart offline
- **NEW** Added external image security scanning capability in daily build
- **NEW** Release auto-update mirror version in chart

#### fix

- **Fix** Nacos Namespace creation exception
- **Fix** Nacos persistent storage modification exception issue
- **Fix** Nacos life cycle management resource verification problem
- **Fix** data display problem on gateway monitoring panel
- **Fix** Ghippo link GRPC address missing issue
- **Fix** Sentinel access cluster flow control API problem
- **Fix** The problem that the status of managed Nacos resources is not updated
- **Fix** Sentinel adapts Nacos public string problem
- **Fix** Sentinel get resource API does not aggregate different instances
- **Fix** Sentinel system rules not taking effect
- **Fix** the problem of pagination error of gateway service registration center type
- **Fix** Create service port error
- **Fix** database initialization problem
- **FIX** Use Helm command instead of Argocd to deploy Alpha environment
- **Fix** base image CVE issue and upgrade to 3.17.2
- **FIXED** Chart update issue in release process

#### Optimization

- **Optimize** upgrade gateway-api to v0.6.0
- **Optimization** Resource acquisition to be updated is changed from clusterpedia to client-go
- **Optimized** Sentinel application monitoring template
- **Optimize** make offline chart build CI step independent
- **Optimized** Contour upgrade to v1.24.1
- **optimized** envoy upgrade to v1.25.1
- **Optimize** Use the Chart ability to make Skoala Init fix the namespace when installing

## 2022-12-30

### v0.16.1

#### fix

- **Fix** the problem of repeatedly creating builder when building the image

#### Optimization

- **Optimized** Sentinel application monitoring panel details

## 2022-12-29

### v0.16.0

#### fix

- **Fix** Sentinel call has authentication to open the Nacos interface problem
- **Fix** the problem that nacos-operator frequently modifies service resources

#### Optimization

- **Optimized** Add Sentinel service Grafana monitoring panel
- **Optimization** Upgrade Insight to the latest version to support querying monitoring data by cluster name

## 2022-12-28

### v0.15.2

#### Features

- **NEW** Gateway API support for authentication server
- **NEW** Added hosting registry service access API
- **New** Sentinel cluster flow control related API

#### fix

- **Fix** Sentinel rule stitching error
- **FIXED** Sentinel Dashboard name issue
- **Fix** the Service IP problem of the management component Chart for the production environment
- **Fix** Nacos controller processing logic problem
- **Fix** egress address issue integrated with cluster management

#### Optimization

- **Optimize** Managed Nacos monitoring dashboard issues
- **Optimize** Nacos-operator database initialization file acquisition address
- **Optimized** Update Sentinel image to v0.6.0

## 2022-12-22

### v0.14.0

#### Features

- **NEW** Added offline support for images required by Init Chart
- **NEW** Get token for hosting Nacos

#### fix

- **Fix** Values naming problem in Skoala Chart
- **Fix** mirroring issue in CI process

#### Optimization

- **Optimization** Set the default log output to the console
- **Optimize** Upgrade nacos-operator to community version
- **Optimization** Update the authentication enablement support for Nacos custom resources
- **Optimize** Set the default component log level

## 2022-12-21

### v0.13.0

#### Features

- **Add** related APIs for docking middleware MySQL and Redis
- **NEW** API supported by gateway JWT verification
- **Add** gateway domain name verification logic
- **New** Sentinel resource list API
- **New** interface for gateway query registry service
- **NEW** Push Init Chart to addon repository after release
- **New** Complete gitlab release operation when the version is released
- **NEW** Dynamically change the log level

#### fix

- **Fix** the problem that the global current limiting rule does not take effect when updating
- **Fix** Envoy Log Level not set issue
- **Fix** The problem that the exception is not judged when updating the gateway
- **Fix** database initialization problem of managed Nacos

#### Optimization

- **Optimized** The registry list is sorted in descending order by update time
- **Optimize** Unified Gateway JWT related field names
- **Optimize** The gateway domain name list adds whether to enable JWT field
- **Optimize** the logic of Sentinel service name connector
- **Optimization** Upgrade Contour to version 1.23
- **Optimization** Upgrade Envoy to version 1.24
- **Optimize** Upgrade k8s.io/related components to version 0.25
- **Optimize** Return go-replayers component to community version
- **Optimize** Return go-helm-client component to community version
- **Optimized** Upgrade Contour to version 1.23.1
- **Optimization** Modify the Agent component to force no mesh sidecar injection
- **Optimize** Return the default configuration of the Nacos image to the community version
- **Optimize** remove Nacos image related CI process

## 2022-12-13

### v0.12.2

#### Features

- **NEW** Add support for Grafana templates monitored by Sentinel itself
- **NEW** Add configuration information for custom configuration gateway index

#### fix

- **Fix** Microservice integration observable component status issue
- **FIXED** Governance status issue of registry center enabling mesh plug-in capability
- **FIX** gateway log index issue
- **Fix** the problem of pre-dependency checking interface
- **Fix** Sentinel logic problem matching with Nacos default namespace
- **Fix** the logic of the abnormal situation of the port connected to the container management module
