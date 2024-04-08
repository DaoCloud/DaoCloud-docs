---
MTPE: windsonsea
date: 2024-03-07
---

# Install Dependencies

Before installing DCE 5.0, you need to install some dependencies.

- For DCE Community, install the dependencies on the K8s Master node.
- For DCE 5.0 Enterprise, install the dependencies on the [Bootstrap Node](./commercial/deploy-arch.md).

!!! note

    The installed dependencies include:

    - podman
    - helm
    - skopeo
    - kind
    - kubectl
    - yq
    - minio client
    - charts-syncer
    
    If there are any existing tools in your environment with versions lower than what we define,
    they will be forcefully updated and replaced during the installation process.

## Online Install Dependencies

1. Download the script.

    ```bash
    export VERSION=v0.15.0
    curl -LO https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite_${VERSION}.sh
    ```

    Add executable permission to `install_prerequisite_${VERSION}.sh`:

    ```bash
    chmod +x install_prerequisite_${VERSION}.sh
    ```

2. Start the online installation of prerequisites.

    - For DCE Community:

        ```bash
        bash install_prerequisite_${VERSION}.sh online community
        ```

    - For DCE 5.0 Enterprise:

        ```bash
        bash install_prerequisite_${VERSION}.sh online full
        ```

## Offline Install Dependencies

Offline installation means that the target host is in an offline state and cannot download the required dependencies. Therefore, you need to create an offline package in an online environment first.

1. Download the script.

    ```bash
    export VERSION=v0.16.0
    curl -LO https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite_${VERSION}.sh
    ```

2. Download the offline package for prerequisites.

    ```bash
    export VERSION=v0.16.0
    curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/prerequisite_${VERSION}_amd64.tar.gz
    ```

    !!! note

        - For arm architecture, use the download link for arm:
          <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/prerequisite_${VERSION}_arm64.tar.gz>
        - Make sure the offline package and the script are in the same directory level.

3. Perform the offline installation.

    - For DCE Community:

        ```bash
        export BINARY_TAR=prerequisite_${VERSION}_amd64.tar.gz
        chmod +x install_prerequisite_${VERSION}.sh
        ./install_prerequisite_${VERSION}.sh offline community
        ```

    - For DCE 5.0 Enterprise:

        ```bash
        export BINARY_TAR=prerequisite_${VERSION}_amd64.tar.gz
        chmod +x install_prerequisite_${VERSION}.sh
        ./install_prerequisite_${VERSION}.sh offline full
        ```

You can now proceed to install DCE 5.0 [Community](community/resources.md) or
[Enterprise](commercial/deploy-requirements.md).
