# Function overview

The "DaoCloud" microservice engine is a one-stop microservice management platform for the mainstream microservice ecosystem in the industry. It mainly provides two-dimensional functions of microservice governance center and microservice gateway, including service registration discovery, configuration management, and traffic management. , service-level link tracking, API management, domain name management, monitoring alarms, etc., covering various management scenarios in the microservice life cycle. The microservice engine has strong compatibility. It can not only seamlessly connect to other components of DCE 5.0, but also perfectly compatible with open source ecosystems such as Spring Cloud and Dubbo, helping you to use open source microservice technology to build your own microservice system more conveniently.

## Microservice Registration and Discovery

Unified management of traditional microservices and cloud-native microservices, realizing a smooth transition from traditional microservice ecology to cloud-native microservice ecology, and helping enterprises move towards cloud-native.

- Supports the creation of a Nacos hosting center to manage microservice namespaces, manage microservice traffic, manage microservice configuration, link tracking and monitoring, etc.
- Supports access to three types of traditional microservice registration centers: Eureka, Zookeeper, and Nacos.
- Supports access to two types of cloud-native microservice registries, Kubernetes and Service Mesh.

## Microservice Traffic Governance

In terms of traffic management, the online traffic management solution can be quickly integrated with mainstream open source microservice frameworks, and Sentinel and Mesh can be used to solve pain points in different production situations.

-Support the east-west traffic of traditional microservices governed by Sentinel using rules such as flow control, circuit breaker downgrade, hotspot, system, authorization, and cluster flow control.
- Supports managing microservice traffic in the grid through Service Mesh through virtual services, target rules, and gateway rules.

## Microservice Configuration Center

The Nacos hosting registry can be used as a configuration manager for microservices. It can extract common configurations from different projects for unified management in advance, and can also apply multiple different configurations to the same project to achieve differentiated management.

- Isolation of configuration files based on microservice namespace and grouping (Group).
- Dynamically update configuration items in combination with `@RefreshScope` annotation.
- Manage historical versions of configuration files, support version difference comparison and roll back to a specific version with one click.
- Support querying the currently configured listener and MD5 check value.
- Provide sample code, which is convenient for novices to quickly use client programming to consume the configuration, lowering the threshold for novices to use.

## Microservice Gateway

The microservice gateway is responsible for managing the north-south traffic control of microservices, providing API management, interface current limiting, multiple policy security authentication, black and white lists, routing and forwarding, MockAPI and other capabilities, while providing enterprise-level high-performance and highly scalable cloud services ability.

- Multi-gateway management: natively supports the management of multi-cluster and multi-namespace gateway instances in the [Container Management](../../kpanda/03ProductBrief/WhatisKPanda.md) module, and supports full life cycle management of gateway instances .
- API policy management: Add, delete, modify and query APIs through a graphical interface, and configure API policies, such as load balancing, path rewriting, timeout configuration, retry mechanism, request header/response header rewriting, WebSocket, local current limiting, health check etc. **At the same time, the ability of the native API is not affected**.
- Plug-in management: Provides a wealth of plug-in functions, supports plug-ins such as security, traffic control, and cache, and supports one-click enabling/disabling of plug-ins.
- Monitoring and alarming: The microservice gateway will automatically configure monitoring, alarming and other functions when deployed. Each gateway comes with complete resource monitoring and gateway business monitoring.