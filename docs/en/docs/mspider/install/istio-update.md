---
hide:
  - toc
---

# Upgrade Istio

!!! warning "Update Reminder"

    Try to avoid making configuration or related changes during the update. Please plan your upgrade schedule accordingly.

There are three types of service meshes supported, including Hosted Mesh and Dedicated Mesh created and managed by DaoCloud, and External Mesh which refers to the existing service mesh of the customer.

## One-click Upgrade: Hosted Mesh and Dedicated Mesh

For the hosted mesh types provided by DaoCloud, Istio versions can be upgraded continuously. DaoCloud offers two types of upgrade versions: native version and customized version.

- Native version: The community-native Istio without any customization.
- Customized version: Based on Istio, it has been customized with certain functionalities (suffix: -mspider).
  For example, integration with [Merbridge](../../community/merbridge.md) to improve mesh communication performance,
  support for intelligent recognition of traditional microservices such as SpringCloud and Dubbo,
  and support for sidecar hot-upgrade capability.

The upgrade process is the same for both types of versions, but mixed upgrades of different types are not supported. Therefore, please confirm the required version when creating a mesh instance.

DaoCloud will continue to provide adaptation work for new Istio versions. When a new Istio version is detected by the system, the mesh list will prompt for upgradable mesh instances (a card with an exclamation mark icon will appear).

Check the content of the icon and click the `Upgrade Now` button to enter the upgrade wizard.

![Upgrade Now](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/IstioUpdate01.png)

The Istio upgrade wizard includes three steps: `Select target version`, `Environment detection`, and `Perform upgrade`.

After the upgrade is completed, the mesh can be immediately deployed and run online. The specific steps are as follows:

1. **Select Target Version**: Select the desired version to upgrade from the list. After the upgrade,
   rolling back to a lower version will not be possible, so choose carefully.

    ![Target Version](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/IstioUpdate02.png)

    > It is not recommended by the official to perform cross-version upgrades for Istio.
    > It is suggested to upgrade in a step-by-step manner, for example, upgrading from `1.15.x` to `1.16.x`.
    > It is not recommended to directly upgrade to versions greater than `1.16.x`.

2. **Environment Detection**: The system will detect whether the versions of each cluster (k8s) under the mesh meet the upgrade requirements based on the selected target version. If they meet the requirements, the `Next` button will be activated; otherwise, the user needs to address any environment issues.

    ![Environment Detection](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/IstioUpdate03.png)

	  - If the cluster (k8s) version is too low, you can upgrade the cluster (k8s) version first in the
      container management and then click the `Redetect` button.

	  - If the cluster (k8s) version is too high, it is recommended to go back and select a higher version of Istio
      in the "Select target version" step.

3. **Perform Upgrade**: After passing the environment detection, you will enter the upgrade phase, which includes two stages: `Upgrade` and `Health Check`.

	  - Istio Upgrade: Pulling Istio images and upgrading control plane components.

	  - Istio Health Check: Checking the running status of Istio control plane components.

	  ![Perform Upgrade](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/IstioUpdate04.png)

After the upgrade is completed, go back to the mesh list page, and you will see that the Istio version of the mesh has been changed.

![Upgrade](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/IstioUpdate05.png)

!!! note

    - Once the upgrade process starts, it cannot be terminated.
      It is recommended not to perform any configuration operations on the mesh during the upgrade.
    - For a more intuitive demonstration of the process, please refer to the [video tutorial](../../videos/mspider.md).

## Manual Upgrade: External Mesh

Since the external mesh is self-managed by users, the deployment form of the mesh cannot be determined.
Therefore, users need to perform the upgrade themselves. This article provides several upgrade suggestions
recommended by Istio official. Please follow the actual deployment scenario to proceed.

- **Canary Upgrades**: Upgrade Istio by running a new control plane with canary deployment.
- **In-place Upgrades**: Upgrade and rollback in-place.
- **Upgrade with Helm**: Instructions for upgrading Istio using Helm.

!!! warning "Important"

    One-step upgrades for multiple versions (e.g., from 1.6.x to 1.8.x) have not been officially tested
    and promoted. It is strongly recommended to upgrade in a step-by-step manner.

For more considerations on manual upgrade, please refer to the official [Istio Documentation](https://istio.io/latest/docs/setup/upgrade/)
