---
hide:
  - navigation
MTPE: windsonsea
date: 2024-01-05
---

# RocketMQ Message Queue Release Notes

This page provides the Release Notes for RocketMQ Message Queue, allowing you to understand the evolution and feature changes of each version.

## 2025-02-28  

### v0.14.0  

- **Added** support for configuring static IPs for `RocketMQ` instances.  
- **Updated** support for configuring time zone environment variables.  
- **Updated** the operator image version.  
- **Fixed** an issue with console connection errors after the nameserver restart.

## 2024-09-30

### v0.11.0

- **Fixed** an issue where the container group list did not display all related container groups in the instance
- **Fixed** an issue with permission leakage when querying the Redis list by selecting a workspace
- **Fixed** an issue with missing audit logs for certain operations

## 2024-08-31

### v0.10.0

- **Improved** the process so that abnormal clusters cannot be selected when creating instances

## 2024-04-30

### v0.6.0

- **Improved** JVM parameters for starting Broker nodes
- **Added** a prompt for namespace quota

## 2024-03-31

### v0.18.0

- **Improved** support for Chinese monitoring dashboard in Chinese mode

## 2024-01-31

### v0.4.0

- **Improved** RocketMQ version display in global management.

## 2023-12-31

### v0.3.0

- **Fixed** compatibility issue between exporter and RocketMQ version
- **Fixed** an issue where validation for input fields with special characters was not effective when creating an instance

## 2023-11-30

### v0.1.3

- **Added** support for recording operation audit logs
- **Improved** prompt when instance list information is not obtained

## 2023-10-31

### v0.1.1

- **Added** support for RocketMQ middleware
- **Added** offline upgrade functionality
