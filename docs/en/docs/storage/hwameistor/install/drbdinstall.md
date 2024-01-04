---
hide:
  - toc
---

# Install DRBD (Optional)

If you need to use high-availability data volumes, enable DRDB when deploying Hwameistor. Here is how to install it:

## Synchronous Installation during HwameiStor Deployment

You can directly enable the DRDB component when installing HwameiStor. For details, please refer to [Install HwameiStor with Operator](deploy-operator.md)

## Install with UI

1. Please go to `Container Management` -> `Helm Charts`, and select `drbd-adapter`.

2. Click on `drdb-adapter`, click on install, and enter the configuration page.

    ![drbd02](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/storage/hwameistor/img/drbd02.png)

    - `Namespace`: It is recommended to deploy in the same namespace as HwameiStor. The namespace created in this example is `HwameiStor`.
    - `Version`: Select the latest version by default.
    - `Deletion failed`: Turned off by default. When enabled, it will wait for the application to be installed by default, and will delete the installation in case of installation failure.
    - `Wait`: Turned off by default. When enabled, it will wait for all resources associated with the application to be ready before marking the application as successfully installed.
    - `Detailed Logs`: Turned off by default. Enable detailed output of installation process logs.

3. Click `OK` to complete the creation.

## Installation Through Helm

If you are installing through Helm, please use the following method to install:

```console
helm repo add hwameistor https://hwameistor.io/hwameistor

helm repo update hwameistor

helm pull hwameistor/drbd-adapter --untar

helm install drbd-adapter ./drbd-adapter -n hwameistor --create-namespace
```

Users in Chinese mainland can use the image repository `daocloud.io/daocloud` for acceleration:

```console
helm install drbd-adapter ./drbd-adapter \
    -n hwameistor --create-namespace \
    --set imagePullPolicy=Always \
    --set registry=daocloud.io/daocloud
```
