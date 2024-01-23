# Manage Helm repository

The Helm repository is a repository for storing and publishing Charts. The Helm application module supports HTTP(s) protocol to access Chart packages in the repository. By default, the system has 4 built-in helm repos as shown in the table below to meet common needs in the production process of enterprises.

| registry | Description | Example |
| --------- | --------------------------------------- --------------------- | ------------ |
| partner | Various high-quality features provided by ecological partners Chart | tidb |
| system | Chart that must be relied upon by system core functional components and some advanced features. For example, insight-agent must be installed to obtain cluster monitoring information | Insight |
| addon | Common Chart in business cases | cert-manager |
| community | The most popular open source components in the Kubernetes community Chart | Istio |

In addition to the above preset repositories, you can also add third-party Helm repositories yourself. This page will introduce how to add and update third-party Helm repositories.

## Prerequisites

- The container management module [connected to the Kubernetes cluster](../clusters/integrate-cluster.md) or [created the Kubernetes cluster](../clusters/create-cluster.md), and can access the UI interface of the cluster

- Completed a [namespace creation](../namespaces/createns.md), [user creation](../../../ghippo/user-guide/access-control/user.md), and grant [`NS Admin`](../permissions/permission-brief.md#ns-admin) or higher permissions to the user. For details, refer to [Namespace Authorization](../permissions/cluster-ns-auth.md).

- If using a private registry, the current operating user should have read and write permissions to the private registry.

## Introduce third-party Helm repository

The following takes the public container registry of Kubevela as an example to introduce and manage the helm repo.

1. Find the cluster that needs to be imported into the third-party helm repo, click the cluster name, and enter __Cluster Details__ .

     

2. In the left navigation bar, click __Helm Apps__ -> __helm repo__ to enter the helm repo page.

     

3. Click the __Create registry__ button on the helm repo page to enter the Create registry page, and configure relevant parameters according to the table below.

     - registry name: Set the registry name. Up to 63 characters, can only contain lowercase letters, numbers and separator __-__ , and must start and end with lowercase letters or numbers, such as kubevela
     - registry address: the http(s) address used to point to the target helm repo. For example <https://charts.kubevela.net/core>
     - Authentication method: The method used for identity verification after connecting to the registry address. For public repositories, you can choose __None__ , private repositories need to enter username/password for identity verification
     - Tags: Add tags for this Helm repository. For example key: repo4; value: Kubevela
     - Annotations: Add annotations to the Helm repository. For example key: repo4; value: Kubevela
     - Description: Add a description for this Helm repository. Example: This is a Kubevela public Helm repository

     

4. Click __OK__ to complete the creation of the Helm repository. The page will automatically jump to the list of Helm repositories.

     

## Update the Helm repository

When the address information of the helm repo changes, the address, authentication method, label, annotation, and description information of the helm repo can be updated.

1. Find the cluster where the registry to be updated is located, click the cluster name, and enter __Cluster Details__ .

     

2. In the left navigation bar, click __Helm Apps__ -> __helm repo__ to enter the helm repo list page.

     

3. Find the Helm repository that needs to be updated on the repository list page, click the __⋮__ button on the right side of the list, and click __Update__ in the pop-up menu.

     

4. Update on the __Edit Helm Repository__ page, and click __OK__ when finished.

     

5. Return to the helm repo list, and the screen prompts that the update is successful.

## Delete the Helm repository

In addition to importing and updating registrys, you can also delete unnecessary registrys, including system preset registrys and third-party registrys.

1. Find the cluster where the registry to be deleted is located, click the cluster name, and enter __Cluster Details__ .

     

2. In the left navigation bar, click __Helm Apps__ -> __helm repo__ to enter the helm repo list page.

     

3. Find the Helm repository that needs to be updated on the repository list page, click the __⋮__ button on the right side of the list, and click __Delete__ in the pop-up menu.

     

4. Enter the registry name to confirm, and click __Delete__ .

     

5. Return to the list of Helm repositories, and the screen prompts that the deletion is successful.