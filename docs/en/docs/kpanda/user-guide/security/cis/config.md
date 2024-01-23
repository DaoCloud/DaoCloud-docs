# Scan Configuration

The first step in using [CIS Scanning](../index.md) is to create a scan configuration. Based on the scan configuration, you can then create scan policies, execute scan policies, and finally view scan results.

## Create a Scan Configuration

The steps for creating a scan configuration are as follows:

1. Click __Security Management__ in the left navigation bar of the homepage of the container management module.

    

2. By default, enter the __Compliance Scanning__ page, click the __Scan Configuration__ tab, and then click __Create Scan Configuration__ in the upper-right corner.

    

3. Fill in the configuration name, select the configuration template, and optionally check the scan items, then click __OK__ .

    Scan Template: Currently, two templates are provided. The __kubeadm__ template is suitable for general Kubernetes clusters. The __daocloud__ template ignores scan items that are not applicable to DCE 5.0 based on the __kubeadm__ template and the platform design of DCE 5.0.

    

## View Scan Configuration

Under the scan configuration tab, clicking the name of a scan configuration displays the type of the configuration, the number of scan items, the creation time, the configuration template, and the specific scan items enabled for the configuration.

    

## Updat/Delete Scan Configuration

After a scan configuration has been successfully created, it can be updated or deleted according to your needs.

Under the scan configuration tab, click the __ⵗ__ action button to the right of a configuration:

- Select __Edit__ to update the configuration. You can update the description, template, and scan items. The configuration name cannot be changed.
- Select __Delete__ to delete the configuration.

    