---
MTPE: WANG0608GitHub
Date: 2024-08-26
---

# Install Container Runtime on Edge Nodes

Before edge nodes connect to the system, it is necessary to configure the node environment,
which includes installing a container runtime. This article describes how to install containerd, a container runtime recommended in kubernetes community.

!!! note

    - If the installed version of KubeEdge is higher than v1.12.0, it is recommended to install containerd.
    - For KubeEdge v1.15.0 and above, please install containerd v1.6.0 or higher.

## Install containerd

To integrate an Edge node requires some CNI plugins, so it is recommended to directly install containerd with CNI plugins. The steps are as follows:

1. Download containerd installation package and upload it to the edge node. See [download link](https://github.com/containerd/containerd/tags)
   and select the appropriate version of the installation package based on the operating system and
   CPU architecture of the edge node.

2. Unpack the installation package to the root directory.

    ```shell
    tar xvzf {installation_package_name} -C /
    ```

3. Generate the containerd configuration file.

    ```shell
    mkdir /etc/containerd
    containerd config default > /etc/containerd/config.toml
    ```

4. Start containerd.

    ```shell
    systemctl start containerd && systemctl enable containerd
    ```

5. Verify whether containerd is successfully installed and running.

    ```shell
    systemctl status containerd
    ```

## Install the nerdctl tool (optional)

It is recommended to install the nerdctl command-line tool for easier container operation
and debugging on the node. The steps are as follows:

1. Download the nerdctl installation package and upload it to the edge node. See [download page](https://github.com/containerd/nerdctl/releases).

    !!! note

        Please select the appropriate installation package based on the operating system and CPU architecture. Install nerdctl v1.7.0 or higher.

2. Unpack the installation package and copy the binary file to the **/usr/local/bin** directory.

    ```shell
    tar -zxvf nerdctl-1.7.6-linux-amd64.tar.gz
    cd nerdctl-1.7.6-linux-amd64
    cp nerdctl /usr/local/bin
    ```

3. Verify that containerd is successfully installed.

    Use the following command to check the nerdctl version. If it is displayed correctly,
    it indicates that nerdctl has been successfully installed.

    ```shell
    nerdctl version
    ```
