# Lightweight Deployment Using the Installer

This document describes how to perform a lightweight deployment of DCE 5.0 using the installer. If you want to understand what specific optimizations and reductions have been made for the lightweight version, please refer to [Lightweight Deployment Optimization Validation](./light-install-solution.md).

## Preparation

### Configuration Preparation

1. Example component configuration file: manifest.yaml

    !!! note

        The specific component versions should match those in the offline package.

    ```yaml title="manifest.yaml"
    apiVersion: manifest.daocloud.io/v1alpha1
    kind: DCEManifest
    metadata:
      creationTimestamp: null
    global:
      helmRepo: https://release.daocloud.io/chartrepo
      imageRepo: release.daocloud.io
    infrastructures:
      istio:
        enable: true
        version: 1.16.1
      mysql:
        kpandaMode: master-slave # mgr|master-slave
        kpandaModeEnable: true
        commonMode: master-slave # mgr|master-slave
        commonModeEnable: true
        version: 8.0.29
        cpuLimit: 1
        memLimit: 2Gi
        enableAutoBackup: true
        pvcSize: 15Gi
        pvcSizeClusterPedia: 25Gi
      redis:
        version: 6.2.6-debian-10-r120
        cpuLimit: 400m
        memLimit: 500Mi
    components:
        kubean:
          enable: true
          helmVersion: v0.18.4
          helmRepo: https://kubean-io.github.io/kubean-helm-chart
          variables:
        ghippo:
          enable: true
          helmVersion: 0.29.0
          variables:
        kpanda:
          enable: true
          helmVersion: 0.31.0
          variables:
        kangaroo:
          enable: true
          helmVersion: 0.20.0
          variables:
        kairship:
          enable: true
          helmVersion: 0.22.0
          variables:
        mcamel-mysql:
          enable: false
          helmVersion: 0.21.0
          variables:
        mcamel-redis:
          enable: false
          helmVersion: 0.21.0
          variables:
        mcamel-minio:
          enable: false
          helmVersion: 0.17.0
          variables:
    ```

2. Example cluster configuration file: ClusterConfig.yaml

    ```yaml title="ClusterConfig.yaml"
    apiVersion: provision.daocloud.io/v1alpha4
    kind: ClusterConfig
    metadata:
      creationTimestamp: null
    spec:
      clusterName: my-cluster
    
    loadBalancer:
      type: NodePort
    
    masterNodes:
      - nodeName: "g-master1"
        ip: 10.7.10.7
        ansibleUser: "root"
        ansiblePass: "dangerous@2022"
    
    ntpServer:
      - 0.pool.ntp.org
      - ntp1.aliyun.com
      - ntp.ntsc.ac.cn
    
    fullPackagePath: "/home/offline"
    osRepos:
      type: builtin
      isoPath: "/home/iso/Kylin-Server-V10-SP3-2403-Release-20240426-arm64.iso"
      osPackagePath: "/home/ospkgs/os-pkgs-kylin-v10sp3-v0.17.5.tar.gz"
    
    imagesAndCharts:
      type: builtin
    
    binaries:
      type: builtin
    ```

### Offline Package Preparation

!!! note

    The installation package must be downloaded in an online environment. Please download it in advance before arriving at the customer site.

1. Download the offline package for the installer

    The installation package version must be **v0.21.0** or higher. It is recommended to download the latest version from the official website.

    | Name | Version | Download | Updated On |
    | ---- | ------- | -------- | ---------- |
    | offline-v0.21.0-arm64.tar | v0.21.0 | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.21.0-arm64.tar) | 2024-11-04 |
    | offline-v0.21.0-amd64.tar | v0.21.0 | [:arrow_down: Download](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.21.0-amd64.tar) | 2024-11-04 |

2. Prepare the jq tool

    | Name | Version | Download | Updated On |
    | ---- | ------- | -------- | ---------- |
    | jq-linux-arm64 | V1.7.1 | [:arrow_down: Download](https://github.com/jqlang/jq/releases/download/jq-1.7.1/jq-linux-arm64) | 2024-11-04 |
    | jq-linux-arm64 | V1.7.1 | [:arrow_down: Download](https://github.com/jqlang/jq/releases/download/jq-1.7.1/jq-linux-amd64) | 2024-11-04 |

### Script Preparation

!!! note

    Please download these scripts in advance before arriving at the customer site.

1. Istio sidecar cleanup script:
   [clean_istio_proxy.sh](https://gitlab.daocloud.cn/bo.jiang/installer-tools/-/blob/master/clean_istio_proxy.sh)

2. Registry deployment script:
   [mv-registry.sh](https://gitlab.daocloud.cn/bo.jiang/installer-tools/-/blob/master/mv-registry.sh)

## Installation Steps

### Install Dependencies

Before starting the installation, make sure all prerequisite dependencies are installed.

```shell
export VERSION=v0.28.0
curl -LO https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite_${VERSION}.sh
curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/prerequisite_${VERSION}_amd64.tar.gz

export BINARY_TAR=prerequisite_${VERSION}_amd64.tar.gz
chmod +x install_prerequisite_${VERSION}.sh
./install_prerequisite_${VERSION}.sh offline full
```

### Start Installation

For detailed installation instructions, please refer to the [Installation Guide](../index.md)

```shell
export INSTALLER_CUSTOM_CPU_THRESHOLD=8
export INSTALLER_CUSTOM_MEM_THRESHOLD=8
export INSTALLER_COMMON_DB_SHARED=1
./dce5-installer cluster-create -d -c clusterConfig.yaml -m manifest.yml -z -j1,2,3,4,5,6,8,10,11,12
```

### Minimal Insight Installation (Optional)

!!! note

    Adding the Insight component requires at least **12 GB of memory**.  
    If resources are limited, it is recommended **not** to install it, as this may affect the overall system stability.

To add the minimal Insight component, follow these steps:

1. Add the following content at the end of the manifest.yaml file

    ```yaml title="manifest.yaml"
    insight:
      enable: true
      helmVersion: 0.30.0-rc2
      variables:
    insight-agent:
      enable: true
      helmVersion: 0.30.0-rc2
    ```

    !!! note

        The specific component versions should match those in the offline package.

2. Run steps 11 and 12 of the installer again

    ```shell
    ./dce5-installer cluster-create -c clusterConfig.yaml -m manifest.yml -z -j11,12
    ```

3. Save the following as insight-server-patch.yaml

    ```yaml title="insight-server-patch.yaml"
    global:
      kafka:
        enabled: false
      tracing:
        enable: false
        aggregator:
          enabled: false
        kafkaReceiver:
          enabled: false
      applyDependenciesCrds: true
      ghippo:
        applyCR: true
      elasticAlert:
        enable: false
    vector:
      enabled: false
    ```

4. Save the following as insight-agent-patch.yaml

    ```yaml title="insight-agent-patch.yaml"
    global:
      exporters:
        trace:
          enable: false
    tailing-sidecar-operator:
      enabled: false
    opentelemetry-kubernetes-collector:
      enabled: false
    fluent-bit:
      enabled: false
    ```

5. Update insight-server and insight-agent

    ```shell
    helm upgrade -n insight-system insight offline/dce5/insight-0.30.0-rc2.tgz --version 0.30.0-rc2 --reuse-values -f insight-server-patch.yml
    helm upgrade -n insight-system insight-agent offline/dce5/insight-agent-0.30.0-rc2.tgz --version 0.30.0-rc2 --reuse-values -f insight-agent-patch.yml
    ```

## Post-Installation Optimization

1. Clean up Istio sidecars

    ```shell
    # jq tool must be installed first
    chmod +x jq-linux-amd64
    mv jq-linux-amd64 /usr/local/bin/jq

    # Execute sidecar cleanup script
    bash clean_istio_proxy.sh
    ```

2. Deploy registry and manage manually

    ```shell
    export REGISTRY_NODEPORT=30143 # Set new registry nodeport
    bash mv-registry.sh clusterConfig.yaml
    ```

    Manual management steps:

    1. **Global Management** -> **Workspaces and Folders** -> **Create Workspace**

    2. Add authorization and set the current logged-in user as the workspace administrator

    3. Select the workspace for the image registry

    4. Repository Integration


3. Update Multi-Cloud Management Configuration

    You need to update the seed image address of the multi-cloud management component to the new registry.

    ```shell
    # Suppose the current node IP is 10.5.14.160
    # and the REGISTRY_NODEPORT environment variable is 30143
    # Then generate a patch configuration for 10.5.14.160:30143
    # * Please replace with actual IP and port values *
    export REGISTRY_ADDR="10.5.14.160:30143"
    cat << EOF >> kairship-patch.yml 
    global:
      imageRegistry: ${REGISTRY_ADDR}/release.daocloud.io
      kairship:
        instanceConfig:
          karmadaRegistry: ${REGISTRY_ADDR}/release.daocloud.io/karmada
          kubeRegistry: ${REGISTRY_ADDR}/release.daocloud.io/karmada
    EOF

    # This assumes:
    # The offline package extraction path is /home/offline/
    # and the kairship version is 0.22.0-rc1
    # * Replace with actual path and version *
    export KAIRSHIP_VERSION="0.22.0-rc1"
    export OFFLINE_RESOURCES_PATH="/home/offline"
    helm upgrade -n kairship-system kairship \
        ${OFFLINE_RESOURCES_PATH}/dce5/kairship-${KAIRSHIP_VERSION}.tgz \
        --reuse-values -f kairship-patch.yml \
        --version ${KAIRSHIP_VERSION}
    ```

4. Shut Down the KIND Seed Cluster

    !!! note

        The seed cluster should only be shut down after all installation operations have been successfully completed.

    ```shell
    tinder_name=$(yq '.spec.tinderKind.instanceName' clusterConfig.yaml)
    [ "$tinder_name" == null ] && tinder_name=my-cluster-installer
    kind delete cluster -n $tinder_name
    ```

That completes the lightweight version installation and deployment.
