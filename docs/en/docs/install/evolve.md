---
MTPE: windsonsea
date: 2024-05-11
---

# Upgrade DCE 5.0 Standard to Platinum

DCE 5.0 supports multiple versions, and all versions except DCE Community are DCE 5.0 Enterprise. This page demonstrates how to upgrade from DCE 5.0 Standard to DCE 5.0 Platinum.

![Modules](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/dce-modules04.jpg)

## Prerequisites

- You need to have a cluster environment of DCE 5.0, refer to [Offline Deployment of DCE 5.0 Enterprise](commercial/start-install.md)
- Ensure that your bootstrap machine is still alive, and the corresponding offline package of the current environment is still available. Otherwise, you need to redownload it.

## Steps

### Step 1: Edit manifest.yaml

Change all `enable: false` to `enable: true` in the manifest.yaml file.

```yaml
skoala:
   enable: false
   helmVersion: 0.26.1
   variables:
 mspider:
   enable: false
   helmVersion: v0.18.0-rc2
   variables:
 mcamel-rabbitmq:
   enable: false
   helmVersion: 0.12.2
   variables:
 mcamel-elasticsearch:
   enable: false
   helmVersion: 0.9.2
   variables:
 ...
 mcamel-mysql:
   enable: false
   helmVersion: 0.10.2
   variables:
 mcamel-redis:
   enable: false
   helmVersion: 0.10.0-rc2
   variables:
 mcamel-kafka:
   enable: false
   helmVersion: 0.7.2
   variables:
 mcamel-minio:
   enable: false
   helmVersion: 0.7.2
   variables:
 mcamel-postgresql:
   enable: false
   helmVersion: 0.4.0-rc2
   variables:
 mcamel-mongodb:
   enable: false
   helmVersion: 0.2.0-rc2
   variables:
```

### Step 2: Run commands

Perform the upgrade command by running:

```bash
./offline/dce5-installer cluster-create -c ./sample/clusterConfig.yaml -m ./sample/manifest.yaml -j 11,12
```

!!! note

    The clusterConfig.yaml file needs to be consistent with the parameters used during installation.

    -j 11, 12 are required parameters for upgrading from the Standard Package to the Platinum Package.

### Step 3: Success

![upgrade](commercial/images/succeed01.png)
