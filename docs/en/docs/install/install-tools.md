# Dependencies of DCE 5.0

Before you start installing DCE 5.0, you must have these dependencies installed first, otherwise you installation of DCE 5.0 may get failed.

- For the Community package, install the dependencies on the K8s Controller node.
- For the Enterprise Package, install the dependencies on the [Spark Node](./commercial/deploy-arch.md).

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

If the target host is disconnected from the Internet, you can follow these steps to install dependencies offline.

1. Build an offline dependency package on another host that is connected to the Internet.

    - Command for the Community package:

        ```bash
        bash install_prerequisite.sh export community
        ```

    - Command for the Enterprise package:

        ```bash
        bash install_prerequisite.sh export full
        ```

    After executing the above command, a compressed package named `pre_pkgs.tar.gz` will be generated in the working directory. This file contains all dependencies mentioned above.

2. Upload all the files in the directory to the target host.

    ```bash
    # script and the offline package are located at the same level in the directory.
    $ tree .
    .
    ├── install_prerequisite.sh
    └── pre_pkgs.tar.gz
    ```

3. Install dependencies in the target host.

    - For the Community package:

        ```bash
        bash install_prerequisite.sh offline community
        ```

    - For the Enterprise package:

        ```bash
        bash install_prerequisite.sh offline full
        ```

You can now go to [install DCE 5.0 Community package](community/resources.md) or [DCE 5.0 Enterprise package](commercial/deploy-requirements.md)
