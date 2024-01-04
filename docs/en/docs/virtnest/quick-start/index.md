# Install virtnest-agent in a Cluster

This guide explains how to install the virtnest-agent in a cluster.

To utilize the Virtual Machine (VM), the virtnest-agent component needs to be installed in the cluster using Helm.

1. Click on `Container Management` in the left navigation menu, then click on `Virtual Machines`. If the virtnest-agent component is not installed, you will not be able to use the VM. The interface will display a reminder for you to install within the required cluster.

    ![Instruction](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/virtnest001.png)

2. Select the desired cluster, click on `Helm Apps` in the left navigation menu, then click on `Helm Charts` to view the template list.

    ![Helm Charts](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/virtnest002.png)

3. Search for the `virtnest-agent` component, and click to the see details. Select the appropriate version and click on `Install` button to install.

    ![virtnest-agent](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/virtnest003.png)

    ![Details](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/virtnest004.png)

4. On the installation page, fill in the required information, and click on `OK` to finish the installation.

    ![Install](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/virtnest005.png)

5. Go back to the `Virtual Machines` in the navigation menu. If the installation is successful, you will see the VM list, and you can now use the VM.

    ![VM List](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/virtnest006.png)
