# Install Dependencies

Before installing Token Factory, you need to install some dependencies on the
[Bootstrap Node](./commercial/deploy-arch.md).

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
    export VERSION=v0.44.0   # (1)!
    curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite_${VERSION}.sh
    ```

    1. The installer version

    Add executable permission to `install_prerequisite_${VERSION}.sh`:

    ```bash
    chmod +x install_prerequisite_${VERSION}.sh
    ```

2. Start the online installation of prerequisites.

    ```bash
    bash install_prerequisite_${VERSION}.sh online full
    ```

## Offline Install Dependencies

Offline installation means that the target host is in an offline state and cannot download the required dependencies.
Therefore, you need to create an offline package in an online environment first.

1. Find a machine with internet access and download the installation script.

    ```bash
    export VERSION=v0.44.0
    curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite_${VERSION}.sh
    ```

2. Download the offline package for prerequisites.

    ```bash
    export VERSION=v0.44.0  
    curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/prerequisite_${VERSION}_amd64.tar.gz
    ```

    !!! note

        - For ARM architecture, use the download link for ARM:
          <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/prerequisite_${VERSION}_arm64.tar.gz>
        - Make sure the offline package and the script are in the same directory level.

3. Upload the downloaded offline packages to a control plane node of a K8s cluster and perform the offline installation.

    ```bash
    export BINARY_TAR=prerequisite_${VERSION}_amd64.tar.gz
    chmod +x install_prerequisite_${VERSION}.sh
    ./install_prerequisite_${VERSION}.sh offline full
    ```

You can now proceed to [install Token Factory](./start-install.md).
