# Create configuration items

Configuration items (ConfigMap) store non-confidential data in the form of key-value pairs to achieve the effect of mutual decoupling of configuration data and application code. Configuration items can be used as environment variables for containers, command-line parameters, or configuration files in storage volumes.

!!! note

     - The data saved in configuration items cannot exceed 1 MiB. If you need to store larger volumes of data, it is recommended to mount a storage volume or use an independent database or file service.

     - Configuration items do not provide confidentiality or encryption. If you want to store encrypted data, it is recommended to use [key](use-secret.md), or other third-party tools to ensure the privacy of data.

Two creation methods are supported:

- Graphical form creation
- YAML creation

## Prerequisites

- The container management module [connected to the Kubernetes cluster](../clusters/integrate-cluster.md) or [created the Kubernetes cluster](../clusters/create-cluster.md), and can access the UI interface of the cluster

- Completed a [namespace creation](../namespaces/createns.md), [user creation](../../../ghippo/user-guide/access-control/user.md), and authorize the user as [`NS Edit`](../permissions/permission-brief.md#ns-edit) role, for details, please refer to [Namespace Authorization](../permissions/cluster-ns-auth.md).

## Graphical form creation

1. Click the name of a cluster on the `Cluster List` page to enter `Cluster Details`.

     

2. In the left navigation bar, click `Configuration and Key` -> `Configuration Item`, and click the `Create Configuration Item` button in the upper right corner.

     

3. Fill in the configuration information on the `Create Configuration Item` page, and click `OK`.

     !!! note

         Click `Upload File` to import an existing file locally to quickly create configuration items.

     

4. After the creation is complete, click More on the right side of the configuration item to edit YAML, update, export, delete and other operations.

     

## YAML creation

1. Click the name of a cluster on the `Cluster List` page to enter `Cluster Details`.

     

2. In the left navigation bar, click `Configuration and Key` -> `Configuration Item`, and click the `YAML Create` button in the upper right corner.

     

3. Fill in or paste the configuration file prepared in advance, and then click `OK` in the lower right corner of the pop-up box.

     !!! note

         - Click `Import` to import an existing file locally to quickly create configuration items.
         - After filling in the data, click `Download` to save the configuration file locally.

     

4. After the creation is complete, click More on the right side of the configuration item to edit YAML, update, export, delete and other operations.

     

## configuration item YAML example

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

[Next step: Use configuration items](use-configmap.md){ .md-button .md-button--primary }