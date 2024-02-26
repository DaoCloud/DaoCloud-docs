# Install virtnest-agent in a Cluster

This guide explains how to install the virtnest-agent in a cluster.

## Prerequisites

Before installing the virtnest-agent, the following prerequisites must be met:

- The kernel version needs to be v3.15 or above.

## Steps

To utilize the Virtual Machine (VM), the virtnest-agent component needs to be installed in the cluster using Helm.

1. Click __Container Management__ in the left navigation menu, then click __Virtual Machines__ . If the virtnest-agent component is not installed, you will not be able to use the VM. The interface will display a reminder for you to install within the required cluster.

    ![Instruction](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/virtnest001.png)

2. Select the desired cluster, click __Helm Apps__ in the left navigation menu, then click __Helm Charts__ to view the template list.

    ![Helm Charts](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/virtnest002.png)

3. Search for the __virtnest-agent__ component, and click to the see details. Select the appropriate version and click __Install__ button to install.

    ![virtnest-agent](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/virtnest003.png)

    ![Details](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/virtnest004.png)

4. On the installation page, fill in the required information, and click __OK__ to finish the installation.

    ![Install](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/virtnest005.png)

5. Go back to the __Virtual Machines__ in the navigation menu. If the installation is successful, you will see the VM list, and you can now use the VM.

    ![VM List](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/virtnest/images/virtnest006.png)
