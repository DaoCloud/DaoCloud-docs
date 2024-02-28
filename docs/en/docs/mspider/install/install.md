---
date: 2022-11-17
hide:
   - toc
---

# Install the service mesh

Please confirm that your cluster has successfully connected to the container management platform, and then perform the following steps to install the service mesh.

1. Click __Container Management__ from the left navigation bar, enter the __Cluster List__ , and click the name of the cluster where the service mesh is to be installed.

    ![cluster list](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/login01.png)

2. On the __Cluster Overview__ page, click __Console__ .

    ![console](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/login02.png)

3. Enter the following commands line by line from the console (change the VERSION based on your actual demands):

    ```shell
    export VERSION=0.0.0-xxxx
    helm repo add mspider https://release.daocloud.io/chartrepo/mspider
    helm repo update
    helm upgrade --install --create-namespace -n mspider-system mspider mspider/mspider --version=${VERSION} --set global.imageRegistry=release.daocloud.io/mspider
    ```

    !!! note

        Please replace `0.0.0-xxx` with the version number of the service mesh you plan to install.

4. Check the Pod information under the namespace __mspider-system__ , and see that the relevant Pods have been created and running, indicating that the service mesh is installed successfully.

Next step: [Create Mesh](../user-guide/service-mesh/README.md)
