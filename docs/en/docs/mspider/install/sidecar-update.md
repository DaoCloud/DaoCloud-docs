# sidecar version upgrade

After the Istio version of the mesh is upgraded, the sidecar upgrade function will be triggered. Sidecar upgrades can be divided into two upgrade methods: `hot upgrade` and `restart upgrade`.

- Hot upgrade: The Istio lower sidecar of Daoke's customized version can complete the sidecar upgrade without restarting the user's Pod, so as to achieve uninterrupted business;
- Reboot upgrade: The upgrade method of the community-native Istio or the customized version of Istio that does not meet the requirements of the hot upgrade environment requires restarting the user Pod.

After the Istio version upgrade is completed, enter the `Workload Sidecar Management` interface, and the workload that meets the upgrade conditions will display an exclamation mark prompt message. Select the workload you want to upgrade, and the `Sidecar Upgrade` button will appear.



Click the `Sidecar Upgrade` button to enter the `Sidecar Upgrade Version` wizard, which is divided into three steps: `Environment Detection`, `Select Target Version`, and `Execute Upgrade`. In "Hot Upgrade" and "Restart Upgrade" There will be some differences in operation under the two methods.

## Hot upgrade

1. **Environment detection**: In this step, it will detect whether the cluster environment meets the hot upgrade requirements. The detection items include the following three items:

- Istio version: whether it is a customized version (version suffix: -mspider)
- K8s version: whether it meets the hot upgrade requirement range
- EphemeralContainer: is it enabled

After the above three items are met, it will enter the hot upgrade process in the next step.

    

2. **Sidecar upgrade version**: During the hot upgrade process, you can select the sidecar version you want to upgrade. The default is the latest version. If you select another version, the relevant Pod will be automatically upgraded to the latest version after restarting.

    

3. **Execute upgrade**: The selected workload and related sidecar information are displayed on the upgrade page. Click `One-click upgrade` to start the upgrade process.

    

## restart upgrade

1. **Environmental testing**: If the detected items do not meet the hot upgrade requirements during the testing phase, the next two steps will enter the restarting upgrade process.

    

2. **Sidecar upgrade version** In the restart upgrade process, the version cannot be selected, and only the latest version is supported.



3. **Execute upgrade**: The upgrade page displays the basic information of the selected workload and sidecar version information. Clicking `One-click Upgrade` will restart the Pod immediately. Please be careful.





!!! note

    Closing the upgrade wizard during the upgrade will not interrupt the current upgrade task.