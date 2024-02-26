---
MTPE: windsonsea
date: 2024-02-19
hide:
  - toc
---

# Install DRBD (Optional)

If you need to use high-availability data volumes, enable DRDB when deploying Hwameistor. Here is how to install it:

## Install DRDB while installing HwameiStor

You can directly enable the DRDB component when installing HwameiStor.
For details, please refer to [Install HwameiStor with Operator](deploy-operator.md).

## Install with UI

1. Go to `Container Management` -> `Helm Charts`, and select `drbd-adapter`.

2. Click `drdb-adapter`, click install, and enter the configuration page.

    ![drbd02](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/storage/hwameistor/img/drbd02.png)

    - `Namespace`: It is recommended to deploy in the same namespace as HwameiStor. The namespace created in this example is `HwameiStor`.
    - `Version`: Select the latest version by default.
    - `Deletion failed`: Turned off by default. When enabled, it will wait for the application to be installed by default, and will delete the installation in case of installation failure.
    - `Wait`: Turned off by default. When enabled, it will wait for all resources associated with the application to be ready before marking the application as successfully installed.
    - `Detailed Logs`: Turned off by default. Enable detailed output of installation process logs.

3. Click `OK` to complete the creation.

## Install with Helm

Deploy the following `DaemonSet`. It will start a Pod on each Kubernetes worker node to install the DRBD module and tools.

```bash
helm repo add drbd-adapter https://hwameistor.io/drbd-adapter/
helm repo update drbd-adapter
helm pull drbd-adapter/drbd-adapter --untar
helm install drbd-adapter ./drbd-adapter -n hwameistor --create-namespace
```

!!! tip

    Users in Chinese mainland can use the image repository `daocloud.io/daocloud` for acceleration:

    ```bash
    helm install drbd-adapter ./drbd-adapter \
        -n hwameistor --create-namespace \
        --set imagePullPolicy=Always \
        --set registry=daocloud.io/daocloud
    ```
