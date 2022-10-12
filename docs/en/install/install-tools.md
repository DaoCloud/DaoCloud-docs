# Install Dependencies

After deploying k8s clusters, you shall install some dependencies before you explore the capabilities of DCE 5.0.

## Install online

1. On the k8s control plane (master node), download the dce5-installer binary package.

    ```shell
    curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite.sh
    ```

    Add the executable permission to `install_prerequisite.sh`:

    ```bash
    chmod +x install_prerequisite.sh
    ```

2. Start to install all prerequisites dependencies.

    ```bash
    bash install_prerequisite.sh online community
    ```

    !!! note

        Currently, this script includes the following dependencies:

        - helm 3.9.4
        - skopeo 1.9.2
        - kubectl 1.25.0
        - yq 4.27.5

## Install offline

Offline installation means that your hosts are offline and you cannot download the required dependencies, so you need to make an offline package in an online environment.

1. Make the offline package.

    ```bash
    bash install_prerequisite.sh export community
    ```

    !!! note

        When you performed the above command, `pre_pkgs.tar.gz` will be generated in the current directory.

2. Upload all files in the directory to the offline environment.

    ``` bash
    # The script is in the same folder as the offline package
    $ tree .
    .
    ├── install_prerequisite.sh
    └── pre_pkgs.tar.gz
    ```

3. Perform offline installation.

    ``` bash
    bash install_prerequisite.sh offline community
    ```
    