---
MTPE: windsonsea
Date: 2024-07-18
---

# Reintegrate Worker Clusters After Global Service Cluster Redeployed

## Background

A client needs to decommission the existing environment and redeploy due to architectural adjustments of the
[Global Service Cluster](../../kpanda/user-guide/clusters/cluster-role.md#global-service-cluster).
Considering that multiple [Worker Clusters](../../kpanda/user-guide/clusters/cluster-role.md#worker-clusters)
have already been deployed in the original environment, the client wishes to reintegrate these worker clusters
into the new environment to manage their lifecycle.

## Solution

### Back up Resources

Before decommissioning the existing environment, the following related resources need
to be backed up to restore them in the new environment.

#### Back up Kubean Resources

[Kubean](../../community/kubean.md) is a cluster lifecycle management tool built on Kubespray.

1. Get the `configmap` resources in the `kubean-system` namespace and back up the resources `<cluster-name>-hosts-conf`, `<cluster-name>-kubeconf`, `<cluster-name>-vars-conf`, `kubean-localservice`. In this example, the resources are `migrate-cluster-hosts-conf`, `migrate-cluster-kubeconf`, `migrate-cluster-vars-conf`, `kubean-localservice`.

    ```shell
    # Get resources
    kubectl -n kubean-system get cm --no-headers | awk '{print $1}'

    # Back up resources
    kubectl -n kubean-system get cm migrate-cluster-hosts-conf -o yaml >> hosts-conf.yaml
    kubectl -n kubean-system get cm migrate-cluster-kubeconf -o yaml >> kubeconf.yaml
    kubectl -n kubean-system get cm migrate-cluster-vars-conf -o yaml >> vars-conf.yaml
    ```

2. Get the `secret` resources in the `kubean-system` namespace and back up the resources `sh.helm.release.v1.kubean.v1`,
   `webhook-http-ca-secret`. If virtual machines use username/password during deployment, this step is not required.

    ```shell
    # Get resources
    kubectl -n kubean-system get secret --no-headers | awk '{print $1}'

    # No backup needed if clusterconfig.yaml virtual machines use username/password
    ```

3. Back up `cluster.kubean.io` resources which identify all K8s clusters in the current environment.

    ```shell
    # Get resources
    kubectl get cluster.kubean.io --no-headers | awk '{print $1}'

    migrate-cluster
    my-cluster
    ```

    ```shell
    # Back up resources except for my-cluster
    kubectl get cluster.kubean.io migrate-cluster -o yaml >> migrate-cluster.yaml
    ```

4. Back up `localartifactsets.kubean.io` resources which record the component and versions
   supported by the offline package in the current environment.

    ```shell
    # Get resources
    kubectl get localartifactsets.kubean.io --no-headers | awk '{print $1}'

    # Back up resources
    kubectl get localartifactsets.kubean.io <localartifactsets-name> -o yaml >> localartifactset.yaml
    ```

5. Back up `manifests.kubean.io` resources which record and maintain the components, packages,
   and versions used and compatible with the current version of Kubean.

    ```shell
    # Get resources
    kubectl get manifests.kubean.io --no-headers | awk '{print $1}'

    # Back up resources
    kubectl get manifests.kubean.io <manifest-name> -o yaml >> manifest.yaml
    ```

#### Back up Kpanda Component Related Resources

Kpanda is the internal code of the [Container Management Module](../../kpanda/intro/index.md).

1. Back up `clusters.cluster.kpanda.io`, only backing up the information of the worker clusters.
   For example, only back up the `migrate-cluster` information:

    ```shell
    [root@g-master1]# kubectl get clusters.cluster.kpanda.io
    NAME                    VERSION   MODE   PROVIDER             RUNNING   KUBESYSTEMID                           AGE
    kpanda-global-cluster   v1.27.5   Push   DAOCLOUD_KUBESPRAY   True      b4a1404d-04fd-4b48-bd87-c1494322bebb   50m
    migrate-cluster         v1.27.5   Push   DAOCLOUD_KUBESPRAY   True      7a45e8c4-b693-4c4c-a06b-19bd9052be64   44m

    [root@g-master1]# kubectl get clusters.cluster.kpanda.io migrate-cluster -o yaml >> kpanda-migrate-cluster.yaml
    ```

2. Back up the `secret` resources related to the worker clusters in the `kpanda-system` namespace,
   named `<cluster-name>-secret`. In this example, it is `migrate-cluster-secret`.

    ```shell
    # Back up resources
    kubectl -n kpanda-system get secrets migrate-cluster-secret -o yaml >> kpanda-migrate-cluster-secret.yaml
    ```

3. Back up the `configmap` resources related to the worker clusters in the `kpanda-system` namespace,
   named `<cluster-name>-setting`. In this example, it is `migrate-cluster-setting`, which records
   the information under **Cluster Operations** -> **Cluster Settings**. If there are no updates, this backup is not needed.

    ```shell
    # Back up resources
    kubectl -n kpanda-system get cm migrate-cluster-setting -o yaml >> kpanda-migrate-cluster-setting.yaml
    ```

### Restore Resources

Restore the resources backed up in the previous step in the new environment
so that the new environment can manage the original worker clusters.

#### Restore Kubean Resources

1. Restore `cluster.kubean.io` resources.

    ```shell
    # Create resources
    kubectl apply -f migrate-cluster.yaml
    ```

    ```shell
    # View the created cluster.kubean.io/migrate-cluster resource information and get the uid 
    kubectl get cluster.kubean.io mig-cluster -o yaml | grep "uid: "
    ```

    In this example, the retrieved uid is `6b81413c-270e-4720-b215-fe7cf1364d45`.

2. Restore `localartifactsets.kubean.io` resources.

    ```shell
    # Create resources
    kubectl apply -f localartifactset.yaml
    ```

3. Restore `manifests.kubean.io` resources.

    ```shell
    # Create resources
    kubectl apply -f manifest.yaml
    ```

4. Update the backed-up `hosts-conf.yaml`, `kubeconf.yaml`, and `vars-conf.yaml` to update the `ownerReferences` section
   with the [uid obtained in step 1](#restore-kubean-resources). If `secret` resources were backed up,
   they also need to be updated accordingly.

    ```yaml
    ownerReferences:
    - apiVersion: kubean.io/v1alpha1
        blockOwnerDeletion: true
        controller: true
        kind: Cluster
        name: mig-cluster
        uid: 6b81413c-270e-4720-b215-fe7cf1364d45 # (1)!
    resourceVersion: "15986"
    uid: 9075713e-79ca-436a-8765-db9d25e2667b
    ```

    1. Update this field; all configmap resources mentioned above need to be changed.

#### Restore Kpanda Related Resources

1. Restore `clusters.cluster.kpanda.io` resources.

    ```shell
    # Create resources
    kubectl apply -f kpanda-migrate-cluster.yaml
    ```

    ```shell
    # View the created clusters.cluster.kpanda.io/migrate-cluster resource information and get the uid 
    kubectl get clusters.cluster.kpanda.io mig-cluster -o yaml | grep "uid: "
    ```

    In this example, the retrieved uid is `6dc22267-ab04-430d-afd5-e332d509c7d3`.

2. Based on the `uid` obtained from the `clusters.cluster.kpanda.io` resource in the previous step,
   update the `ownerReferences` uid in `kpanda-migrate-cluster-secret.yaml`.

    ```yaml
    ownerReferences:
    - apiVersion: cluster.kpanda.io/v1alpha1
        blockOwnerDeletion: true
        controller: true
        kind: Cluster
        name: mig-cluster
        uid: 6dc22267-ab04-430d-afd5-e332d509c7d3 # (1)!
    resourceVersion: "1006873"
    uid: f726d1e3-c2aa-4341-88ad-ce9322d5d1ba
    type: Opaque
    ```

    1. Update this field

3. If needed, based on the `uid` obtained from the `clusters.cluster.kpanda.io` resource in the previous step,
   update the `ownerReferences` uid in `kpanda-migrate-cluster-setting.yaml`.

## Verification

After successfully executing the above steps, you can perform node deletion and addition operations on
the integrated worker clusters in the new environment. If there are any issues,
[please contact DaoCloud for official support](../index.md#contact-us)!
