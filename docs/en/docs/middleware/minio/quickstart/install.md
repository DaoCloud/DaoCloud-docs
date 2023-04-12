# Install MinIO

Because MinIO belongs to the application layer of DCE 5.0, a DCE environment needs to be prepared first.

Follow the steps below to install MinIO.

## Install MinIO-operator

1. On the left navigation bar, click `Container Management` -> `Cluster List`.

    

2. Select the cluster where MinIO is to be installed, and click the cluster name.

    

3. In the left navigation bar, click `Helm Application` -> `Helm Template`, enter `minio` in the search box, press the Enter key, and click the MinIO-operator tile card.

    

4. After selecting the appropriate version, click the `Install` button. You can also follow the text prompts in the black area to install from the command line.

    

5. Enter an appropriate name, select the namespace and version, and click `OK`. You can also configure YAML at the bottom to install.

    

    

6. The system returns the `Helm application` list, and the screen prompts that the creation is successful. After a short wait, the status will change from 'Installing' to 'Deployed'.

    

## Install mcamel-MinIO

1. Configure the repository.

    ```shell
    helm repo add mcamel-release https://release.daocloud.io/chartrepo/mcamel
    helm repo update
    ```

2. Check the version.

    ```shell
    helm search repo mcamel-release/mcamel-minio --versions
    NAME CHART VERSION APP VERSION DESCRIPTION
    mcamel-release/mcamel-MinIO 0.1.0 0.1.0 A Helm chart for Kubernetes
    ```

3. Install and upgrade.

    ```shell
    helm upgrade --install mcamel-minio --create-namespace -n mcamel-system --cleanup-on-fail \
    --set global.mcamel.imageTag=v0.1.0 \
    --set global.imageRegistry=release.daocloud.io\
    mcamel-release/mcamel-minio \
    --version 0.1.0
    ```

    Parameter Description:

    ```shell
    --set ui.image.tag # Specify the front-end image version
    --set ghippo.createCrd # Register ghippo route, open by default
    --set insight.serviceMonitor.enabled # Enable monitoring, enabled by default
    --set insight.grafanaDashboard.enabled # Turn on the monitoring panel, which is enabled by default

    # global parameters
    --set global.mcamel.imageTag # mcamel-MinIO image version
    --set global.imageRegistry # container registry address
    ```

## uninstall

When uninstalling, first uninstall mcamel-minio, and then delete minio-operator to release related resources.

### Uninstall mcamel-minio

```shell
helm uninstall mcamel-minio -n mcamel-system
```

### remove minio-operator

1. In the Helm application list, click `⋮` on the far right or the name of a Helm application, and select `Delete`.

    

2. Enter the name to be deleted in the pop-up window, and click `Delete` after confirming that it is correct.

    