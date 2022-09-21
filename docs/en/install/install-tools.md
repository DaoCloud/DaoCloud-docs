# Install Dependencies

After [deploying k8s clusters](install-k8s.md), you shall install some dependencies before you explore the capabilities of DCE 5.0.

## Install dependencies online

On the k8s control plane (or master node), run the following command to install dependencies:

```shell
curl -s https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite.sh | bash
```

!!! note

    This curl command will run the `install_prerequisite.sh` script and will install:

    - helm 3.9.4
    - skopeo 1.9.2
    - kubectl 1.25.0
    - yq 4.27.5

## Install dependencies offline

Offline installation means that your hosts are offline and you cannot download the required dependencies, so you need to make an offline package in an online environment.

1. Make the offline package.

    ```bash
    bash install_prerequisite.sh export
    ```

2. Upload all files in the directory to the offline environment and perform offline installation.

    ``` bash
    # The script is in the same folder as the offline package
    $ tree .
    .
    ├── install_prerequisite.sh
    └── pre_pkgs.tar.gz

    # Perform the offline instalaltion
    $ bash install_prerequisite.sh offline
    ```
