---
hide:
  - toc
MTPE: ModetaNiu
DATE: 2024-08-19
---

# Features

This page explains about the functional features of MySQL.

- High availability architecture

    It supports active/standby hot backup architecture, flexibly meets various availability requirements, 
    and its stable and reliable performance far exceeds the industry average.

- Rapid deployment

    Instances can be quickly deployed online, and the graphical interface is easy to operate, 
    which improves the efficiency of self-built databases including procurement, deployment, and configuration, 
    shortens the project cycle, and helps businesses go online quickly.

- Ensure data security

    Based on real-time copy technology, it adapts to public cloud, hybrid cloud and private cloud, 
    and strictly controls accounts to ensure data security.

- Lower cost

    The required resources can be activated in real time according to business needs, and there is no need 
    to purchase high-cost hardware at the initial stage of business, effectively reducing initial asset investment 
    and avoiding waste of idle resources.

- Autoscaling

    Database resources can be scaled automatically according to your business pressure to meet the needs of 
    database performance and storage space in different business stages.

- Automatic operation and maintenance

    You can set automatic backup policies, monitoring and alert policies, automatic capacity expansion policies, etc.

After MySQL is deployed in DCE 5.0, the following features will also be supported:

- Implement MySQL high availability and topology management based on Orchestrator
- Support single node and active/standby mode
- Support phpmyadmin, provide management page
- Expose metrics based on mysqld-exporter
- Use Grafana Operator to integrate MySQL Dashboard to display monitoring data
- Use ServiceMonitor to connect to Prometheus to capture metrics
- Supports backup and recovery (depends on storage that supports the S3 protocol)