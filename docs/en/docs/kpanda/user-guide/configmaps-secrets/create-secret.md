# Create Secret

A secret is a resource object used to store and manage sensitive information such as passwords,
OAuth tokens, SSH, TLS credentials, etc. Using keys means you don't need to include sensitive secrets
in your application code.

Secrets can be used in some cases:

- Used as an environment variable of the container to provide some necessary information
  required during the running of the container.
- Use secrets as pod data volumes.
- As the identity authentication credential for the container registry
  when the kubelet pulls the container image.

You can create ConfigMaps with two methods:

- Graphical form creation
- YAML creation

## Prerequisites

- [Integrated the Kubernetes cluster](../clusters/integrate-cluster.md) or
  [created the Kubernetes cluster](../clusters/create-cluster.md),
  and you can access the UI interface of the cluster

- Created a [namespace](../namespaces/createns.md),
  [user](../../../ghippo/user-guide/access-control/user.md),
  and authorized the user as [NS Editor](../permissions/permission-brief.md#ns-editor).
  For details, refer to [Namespace Authorization](../permissions/cluster-ns-auth.md).

## Create secret with wizard

1. Click the name of a cluster on the __Clusters__ page to enter __Cluster Details__ .

     

2. In the left navigation bar, click __ConfigMap and Secret__ -> __Secret__ , and click the __Create Secret__ button in the upper right corner.

     

3. Fill in the configuration information on the __Create Secret__ page, and click __OK__ .

     

     Note when filling in the configuration:

     - The name of the key must be unique within the same namespace
     - Key type:
         - Default (Opaque): Kubernetes default key type, which supports arbitrary data defined by users.
         - TLS (kubernetes.io/tls): credentials for TLS client or server data access.
         - Container registry information (kubernetes.io/dockerconfigjson): Credentials for Container registry access.
         - username and password (kubernetes.io/basic-auth): Credentials for basic authentication.
         - Custom: the type customized by the user according to business needs.
     - Key data: the data stored in the key, the parameters that need to be filled in are different for different data
         - When the key type is default (Opaque)/custom: multiple key-value pairs can be filled in.
         - When the key type is TLS (kubernetes.io/tls): you need to fill in the certificate certificate and private key data. Certificates are self-signed or CA-signed credentials used for authentication. A certificate request is a request for a signature and needs to be signed with a private key.
         - When the key type is container registry information (kubernetes.io/dockerconfigjson): you need to fill in the account and password of the private container registry.
         - When the key type is username and password (kubernetes.io/basic-auth): Username and password need to be specified.

## YAML creation

1. Click the name of a cluster on the __Clusters__ page to enter __Cluster Details__ .

     

2. In the left navigation bar, click __ConfigMap and Secret__ -> __Secret__ , and click the __YAML Create__ button in the upper right corner.

     

3. Fill in the YAML configuration on the __Create with YAML__ page, and click __OK__ .

     > Supports importing YAML files from local or downloading and saving filled files to local.

     

## key YAML example

     ```yaml
     apiVersion: v1
     kind: Secret
     metadata:
       name: secretdemo
     type: Opaque
     data:
       username: ****
       password: ****
     ```

[Next step: use secret](use-secret.md){ .md-button .md-button--primary }