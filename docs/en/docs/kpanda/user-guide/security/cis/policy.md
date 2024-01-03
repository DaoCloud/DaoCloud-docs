# Scan Policy

## Create a Scan Policy

After creating a scan configuration, you can create a scan policy based on the configuration.

1. Under the __Security Management__ -> __Compliance Scanning__ page, click the __Scan Policy__ tab on the right to create a scan policy.

    

2. Fill in the configuration according to the following instructions and click __OK__ .

    - Cluster: Select the cluster to be scanned. The optional cluster list comes from the clusters accessed or created in the [Container Management](../../../intro/index.md) module. If the desired cluster is not available, you can access or create a cluster in the Container Management module.
    - Scan Configuration: Select a pre-created scan configuration. The scan configuration determines which specific scan items need to be performed.
    - Scan Type:

        - Immediate scan: Perform a scan immediately after the scan policy is created. It cannot be automatically/manually executed again later.
        - Scheduled scan: Automatically repeat the scan at scheduled intervals.

    - Number of Scan Reports to Keep: Set the maximum number of scan reports to be kept. When the specified retention quantity is exceeded, delete from the earliest report.

    

## Update/Delete Scan Policies

After creating a scan policy, you can update or delete it as needed.

Under the __Scan Policy__ tab, click the __ⵗ__ action button to the right of a configuration:

- For periodic scan policies:

    - Select __Execute Immediately__ to perform an additional scan outside the regular schedule.
    - Select __Disable__ to interrupt the scanning plan until __Enable__ is clicked to resume executing the scan policy according to the scheduling plan.
    - Select __Edit__ to update the configuration. You can update the scan configuration, type, scan cycle, and report retention quantity. The configuration name and the target cluster to be scanned cannot be changed.
    - Select __Delete__ to delete the configuration.

- For one-time scan policies: Only support the __Delete__ operation.

    