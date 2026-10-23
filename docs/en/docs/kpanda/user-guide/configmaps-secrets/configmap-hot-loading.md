# ConfigMap/Secret Hot Reloading

ConfigMap/Secret hot reloading means that when a ConfigMap/Secret is mounted as a data volume in a container, the container automatically reads the updated configuration of the ConfigMap/Secret when the configuration changes, without restarting the Pod.

## Procedure

1. Refer to Creating a Workload - [Container Settings](../workloads/create-deployment.md#container-settings) to configure container data storage, and select __ConfigMap__ , __ConfigMap Key__ , __Secret__ , or __Secret Key__ to mount as a data volume in the container.

    ![Use a ConfigMap as a Data Volume](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/user_configmap_to_volume.jpg)

    !!! note

        Configuration files mounted using the subpath method do not support hot reloading.

2. Go to the __ConfigMaps and Secrets__ page, enter the ConfigMap details page, find the corresponding __container__ resource in __Associated Resources__ , and click the __Load Now__ button to enter the configuration hot reloading page.

    ![Use a ConfigMap as a Data Volume](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/configmap-hot-loading03.png)

    !!! note

        If your application supports automatically reading the updated configuration of the ConfigMap/Secret, you do not need to manually perform the hot reloading operation.

3. In the hot reloading configuration dialog box, enter the __Execution Command__ to be run inside the container and click the __OK__ button to reload the configuration. For example, in an nginx container, run the __nginx -s reload__ command as the root user to reload the configuration.

    ![Use a ConfigMap as a Data Volume](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/configmap-hot-loading02.png)

4. Check the application reload status in the web terminal that pops up in the interface.

    ![Use a ConfigMap as a Data Volume](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/configmap-hot-loading.jpg)
