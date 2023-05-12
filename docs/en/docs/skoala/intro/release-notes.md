# The microservice engine releases Notes

This page lists the Release Notes of the microservice engine so that you can understand the evolution path and feature changes of each version.

# 2023-04-25

## V0.21.0

### New function

- ** add ** Separate display of gateway access internal and external addresses
- ** add ** API related to cloud native micro-service governance capability
- ** add ** Alarm message list API
- ** add ** The gateway uses plug-in related apis
- ** add ** Gateway logical API of various plug-ins

### repair

- ** repair ** Problem that Envoy configuration is not updated when the gateway is updated
- ** repair ** Only a single port can be added to the gateway
- ** repair ** Insight problems integrating JVM queries
- ** repair ** The problem of cloud native micro-service governance API
- ** repair ** The Sentinel rule cannot be accessed
- ** repair ** Some API calls cause the program to crash when the database is not connected
- ** repair ** Problem with resource state API
- ** repair ** Cloud native micro service governance API time unit problem
- ** repair ** Domain name format verification problem
- ** repair ** Plugin issues with some fields being named incorrectly

### optimization

- ** optimization ** Insight integrated to 0.16.0
- ** optimization ** Deployment template end front-end service name Add a prefix to the module name

# 2023-04-21

## V0.20.0

### repair

- ** repair ** Contour Image version
- ** repair ** User-defined role function points and API mappings
- ** repair ** Gateway Overview API sort and entry

### New function

- ** add ** Sentinel portal version
- ** add ** Gateway domain name level whitelist Supported
- ** add ** Native service governance list API
- ** add ** Native service governance editing API
- ** add ** Observable JVM monitoring integration
- ** add ** Displays the status of the gateway resource workload
- ** add ** Select the gateway load policy

### optimization

- ** optimization ** plug-in center related API
- ** optimization ** Configuration file structure
- ** optimization ** The configuration parameter is implemented in the configuration package instead of being read directly
- ** optimization ** Manage the overall package structure of components
- ** optimization ** Management component
- ** optimization ** Contour upgraded to v1.24.3-ipfilter-tracing
- ** optimization ** Envoy upgraded to v1.25.4

# 2023-04-10

## V0.19.4

### repair

- ** repair ** Startup problems with managed Nacos

# 2023-04-10

## V0.19.3

### repair

- ** repair ** Front-end problem

# 2023-04-04

## V0.19.2

### repair

- ** repair ** Nacos and Sentinel verify account problem by default
- ** repair ** Overview of gateway API sorting problems

## 2023-04-04

### v0.19.1

#### repair

- ** repair ** CVE-2022-31045 vulnerability
- ** repair ** Plug-in center API problem
- ** repair ** The gateway is restarted
- ** repair ** The version cannot be successfully updated when the plugin is updated
- ** repair ** Nacos and Sentinel verify account by default
- ** repair ** Overview of the gateway API sorting problem of the micro service gateway

## 2023-03-24

### v0.19.0

#### New function

- ** add ** Custom permission points and API implementation
- ** add ** Registry Overview related apis
- ** add ** API related to gateway whitelist
- ** add ** API related to gateway health in Overview
- ** add ** Nacos supports versions up to 2.1.2
- ** add ** API for obtaining Nacos and gateway version information
- ** add ** Register the Configuration Center statistics collector in Overview
- ** add ** Register the Configuration center statistics API in Overview
- ** add ** Cloud native micro service service list API
- ** add ** Cloud native micro-service service import related apis
- ** add ** Plug-in Center custom resource design
- ** add ** Plug-in center plug-in management related apis
- ** add ** Gateway front-end traffic interception configuration API
- ** add ** Cascade resource operation adds transaction (similar) mechanism processing package
- ** add ** Resource restart function

#### repair

- ** repair ** Database script problem for initializing Nacos in Nacos Operator
- ** repair ** Sentinel related data overview API problems
- ** repair ** Overview API problems with gateway related data
- ** repair ** Gateway lifecycle management reduces the abnormal restart of the gateway
- ** repair ** Overview API path capitalization
- ** repair ** Nacos 2.1.2 Cluster Creation failure
- ** repair ** The traffic interception modification does not take effect
- ** repair ** Gateway whitelist API problem
- ** repair ** Nacos GRPC port name Problems in integrating Istio
- ** repair ** External mirror security scan in daily builds

#### optimization

- ** optimization ** CI flow and simplify unnecessary tasks
- ** optimization ** All resources are updated using the retry mechanism
- ** optimization ** Reconstruct functions related to the gateway

## 2023-02-25

### v0.18.0

#### New function

- ** add ** Add registry configure hub separation API
- ** add ** Add overview related logic and API

#### repair

- ** repair ** The gateway-api image version is incorrect
- ** repair ** Load balancing mode The IP address pool loading of the gateway fails
- ** repair ** Health check related problems

## 2023-02-22

### v0.17.1

#### New function

** add ** Gateway NodePort Support

- ** add ** Gateway LoadBalancer
- ** add ** Sentinel rule statistics API
- ** add ** Service list API governed by Sentinel
- ** add ** Cookie rewriting policy for gateway API
- ** add ** Overview data scheduling tasks
- ** add ** Regular collection of exception Sentinel tasks
- ** add ** Sentinel cluster flow control detail API
- ** add ** Gateway Access Service list port selection
- ** add ** Gateway service health check policy
- ** add ** Support for health policies in the gateway API
- ** add ** Sentinel statistics related API
- ** add ** Support chart offline CI process
- ** add ** Added security scanning capability for external images in daily builds
- ** add ** Publish an automatic update of the mirrored version in the chart

#### repair

- ** repair ** Nacos Namespace creation exception
- ** repair ** Nacos persistent storage modification exception
- ** repair ** Nacos life cycle management resource verification problem
- ** repair ** Gateway monitoring panel data display problem
- ** repair ** Ghippo link GRPC address missing problem
- ** repair ** Sentinel acquiring cluster flow control API problems
- ** repair ** The status of the managed Nacos resource is not updated
- ** repair ** Sentinel ADAPTS to Nacos public string problems
- ** repair ** Sentinel does not have problems aggregating different instances of the resource API
- ** repair ** Sentinel system rule invalid problem
- ** repair ** Gateway service Registry type paging error
- ** repair ** Incorrect service port creation
- ** repair ** Database initialization setup problem
- ** repair ** Use the Helm command instead of Argocd to deploy the Alpha environment
- ** repair ** Base image CVE problem and upgrade to 3.17.2
- ** repair ** Issue process Chart update problem

#### optimization

- ** optimization ** Upgrade gateway-api to v0.6.0
- ** optimization ** Resource to be updated gets client-go instead of clusterpedia
- ** optimization ** Sentinel application monitoring template
- ** optimization ** makes the off-line chart build CI step independent
- ** optimization ** Contour upgraded to v1.24.1
- ** optimization ** envoy upgraded to v1.25.1
- ** optimization ** Fixed namespace when Skoala Init is installed with Chart capability

## 2022-12-30

### v0.16.1

#### repair

- ** repair ** Problem of repeatedly creating the builder when building an image

#### optimization

- ** optimization ** Sentinel application monitor panel details

## 2022-12-29

### v0.16.0

#### repair

- ** repair ** Sentinel invoke problem of opening Nacos interface with authentication
- ** repair ** nacos-operator Frequently modifies service resources

#### optimization

- ** optimization ** Adds the Grafana monitor panel for the Sentinel service
- ** optimization ** Upgrading Insight to the latest version supports querying monitoring data by cluster name

## 2022-12-28

### v0.15.2

#### New function

- ** add ** Gateway API support for authentication servers
- ** add ** Managed registry service access API
- ** add ** Sentinel cluster flow control API

#### repair

- ** repair ** Sentinel rule concatenation error
- ** repair ** Sentinel dashboard name problem
- ** repair ** Management component Chart for the Service IP problem of the production change environment
- ** repair ** Problem of Nacos controller processing logic
- ** repair ** The address of the egress integrated with cluster management is faulty

#### optimization

- ** optimization ** Managed Nacos monitors dashboard problems
- ** optimization ** nacos-operator database initialization file obtain address
- ** optimization ** Update the Sentinel image to v0.6.0

## 2022-12-22

### v0.14.0

#### New function

- ** add ** Init Chart requires offline support for images
- ** add ** Gets a token to host Nacos

#### repair

- ** repair ** Naming of Values in Skoala Chart
- ** repair ** Mirroring problem in CI flow

#### optimization

- ** optimization ** Sets the default log output to the console
- ** optimization ** Upgrade nacos-operator to the community version
- ** optimization ** Updated enable support for authentication of Nacos custom resources
- ** optimization ** Set the default component log level

## 2022-12-21

### v0.13.0

#### New function

- ** add ** Connect to apis of the middleware MySQL and Redis
- ** add ** Gateway JWT verifies supported apis
- ** add ** Gateway domain name verification logic
- ** add ** Sentinel resource listing API
- ** add ** Gateway interface for querying registry services
- ** add ** Push Init Chart to addon registry after release
- ** add ** Complete the gitlab release operation when the version is released
- ** add ** Dynamically change the log level

#### repair

- ** repair ** All restricted flow rules do not take effect when updated
- ** repair ** Envoy Log Level No problem set
- ** repair ** An error occurred when the gateway was updated
- ** repair ** Database initialization problem of managed Nacos

#### optimization

- ** optimization ** The registry is listed in descending order by update time
- ** optimization ** Field name of unified gateway JWT
- ** optimization ** Added whether to enable the JWT field in the gateway domain name list
- ** optimization ** Logic for the Sentinel service name connector
- ** optimization ** Upgrade Contour to version 1.23
- ** optimization ** Upgrade Envoy to version 1.24
- ** optimization ** Upgrade k8s.io/ related components to version 0.25
- ** optimization ** Return the go-replayers component to the community version
- ** optimization ** Revert the go-helm-client component to the community version
- ** optimization ** Upgrade Contour to version 1.23.1
- ** optimization ** Modified Agent component to force no mesh sidecar injection
- ** optimization ** Revert the default configuration of the Nacos image to the community version
- ** optimization ** Remove CI flow associated with Nacos image

## 2022-12-13

### v0.12.2

#### New function

- ** add ** Adds Grafana template support for Sentinel"s own monitoring
- ** add ** Add the configuration information of the customized gateway index

#### repair

- ** repair ** State problem of microservice integration observable components
- ** repair ** Governance status issue of registry"s ability to enable mesh plug-ins
- ** repair ** Gateway log index problem
- ** repair ** Pre-dependency check interface problems
- ** repair ** Logical problem of Sentinel matching Nacos default namespace
- ** repair ** Logic of the abnormal port connected to the container management module
