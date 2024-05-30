---
MTPE: FanLin
Date: 2024-02-29
---

# Manage Helm Repository

The Helm repository is a repository for storing and publishing Charts. The Helm application module supports HTTP(s) protocol to access Chart packages in the repository. By default, the system has 4 built-in helm repos as shown in the table below to meet common needs in the production process of enterprises.

| repository | Description | Example |
| --------- | --------------------------------------- --------------------- | ------------ |
| partner | Various high-quality features provided by ecological partners Chart | tidb |
| system | Chart that must be relied upon by system core functional components and some advanced features. For example, insight-agent must be installed to obtain cluster monitoring information | Insight |
| addon | Common Chart in business cases | cert-manager |
| community | The most popular open source components in the Kubernetes community Chart | Istio |

In addition to the above preset repositories, you can also add third-party Helm repositories yourself. This page will introduce how to add and update third-party Helm repositories.

## Prerequisites

- [Integrated the Kubernetes cluster](../clusters/integrate-cluster.md) or
  [created the Kubernetes cluster](../clusters/create-cluster.md),
  and you can access the UI interface of the cluster.

- Created a [namespace](../namespaces/createns.md),
  [user](../../../ghippo/user-guide/access-control/user.md),
  and granted [`NS Admin`](../permissions/permission-brief.md#ns-admin) or higher permissions to the user.
  For details, refer to [Namespace Authorization](../permissions/cluster-ns-auth.md).

- If using a private repository, you should have read and write permissions to the repository.

## Introduce third-party Helm repository

The following takes the public container repository of Kubevela as an example to introduce and manage the helm repo.

1. Find the cluster that needs to be imported into the third-party helm repo, click the cluster name, and enter cluster details.

    ![Clusters](../images/crd01.png)

2. In the left navigation bar, click __Helm Apps__ -> __Helm Repositories__ to enter the helm repo page.

    ![Helm Repo](../images/helmrepo01.png)

3. Click the __Create Repository__ button on the helm repo page to enter the Create repository page, and configure relevant parameters according to the table below.

     - Repository name: Set the repository name. Up to 63 characters, can only contain lowercase letters, numbers and separator __-__ , and must start and end with lowercase letters or numbers, such as kubevela
     - URL: the http(s) address used to point to the target helm repo. For example <https://charts.kubevela.net/core>
     - Authentication: The method used for identity verification after connecting to the repository address. For public repositories, you can choose __None__ , private repositories need to enter username/password for identity verification
     - Labels: Add tags for this Helm repository. For example key: repo4; value: Kubevela
     - Annotations: Add annotations to the Helm repository. For example key: repo4; value: Kubevela
     - Description: Add a description for this Helm repository. Example: This is a Kubevela public Helm repository

    ![Config](../images/helmrepo02.png)

4. Click __OK__ to complete the creation of the Helm repository. The page will automatically jump to the list of Helm repositories.

    ![Confirm](../images/helmrepo03.png)

## Update the Helm repository

When the address information of the helm repo changes, the address, authentication method, label, annotation, and description information of the helm repo can be updated.

1. Find the cluster where the repository to be updated is located, click the cluster name, and enter cluster details .

    ![Clusters](../images/crd01.png)

2. In the left navigation bar, click __Helm Apps__ -> __Helm Repositories__ to enter the helm repo list page.

    ![Helm Repo](../images/helmrepo01.png)

3. Find the Helm repository that needs to be updated on the repository list page, click the __⋮__ button on the right side of the list, and click __Update__ in the pop-up menu.

    ![Update](../images/helmrepo04.png)

4. Update on the __Update Helm Repository__ page, and click __OK__ when finished.

    ![Confirm](../images/helmrepo05.png)

5. Return to the helm repo list, and the screen prompts that the update is successful.

## Delete the Helm repository

In addition to importing and updating repositorys, you can also delete unnecessary repositories, including system preset repositories and third-party repositories.

1. Find the cluster where the repository to be deleted is located, click the cluster name, and enter cluster details .

    ![Clusters](../images/crd01.png)

2. In the left navigation bar, click __Helm Apps__ -> __Helm Repositories__ to enter the helm repo list page.

    ![Helm Repo](../images/helmrepo01.png)

3. Find the Helm repository that needs to be updated on the repository list page, click the __⋮__ button on the right side of the list, and click __Delete__ in the pop-up menu.

    ![Delete](../images/helmrepo07.png)

4. Enter the repository name to confirm, and click __Delete__ .

    ![Confirm](../images/helmrepo08.png)

5. Return to the list of Helm repositories, and the screen prompts that the deletion is successful.
