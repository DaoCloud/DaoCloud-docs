# Vulnerability Scan

To use the [Vulnerability Scan](index.md) function, you need to create a scan policy first. After executing the policy, a scan report will be automatically generated for viewing.

## Create a Scan Policy

1. On the left navigation bar of the homepage in the Container Management module, click `Security Management`.



2. Click `Vulnerability Scan` on the left navigation bar, then click the `Scan Policy` tab and click `Create Scan Policy` on the right.


3. Fill in the configuration according to the following instructions, and then click `OK`.

    - Cluster: Select the cluster to be scanned. The optional cluster list comes from the clusters accessed or created in the [Container Management](../../intro/index.md) module. If the desired cluster is not available, you can access or create a cluster in the Container Management module.
    - Scan Type:

        - Immediate scan: Perform a scan immediately after the scan policy is created. It cannot be automatically/manually executed again later.
        - Scheduled scan: Automatically repeat the scan at scheduled intervals.

    - Number of Scan Reports to Keep: Set the maximum number of scan reports to be kept. When the specified retention quantity is exceeded, delete from the earliest report.


## Update/Delete Scan Policies

After creating a scan policy, you can update or delete it as needed.

Under the `Scan Policy` tab, click the `ⵗ` action button to the right of a configuration:

- For periodic scan policies:

    - Select `Execute Immediately` to perform an additional scan outside the regular schedule.
    - Select `Disable` to interrupt the scanning plan until `Enable` is clicked to resume executing the scan policy according to the scheduling plan.
    - Select `Edit` to update the configuration. You can update the scan configuration, type, scan cycle, and report retention quantity. The configuration name and the target cluster to be scanned cannot be changed.
    - Select `Delete` to delete the configuration.

- For one-time scan policies: Only support the `Delete` operation.



## Viewe Scan Reports

1. Under the `Security Management` -> `Vulnerability Scanning` -> `Scan Reports` tab, click the report name.

    > Clicking `Delete` on the right of a report allows you to manually delete the report.


2. View the scan report content, including:

    - The target cluster scanned.
    - The scan policy used.
    - The scan frequency.
    - The total number of risks, high risks, medium risks, and low risks.
    - The time of the scan.
    - Check details such as vulnerability ID, vulnerability type, vulnerability name, vulnerability description, etc.

