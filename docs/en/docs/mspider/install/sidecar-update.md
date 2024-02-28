# Upgrade Sidecar

After upgrading the Istio version of the mesh, the sidecar upgrade feature will be triggered. The sidecar upgrade can be divided into two methods: __hot upgrade__ and __restart to upgrade__ .

- Hot upgrade: The customized version of DaoCloud's lower sidecar can complete the upgrade without restarting the user's Pod to achieve uninterrupted business.
- Restart to upgrade: The community-native Istio upgrade method or the customized version of Istio that does not meet the hot upgrade environment requirements requires restarting the user Pod.

After the Istio version upgrade is completed, go to the __Workload__ interface. Workloads that meet the upgrade conditions will display an exclamation mark prompt message. Select the workload you want to upgrade, and the __Upgrade Sidecar__ button will appear.

![workload sidecars](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/sidecar-update01.png)

Click the __Upgrade Sidecar__ button to enter the __Sidecar Version to Upgrade__ wizard, which has three steps: __Environment Check__ , __Select Target Version__ , and __Upgrade__ . Differences in operation between "hot upgrade" and "restart to upgrade" exist.

## Hot upgrade

1. **Environment Check**: In this step, it will detect whether the cluster environment meets the hot upgrade requirements. The detection items include:

- Istio version: whether it is a customized version (version suffix: -mspider)
- K8s version: whether it meets the hot upgrade requirement range
- EphemeralContainer: is it enabled

After meeting the above requirements, proceed to the next step for hot upgrade.

2. **Select Target Version**: During the hot upgrade process, you can select the sidecar version you want to upgrade. The default is the latest version. If you select another version, the relevant Pod will be automatically upgraded to the latest version after restarting.

3. **Upgrade**: The selected workload and related sidecar information are displayed on the upgrade page. Click __Upgrade with one-click__ to start the upgrade process.

## Restart to upgrade

1. **Environmental Check**: If the detected items do not meet the hot upgrade requirements during the testing phase, proceed to the next two steps for restart to upgrade.

    ![env check](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/SidecarUpdate05.png)

2. **Select Target Version**: In the restart to upgrade process, only the latest version is supported and cannot be selected.

	![select target version](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/SidecarUpdate06.png)

3. **Upgrade**: The upgrade page displays the basic information of the selected workload and sidecar version information. Clicking __Upgrade with one-click__ will immediately restart the Pod. Please be careful.

	![upgrade](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/SidecarUpdate07.png)

	![upgrade](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/SidecarUpdate08.png)

!!! note

    - Closing the upgrade wizard during the upgrade will not interrupt the current upgrade task.
    - If you want to abort the upgrade, directly click __Disabled__ at the bottom.
