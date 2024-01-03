---
MTPE: windsonsea
Date: 2023-12-08
---

# Installer Release Notes

This page lists the Release Notes of the installer, so that you can understand the evolution path and feature changes of each version.

## 2023-12-31

### v0.14.0

#### Improvements

- __Improved__ The installer supports merging images for multiple architectures by calling the upstream function of `kubean`.
- __Improved__ Enable the `localArtifactSet` configuration only in offline mode.
- __Improved__ Add compatibility support for older versions of Kubernetes in the `kubean` component.
- __Improved__ Remove the seed node check in the Community Edition.
- __Improved__ Use `LocalArtifactSet` only in offline scenarios.

#### Bug Fixes

- __Bug Fix__ Fix the issue of pod restart on the seed node in the OpenEuler 22.03 environment.
- __Bug Fix__ Update the version of the operator component when upgrading `kubean`.

## 2023-11-30

### v0.13.0

#### New Features

- __Added__ Support separate deployment of etcd nodes.
- __Added__ Support external Kafka component.

#### Enhancements

- __Improved__ Set the certificate validity period of the built-in image repository in the seed machine to 10 years.
- __Improved__ Update versions of prerequisite software.

#### Bug Fixes

- __Bug Fix__ Fix the infinite loop issue in the chart values parsing framework caused by line breaks.
- __Bug Fix__ Fix the incorrect handling of the Internal Field Separator (IFS) in the concurrent scheduling framework.

#### Known Issues

- IPv6 must be enabled in the seed node when using Podman.
- Global clusters may encounter `etcd NOSPACE` warning risks.

## 2023-10-31

### v0.12.0

#### Added

- __Added__ download offline package breakpoint resume feature.
- __Added__ Installer now checks if lvm2 is installed on each host node when enabling Brow Storage component.
- __Added__ Default Kubernetes version in the installer upgraded to `1.27.5`.

#### Optimized

- __Optimized__ Removed CPU/Memory resource request and limit for Global Management, Container Management, and Observability components in community edition minimal installation with `-z` flag.
- __Optimized__ Improved error handling for installer's `-m` parameter, now it throws an error and exits installation when manifest file is not specified for `-m`.
- __Optimized__ Enhanced logging display for upgrade functionality.
- __Optimized__ Adapted containerd-related parameters from kubean.
- __Optimized__ Repackaged GProduct component and uploaded it to ChartMuseum on Sparkle nodes.
- __Optimized__ Improved log output when uploading addon fails.
- __Optimized__ Adapted helm installation parameters for reusing during GProduct component upgrade.
- __Optimized__ Adjusted maximum pod count per node to 180 for Global cluster.
- __Optimized__ Improved excessive logging during migration of charts.

#### Fixed

- __Fixed__ privilege issue with cache files when installing with non-root user.
- __Fixed__ error during migration of data from Sparkle nodes to Global cluster during installation.
- __Fixed__ possible failure during addon upload.
- __Fixed__ Addressed potential "helm operation in progress" issue in the code.
- __Fixed__ support for external redis with password in sentry mode for Kpanda component.
- __Fixed__ failure to deploy Global cluster with docker runtime.
- __Fixed__ redirection issue in LB mode for Ghippo.
- __Fixed__ missing metric indicators when starting MinIo component.

#### Known Issues

- Podman in Sparkle nodes requires IPv6 to be enabled.
- Global cluster may encounter `etcd NOSPACE` warning risk.

## 2023-8-31

### v0.11.0

#### New Features

- __Added__ Update the k8s version of Global clusters to v1.26.7 to avoid security vulnerabilities in older versions
- __Added__ Support for setting ansible extension parameters in clusterConfig.yaml
- __Added__ Support for adding certificate renewal configuration in clusterConfig.yaml, including periodic and one-time updates
- __Added__ Support for offline deployment of Red Hat 9.2 systems
- __Added__ Diagnostic script diag.sh for Global cluster in the offline package
- __Added__ Added `--multi-arch` flag to avoid upgrading issues with overriding multi-architecture images

#### Improvements

- __Improved__ Optimized installer source code structure modules

#### Bug Fixes

- __Fixed__ issue where redis sentinel mode does not support sentinel instance password
- __Fixed__ failure when adding TencentOS 3.1 system nodes to the working cluster

## 2023-7-31

### v0.10.0

#### Added

- __Added__ Support for Oracle Linux R8-U7 operating system
- __Added__ Support for flexibly exposing kind container mappings to the host machine's ports
- __Added__ import-artifact subcommand supports importing offline resources based on external services defined in clusterConfig.yaml configuration file

#### Improved

- __Improved__ For environments deployed using the installer through external OS repo, optimized the ability to select external OS repo when creating a cluster in container management
- __Improved__ Refactored and abstracted clusterConfig detection layer
- __Improved__ Improved error messages for pre-requisite dependency installation script
- __Improved__ Allow installation to continue when ES health status is 'yellow' during minimal installation process
- __Improved__ Eliminated redundant image integration steps in import-artifact subcommand
- __Improved__ Expanded default expansion of fullPackagePath property in clusterConfig template for offline resource external or built-in scenarios

#### Fixed

- __Fixed__ incorrect detection of external image service address
- __Fixed__ formatting error in kubeconfig output by spark kind cluster
- __Fixed__ issue of multiple version charts appearing due to unpacking different version offline packages to the same directory
- __Fixed__ incorrect instruction set architecture information in prerequisite.tgz
- __Fixed__ import-artifact exception when -C is not specified
- __Fixed__ issue where incorrect exit command caused installer exit prompt message not to be displayed
- __Fixed__ certificate authentication failure for kube-controller-manager and kube-scheduler caused by podman base + kind restart
- __Fixed__ issue where printing embedded manifest subcommand command indicator would return full mode manifest as long as it is not specified as `install-app`
- __Fixed__ command name typo for printing embedded manifest subcommand
- __Fixed__ failure to import arm64 package again for existing amd64 resources in import-artifact subcommand

#### Known Issues

- Upgrading is not supported through the install-app subcommand, only create-cluster subcommand is supported.
- After restarting, kubelet service fails to start on Redhat 8.6 operating system with error: `failed to initialize top level QOS containers: root container [kubelet kubepods] doesn't exist`
- When installing a cluster based on TencentOS 3.1, the package manager cannot be correctly identified. If TencentOS 3.1 is needed, please use installer version 0.9.0.

## 2023-6-30

### v0.9.0

#### New Features

- __Added__: The `istio-ingressgateway` now supports high availability mode. When upgrading from v0.8.x or earlier to v0.9.0, the following command must be executed: `./offline/dce5-installer cluster-create -c clusterConfig.yaml -m manifest.yaml --upgrade infrastructure,gproduct`
- __Added__: Support configuring the exposed bootstrapping kind address and port in the clusterConfig.yaml file.
- __Added__: The installer now performs a pre-check on each node to verify if lvm2 is installed when using eyebrow storage.
- __Added__: The installer includes an embedded default upgrade of the k8s version to v1.26.5.
- __Added__: Support specifying the local file mount path for the bootstrapping kind in the clusterConfig.yaml file.
- __Added__: Integrated ISO image file import script into the installer binary.

#### Improvements

- __Improved__: Optimized download scripts.
- __Improved__: Optimized logic and functionality of the `import-artifact` command.
- __Improved__: Made `isoPath` and `osPackagePath` optional fields in clusterConfig.yaml during the upgrade process.
- __Improved__: Enhanced temporary file cleanup mechanism in the installer.
- __Improved__: Enhanced reuse functionality of the bootstrapping node.

#### Fixes

- __Fixed__: Fixed the issue where the ES component could not start in OCP.
- __Fixed__: Fixed the issue where the UI interface was inaccessible after installing DCE in TencentOS.
- __Fixed__: Fixed the high probability of failed database creation for middleware databases in arm64 environments.
- __Fixed__: Fixed shell expansion error in the image upload success check process.

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

- __Improved__ Upgraded ipavo component to v0.9.3
- __Improved__ Upgraded amamba component to v0.17.4
- __Improved__ Upgraded hwameistor-operator component to v0.10.4
- __Improved__ Upgraded kangaroo component to v0.8.2
- __Improved__ Upgraded insight component to v0.17.3

#### Fixes

- __Fixed__ the issue of failed image synchronization for Harbor repositories using external HTTP.
- __Fixed__ indentation error in `clusterConfig.yaml` configuration file.
- __Fixed__ rendering error in localService configuration when using an external yum repo.
- __Fixed__ integration issue with external JFrog charts repository.

## 2023-5-31

### v0.8.0

#### New Features

- __Added__ Other Linux mode supports the OpenAnolis 8.8 GA operating system
- __Added__ Supports the OracleLinux R9 U1 operating system
- __Added__ Added node status detection
- __Added__ Added file verification for OS PKGs
- __Added__ Supports cluster installation on non-22 ports
- __Added__ External file service supports k8s binary resources
- __Added__ Supports external JFrog image and charts repositories
- __Added__ Supports mixed architecture deployment solutions
- __Added__ Supports external Redis components

#### Improvements

- __Optimized__ Fixed issue of missing images when deploying Nacos instances
- __Optimized__ Fixed issue of repeated execution of cluster installation task during cluster module upgrade

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

- __Optimized__ Upgrade of monitoring components version

#### Bug Fixes

- __Fixed__ Binary output of DCE Community manifest was incorrect

## 2023-4-30

### v0.7.0

#### Features

- __Added__ Added support for Other Linux to deploy DCE5.0, [Reference Documentation](os-install/otherlinux.md)
- __Added__ Added support for operating system OpenEuler 22.03
- __Added__ supports external OS Repos, [refer to cluster configuration file description](commercial/cluster-config.md)
- __Added__ supports kernel parameter tuning, [refer to cluster configuration file description](commercial/cluster-config.md)
- __Added__ support for detecting whether external ChartMuseum and MinIo services are available

#### Optimization

- __Optimized__ Optimized the pre-verification of tar and other commands
- __Optimized__ Optimized the command line parameters of the upgrade operation
- __Optimized__ closed Kibana's access through NodePort, Insight uses ES's NodePort or VIP access
- __Optimized__ Optimized the display of concurrent logs, terminate tasks using SIGTERM signal instead of SIGKILL

#### Fixes

- __Fixed__ Fix the problem that the Kcoral helm chart cannot be found during online installation
- __Fixed__ Fix KubeConfig can't find problem when upgrading

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

- __Optimized__ Upgraded Kpanda to v0.16.1
- __Optimized__ Upgraded Skoala to v0.19.4

## 2022-4-06

### v0.6.0

#### Features

- __Added__ Added support for one-click upgrade of Gproduct components
- __Added__ Adapted operating system: UOS V20 1020a / Ubuntu 20.04
- __Added__ Support OCP (OpenShift Container Platform) to install DCE5.0
- __Added__ CLI supports generating clusterConfig templates
- __Added__ All in one mode starts the minimal installation mode by default
- __Added__ Added Kcollie component in Gproduct component
- __Added__ Support community version to sync image to external repository

#### Optimization

- __Optimized__ Decouple the code for generating offline packages and the code required for the installation process
- __Optimized__ Optimize bootstrapping node inotify parameters
- __Optimized__ Optimize the full-mode online installation experience
- __Optimized__ optimize clusterConfig structure and configuration
- __Optimized__ DCE Community allows not to check clusterConfig format and parameters
- __Optimized__ Optimize installer execution scheduler log output

#### Fixes

- __Fixed__ Removed dependency on wget
- __Fixed__ Fix the problem of installation failure after repeated decompression of offline packages
- __Fixed__ Fix MinIo non-reentrant issue
- __Fixed__ Fix redis pvc that continues to be left behind when middleware Redis CR is removed
- __Fixed__ Fix the problem of sequence dependency when Amamba and Amamba-jenkins are installed concurrently
- __Fixed__ Fix the problem that the installer command line -j parameter parsing fails

## 2022-2-28

### v0.5.0

#### Features

- __Added__ Offline package separation osPackage, needs to define `osPackagePath` in the cluster configuration file
- __Added__ Support addon offline, you need to define `addonOfflinePackagePath` in the cluster configuration file
- __Added__ Offline installation supports operating systems REHL 8.4, REHL 7.9

#### Optimization

- __Optimized__ Upgraded the version of pre-dependent tools

#### Fixes

- __Fixed__ installer command line `-j` parameter validity detection problem
- __Fixed__ The installation path problem of pre-dependent tools
- __Fixed__ the problem that the host list password is invalid for pure numbers
- __Fixed__ When the runtime is Docker, the built-in registry image cannot be pulled

#### Known Issues

- The installer installation fails due to the pre-installed runc on REHL8 with non-minimal installation. Temporary solution: run `rpm -qa | grep runc && yum remove -y runc` on each of the above nodes before installation
- Illegal kernel parameter settings on REHL8 with non-minimal installation, temporary solution; run on each of the above nodes before installation
   `eval $(grep -i 'vm.maxmapcount' /etc/sysctl.conf -r /etc/sysctl.d | xargs -L1 | awk -F ':' '{printf("sed -i -r \"s /(%s)/#\\1/\" %s; ", $2, $1)}') && sysctl --system`
- There are potential risks in the concurrent installation of helm, and the installation cannot continue after failure

## 2022-12-30

### v0.4.0

#### Features

- __Added__ The syntax of clusterConfig has been upgraded from v1alpha1 to v1alpha2, the syntax has incompatible changes, you can check the documentation
- __Added__ No longer install permanent Harbor and permanent MinIO on the global service cluster
- __Added__ bootstrapping nodes need to exist permanently, users install minio, chart museum, registry
- __Added__ Added installation of contour as default ingress-controller for commercial version
- __Added__ New installation of cert-manager in commercial version
- __Added__ Support cluster deployment in private key mode
- __Added__ supports external container registry for deployment

#### Optimized

- __Optimized__ The offline package no longer includes the ISO of the operating system, which needs to be downloaded separately. In the case of pure offline, the absolute path of the ISO needs to be defined in the clusterConfig file
- __Optimized__ Commercial version uses Contour as default ingress-controller
- __Optimized__ MinIO supports using VIP
- __Optimized__ coredns automatically inject registry VIP analysis
- __Optimized__ Optimize the offline package production process and speed up the packaging of Docker images
- __Optimized__ Optimized the offline package size
- __Optimized__ infrastructure support 1.25: upgrade redis-operator, eck-operator, hwameiStor
- __optimized__ upgrade to keycloakX
- __Optimized__ istio version upgrade v1.16.1

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

- __Added__ ARM64 support: build arm64 offline packages.
- __Added__ Added support for kylin v10 sp2 offline package.
- __Added__ Infrastructure Support 1.25: Upgrade redis-operator, eck-operator, hwameiStor and other components.
- __Added__ Added support for cluster deployment in private key mode.
- __Added__ The workload is elastically scaled based on custom metrics, which is closer to the user's actual business elastic expansion and contraction needs.

#### Optimized

- __Optimized__ Create permanent harbor with operator, enable HTTPS, and use Postgressql operator.
- __Optimized__ Commercial version uses contour as default ingress-controller.
- __Optimized__ MinIO supports using VIP.
- __Optimized__ coredns is automatically injected into registry VIP resolution.
- __Optimized__ Optimize the offline package production process and speed up the packaging of docker images.

#### Fixes

- __Fixed__ issues with fair cloud service.
- __Fixed__ issues with image and helm for various submodules.
- __Fixed__ Bug fixes for offline package loading.

#### Known issues

- Because some operators need to be upgraded to support 1.25, DCE 5.0 does not support 1.20 downwards.
- The default k8s version of kubean and the offline package are still limited to k8s 1.24 version, which has not been updated to 1.25 (postgres-operator is not supported yet).
- In the case of Image Load, the istio-ingressgateway imagePullPolicy is always.
- For the ARM version, step 16 (harbor) cannot be performed, because harbor does not support ARM for the time being. The mainfest.yaml file needs to be modified, the postgressql operator is fasle, and -j 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 should be added when executing the installation command
