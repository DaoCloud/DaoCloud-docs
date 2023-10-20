# Upgrading

This page explains how to upgrade the old version of SpiderPool (v0.5.0 or lower) in DCE 5.0 to the new version v0.7.0.

## Prerequisites

1. A Kubernetes cluster.
2. Helm installed.

## Upgrade Environment

SpiderPool v0.5.0 or lower version deployed in DCE 5.0.

## Get the Chart Package

1. Obtain the chart package using one of the following methods:

    - Download the v0.7.0 chart package through the DCE 5.0 UI:

2. Upload and extract the chart package to your environment:

    ```bash
    tar -xvf spiderpool-0.7.0.tgz -C /root/spiderpool
    ```

## Delete spiderpool-init

The new version introduces the Spidercoordinators plugin, and the default configuration of Spidercoordinators will be automatically applied when the spiderpool-init Pod is created. Before performing the upgrade, delete the spiderpool-init Pod. The spiderpool-init Pod will be automatically recreated and the default coordinator configuration will be applied when upgrading with `helm upgrade`.

```bash
[root@controller-node-1 ~]# kubectl get po -n kube-system spiderpool-init
NAME              READY   STATUS      RESTARTS   AGE
spiderpool-init   0/1     Completed   0          49m
[root@controller-node-1 ~]# kubectl delete po -n kube-system spiderpool-init
pod "spiderpool-init" deleted
```

## Update CRDs

Update all the SpiderPool v0.7.0 CRDs using `kubectl apply`.

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

## Upgrade via DCE 5.0 UI

When upgrading through the DCE 5.0 UI, make sure to disable the "Install multus" button to avoid duplicate installation of Multus. In the new version of SpiderPool, Multus is already integrated. Click "Upgrade" and wait for the upgrade to complete.

## Verification

Check that the version is updated correctly.

In the new version of SpiderPool, a SpiderMultusConfig CR is provided to automatically manage the Multus NetworkAttachmentDefinition CRs. If you have existing Multus CRs in your cluster, they will not be displayed in the UI due to the different creation mechanisms. You can create a new Multus CR with the same name through the UI, which will not affect the functionality of your existing CRs. Ensure that the values filled in the UI, such as `Vlan ID` and `NIC Interface`, are exactly the same as in your original Multus CR.
