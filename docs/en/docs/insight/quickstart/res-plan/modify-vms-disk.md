# vmstorage Disk Expansion

This article describes the method for expanding the vmstorage disk. Please refer to the [vmstorage disk capacity planning](../res-plan/vms-res-plan.md) for the specifications of the vmstorage disk.

## Procedure

### Enable StorageClass expansion

1. Log in to the DCE 5.0 platform as a global service cluster administrator. Click __Container Management__ -> __Clusters__ and go to the details of the __kpanda-global-cluster__ cluster.

2. Select the left navigation menu __Container Storage__ -> __PVCs__ and find the PVC bound to the vmstorage.

    ![Find vmstorage](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/vmdisk01.png)

3. Click a vmstorage PVC to enter the details of the volume claim for vmstorage and confirm the StorageClass that the PVC is bound to.

    ![Modify Disk](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/vmdisk02.png)

4. Select the left navigation menu __Container Storage__ -> __Storage Class__ and find __local-path__ . Click the __⋮__ on the right side of the target and select __Edit__ in the popup menu.

    ![Edit StorageClass](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/vmdisk03.png)

5. Enable __Scale Up__ and click __OK__ .

    ![Scale Up](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/vmdisk04.png)

### Modify the disk capacity of vmstorage

1. Log in to the DCE 5.0 platform as a global service cluster administrator and go to the details of the __kpanda-global-cluster__ cluster.

2. Select the left navigation menu __CRDs__ and find the custom resource for __vmcluster__ .

    ![vmcluster](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/vmdisk05.png)

3. Click the custom resource for vmcluster to enter the details page, switch to the __insight-system__ namespace, and select __Edit YAML__ from the right menu of __insight-victoria-metrics-k8s-stack__ .

    ![Edit YAML](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/vmdisk06.png)

4. Modify according to the legend and click __OK__ .

    ![Confirm Edit](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/vmdisk07.png)

5. Select the left navigation menu __Container Storage__ -> __PVCs__ again and find the volume claim bound to vmstorage. Confirm that the modification has taken effect. In the details page of a PVC, click the associated storage source (PV).

    ![Relate PV](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/vmdisk08.png)

6. Open the volume details page and click the __Update__ button in the upper right corner.

    ![Update](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/vmdisk09.png)

7. After modifying the __Capacity__ , click __OK__ and wait for a moment until the expansion is successful.

    ![Edit Storage](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/vmdisk10.png)

### Clone the storage volume

If the storage volume expansion fails, you can refer to the following method to clone the storage volume.

1. Log in to the DCE 5.0 platform as a global service cluster administrator and go to the details of the __kpanda-global-cluster__ cluster.

2. Select the left navigation menu __Workloads__ -> __StatefulSets__ and find the stateful set for __vmstorage__ . Click the __⋮__ on the right side of the target and select __Status__ -> __Stop__ -> __OK__ in the popup menu.

    ![Stop Status](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/vmdisk11.png)

3. After logging into the __master__ node of the __kpanda-global-cluster__ cluster in the command line, run the following command to copy the vm-data directory in the vmstorage container to store the metric information locally:

    ```bash
    kubectl cp -n insight-system vmstorage-insight-victoria-metrics-k8s-stack-1:vm-data ./vm-data
    ```

4. Log in to the DCE 5.0 platform and go to the details of the __kpanda-global-cluster__ cluster. Select the left navigation menu __Container Storage__ -> __PVs__ , click __Clone__ in the upper right corner, and modify the capacity of the volume.

    ![Clone](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/vmdisk12.png)

    ![Edit Storage](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/vmdisk13.png)

5. Delete the previous data volume of vmstorage.

    ![Delete vmstorage](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/vmdisk14.png)

6. Wait for a moment until the volume claim is bound to the cloned data volume, then run the following command to import the exported data from step 3 into the corresponding container, and then start the previously paused __vmstorage__ .

    ```bash
    kubectl cp -n insight-system ./vm-data vmstorage-insight-victoria-metrics-k8s-stack-1:vm-data
    ```
