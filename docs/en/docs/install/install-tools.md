# Dependencies of DCE 5.0

Before you start installing DCE 5.0, you must have these dependencies installed first, otherwise you installation of DCE 5.0 may get failed.

- For the Community package, install the dependencies on the K8s Controller node.
- For the Enterprise Package, install the dependencies on the [Bootstrapping Node](./commercial/deploy-arch.md).

!!! note
    
    You should install **all** of the following dependencies:

    - podman
    - helm
    - skopeo
    - kind
    - kubectl
    - yq
    - minio client
    
    If you have already installed lower versions of these tools, just follow these steps and they will be automatically and mandatorily upgrade versions required for DCE 5.0.

## Online Install

1. Download the script.

    ```bash
    curl -LO https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite.sh
    ```

    Add permission to run `install_prerequisite.sh`:

    ```bash
    chmod +x install_prerequisite.sh
    ```

2. Execute the install script.

    - For the Community package, run:

        ```bash
        bash install_prerequisite.sh online community
        ```

    - For the Enterprise package, run:

        ```bash
        bash install_prerequisite.sh online full
        ```

## Offline Install

Offline installation means that the target host is not connected to the network and cannot download the required dependencies. Therefore, it is necessary to create the offline package in an online environment first.

1. Download the script.

    ```bash
    curl -LO https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite.sh
    ```

2. Download the prerequisite components' offline package.

    ```bash
    export VERSION=v0.8.0
    curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/prerequisite_${VERSION}_amd64.tar.gz

    tar -xvf prerequisite_${VERSION}_amd64.tar.gz
    ```

    !!! note

        - If you are using an arm architecture, the download address will be: https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/prerequisite_${VERSION}_arm64.tar.gz
        - Make sure the offline package and the script are in the same directory level.

3. Perform the offline installation.

    - For the community package:

        ```bash
        bash install_prerequisite.sh offline community
        ```

    - For the enterprise package:

        ```bash
        bash install_prerequisite.sh offline full
        ```

You can now go to [install DCE 5.0 Community package](community/resources.md) or [DCE 5.0 Enterprise package](commercial/deploy-requirements.md)
