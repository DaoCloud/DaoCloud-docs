---
MTPE: windsonsea
Date: 2024-03-17
---

# Installer Release Notes

This page lists the Release Notes of the installer, so that you can understand
the evolution path and feature changes of each version.

*[Amamba]: Dev codename for Workbench in DCE 5.0
*[Ghippo]: Dev codename for Global Management in DCE 5.0
*[insight-agent]: Essential component that implements observability capabilities in DCE 5.0. It is installed by default in the insight-system namespace.
*[Kangaroo]: Dev codename for the Container Registry in DCE 5.0
*[Kpanda]: Dev codename for Container Management in DCE 5.0
*[Skoala]: Dev codename for Microservice Engine in DCE 5.0

## 2024-03-31

### v0.16.0

#### Improvements

- **Improved** Support for deploying on Rocky Linux 9.2 x86 with containerd
- **Improved** Optimized maximum number of user instances for Rocky Linux
- **Improved** Simplified extension usage of custom actions on the installer side
- **Improved** Added manual trimming tool script for offline package
- **Improved** persistence and reloadability of Firestarter data
- **Improved** Allow skipping Docker runtime installation when deploying clusters
- **Improved** Allow specifying configuration for Firestarter apiserver port

#### Bug Fixes

- **Fixed** issue where OCI_PATH was not effective when importing heterogeneous images
- **Fixed** manifest disorder issue with kubean custom actions
- **Fixed** issue where the timezone of the Firestarter cluster was inconsistent with the host machine

## 2024-03-01

### v0.15.2

#### Fixes

- **Fixed** CVE-2024-21626 security vulnerability by upgrading containerd to v1.7.13 and runc to v1.1.12

#### Notes

1. After upgrading to v0.15.2, the supported cluster have been updated from v1.26.0 ~ v1.29.0 to v1.27.0 ~ v0.29.1.
   If the lifecycle management does not support the cluster version range, please refer to
   [Deploying and Upgrading Downward Compatible Versions in Offline Scenarios with Kubean](./best-practices/cve-20240-21626.md)
2. For more information, refer to [Fix CVE-2024-21626 Vulnerability](./best-practices/cve-20240-21626.md)

## 2024-02-26

### v0.15.1

#### Improvements

- **Improved** support for Rocky Linux 9.2

## 2024-01-31

### v0.15.0

#### Improvements

- **Improved** the stability of installing mysql-operator
- **Improved** the process of stopping middleware components' PDB during cluster upgrade
- **Improved** the process of stopping istiod's PDB during cluster upgrade
- **Improved** the process of skipping the push of iso and ospkg during gproduct upgrade
- **Improved** the version of chart-sycner used when importing addon packages with the installer dependencies
- **Improved** Reduce invalid logs generated during the process of merging chart values during upgrades

#### Bug Fixes

- **Fixed** the incorrect rule for extracting external database password when installing container management components
- **Fixed** an issue of ineffective anti-affinity settings for kafak/zookeeper pods
- **Fixed** an issue of ineffective upgrade for some components and eliminate all images generated during the process of merging chart values during upgrades

## 2023-12-31

### v0.14.0

#### Improvements

- **Improved** The installer supports merging images for multiple architectures by calling the upstream function of `kubean`.
- **Improved** Enable the `localArtifactSet` configuration only in offline mode.
- **Improved** Add compatibility support for older versions of Kubernetes in the `kubean` component.
- **Improved** Remove the bootstrap node check in the Community Edition.
- **Improved** Use `LocalArtifactSet` only in offline scenarios.

#### Bug Fixes

- **Fixed** an issue of pod restart on the bootstrap node in the OpenEuler 22.03 environment.
- **Bug Fix** Update the version of the operator component when upgrading `kubean`.

## 2023-11-30

### v0.13.0

#### New Features

- **Added** Support separate deployment of etcd nodes.
- **Added** Support external Kafka component.

#### Enhancements

- **Improved** Set the certificate validity period of the built-in Container Registry in the bootstrap machine to 10 years.
- **Improved** Update versions of prerequisite software.

#### Bug Fixes

- **Fixed** the infinite loop issue in the chart values parsing framework caused by line breaks.
- **Fixed** the incorrect handling of the Internal Field Separator (IFS) in the concurrent scheduling framework.

#### Known Issues

- IPv6 must be enabled in the bootstrap node when using Podman.
- Global clusters may encounter `etcd NOSPACE` warning risks.

## 2023-10-31

### v0.12.0

#### Added

- **Added** download offline package breakpoint resume feature.
- **Added** Installer now checks if lvm2 is installed on each host node when enabling Brow Storage component.
- **Added** Default Kubernetes version in the installer upgraded to `1.27.5`.

#### Optimized

- **Improved** Removed CPU/Memory resource request and limit for Global Management, Container Management, and Observability components in community edition minimal installation with `-z` flag.
- **Improved** error handling for installer's `-m` parameter, now it throws an error and exits installation when manifest file is not specified for `-m`.
- **Improved** Enhanced logging display for upgrade functionality.
- **Improved** Adapted containerd-related parameters from kubean.
- **Improved** Repackaged GProduct component and uploaded it to ChartMuseum on Sparkle nodes.
- **Improved** log output when uploading addon fails.
- **Improved** Adapted helm installation parameters for reusing during GProduct component upgrade.
- **Improved** Adjusted maximum pod count per node to 180 for Global cluster.
- **Improved** excessive logging during migration of charts.

#### Fixed

- **Fixed** privilege issue with cache files when installing with non-root user.
- **Fixed** error during migration of data from Sparkle nodes to Global cluster during installation.
- **Fixed** possible failure during addon upload.
- **Fixed** Addressed potential "helm operation in progress" issue in the code.
- **Fixed** support for external redis with password in sentry mode for Kpanda component.
- **Fixed** failure to deploy Global cluster with docker runtime.
- **Fixed** redirection issue in LB mode for Ghippo.
- **Fixed** missing metric indicators when starting MinIo component.

#### Known Issues

- Podman in Sparkle nodes requires IPv6 to be enabled.
- Global cluster may encounter `etcd NOSPACE` warning risk.

## 2023-8-31

### v0.11.0

#### New Features

- **Added** Update the k8s version of Global clusters to v1.26.7 to avoid security vulnerabilities in older versions
- **Added** Support for setting ansible extension parameters in clusterConfig.yaml
- **Added** Support for adding certificate renewal configuration in clusterConfig.yaml, including periodic and one-time updates
- **Added** Support for offline deployment of Red Hat 9.2 systems
- **Added** Diagnostic script diag.sh for Global cluster in the offline package
- **Added** `--multi-arch` flag to avoid upgrading issues with overriding multi-architecture images

#### Improvements

- **Improved** installer source code structure modules

#### Bug Fixes

- **Fixed** issue where redis sentinel mode does not support sentinel instance password
- **Fixed** failure when adding TencentOS 3.1 system nodes to the working cluster

## 2023-7-31

### v0.10.0

#### Added

- **Added** Support for Oracle Linux R8-U7 operating system
- **Added** Support for flexibly exposing kind container mappings to the host machine's ports
- **Added** import-artifact subcommand supports importing offline resources based on external services defined in clusterConfig.yaml configuration file

#### Improved

- **Improved** For environments deployed using the installer through external OS repo, optimized the ability to select external OS repo when creating a cluster in container management
- **Improved** Refactored and abstracted clusterConfig detection layer
- **Improved** error messages for pre-requisite dependency installation script
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
- After restarting the seed node with Redhat 8.6 operating system, the kubelet service fails to start and reports the following error:

    ```message
    failed to initialize top level QOS containers: root container [kubelet kubepods] doesn't exist
    ```

    A temporary solution is to execute the following command:

    ```sh
    podman restart [containerid] --time
    ```

- When installing a cluster based on TencentOS 3.1, the package manager cannot be correctly identified. If TencentOS 3.1 is needed, please use installer version 0.9.0.

## 2023-6-30

### v0.9.0

#### New Features

- **Added** The `istio-ingressgateway` now supports high availability mode. When upgrading from v0.8.x or earlier to v0.9.0, the following command must be executed: `./offline/dce5-installer cluster-create -c clusterConfig.yaml -m manifest.yaml --upgrade infrastructure,gproduct`
- **Added** Support configuring the exposed bootstrapping kind address and port in the clusterConfig.yaml file.
- **Added** The installer now performs a pre-check on each node to verify if lvm2 is installed when using eyebrow storage.
- **Added** The installer includes an embedded default upgrade of the k8s version to v1.26.5.
- **Added** Support specifying the local file mount path for the bootstrapping kind in the clusterConfig.yaml file.
- **Added** Integrated ISO image file import script into the installer binary.

#### Improvements

- **Improved** download scripts.
- **Improved** logic and functionality of the `import-artifact` command.
- **Improved** Made `isoPath` and `osPackagePath` optional fields in clusterConfig.yaml during the upgrade process.
- **Improved** temporary file cleanup mechanism in the installer.
- **Improved** reuse functionality of the bootstrapping node.

#### Fixes

- **Fixed** an issue where the ES component could not start in OCP.
- **Fixed** an issue where the UI interface was inaccessible after installing DCE in TencentOS.
- **Fixed** the high probability of failed database creation for middleware databases in arm64 environments.
- **Fixed** shell expansion error in the image upload success check process.

#### Known Issues

When upgrading from v0.8.x to v0.9.0, the following commands need to be executed for verification:

- Check if the `istio-ingressgateway` port is `80` or `8080`

    ```bash
    kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].targetPort}'
    ```

- Check if the `istio-ingressgateway` port is `443` or `8443`

    ```bash
    kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].targetPort}'
    ```

If the output is `80` or `443`, the upgrade command needs to include the `infrastructure` parameter. Example:

```bash
./offline/dce5-installer cluster-create -c clusterConfig.yaml -m manifest.yaml --upgrade infrastructure,gproduct
```

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

- **Fixed** an issue of failed image synchronization for Harbor repositories using external HTTP.
- **Fixed** indentation error in `clusterConfig.yaml` configuration file.
- **Fixed** rendering error in localService configuration when using an external yum repo.
- **Fixed** integration issue with external JFrog charts repository.

## 2023-5-31

### v0.8.0

#### New Features

- **Added** other Linux mode supports the OpenAnolis 8.8 GA operating system
- **Added** supports the OracleLinux R9 U1 operating system
- **Added** node status detection
- **Added** file verification for OS PKGs
- **Added** supports cluster installation on non-22 ports
- **Added** external file service supports k8s binary resources
- **Added** supports external JFrog image and charts repositories
- **Added** supports mixed architecture deployment solutions
- **Added** supports external Redis components

#### Improvements

- **Improved** Fixed issue of missing images when deploying Nacos instances
- **Improved** Fixed issue of repeated execution of cluster installation task during cluster module upgrade

#### Known Issues

- Addon offline package does not currently support uploading to external JFrog services
- The container management platform offline mode currently does not support adding nodes to working clusters
- When using an external OS Repo repository in an offline scenario, i.e. defining `osRepos.type=external` in clusterConfig.yaml, after successfully deploying DCE5.0, you cannot create working clusters in the container management. A temporary solution is as follows:
  After installing the global cluster, immediately update the configmap kubean-localservice in the kubean-system namespace of the global cluster to replace all double quotes with single quotes in the value of `yumRepos.external`. For example, replace all double quotes in the file with single quotes:

    ```yaml
    yumRepos:
      external: [ "http://10.5.14.100:8081/centos/\$releasever/os/\$basearch","http://10.5.14.100:8081/centos-iso/\$releasever/os/\$basearch" ]
    ```

    replaced with:

    ```yaml
    yumRepos:
      external:
        [
          'http://10.5.14.100:8081/centos/\$releasever/os/\$basearch',
          'http://10.5.14.100:8081/centos-iso/\$releasever/os/\$basearch',
        ]
    ```

## 2023-5-30

### v0.7.1

#### Improvements

- **Improved** Upgrade of monitoring components version

#### Bug Fixes

- **Fixed** Binary output of DCE Community manifest was incorrect

## 2023-4-30

### v0.7.0

#### Features

- **Added** support for Other Linux to deploy DCE5.0, [Reference Documentation](os-install/otherlinux.md)
- **Added** support for operating system OpenEuler 22.03
- **Added** supports external OS Repos, [refer to cluster configuration file description](commercial/cluster-config.md)
- **Added** supports kernel parameter tuning, [refer to cluster configuration file description](commercial/cluster-config.md)
- **Added** support for detecting whether external ChartMuseum and MinIo services are available

#### Improvements

- **Improved** the pre-verification of tar and other commands
- **Improved** the command line parameters of the upgrade operation
- **Improved** closed Kibana's access through NodePort, Insight uses ES's NodePort or VIP access
- **Improved** the display of concurrent logs, terminate tasks using SIGTERM signal instead of SIGKILL

#### Fixes

- **Fixed** an issue that the Kcoral helm chart cannot be found during online installation
- **Fixed** KubeConfig can't find problem when upgrading

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

#### Improvements

- **Improved** Upgraded Kpanda to v0.16.1
- **Improved** Upgraded Skoala to v0.19.4

## 2022-4-06

### v0.6.0

#### Features

- **Added** support for one-click upgrade of Gproduct components
- **Added** Adapted operating system: UOS V20 1020a / Ubuntu 20.04
- **Added** Support OCP (OpenShift Container Platform) to install DCE5.0
- **Added** CLI supports generating clusterConfig templates
- **Added** all-in-one mode starts the minimal installation mode by default
- **Added** Kcollie component in Gproduct component
- **Added** Support community version to sync image to external repository

#### Improvements

- **Improved** Decouple the code for generating offline packages and the code required for the installation process
- **Improved** bootstrapping node inotify parameters
- **Improved** the full-mode online installation experience
- **Improved** clusterConfig structure and configuration
- **Improved** DCE Community allows not to check clusterConfig format and parameters
- **Improved** installer execution scheduler log output

#### Fixes

- **Fixed** Removed dependency on wget
- **Fixed** an issue of installation failure after repeated decompression of offline packages
- **Fixed** MinIo non-reentrant issue
- **Fixed** redis pvc that continues to be left behind when middleware Redis CR is removed
- **Fixed** an issue of sequence dependency when Amamba and Amamba-jenkins are installed concurrently
- **Fixed** an issue that the installer command line -j parameter parsing fails

## 2022-2-28

### v0.5.0

#### Features

- **Added** Offline package separation osPackage, needs to define `osPackagePath` in the cluster configuration file
- **Added** Support addon offline, you need to define `addonOfflinePackagePath` in the cluster configuration file
- **Added** Offline installation supports operating systems REHL 8.4, REHL 7.9

#### Improvements

- **Improved** Upgraded the version of pre-dependent tools

#### Fixes

- **Fixed** installer command line `-j` parameter validity detection problem
- **Fixed** The installation path problem of pre-dependent tools
- **Fixed** an issue that the host list password is invalid for pure numbers
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
- **Added** installation of contour as default ingress-controller for commercial version
- **Added** New installation of cert-manager in commercial version
- **Added** Support cluster deployment in private key mode
- **Added** supports external container registry for deployment

#### Optimized

- **Improved** The offline package no longer includes the ISO of the operating system, which needs to be downloaded separately. In the case of pure offline, the absolute path of the ISO needs to be defined in the clusterConfig file
- **Improved** Commercial version uses Contour as default ingress-controller
- **Improved** MinIO supports using VIP
- **Improved** coredns automatically inject registry VIP analysis
- **Improved** the offline package production process and speed up the packaging of Docker images
- **Improved** the offline package size
- **Improved** infrastructure support 1.25: upgrade redis-operator, eck-operator, hwameiStor
- **Improved** upgrade to keycloakX
- **Improved** istio version upgrade v1.16.1

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
- **Added** support for kylin v10 sp2 offline package.
- **Added** Infrastructure Support 1.25: Upgrade redis-operator, eck-operator, hwameiStor and other components.
- **Added** support for cluster deployment in private key mode.
- **Added** The workload is elastically scaled based on custom metrics, which is closer to the user's actual business elastic expansion and contraction needs.

#### Optimized

- **Improved** Create permanent harbor with operator, enable HTTPS, and use Postgressql operator.
- **Improved** Commercial version uses contour as default ingress-controller.
- **Improved** MinIO supports using VIP.
- **Improved** coredns is automatically injected into registry VIP resolution.
- **Improved** the offline package production process and speed up the packaging of docker images.

#### Fixes

- **Fixed** issues with fair cloud service.
- **Fixed** issues with image and helm for various submodules.
- **Fixed** Bug fixes for offline package loading.

#### Known issues

- Because some operators need to be upgraded to support 1.25, DCE 5.0 does not support 1.20 downwards.
- The default k8s version of kubean and the offline package are still limited to k8s 1.24 version, which has not been updated to 1.25 (postgres-operator is not supported yet).
- In the case of Image Load, the istio-ingressgateway imagePullPolicy is always.
- For the ARM version, step 16 (harbor) cannot be performed, because harbor does not support ARM for the time being.
  The manifest.yaml file needs to be modified, the postgressql operator is fasle, and
  -j 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 should be added when executing the installation command
