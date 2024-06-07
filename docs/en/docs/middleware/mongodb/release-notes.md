---
MTPE: windsonsea
date: 2024-01-05
---

# MongoDB Release Notes

This page lists the release notes for MongoDB databases, allowing you to understand the evolution path and feature changes for each version.

*[Mcamel-MongoDB]: "mcamel" is the dev name for DaoCloud's middlewares, and "MongoDB" is a database middleware that provides services for documentation

## 2024-05-31

### v0.10.0

- **Added** parameter template import feature
- **Improved** support for batch modification of instance parameters
- **Improved** option to delete backup data in S3 when deleting backups

## 2024-04-30

### v0.9.0

- **Added** a prompt for namespace quota
- **Improved** When deleting backups, you can now choose to delete the backup data in S3
- **Fixed** the issue of mongodb-agent readinessProbe timing out in certain scenarios
- **Fixed** incorrect search results for instance configuration parameters

## 2024-03-31

### v0.8.0

- **Added** support for backup and restoration of MongoDB instances
- **Added** support for parameter templates
- **Added** Ability to create MongoDB instances via templates
- **Fixed** issue when the MongoDB backup source cluster does not exist

## 2024-01-31

### v0.7.0

#### Improvements

- **Added** display of MongoDB version in global management

## 2023-12-31

### v0.6.0

- **Added** multilingual support for the monitoring dashboard
- **Fixed** an issue where validation for special characters in input fields was not working when creating instances

## 2023-11-30

### v0.5.0

- **Added** __Mcamel-MongoDB__ console MongoDB Express

## 2023-10-31

### v0.4.0

- **Added** offline upgrade functionality
- **Added** restart functionality for instances
- **Fixed** cloudshell permissions issue

## 2023-08-31

### v0.3.0

- **Improved** syntax compatibility for KindBase
- **Improved** page display during operator creation process

## 2023-07-31

### v0.2.0

- **Added** configuration capabilities for the __pvc__ where the __log__ directory is located
- **Improved** anti-affinity default label to the create instance dialog, simplifying the configuration process
- **Improved** ability to create MongoDB instances in namespaces other than the one where the Operator is located
- **Improved** display information related to frontend interface permissions

## 2023-06-30

### v0.1.0

- **Added** support for managing MongoDB instances such as creation, viewing, and deletion in __Mcamel-MongoDB__ 
