# Limited Scenario Migration from DCE 4.0 to DCE 5.0

## Environment Preparation

1. Available DCE 4.0 environment.
2. Available DCE 5.0 environment.
3. Kubernetes cluster for data restoration, referred to as the __restoration cluster__.

## Prerequisites

1. Install the CoreDNS plugin on DCE 4.0. Refer to [Install CoreDNS](https://dwiki.daocloud.io/pages/viewpage.action?pageId=36668076) for installation steps.

2. Migrate DCE 4.0 to DCE 5.0. Refer to [Integrate Cluster](../user-guide/clusters/integrate-cluster.md) for migration steps. The DCE 4.0 cluster migrated to DCE 5.0 is referred to as the __backup cluster__.

    !!! note

        When integrating the cluster, select __DaoCloud DCE4__ as the distribution.

3. Install Velero on the managed DCE 4.0 cluster. Refer to [Install Velero](../user-guide/backup/install-velero.md) for installation steps.

4. Migrate the restoration cluster to DCE 5.0, which can be done by creating a cluster or integrating it.

5. Install Velero on the restoration cluster. Refer to [Install Velero](../user-guide/backup/install-velero.md) for installation steps.

!!! note

    - The object storage configuration must be consistent between the managed DCE 4.0 cluster and the restoration cluster.
    - If you need to perform pod migration, open the __Migration Plugin Configuration__ switch in the form parameters (supported in Velero version 5.2.0+).


## Optional Configuration

If you need to perform pod migration, follow these steps after completing the prerequisites. These steps can be ignored for non-pod migration scenarios.

!!! note

    These steps are executed in the restoration cluster managed by DCE 5.0.

### Configure the Velero Plugin

1. After the Velero plugin is installed, you can use the following YAML file to configure the Velero plugin.

    !!! note

        When installing the Velero plugin, make sure to open the __Migration Plugin Configuration__ switch in the form parameters.

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      # any name can be used; Velero uses the labels (below) to identify it rather than the name
      name: velero-plugin-for-migration
      # must be in the velero namespace
      namespace: velero
      # the below labels should be used verbatim in your ConfigMap.
      labels:
        # this value-less label identifies the ConfigMap as
        # config for a plugin (i.e. the built-in restore item action plugin)
        velero.io/plugin-config: "velero-plugin-for-migration"
        # this label identifies the name and kind of plugin that this ConfigMap is for.
        velero.io/velero-plugin-for-migration: RestoreItemAction
    data:
      velero-plugin-for-migration: '{"resourcesSelector":{"includedNamespaces":["kube-system"],"excludedNamespaces":["default"],"includedResources":["pods","deployments","ingress"],"excludedResources":["secrets"],"skipRestoreKinds":["endpointslice"],"labelSelector":"app:dao-2048"},"resourcesConverter":[{"ingress":{"enabled":true,"apiVersion":"extensions/v1beat1"}}],"resourcesOperation":[{"kinds":["pod"],"domain":"labels","operation":{"add":{"key1":"values","key2":""},"remove":{"key3":"values","key4":""},"replace":{"key5":["source","dest"],"key6":["","dest"],"key7":["source",""]}}},{"kinds":["deployment","daemonset"],"domain":"annotations","scope":"resourceSpec","operation":{"add":{"key1":"values","key2":""},"remove":{"key3":"values","key4":""},"replace":{"key5":["source","dest"],"key6":["","dest"],"key7":["source",""]}}}]}'
    ```

    !!! note

        - Do not modify the name of the plugin configuration ConfigMap, and it must be created in the velero namespace.
        - Pay attention to whether you are filling in resource resources or kind in the plugin configuration.
        - After modifying the plugin configuration, restart the Velero pod.
        - The YAML below is a display style for the plugin configuration, and it needs to be converted to JSON and added to the ConfigMap.

    Refer to the following YAML and comments for how to configure __velero-plugin-for-migration__:

    ```yaml
    resourcesSelector: # The resources that the plugin needs to handle or ignore
      includedNamespaces: # Exclude the namespaces included in the backup
        - kube-system
      excludedNamespaces: # Do not handle the namespaces included in the backup
        - default
      includedResources:  # Handle the resources included in the backup
        - pods
        - deployments
        - ingress
      excludedResources:  # Do not handle the resources included in the backup
        - secrets
      skipRestoreKinds:
        - endpointslice  # The restore plugin skips the resources included in the backup, that is,
                         # it does not perform the restore operation. This resource needs to be included in
                         # includedResources to be captured by the plugin. This field needs to be filled
                         # with the resource kind, case insensitive.
      labelSelector: 'app:dao-2048'
    resourcesConverter: # The resources that the restore plugin needs to convert, does not support
                        # configuring specific resource field conversions
      - ingress:
          enabled: true
          apiVersion: extensions/v1beat1
    resourcesOperation: # The restore plugin modifies the annotations/labels of the resource/template
      - kinds: ['pod']  # Fill in the resource kind included in the backup, case insensitive
        domain: labels  # Handle the resources labels
        operation:
          add:
            key1: values # Add labels key1:values
            key2: ''
          remove:
            key3: values # Remove lables key3:values, match key,values
            key4: ''     # Remove lables key4, only match key, not match values
          replace:
            key5:   # Replace lables key5:source -> key5:dest
              - source
              - dest
            key6:   # Replace lables key6: -> key6:dest, not match key6 values
              - ""
              - dest
            key7:   # Replace lables key7:source -> key7:""
              - source
              - ""
      - kinds: ['deployment', 'daemonset'] # Fill in the resource kind included in the backup, case insensitive
        domain: annotations  # Handle the resources template annotations
        scope: resourceSpec  # Handle the resources template spec annotations or labels, depending on the domain configuration
        operation:
          add:
            key1: values # Add annotations key1:values
            key2: ''
          remove:
            key3: values # Remove annotations key3:values, match key,values
            key4: ''     # Remove annotations key4, only match key, not match values
          replace:
            key5:   # Replace annotations key5:source -> key5:dest
              - source
              - dest
            key6:   # Replace annotations key6: -> key6:dest, not match key6 values
              - ""
              - dest
            key7:   # Replace annotations key7:source -> key7:""
              - source
              - ""
    ```

2. After obtaining the velero-plugin-for-dce plugin configuration, perform chained operations on resources according to the configuration. For example, after ingress is processed by resourcesConverter, it will be processed by resourcesOperation.

### Image Repository Migration

The following steps describe how to migrate images between image repositories.

1. Integrate the DCE 4.0 image repository with the Kangaroo repository integration (admin).
   Refer to [Repository Integration](../../kangaroo/integrate/integrate-admin.md) for the operation steps.


    !!! note

        - Use the VIP address IP of dce-registry as the repository address.
        - Use the account and password of the DCE 4.0 administrator.

2. Create or integrate a Harbor repository in the administrator interface to migrate the source images.


3. Configure the target repository and synchronization rules in the Harbor repository instance. After the rules are triggered, Harbor will automatically pull images from dce-registry.


4. Click the name of the synchronization rule to view whether the image synchronization is successful.


### Network Policy Migration

#### Calico Network Policy Migration

Refer to the resource and data migration process to migrate the Calico service from DCE 4.0 to DCE 5.0.
Due to the different ippool names, services may be abnormal after migration. Manually delete the annotations in the service YAML after migration to ensure that the service starts properly.

!!! note

    - In DCE 4.0, the name is default-ipv4-ippool.
    - In DCE 5.0, the name is default-pool.

```yaml
annotations:
  dce.daocloud.io/parcel.net.type: calico
  dce.daocloud.io/parcel.net.type: default-ipv4-ippool
```

#### Parcel Underlay Network Policy Migration

The following steps describe how to migrate Parcel underlay network policies.

1. Install the spiderpool Helm application in the restoration cluster. Refer to [Install Spiderpool](../user-guide/helm/helm-app.md) for installation steps.


2. Go to the details page of the restoration cluster and select __Container Network__ -> __Network Configuration__ from the left menu.


3. Create a subnet and reserve IPs in the __Static IP Pool__.


4. Create a Multus CR with the same IP (the default pool can be left blank, and the port is consistent with the actual port).


5. Create a Velero DCE plugin configmap.

    ```yaml
    ---
      resourcesSelector:
        includedResources:
        - pods
        - deployments
      resourcesConverter:
      resourcesOperation:
      - kinds:
        - pod
        domain: annotations
        operation:
          replace:
            cni.projectcalico.org/ipv4pools:
            - '["default-ipv4-ippool"]'
            - default-pool
      - kinds:
        - deployment
        domain: annotations
        scope: resourceSpec
        operation:
          remove:
            dce.daocloud.io/parcel.egress.burst:
            dce.daocloud.io/parcel.egress.rate:
            dce.daocloud.io/parcel.ingress.burst:
            dce.daocloud.io/parcel.ingress.rate:
            dce.daocloud.io/parcel.net.type:
            dce.daocloud.io/parcel.net.value:
            dce.daocloud.io/parcel.ovs.network.status:
          add:
            ipam.spidernet.io/subnets: ' [ { "interface": "eth0", "ipv4": ["d5"] } ]'
            v1.multus-cni.io/default-network:  kube-system/d5multus
    ```

6. Verify whether the migration is successful.

    1. Check whether there are annotations in the application YAML.

        ```yaml
        annotations:
          ipam.spidernet.io/subnets: ' [ { "interface": "eth0", "ipv4": ["d5"] } ]'
          v1.multus-cni.io/default-network: kube-system/d5multus
        ```

    1. Check whether the pod IP is within the configured IP pool.
