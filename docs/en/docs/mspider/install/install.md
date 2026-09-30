---
date: 2022-11-17
hide:
   - toc
---

# Install the Service Mesh

Please confirm that your cluster has successfully connected to the container management platform, and then perform the following steps to install the service mesh.

1. Click __Container Management__ from the left navigation bar, enter the __Cluster List__ , and click the name of the cluster where the service mesh is to be installed.

    ![cluster list](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/login01.png)

2. On the __Cluster Overview__ page, click __Console__ .

    ![console](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/login02.png)

3. Enter the following commands line by line from the console (change the VERSION accordingly):

    ```sh
    # Add the mspider repository and update it. If you use a private registry, replace release.daocloud.io with the private registry address
    helm repo add mspider https://release.daocloud.io/chartrepo/mspider
    helm repo update
    
    # Find the version number in the mspider repository. Generally, choose the latest version
    helm search repo mspider/mspider
    NAME                            CHART VERSION   APP VERSION     DESCRIPTION                                       
    mspider/mspider         v0.30.1         v0.30.1         Mspider management plane application, deployed ...
    mspider/mspider-mcpc    v0.30.1         v0.30.1         Mspider control plane application, independent ...

    # Specify the version number
    export VERSION=v0.30.1
    
    helm upgrade --install mspider mspider/mspider \
        --create-namespace -n mspider-system  \
        --set global.imageRegistry=release.daocloud.io/mspider \
        --version=${VERSION}
    ```

    ![install collector](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/install01.jpg)

    !!! note

        Please replace __0.0.0-xxx__ with the version number of the service mesh you plan to install.

4. Check the Pod information under the namespace __mspider-system__ , and see that the relevant Pods have been created and running, indicating that the service mesh is installed successfully.

    ![install collector](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/install02.jpg)

Next step: [Create Mesh](../user-guide/service-mesh/index.md)
