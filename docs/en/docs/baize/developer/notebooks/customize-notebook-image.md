# Customize a Development Environment Image for Notebook

*[Baize]: Development codename for the AI Lab component

Notebook provides a powerful set of online development environments. However, when facing specific algorithm models,
you may need different versions of dependency libraries (for example, a specific version of CUDA, PyTorch, or TensorFlow). In such cases, the built-in images of the platform cannot fully cover your requirements.

This document will guide you on how to build and register a Notebook image that contains custom dependencies based on the base image provided by AI Lab, so that platform users can directly select this custom image when creating a Notebook instance.

## Prerequisites

Before you start, make sure you have the following conditions:

### Permission Requirements

- You have the kubectl administrative permission for the target Kubernetes cluster, or you can edit the ConfigMap and Deployment resources in the **baize-system** namespace through the platform UI;
- You have an available container image registry and the permission to push images to it.

### Tool Requirements

- A container build tool is installed on your local machine or server;
- The kubectl command-line tool is configured locally and connected to the target cluster.

## Steps

The whole process consists of four core steps:

1. [Get the Base Notebook Image](#get-the-base-notebook-image): Get the base Notebook image address corresponding to the current AI Lab version.
1. [Customize and Build the Image](#customize-and-build-the-image): Write a Dockerfile to add custom dependencies, then build and push the image.
1. [Register the New Image](#register-the-new-image): Register the address of the new image in the AI Lab configuration, and restart the service to make it take effect.
1. [Use the New Environment](#use-the-new-environment): When creating a Notebook instance, select your newly added image from the dropdown list.

### Get the Base Notebook Image

First, we need to find the base Notebook image address that the current AI Lab version depends on. This address will be used as the `FROM` source of the Dockerfile.

=== "Command-line Operations"

    1. Log in to the management node of the Kubernetes cluster through SSH.

    1. Run the following command to view the installed AI Lab version. This helps you locate the image for the corresponding version.

        ```bash
        helm list -n baize-system | grep baize
        ```

        You will see output similar to the following. Note the version number in the `APP VERSION` column (for example, `v0.19.1`).

        ```text
        NAME    NAMESPACE     REVISION    UPDATED                                  STATUS      CHART            APP VERSION
        baize   baize-system  5           2025-08-18 11:39:12.328965189 +0800 CST  deployed    baize-v0.19.1    v0.19.1
        ```

    1. Run the following command. In the output YAML content, find the `notebook_images` field or a similar field, and locate the image address that matches the version number.
       Copy one of the image addresses that matches the version for later use, for example, `192.168.157.30/release.daocloud.io/baize/baize-notebook:v0.19.1`.

        ```bash
        kubectl get cm baize -n baize-system -o yaml
        ```

        <!-- ![View the base Notebook image](../../images/custom-image-01.png) -->

=== "Graphical Operations"

    1. Log in to DCE, go to **Container Management** -> **Cluster List** from the left navigation bar, and find and click the **kapanda-global-cluster** global service cluster.

        <!-- ![Enter the cluster list](../../images/custom-image-02.png) -->

    1. In the left navigation bar of the **kapanda-global-cluster** cluster, choose **Configurations and Secrets** -> **ConfigMaps**.
       In the **Namespace** dropdown box at the top of the page, select **baize-system**.

        <!-- ![Enter the baize-system namespace](../../images/custom-image-03.png) -->

    1. In the list, find and click the ConfigMap named **baize**.

        <!-- ![Enter the baize ConfigMap](../../images/custom-image-04.png) -->

    1. Click **Edit YAML** in the upper right corner of the page.

        <!-- ![View the YAML](../../images/custom-image-05.png) -->

    1. In the YAML editor that appears, find the `data.config.yaml` -> `notebook_images:` field. The list shows all the built-in Notebook images.
       Copy one of them as the base image address, for example, `192.168.157.30/release.daocloud.io/baize/baize-notebook:v0.19.1`.

        <!-- ![View the base Notebook image](../../images/custom-image-06.png) -->

### Customize and Build the Image

This example demonstrates how to install PyTorch with a specific CUDA version.

1. Create a `Dockerfile` on your local development environment or build server, using the [base image obtained in the previous step](#get-the-base-notebook-image) as the starting point, and install the required dependencies.

    ```dockerfile title="Dockerfile example"
    # Use the base image address obtained in the previous step
    FROM 192.168.157.30/release.daocloud.io/baize/baize-notebook:v0.19.1

    # Install the required dependencies, for example, PyTorch that supports CUDA 11.8
    RUN pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
    ```

1. Build and push the custom image:

    ```bash
    # Define the full name and tag of the new image
    export CUSTOM_IMAGE_NAME="<your-registry-address>/baize/baize-notebook:v0.19.1-cuda11.8-torch2.0.1"

    # Build the image
    podman build -t ${CUSTOM_IMAGE_NAME} -f Dockerfile .

    # Push the image to your registry
    podman push ${CUSTOM_IMAGE_NAME}
    ```

    !!! note

        Replace `<your-registry-address>/...` with your own image registry address, and set a clearly identifiable tag for it, for example, one that includes the version number, the CUDA version, and the key libraries.

### Register the New Image

After the image is pushed to the registry, we need to modify the AI Lab configuration so that the platform "knows" about the new environment, and restart the service to apply the configuration.

=== "Command-line Operations"

    1. On the management node, run the following command to enter the edit mode of the `baize` ConfigMap.

        ```bash
        kubectl edit cm baize -n baize-system
        ```

    1. In the YAML editor, find the `notebook_images` list. Add a new entry to the list that points to the pushed custom image. Finally, save and exit the editor.

        ```yaml title="data.config.yaml"
        # ... (existing configuration)
        data:
          config.yaml: |-
            ...
            notebook_images:
              # - name: ... (existing built-in image)
              # - name: ... (existing built-in image)
              - name: <your-registry-address>/baize/baize-notebook:v0.19.1-cuda11.8-torch2.0.1
                type: JUPYTER
              ...
        # ... (other configuration)
        ```

        - `name`: This is the `CUSTOM_IMAGE_NAME` customized and built in the previous section.
        - `type`: Specifies the category of the image. If it is mainly used for Jupyter, set it to `JUPYTER`.

    1. On the management node, run the following commands in sequence to restart the service.

        ```bash
        # Restart baize-apiserver
        kubectl rollout restart deployment baize-apiserver -n baize-system
        ```

=== "Graphical Operations"

    1. Return to the **Edit YAML** page of the Baize ConfigMap opened in [Get the Base Notebook Image](#get-the-base-notebook-image).
       Find the `data.config.yaml` -> `notebook_images:` list. Add a new entry at the end of the list, with the `name` value set to the `CUSTOM_IMAGE_NAME` pushed in [Customize and Build the Image](#customize-and-build-the-image). Click **OK** in the lower right corner to save your changes.

        <!-- ![Add a new image](../../images/custom-image-07.png) -->

    1. Restart the service. Still on the **kapanda-global-cluster** cluster page, go to **Workloads** -> **Deployments** from the left navigation bar, and select **baize-system** as the **Namespace** at the top of the page.

        <!-- ![View the workloads of baize-system](../../images/custom-image-08.png) -->

    1. In the list, find **baize-apiserver**, click the **┇** action button on the right, and choose **Modify Status** -> **Restart**.

        <!-- ![Restart the service](../../images/custom-image-09.png) -->

### Use the New Environment

After completing all the above steps, your new environment is ready.

1. Navigate to **AI Lab** -> **Developer Console** -> **Notebooks**. Click **Create** in the upper right corner.

    <!-- ![Enter the Notebook creation page](../../images/custom-image-10.png) -->

1. In the **Resource Configuration** step of creating a Notebook, select the Notebook type, and select **Pre-built Image** for **Image Type**.
   In the **Image Address** dropdown menu, you should now see the custom image option you just added (for example, `...:v0.19.1-cuda11.8-torch2.0`).
   Select this image and configure other resources to create the instance.

    <!-- ![Configure resources of the Notebook](../../images/custom-image-11.png) -->
