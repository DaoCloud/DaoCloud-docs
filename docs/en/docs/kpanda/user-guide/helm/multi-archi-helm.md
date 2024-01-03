# Steps for Importing and Upgrading Helm Applications with Multiple Architectures

In a multi-architecture cluster, it is common to use Helm charts that support multiple architectures to address deployment issues caused by architectural differences. This guide will explain how to integrate single-architecture Helm applications into multi-architecture deployments and how to integrate multi-architecture Helm applications.

## Importing

### Single-Architecture Import

Prepare the offline package __addon-offline-full-package-${version}-${arch}.tar.gz__ ,which can be downloaded from the [Download Center](../../../download/addon/history.md).

Specify the path in the __clusterConfig.yml__ configuration file, for example:

```yaml
addonPackage:
  path: "/home/addon-offline-full-package-v0.9.0-amd64.tar.gz"
```

Then execute the import command:

```shell
~/dce5-installer cluster-create -c /home/dce5/sample/clusterConfig.yaml -m /home/dce5/sample/manifest.yaml -d -j13
```

### Multi-Architecture Integration

Prepare the offline package __addon-offline-full-package-${version}-${arch}.tar.gz__ , which can be downloaded from the [Download Center](../../../download/addon/history.md).

Take __addon-offline-full-package-v0.9.0-arm64.tar.gz__ as an example and execute the import command:

```shell
~/dce5-installer import -addon -c /home/dce5/sample/clusterConfig.yaml --addon-path=/home/addon-offline-full-package-v0.9.0-arm64.tar.gz
```

## Upgrading

### Single-Architecture Upgrade

Prepare the offline package __addon-offline-full-package-${version}-${arch}.tar.gz__ , which can be downloaded from the [Download Center](../../../download/addon/history.md).

Specify the path in the __clusterConfig.yml__ configuration file, for example:

```yaml
addonPackage:
  path: "/home/addon-offline-full-package-v0.11.0-amd64.tar.gz"
```

Then execute the import command:

```shell
~/dce5-installer cluster-create -c /home/dce5/sample/clusterConfig.yaml -m /home/dce5/sample/manifest.yaml -d -j13
```

### Multi-Architecture Integration

Prepare the offline package __addon-offline-full-package-${version}-${arch}.tar.gz__ , which can be downloaded from the [Download Center](../../../download/addon/history.md).

Take __addon-offline-full-package-v0.11.0-arm64.tar.gz__ as an example and execute the import command:

```shell
~/dce5-installer import -addon -c /home/dce5/sample/clusterConfig.yaml --addon-path=/home/addon-offline-full-package-v0.11.0-arm64.tar.gz
```

## Considerations

### Disk Space

The offline package is large, and during the process, it needs to be unpacked and load the images. Make sure you have enough disk space available; otherwise, the process may fail due to "no space left" error.

### Retry after Failure

If the multi-architecture integration step fails, clean up any remnants before retrying:

```shell
rm -rf addon-offline-target-package
```

### Image Registry

If the integrated offline package includes image registries that are different from those in the imported offline package, an error may occur during the integration process due to the absence of the image registry:


Solution: Create the missing image registry before the integration step to avoid this error. For example, in the above screenshot, the error can be avoided by creating the image registry __localhost__ beforehand.

### Architecture Conflict

When upgrading to a version lower than 0.12.0 of the addon, the charts-syncer in the target offline package does not check for image existence, resulting in the conversion of a multi-architecture deployment to a single-architecture one during the upgrade process. The conversion back to a multi-architecture deployment will only occur during the subsequent integration.
