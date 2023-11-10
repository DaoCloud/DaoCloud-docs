# Upgrading DCE 5.0 Modules

The upgrade of DCE 5.0 modules involves upgrading the product functionality modules and the infrastructure modules of DCE 5.0.

DCE 5.0 consists of several sub-modules, including container management, global management, insight, and more.
These are primarily defined in the `components` section of the [manifest.yaml](commercial/manifest.md) file.

The components specific to the infrastructure modules of DCE 5.0 are defined in the `infrastructures` section of the [manifest.yaml](commercial/manifest.md) file.

## Prerequisites

- You need to have a DCE 5.0 cluster environment. Refer to [Offline Deployment of DCE 5.0 Enterprise](commercial/start-install.md).
- Ensure that your ignition machine is still alive.
- Confirm the version you want to upgrade to. See [Release Notes](release-notes.md).

## Offline Upgrade Steps

This demonstration shows how to upgrade from v0.8.0 to v0.9.0. Currently, when upgrading from a lower version
to v0.9.0, it is necessary to upgrade both the product functionality modules and the infrastructure modules
of DCE 5.0 in order to make use of the high availability feature of the `istio-gateway` component.

### Step 1: Download the v0.9.0 Offline Package

You can download the latest version from the [Download Center](../download/index.md).

| CPU Architecture | Version | Download Link                                                 |
| :--------------- | :------ | :----------------------------------------------------------- |
| AMD64            | v0.9.0  | [Download Link](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.9.0-amd64.tar) |
| ARM64            | v0.9.0  | [Download Link](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.9.0-arm64.tar) |

After downloading, extract the offline package. For example, for the AMD64 architecture:

```bash
tar -xvf offline-v0.9.0-amd64.tar
```

### Step 2: Configure the Cluster Configuration File clusterConfig.yaml

!!! note

- Make sure that the [cluster configuration file](commercial/cluster-config.md) is consistent with the parameters used during installation.
- Currently, only the `builtin` method of `imagesAndCharts` has been tested.

The file is located under the `offline/sample` directory after extracting the offline package. Refer to the following sample configuration:

```yaml
apiVersion: provision.daocloud.io/v1alpha3
kind: ClusterConfig
metadata:
spec:
  clusterName: my-cluster
  loadBalancer:
    type: metallb 
    istioGatewayVip: 172.30.**.**/32 
    insightVip: 172.30.**.**/32      
  masterNodes:
    - nodeName: "g-master1" 
      ip: 172.30.**.**
      ansibleUser: "root"
      ansiblePass: "*****"
  workerNodes:
    - nodeName: "g-worker1"
      ip: 172.30.**.**
      ansibleUser: "root"
      ansiblePass: "*****"
    - nodeName: "g-worker2"
      ip: 172.30.**.**
      ansibleUser: "root"
      ansiblePass: "*****"
 
  fullPackagePath: "/home/installer/offline"
  osRepos:
    type: builtin
    isoPath: "/home/installer/CentOS-7-x86_64-DVD-2207-02.iso"
    osPackagePath: "/home/installer/os-pkgs-centos7-v0.4.4.tar.gz"
  imagesAndCharts:
    type: builtin
 
  addonPackage:
  binaries:
    type: builtin  # (1)
```

1. `official-service` (if omitted or empty), `builtin`, or `external`

### Step 3: Configure mainfest.yaml (Optional)

The file is located under the `offline/sample` directory after extracting the offline package.

#### Configuration of DCE 5.0 Product Functionality Modules

The components specific to the product functionality modules of DCE 5.0 are defined in the `components` section
of the [manifest.yaml](commercial/manifest.md) file. If you don't want to upgrade certain product components,
you can disable them. For example, if you want to skip the upgrade for Kpanda (container management),
use the following configuration:

```yaml
  components:
    kpanda:
      enable: false
      helmVersion: 0.16.0
      variables:
```

#### Configuration of DCE 5.0 Infrastructure Modules

The components specific to the infrastructure modules of DCE 5.0 are defined in the `infrastructures` section
of the [manifest.yaml](commercial/manifest.md) file. For example, the following configuration is for the
`hwameiStor` component in the infrastructure module:

```yaml
  infrastructures:
    hwameiStor:
      enable: true
      version: v0.10.4
      policy: drbd-disabled
```

!!! note

    Currently, only the upgrade of product components that are already installed in the current environment
    is supported. Non-existent components will be skipped during the upgrade process.

### Step 4: Start the Upgrade

#### Upgrade of DCE 5.0 Product Functionality Modules

Run the upgrade command:

```bash
./offline/dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/sample/manifest.yaml --upgrade gproduct
```

#### Upgrade of DCE 5.0 Infrastructure Modules

Run the upgrade command:

```bash
./offline/dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/sample/manifest.yaml --upgrade infrastructure
```

Explanation of upgrade parameters:

- `install-app` or `cluster-create`: Represents the installation mode type of DCE 5.0. If the initial environment was installed using `cluster-create`, use this command for the upgrade as well.
- `--upgrade`, can be abbreviated as `-u`: Currently supports upgrading DCE 5.0 product functionality modules (`gproduct`) and infrastructure modules (`infrastructures`).
- To upgrade both the product functionality modules and the infrastructure modules together, specify the parameter `--upgrade infrastructures,gproduct`.
- The installer v0.12.0 introduces support for the `--multi-arch` parameter.
  This parameter is mainly used when there are multiple architecture images in the current environment.
  By adding this parameter during the upgrade process, it prevents overwriting of existing multi-architecture images.

### Step 5: Successful Installation Message

![upgrade](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/upgrade.png)
