# Upgrade DCE 5.0 GProduct

GProduct is the collective name for all product modules of DCE 5.0.

This article will introduce how to use dce5-installer to upgrade DCE 5.0 GProduct offline.

## Prerequisites

- You need to have a DCE 5.0 cluster environment, see [Offline Deployment Full Mode](commercial/start-install.md)
- Please make sure your tinder machine is still alive
- Please confirm the version you want to upgrade, see [Version Release Notes](release-notes.md)

## Offline upgrade operation steps

This how-to shows how to upgrade from v0.5.0 to v0.6.0.

### Step 1: Download the v0.6.0 offline package

You can download the latest version at [Download Center](https://docs.daocloud.io/download/dce5/).

| CPU Architecture | Version | Download URL |
| :------- | :----- | :-------------------------------- ------------------------------ |
| AMD64 | v0.6.0 | https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.6.0-amd64.tar |
| ARM64 | v0.6.0 | https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.6.0-arm64.tar |

After downloading, decompress the offline package. Take the AMD64 architecture offline package as an example:

```bash
tar -xvf offline-v0.6.0-amd64.tar
```

### Step 2: Configure the cluster configuration file clusterConfig.yaml

!!! note

     When DCE 5.0 is installed offline, what configuration is used in the cluster configuration file also needs to be consistent during the upgrade.
    
     Since the v0.6.0 version updates the structure of the cluster configuration file, [cluster configuration file description] (commercial/cluster-config.md), it is necessary to ensure that the parameters used in v0.5.0 are consistent, but the structure must be the same as that of v0.6.0 unanimous.
    
     Only the builtin method of imagesAndCharts is currently tested.

The file is in the `offline/sample` directory of the decompressed offline package. The reference configuration file is as follows:

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
     type: builtin # (1)
```

1. official-service(if omit or empty), builtin or external

### Step 3: Configure mainfest.yaml (optional)

The files are in the `offline/sample` directory of the decompressed offline package.

If some product components do not need to be upgraded, you can choose to close them under the corresponding components, and configure as follows, Kpanda will not be upgraded when updating.

```yaml
   kpanda:
     enable: false
     helmVersion: 0.16.0
     variables:
```

!!! note

     Currently only supports the upgrade of product components already installed in the current environment, components that do not exist will skip the upgrade step

### Step 4: Start the upgrade

Execute the upgrade command

```bash
./offline/dce5-installer cluster-create -c sample/clusterconfig.yaml -m sample/manifest.yaml --upgrade 4,5,gproduct
```

Upgrade parameter description:

- `install-app` or `cluster-create`, representing the type of installation mode to install DCE 5.0. If the original environment was installed via `cluster-create`, use this command when upgrading
- `--upgrade` can be abbreviated as `-u`, and execution steps need to be added after the command. At present, if you upgrade GProduct, you need to execute `4,5,gproduct`, and we will optimize it later. After v0.7.0 only need `--upgrade gproduct`

Successful installation results:

![upgrade](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/upgrade.png)
