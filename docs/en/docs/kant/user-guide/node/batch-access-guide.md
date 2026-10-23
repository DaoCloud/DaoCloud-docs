# Batch Onboard Edge Nodes

This document describes how to onboard multiple edge nodes into the system by using a batch task. With the batch onboarding feature, you can:

- Onboard nodes in batches, significantly improving operation and maintenance efficiency
- Reduce operation and maintenance costs and simplify the operation process

## Prerequisites

Before you start to onboard edge nodes in batches, make sure that:

- A control node has been prepared, and this node needs to be able to access all edge nodes to be onboarded.
- The Cloud Edge Collaboration module has been upgraded to v0.20.0 or a later version.

## About the keadm Initialization Script

To simplify the initialization of the keadm tool, we provide a handy initialization script named `keadm_init.sh`. You can go to the [Download Center](https://docs.daocloud.io/en/download/modules/kant) to download the script file.

The script supports the following two important parameters:

- `MULTI_ARCH`: controls whether nodes with multiple architectures can be onboarded
    - `false`: only nodes with the same architecture as the control node can be onboarded
    - `true`: nodes with both the amd64 and arm64 architectures can be onboarded
- `WITH_CONTAINERD`: controls whether containerd is installed automatically
    - `false`: do not install containerd automatically
    - `true`: install the default version of containerd on the node automatically

## Steps to Onboard Nodes in Batches

### Online Mode

1. Create a working directory.

    ```bash
    mkdir keadm-join-node && cd keadm-join-node
    ```

2. Run the keadm initialization script.

    ```bash
    # Set the MULTI_ARCH and WITH_CONTAINERD parameters according to your actual needs
    curl -sfL https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/keadm_init.sh | sudo MULTI_ARCH=false WITH_CONTAINERD=false bash -s --
    ```

3. Prepare the batch configuration file and place it in the working directory.

    ```yaml
    # batch_join_config.yaml
    # Please modify the parameter values in <xxx> according to your actual situation
    # Note: if WITH_CONTAINERD=true in the keadm initialization script, keep the --pre-run=./containerd.sh parameter; otherwise, remove it
    keadm:
      download:
        enable: false
      keadmVersion: v1.20.0
      archGroup:
        - amd64
      offlinePackageDir: .
      cmdTplArgs:
        cmd: join <--pre-run=./containerd.sh> --cgroupdriver=cgroupfs --cloudcore-ipport=<master-ip>:30000 --hub-protocol=websocket --certport=30002 --image-repository=docker.m.daocloud.io/kubeedge --kubeedge-version=v1.17.0 --set modules.edgeHub.quic.server=<master-ip>:30001,modules.edgeStream.server=<master-ip>:30004,modules.edgeHub.websocket.server=<master-ip>:30000,modules.edgeStream.enable=true
        token: <token>
      nodes:
        - nodeName: ubuntu1
          copyFrom: ./manifests
          keadmCmd: '{{.cmd}} --edgenode-name=<edge-node-name1> --token={{.token}}'
          ssh:
            ip: <node-ip>
            username: root   # Log in as the root user
            auth:
              type: password
              passwordAuth:
                password: <****>
        - nodeName: ubuntu2
          copyFrom: ./manifests
          keadmCmd: '{{.cmd}} --edgenode-name=<edge-node-name2> --token={{.token}}'
          ssh:
            ip: <node-ip>
            username: root     # Log in as the root user
            auth:
              type: password
              passwordAuth:
                password: <****>
      maxRunNum: 5
    ```

4. Use keadm to onboard nodes in batches.

    ```bash
    # Run the following command in the working directory
    keadm batch --config=./batch-join-config.yaml
    ```

### Offline Mode

1. Create a working directory.

    ```bash
    mkdir keadm-join-node && cd keadm-join-node
    ```

2. Prepare the offline installation package and the initialization script.

    Prepare the corresponding installation package and initialization script file according to your installation scenario:

    ```bash
    # Single architecture without containerd
    ├── keadm-join-node
        └── keadm_{arch}.tar.gz
        └── keadm_init.sh

    # Single architecture with containerd
    ├── keadm-join-node
        └── keadm-containerd-{arch}.tar.gz
        └── keadm_init.sh

    # Multiple architectures without containerd
    ├── keadm-join-node
        └── keadm_amd64.tar.gz
        └── keadm_arm64.tar.gz
        └── keadm_init.sh

    # Multiple architectures with containerd
    ├── keadm-join-node
        └── keadm-containerd-amd64.tar.gz
        └── keadm-containerd-arm64.tar.gz
        └── keadm_init.sh
    ```

3. Run the initialization script.

    ```bash
    # Set the MULTI_ARCH and WITH_CONTAINERD parameters according to your actual needs
    sudo MULTI_ARCH=false WITH_CONTAINERD=false bash -c keadm_init.sh
    ```

4. Prepare the configuration file.

    Refer to the configuration description for the online mode to create the `batch-join-config.yaml` file. Make sure the directory structure is as follows:

    ```bash
    # Take the single-architecture mode without containerd as an example
    ├── keadm-join-node
        └── keadm_{arch}.tar.gz
        └── {arch}
            └── keadm-{version}-linux-{arch}.tar.gz
        └── keadm_init.sh
        └── batch-join-config.yaml
    ```

5. Run the batch onboarding command.

    ```bash
    # Run the following command in the working directory
    keadm batch --config=./batch-join-config.yaml
    ```
