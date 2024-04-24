---
MTPE: windsonsea
date: 2024-01-05
---

# PostgreSQL Release Notes

This page lists the Release Notes of the PostgreSQL database, so that you can understand the evolution path and feature changes of each version.

*[Mcamel-PostgreSQL]: "Mcamel" is the dev name for DaoCloud's middlewares, and "PostgreSQL" is a relational database

## 2024-03-31

### v0.10.0

- **Added** parameter template management
- **Added** support for creating MongoDB instances via templates
- **Fixed** an issue where comments in configuration access settings were ineffective

## 2024-01-31

### v0.9.0

#### Improvements

- **Improved** Added display of PostgreSQL version in global management

## 2023-12-31

### v0.8.0

- **Improved** support for Chinese language in the monitoring dashboard
- **Fixed** an issue where validation for special characters in input fields was not working when creating instances

## 2023-11-30

### v0.7.0

- **Added** support for setting access whitelist for Mcamel-PostgreDB
- **Added** support for recording operation audit logs
- **Improved** prompt when instance list information is not obtained

## 2023-10-31

### v0.6.0

- **Added** offline upgrade functionality
- **Added** restart functionality for instances
- **Added** support for managing external instances
- **Fixed** Pod list display to show Host IP
- **Fixed** cloudshell permissions issue

## 2023-08-31

### v0.5.0

- **Improved** syntax compatibility for KindBase
- **Improved** page display during operator creation process

## 2023-07-31

### v0.4.0

- **Added** backup management capability
- **Improved** monitoring charts by removing distractions and adding time range selection
- **Fixed** an issue where some panels in the monitoring charts were not displaying

## 2023-06-30

### v0.3.0

- **Added** integration with the global management audit log module
- **Improved** the monitoring charts by removing distracting elements and adding a time range selection

## 2023-04-27

### v0.1.2

- **Added** __Mcamel-PostgreSQL__ UI module is online, support interface management
- **Added** ability to install __Mcamel-PostgreSQL__ PgAdmin offline mirror version
- **Added** __Mcamel-PostgreSQL__ PgAdmin supports LoadBalancer type
- **Improved** __Mcamel-PostgreSQL__ Exporter does not have permission to connect to PostgreSQL in the case of IPv6
- **Improved** __Mcamel-PostgreSQL__ scheduling strategy adds a sliding button

## 2023-04-20

### v0.1.1

- **Added** __Mcamel-PostgreSQL__ supports fast start PostgreSQL cluster
- **Added** __Mcamel-PostgreSQL__ supports deployment in ARM environment
- **Added** __Mcamel-PostgreSQL__ supports custom roles
- **Added** __Mcamel-PostgreSQL__ supports PostgreSQL lifecycle management backend interface
- **Added** __Mcamel-PostgreSQL__ support view log
- **Added** __Mcamel-PostgreSQL__ supports PostgreSQL 15
- **Added** __Mcamel-PostgreSQL__ supports PostgreSQL UI management interface

## 2023-03-29

### v0.0.2

- **Added** __Mcamel-PostgreSQL__ supports PostgreSQL instance creation
