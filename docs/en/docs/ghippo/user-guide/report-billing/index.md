---
MTPE: WANG0608GitHub
Date: 2024-09-18
hide:
  - toc
---

# Operation Management

Operation Management provides a visual representation of the total usage and utilization rates of CPU,
memory, storage and GPU across various dimensions such as cluster, node, namespace, pod, and workspace
within a specified time range on the platform. It also automatically calculates platform consumption
information based on usage, usage time, and unit price. By default, the module enables all report statistics,
but platform administrators can manually enable or disable individual reports. After enabling or disabling,
the platform will start or stop collecting report data within a maximum of 20 minutes. Previously collected
data will still be displayed normally. Operation Management data can be retained on the platform for up to
365 days. Statistical data exceeding this retention period will be automatically deleted. You can also download
reports in CSV or Excel format for further statistics and analysis.

Operation Management is available only for the Standard Edition and above. It is not supported in the Community Edition.

You need to [install or upgrade the Operations Management module](./gmagpie-offline-install.md) first, and then you can experience report management and billing metering.

## Report Management

Report Management provides data statistics for cluster, node, pods, workspace, and namespace across
five dimensions: CPU Utilization, Memory Utilization, Storage Utilization, GPU Computing Power Utilization,
and GPU Memory Utilization. It also integrates with the audit and alert modules to support the statistical
management of audit and alert data, supporting a total of seven types of reports.

## Accounting & Billing

Accounting & Billing provides billing statistics for clusters, nodes, pods, namespaces, and workspaces
on the platform. It calculates the consumption for each resource during the statistical period based on
the usage of CPU, memory, storage and GPU, as well as user-configured prices and currency units. Depending
on the selected time span, such as monthly, quarterly, or annually, it can quickly calculate the actual
consumption for that period.
