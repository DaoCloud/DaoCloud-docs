---
MTPE: windsonsea
Date: 2023-06-29
---

# Installer Release Notes

This page lists the Release Notes of the installer, so that you can understand the evolution path and feature changes of each version.

## 2023-7-31

### v0.10.0

#### Added

- **Added** Support for Oracle Linux R8-U7 operating system
- **Added** Support for flexibly exposing kind container mappings to the host machine's ports
- **Added** import-artifact subcommand supports importing offline resources based on external services defined in clusterConfig.yaml configuration file

#### Improved

- **Improved** For environments deployed using the installer through external OS repo, optimized the ability to select external OS repo when creating a cluster in container management
- **Improved** Refactored and abstracted clusterConfig detection layer
- **Improved** Improved error messages for pre-requisite dependency installation script
- **Improved** Allow installation to continue when ES health status is 'yellow' during minimal installation process
- **Improved** Eliminated redundant image integration steps in import-artifact subcommand
- **Improved** Expanded default expansion of fullPackagePath property in clusterConfig template for offline resource external or built-in scenarios

#### Fixed

- **Fixed** incorrect detection of external image service address
- **Fixed** formatting error in kubeconfig output by spark kind cluster
- **Fixed** issue of multiple version charts appearing due to unpacking different version offline packages to the same directory
- **Fixed** incorrect instruction set architecture information in prerequisite.tgz
- **Fixed** import-artifact exception when -C is not specified
- **Fixed** issue where incorrect exit command caused installer exit prompt message not to be displayed
- **Fixed** certificate authentication failure for kube-controller-manager and kube-scheduler caused by podman base + kind restart
- **Fixed** issue where printing embedded manifest subcommand command indicator would return full mode manifest as long as it is not specified as `install-app`
- **Fixed** command name typo for printing embedded manifest subcommand
- **Fixed** failure to import arm64 package again for existing amd64 resources in import-artifact subcommand

#### Known Issues

- Upgrading is not supported through the install-app subcommand, only create-cluster subcommand is supported.
- After restarting, kubelet service fails to start on Redhat 8.6 operating system with error: `failed to initialize top level QOS containers: root container [kubelet kubepods] doesn't exist`
- When installing a cluster based on TencentOS 3.1, the package manager cannot be correctly identified. If TencentOS 3.1 is needed, please use installer version 0.9.0.

## 2023-6-30

### v0.9.0

#### New Features

- **Added**: The `istio-ingressgateway` now supports high availability mode. When upgrading from v0.8.x or earlier to v0.9.0, the following command must be executed: `./offline/dce5-installer cluster-create -c clusterConfig.yaml -m manifest.yaml --upgrade infrastructure,gproduct`
- **Added**: Support configuring the exposed bootstrapping kind address and port in the clusterConfig.yaml file.
- **Added**: The installer now performs a pre-check on each node to verify if lvm2 is installed when using eyebrow storage.
- **Added**: The installer includes an embedded default upgrade of the k8s version to v1.26.5.
- **Added**: Support specifying the local file mount path for the bootstrapping kind in the clusterConfig.yaml file.
- **Added**: Integrated ISO image file import script into the installer binary.

#### Improvements

- **Improved**: Optimized download scripts.
- **Improved**: Optimized logic and functionality of the `import-artifact` command.
- **Improved**: Made `isoPath` and `osPackagePath` optional fields in clusterConfig.yaml during the upgrade process.
- **Improved**: Enhanced temporary file cleanup mechanism in the installer.
- **Improved**: Enhanced reuse functionality of the bootstrapping node.

#### Fixes

- **Fixed**: Fixed the issue where the ES component could not start in OCP.
- **Fixed**: Fixed the issue where the UI interface was inaccessible after installing DCE in TencentOS.
- **Fixed**: Fixed the high probability of failed database creation for middleware databases in arm64 environments.
- **Fixed**: Fixed shell expansion error in the image upload success check process.

#### Known Issues

- When upgrading from v0.8.x to v0.9.0, the following commands need to be executed for verification:

    - Check if the `istio-ingressgateway` port is `80` or `8080`

        ```bash
        kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].targetPort}'
        ```

    - Check if the `istio-ingressgateway` port is `443` or `8443`

        ```bash
        kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].targetPort}'
        ```
  
    If the output is `80` or `443`, the upgrade command needs to include the `infrastructure` parameter. Example: `./offline/dce5-installer cluster-create -c clusterConfig.yaml -m manifest.yaml --upgrade infrastructure,gproduct`

    If the output is different from the above cases, please follow the upgrade instructions in the document [Upgrade DCE 5.0 Product Modules](upgrade.md).

## 2023-6-15

### v0.8.0

#### Improvements

- **Improved** Upgraded ipavo component to v0.9.3
- **Improved** Upgraded amamba component to v0.17.4
- **Improved** Upgraded hwameistor-operator component to v0.10.4
- **Improved** Upgraded kangaroo component to v0.8.2
- **Improved** Upgraded insight component to v0.17.3

#### Fixes

- **Fixed** the issue of failed image synchronization for Harbor repositories using external HTTP.
- **Fixed** indentation error in `clusterConfig.yaml` configuration file.
- **Fixed** rendering error in localService configuration when using an external yum repo.
- **Fixed** integration issue with external JFrog charts repository.

## 2023-5-31

### v0.8.0

#### New Features

- **Added** Other Linux mode supports the OpenAnolis 8.8 GA operating system
- **Added** Supports the OracleLinux R9 U1 operating system
- **Added** Added node status detection
- **Added** Added file verification for OS PKGs
- **Added** Supports cluster installation on non-22 ports
- **Added** External file service supports k8s binary resources
- **Added** Supports external JFrog image and charts repositories
- **Added** Supports mixed architecture deployment solutions
- **Added** Supports external Redis components

#### Improvements

- **Optimized** Fixed issue of missing images when deploying Nacos instances
- **Optimized** Fixed issue of repeated execution of cluster installation task during cluster module upgrade

#### Known Issues

- Addon offline package does not currently support uploading to external JFrog services
- The container management platform offline mode currently does not support adding nodes to working clusters
- When using an external OS Repo repository in an offline scenario, i.e. defining `osRepos.type=external` in clusterConfig.yaml, after successfully deploying DCE5.0, you cannot create working clusters in the container management. A temporary solution is as follows:
After installing the global cluster, immediately update the configmap kubean-localservice in the kubean-system namespace of the global cluster to replace all double quotes with single quotes in the value of `yumRepos.external`. For example, replace all double quotes in the file with single quotes:

  ```yaml
  yumRepos:
    external: [ "http://10.5.14.100:8081/centos/\$releasever/os/\$basearch","http://10.5.14.100:8081/centos-iso/\$releasever/os/\$basearch" ]
  ```

  with:

  ```yaml
  yumRepos:
    external: [ 'http://10.5.14.100:8081/centos/\$releasever/os/\$basearch','http://10.5.14.100:8081/centos-iso/\$releasever/os/\$basearch' ]
  ```

## 2023-5-30

### v0.7.1

#### Improvements

- **Optimized** Upgrade of monitoring components version

#### Bug Fixes

- **Fixed** Binary output of DCE Community manifest was incorrect

## 2023-4-30

### v0.7.0

#### Features

- **Added** Added support for Other Linux to deploy DCE5.0, [Reference Documentation](os-install/otherlinux.md)
- **Added** Added support for operating system OpenEuler 22.03
- **Added** supports external OS Repos, [refer to cluster configuration file description](commercial/cluster-config.md)
- **Added** supports kernel parameter tuning, [refer to cluster configuration file description](commercial/cluster-config.md)
- **Added** support for detecting whether external ChartMuseum and MinIo services are available

#### Optimization

- **Optimized** Optimized the pre-verification of tar and other commands
- **Optimized** Optimized the command line parameters of the upgrade operation
- **Optimized** closed Kibana's access through NodePort, Insight uses ES's NodePort or VIP access
- **Optimized** Optimized the display of concurrent logs, terminate tasks using SIGTERM signal instead of SIGKILL

#### Fixes

- **Fixed** Fix the problem that the Kcoral helm chart cannot be found during online installation
- **Fixed** Fix KubeConfig can't find problem when upgrading

#### Known Issues

- Online installation of the global cluster will fail, and the following configuration needs to be performed in the `kubeanConfig` block of clusterConfig.yaml:

     ```yaml
     kubeanConfig: |-
       calico_crds_download_url: "https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/calico-crds-v3.25.1.tar.gz"
     ```

     At the same time, creating a working cluster online through container management also has the same problem. You need to add the above configuration in the custom parameters of the advanced configuration on the cluster creation page. The key is `calico_crds_download_url`, and the value is the value of the above calico_crds_download_url

- There is a low probability that Kubean cannot create a spray-job task. Manually delete the corresponding clusteroperations CR resource and run the installation command again
- After deploying DCE5.0 using an external OS Repo, the working cluster cannot be created offline through container management, which can be solved by manually modifying the configmap kubean-localservice of the kubean-system namespace of the global cluster.
   Add the following configuration under `yumRepos`, you need to fill in the external OS Repo address configured in clusterConfig.yaml in external:

     ```yaml
     yumRepos:
       external: []
     ```

     After the modification is complete, select the new configuration for the yum source of the node configuration on the container management creation cluster page

## 2022-4-11

### v0.6.1

#### Optimization

- **Optimized** Upgraded Kpanda to v0.16.1
- **Optimized** Upgraded Skoala to v0.19.4

## 2022-4-06

### v0.6.0

#### Features

- **Added** Added support for one-click upgrade of Gproduct components
- **Added** Adapted operating system: UOS V20 1020a / Ubuntu 20.04
- **Added** Support OCP (OpenShift Container Platform) to install DCE5.0
- **Added** CLI supports generating clusterConfig templates
- **Added** All in one mode starts the minimal installation mode by default
- **Added** Added Kcollie component in Gproduct component
- **Added** Support community version to sync image to external repository

#### Optimization

- **Optimized** Decouple the code for generating offline packages and the code required for the installation process
- **Optimized** Optimize bootstrapping node inotify parameters
- **Optimized** Optimize the full-mode online installation experience
- **Optimized** optimize clusterConfig structure and configuration
- **Optimized** DCE Community allows not to check clusterConfig format and parameters
- **Optimized** Optimize installer execution scheduler log output

#### Fixes

- **Fixed** Removed dependency on wget
- **Fixed** Fix the problem of installation failure after repeated decompression of offline packages
- **Fixed** Fix MinIo non-reentrant issue
- **Fixed** Fix redis pvc that continues to be left behind when middleware Redis CR is removed
- **Fixed** Fix the problem of sequence dependency when Amamba and Amamba-jenkins are installed concurrently
- **Fixed** Fix the problem that the installer command line -j parameter parsing fails

## 2022-2-28

### v0.5.0

#### Features

- **Added** Offline package separation osPackage, needs to define `osPackagePath` in the cluster configuration file
- **Added** Support addon offline, you need to define `addonOfflinePackagePath` in the cluster configuration file
- **Added** Offline installation supports operating systems REHL 8.4, REHL 7.9

#### Optimization

- **Optimized** Upgraded the version of pre-dependent tools

#### Fixes

- **Fixed** installer command line `-j` parameter validity detection problem
- **Fixed** The installation path problem of pre-dependent tools
- **Fixed** the problem that the host list password is invalid for pure numbers
- **Fixed** When the runtime is Docker, the built-in registry image cannot be pulled

#### Known Issues

- The installer installation fails due to the pre-installed runc on REHL8 with non-minimal installation. Temporary solution: run `rpm -qa | grep runc && yum remove -y runc` on each of the above nodes before installation
- Illegal kernel parameter settings on REHL8 with non-minimal installation, temporary solution; run on each of the above nodes before installation
   `eval $(grep -i 'vm.maxmapcount' /etc/sysctl.conf -r /etc/sysctl.d | xargs -L1 | awk -F ':' '{printf("sed -i -r \"s /(%s)/#\\1/\" %s; ", $2, $1)}') && sysctl --system`
- There are potential risks in the concurrent installation of helm, and the installation cannot continue after failure

## 2022-12-30

### v0.4.0

#### Features

- **Added** The syntax of clusterConfig has been upgraded from v1alpha1 to v1alpha2, the syntax has incompatible changes, you can check the documentation
- **Added** No longer install permanent Harbor and permanent MinIO on the global service cluster
- **Added** bootstrapping nodes need to exist permanently, users install minio, chart museum, registry
- **Added** Added installation of contour as default ingress-controller for commercial version
- **Added** New installation of cert-manager in commercial version
- **Added** Support cluster deployment in private key mode
- **Added** supports external container registry for deployment

#### Optimized

- **Optimized** The offline package no longer includes the ISO of the operating system, which needs to be downloaded separately. In the case of pure offline, the absolute path of the ISO needs to be defined in the clusterConfig file
- **Optimized** Commercial version uses Contour as default ingress-controller
- **Optimized** MinIO supports using VIP
- **Optimized** coredns automatically inject registry VIP analysis
- **Optimized** Optimize the offline package production process and speed up the packaging of Docker images
- **Optimized** Optimized the offline package size
- **Optimized** infrastructure support 1.25: upgrade redis-operator, eck-operator, hwameiStor
- **optimized** upgrade to keycloakX
- **Optimized** istio version upgrade v1.16.1

#### Known Issues

- The default installation mode does not support unpartitioned SSD disks. If you want to support it, you need to manually intervene.
- Pure offline environment, no app store by default. Please manually connect the chart-museum of the bootstrapping node to the global cluster, registry address: http://{Tinder IP}:8081, username rootuser, password rootpass123
- There is a known problem in the metallb community. There is a dadfailed IPV6 loopback address in the main network card, and metallb cannot work. Before installing, you need to ensure that the main network card is not dadfailed
- If the machine is too stuck during the startup of insight-api-server, the initialization (migrate) of the database cannot be completed during the Liveness health check cycle, resulting in the need for manual intervention
- The iso path in the clusterConfig configuration file must be an absolute path, relative paths are not supported
- The default k8s version of kubean and the offline package are still limited to k8s 1.24 version, which has not been updated to 1.25 (PG does not support it yet)
- If the external-Registry is Harbor, the Project will not be automatically created for the time being, and it needs to be created manually in advance
- When Docker is running, the built-in registry cannot be pulled, it will be fixed in the next version
- After disabling IPV6, podman cannot start the kind cluster of bootstrapping nodes

## 2022-11-30

### v0.3.29

#### Features

- **Added** ARM64 support: build arm64 offline packages.
- **Added** Added support for kylin v10 sp2 offline package.
- **Added** Infrastructure Support 1.25: Upgrade redis-operator, eck-operator, hwameiStor and other components.
- **Added** Added support for cluster deployment in private key mode.
- **Added** The workload is elastically scaled based on custom metrics, which is closer to the user's actual business elastic expansion and contraction needs.

#### Optimized

- **Optimized** Create permanent harbor with operator, enable HTTPS, and use Postgressql operator.
- **Optimized** Commercial version uses contour as default ingress-controller.
- **Optimized** MinIO supports using VIP.
- **Optimized** coredns is automatically injected into registry VIP resolution.
- **Optimized** Optimize the offline package production process and speed up the packaging of docker images.

#### Fixes

- **Fixed** issues with fair cloud service.
- **Fixed** issues with image and helm for various submodules.
- **Fixed** Bug fixes for offline package loading.

#### Known issues

- Because some operators need to be upgraded to support 1.25, DCE5 does not support 1.20 downwards.
- The default k8s version of kubean and the offline package are still limited to k8s 1.24 version, which has not been updated to 1.25 (postgres-operator is not supported yet).
- In the case of Image Load, the istio-ingressgateway imagePullPolicy is always.
- For the ARM version, step 16 (harbor) cannot be performed, because harbor does not support ARM for the time being. The mainfest.yaml file needs to be modified, the postgressql operator is fasle, and -j 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 should be added when executing the installation command