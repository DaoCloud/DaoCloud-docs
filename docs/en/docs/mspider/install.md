---
date: 2022-11-17
hide:
  - toc
---

# Install the service mesh

Please confirm that your cluster has successfully connected to the container management platform, and then perform the following steps to install the service mesh.

1. Click `Container Management` from the left navigation bar, enter the `Cluster List`, and click the name of the cluster where the service mesh is to be installed.

    ![Install Collector](./images/login01.jpg)

2. On the `Cluster Overview` page, click `Console`.

    ![Install Collector](./images/login02.jpg)

3. Enter the following commands line by line from the console:

    ```sh
    export VERSION=0.0.0-xxxx
    helm repo add mspider https://release.daocloud.io/chartrepo/mspider
    helm repo update
    helm upgrade --install --create-namespace -n mspider-system mspider mspider/mspider --version=${VERSION} --set global.imageRegistry=release.daocloud.io/mspider
    ```

    ![Install Collector](./images/install01.jpg)

    !!! note

        Please replace `0.0.0-xxx` with the version number of the service mesh you plan to install.

4. Check the Pod information under the namespace `mspider-system`, and see that the relevant Pods have been created and running, indicating that the service mesh is installed successfully.

    ![Install Collector](./images/install02.jpg)