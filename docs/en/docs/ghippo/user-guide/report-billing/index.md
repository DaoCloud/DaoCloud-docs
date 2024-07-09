---
hide:
  - toc
---

# Operations Management

Operations Management provides a visual representation of the total usage and utilization rates of CPU, memory, and storage across various dimensions such as clusters, nodes, namespaces, container groups, and workspaces within a specified time range on the platform. It also automatically calculates platform consumption information based on usage, usage time, and unit price. By default, the module enables all report statistics, but platform administrators can manually enable or disable individual reports. After enabling or disabling, the platform will start or stop collecting report data within a maximum of 20 minutes. Previously collected data will still be displayed normally. Operations Management data can be retained on the platform for up to 365 days; statistical data exceeding this retention period will be automatically deleted. You can also download reports in CSV or Excel format for further statistics and analysis.

Operations Management is available only for the Standard Edition and above; it is not supported in the Community Edition.

You need to [install or upgrade the Operations Management module](./gmagpie-offline-install.md) first, and then you can experience report management and billing metering.

## Report Management

Report Management provides data statistics for clusters, nodes, container groups, workspaces, and namespaces across six dimensions: CPU usage, CPU utilization, memory usage, memory utilization, storage usage, and storage utilization. It also integrates with the audit and alert modules to support the statistical management of audit and alert data, supporting a total of seven types of reports.

## Billing Metering

Billing Metering provides billing statistics for clusters, nodes, container groups, namespaces, and workspaces on the platform. It calculates the consumption for each resource during the statistical period based on the usage of CPU, memory, and storage, as well as user-configured prices and currency units. Depending on the selected time span, such as monthly, quarterly, or annually, it can quickly calculate the actual consumption for that period.
