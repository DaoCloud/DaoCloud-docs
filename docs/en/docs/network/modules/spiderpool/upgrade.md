# Upgrade Spiderpool

This page explains how to upgrade an old version of Spiderpool (less than or equal to v0.5.0)
in DCE 5.0 to a newer version. This document uses the upgrade to Spiderpool v0.7.0 as an example.

## Prerequisites

1. A Kubernetes cluster
2. [Helm](https://helm.sh/docs/intro/install/) installed

## Check the Upgrade Environment

Other lower versions of Spiderpool have been deployed in DCE 5.0.

## Obtain Chart Package and Image

You can sync the image package and Chart package to the offline repository in one of the following two ways.

### Method 1: Upgrade the Addon offline package, sync update Spiderpool Chart package and image

The Spiderpool offline package is stored in Addon. You can refer to
[download Addon offline package](../../../download/addon/history.md) to download the latest Addon offline package.
After downloading, open the `clusterConfig.yaml`, modify the `addonOfflinePackagePath` field to
specify the path where Addon is located, and complete the upgrade of the Addon offline package.

1. After upgrading Addon, you can obtain the Chart package as follows:

    Download the v0.7.0 Chart package through the DCE 5.0 interface as follows:

    ![spiderpool chart](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/spiderpool-chart-version-7.png)

2. Upload and unzip the Chart package to the environment

    ```bash
    tar -xvf spiderpool-0.7.0.tgz -C /root/spiderpool
    ```

### Method 2: Manually upgrade Spiderpool

1. Get the Chart package

    Obtain the Chart package in the environment using the following Helm commands.

    ```bash
    $ helm repo add spiderpool https://spidernet-io.github.io/spiderpool
    $ helm repo update spiderpool

    $ helm search repo spiderpool/spiderpool --versions
    NAME                   CHART VERSION   APP VERSION  DESCRIPTION
    spiderpool/spiderpool  0.7.0           0.7.0        ipam for kubernetes cni
    ...

    $ helm fetch spiderpool/spiderpool --version 0.7.0

    $ ls spiderpool-0.7.0.tgz
    spiderpool-0.7.0.tgz
    ```

    Upload the Chart package to the offline repository.

    ```shell
    # Upload Chart package
    helm repo add [addon] http://10.5.10.210:8081 # Replace [addon] with offline repo name, and replace with your image repository URL
    helm cm-push -u rootuser -p rootpass123 --insecure {Chart directory or tar package} # Replace with your image repo username and password
    ```

2. Get the offline image package

    On any internet-connected environment with Docker installed,
    run the following commands to get the Spiderpool images.

    ```shell
    docker pull ghcr.m.daocloud.io/spidernet-io/spiderpool/spiderpool-controller:v0.7.0
    docker pull ghcr.m.daocloud.io/spidernet-io/spiderpool/spiderpool-agent:v0.7.0
    ```

    Save as offline image tar packages using `docker save` and upload to the offline environment.

    ```shell
    docker save -o spiderpool-0.7.0.tar ghcr.m.daocloud.io/spidernet-io/spiderpool/spiderpool-controller:v0.7.0 ghcr.m.daocloud.io/spidernet-io/spiderpool/spiderpool-agent:v0.7.0
    ```

3. Load images into Docker or containerd in the upgrade environment.
  
    === "Docker"

        ```shell
        docker load -i spiderpool-0.7.0.tar
        ```

    === "containerd"

        ```shell
        ctr -n k8s.io image import spiderpool-0.7.0.tar
        ```

!!! note

    Every node needs to load images into Docker or containerd.
    After loading, tag the images to keep the Registry and Repository
    consistent with the installation time.

## Delete spiderpool-init

Starting from version v0.7.0, Spiderpool introduced the Spidercoordinators plugin,
which will automatically deploy its default configuration when the spiderpool-init is created.
Before upgrading Spiderpool, please delete this Pod. When updating through `helm upgrade`,
the spiderpool-init Pod will be automatically created, and the default configuration
for creating Spidercoordinators will be deployed.

```bash
[root@controller-node-1 ~]# kubectl get po -n kube-system spiderpool-init
NAME              READY   STATUS      RESTARTS   AGE
spiderpool-init   0/1     Completed   0          49m

[root@controller-node-1 ~]# kubectl delete po -n kube-system spiderpool-init
pod "spiderpool-init" deleted
```

## Update CRD

Since updating CRDs through Helm is not possible via the interface,
update the Spiderpool CRDs on the Master node using `kubectl apply`.

```bash
[root@controller-node-1 crds]# ls
spiderpool.spidernet.io_spidercoordinators.yaml  spiderpool.spidernet.io_spiderippools.yaml        spiderpool.spidernet.io_spiderreservedips.yaml
spiderpool.spidernet.io_spiderendpoints.yaml     spiderpool.spidernet.io_spidermultusconfigs.yaml  spiderpool.spidernet.io_spidersubnets.yaml

[root@controller-node-1 crds]# ls | grep '\.yaml$' | xargs -I {} kubectl apply -f {}
customresourcedefinition.apiextensions.k8s.io/spidercoordinators.spiderpool.spidernet.io created
customresourcedefinition.apiextensions.k8s.io/spiderendpoints.spiderpool.spidernet.io configured
customresourcedefinition.apiextensions.k8s.io/spiderippools.spiderpool.spidernet.io configured
customresourcedefinition.apiextensions.k8s.io/spidermultusconfigs.spiderpool.spidernet.io created
customresourcedefinition.apiextensions.k8s.io/spiderreservedips.spiderpool.spidernet.io configured
customresourcedefinition.apiextensions.k8s.io/spidersubnets.spiderpool.spidernet.io configured
```

## Upgrade through DCE 5.0 Interface

After correctly uploading the offline Chart and image packages to the offline environment
in the previous steps, you can now perform the upgrade through the 5.0 interface.
In versions below 0.7.0, Spiderpool was used in conjunction with the Multus-underlay plugin,
while the new version of Spiderpool has integrated the Multus plugin.
When updating through the interface, turn off the **install multus** button to avoid redundant
installation. As shown in the image below, click **update** and wait for the update to complete.

![disable multus](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/spiderpool-disable-multus.png)

## Verification

After the upgrade, check that the version is correct.

![spiderpool 0.7.0](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/spiderpool-after-upgrade.png)

In Spiderpool versions 0.7.0 and above, the SpiderMultusConfig CR is provided to automatically
manage the Multus NetworkAttachmentDefinition CR. If your cluster has old Multus CRs,
the new version, due to different creation mechanisms, will not display your old Multus CRs in the UI.
You can create a Multus CR with the same name through the interface to manage it,
and it will not affect the use of your original features.
Note that the values filled in the interface, such as `Vlan ID` and `network interface`,
you need to be completely consistent with those in your original Multus CR.
