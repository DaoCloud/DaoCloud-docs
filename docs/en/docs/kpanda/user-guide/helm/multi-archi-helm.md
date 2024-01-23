---
MTPE: windsonsea
date: 2024-01-17
---

# Import and Upgrade Multi-Arch Helm Apps

In a multi-arch cluster, it is common to use Helm charts that support multiple architectures to address deployment issues caused by architectural differences. This guide will explain how to integrate single-arch Helm apps into multi-arch deployments and how to integrate multi-arch Helm apps.

## Import

### Import Single-arch

Prepare the offline package `addon-offline-full-package-${version}-${arch}.tar.gz`, which can be downloaded from the [Download Center](../../../download/addon/history.md).

Specify the path in the __clusterConfig.yml__ configuration file, for example:

```yaml
addonPackage:
  path: "/home/addon-offline-full-package-v0.9.0-amd64.tar.gz"
```

Then run the import command:

```shell
~/dce5-installer cluster-create -c /home/dce5/sample/clusterConfig.yaml -m /home/dce5/sample/manifest.yaml -d -j13
```

### Integrate Multi-arch

Prepare the offline package `addon-offline-full-package-${version}-${arch}.tar.gz`, which can be downloaded from the [Download Center](../../../download/addon/history.md).

Take `addon-offline-full-package-v0.9.0-arm64.tar.gz` as an example and run the import command:

```shell
~/dce5-installer import-addon -c /home/dce5/sample/clusterConfig.yaml --addon-path=/home/addon-offline-full-package-v0.9.0-arm64.tar.gz
```

## Upgrade

### Upgrade Single-arch

Prepare the offline package `addon-offline-full-package-${version}-${arch}.tar.gz`, which can be downloaded from the [Download Center](../../../download/addon/history.md).

Specify the path in the __clusterConfig.yml__ configuration file, for example:

```yaml
addonPackage:
  path: "/home/addon-offline-full-package-v0.11.0-amd64.tar.gz"
```

Then run the import command:

```shell
~/dce5-installer cluster-create -c /home/dce5/sample/clusterConfig.yaml -m /home/dce5/sample/manifest.yaml -d -j13
```

### Multi-arch Integration

Prepare the offline package `addon-offline-full-package-${version}-${arch}.tar.gz`, which can be downloaded from the [Download Center](../../../download/addon/history.md).

Take `addon-offline-full-package-v0.11.0-arm64.tar.gz` as an example and run the import command:

```shell
~/dce5-installer import-addon -c /home/dce5/sample/clusterConfig.yaml --addon-path=/home/addon-offline-full-package-v0.11.0-arm64.tar.gz
```

## Notes

### Disk Space

The offline package is quite large and requires sufficient space for decompression and loading of images. Otherwise, it may interrupt the process with a "no space left" error.

### Retry after Failure

If the multi-arch fusion step fails, you need to clean up the residue before retrying:

```shell
rm -rf addon-offline-target-package
```

### Registry Space

If the offline package for fusion contains registry spaces that are inconsistent with the imported offline package, an error may occur during the fusion process due to the non-existence of the registry spaces:

![helm](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/multi-arch-helm.png)

Solution: Simply create the registry space before the fusion. For example, in the above error, creating the registry space "localhost" in advance can prevent the error.

### Architecture Conflict

When upgrading to a version lower than 0.12.0 of the addon, the charts-syncer in the target offline package does not check the existence of the image before pushing, so it will recombine the multi-arch into a single architecture during the upgrade process.
For example, if the addon is implemented as a multi-arch in version v0.10, upgrading to version v0.11 will overwrite the multi-arch addon with a single architecture. However, upgrading to version 0.12.0 or above can still maintain the multi-arch.
