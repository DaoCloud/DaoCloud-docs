# Create ConfigMaps

ConfigMaps store non-confidential data in the form of key-value pairs to achieve the effect of
mutual decoupling of configuration data and application code. ConfigMaps can be used as
environment variables for containers, command-line parameters, or configuration files in storage volumes.

!!! note

     - The data saved in ConfigMaps cannot exceed 1 MiB. If you need to store larger volumes of data,
       it is recommended to mount a storage volume or use an independent database or file service.

     - ConfigMaps do not provide confidentiality or encryption. If you want to store encrypted data,
       it is recommended to use [secret](use-secret.md), or other third-party tools to ensure the
       privacy of data.

You can create ConfigMaps with two methods:

- Graphical form creation
- YAML creation

## Prerequisites

- [Integrated the Kubernetes cluster](../clusters/integrate-cluster.md) or
  [created the Kubernetes cluster](../clusters/create-cluster.md),
  and you can access the UI interface of the cluster.

- Created a [namespace](../namespaces/createns.md),
  [user](../../../ghippo/user-guide/access-control/user.md),
  and authorized the user as [NS Editor](../permissions/permission-brief.md#ns-editor).
  For details, refer to [Namespace Authorization](../permissions/cluster-ns-auth.md).

## Graphical form creation

1. Click the name of a cluster on the __Clusters__ page to enter __Cluster Details__ .

     

2. In the left navigation bar, click __ConfigMap and Secret__ -> __ConfigMap__ , and click the __Create ConfigMap__ button in the upper right corner.

     

3. Fill in the configuration information on the __Create ConfigMap__ page, and click __OK__ .

     !!! note

         Click __Upload File__ to import an existing file locally to quickly create ConfigMaps.

     

4. After the creation is complete, click More on the right side of the ConfigMap to edit YAML, update, export, delete and other operations.

     

## YAML creation

1. Click the name of a cluster on the __Clusters__ page to enter __Cluster Details__ .

     

2. In the left navigation bar, click __ConfigMap and Secret__ -> __ConfigMap__ , and click the __YAML Create__ button in the upper right corner.

     

3. Fill in or paste the configuration file prepared in advance, and then click __OK__ in the lower right corner of the pop-up box.

     !!! note

         - Click __Import__ to import an existing file locally to quickly create ConfigMaps.
         - After filling in the data, click __Download__ to save the configuration file locally.

     

4. After the creation is complete, click More on the right side of the ConfigMap to edit YAML, update, export, delete and other operations.

     

## ConfigMap YAML example

     ```yaml
     kind: ConfigMap
     apiVersion: v1
     metadata:
       name: kube-root-ca.crt
       namespace: default
       annotations:
     data:
       version: '1.0'
     ```

[Next step: Use ConfigMaps](use-configmap.md){ .md-button .md-button--primary }