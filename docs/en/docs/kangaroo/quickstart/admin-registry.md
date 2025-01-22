---
hide:
  - toc
MTPE: ModetaNiu
DATE: 2024-08-19
---

# Admin quickly uses the container registry to serve the platform

In DCE 5.0, there are two methods for managing container registries: Managed Harbor (self-built Harbor on DCE) and 
Integrated Registry (integrating external Harbor or Docker Registry).

- [Managed Harbor](../managed/intro.md)（suggested）
- [Integrated Registry](../integrate/integrate-admin/integrate-admin.md)

Harbor is mainly promoted as the Container Registry in DCE 5.0 to provide image services.

## Sharing public images 

Assuming that you have created a Managed Harbor or integrated to an external harbor, follow the steps below to 
share a public image with all namespaces:

```mermaid
graph TB

create[Create managed Harbor] --> setpublic[Create a registry space and set it to public]
--> push[Push image]
--> deploy[Deploy application]

classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class create,setpublic,push,deploy cluster;

click create "https://docs.daocloud.io/en/kangaroo/hosted/"
click setpublic "https://docs.daocloud.io/en/kangaroo/integrate/create-space/"
click push "https://docs.daocloud.io/en/kangaroo/quickstart/push/"
click deploy "https://docs.daocloud.io/en/kpanda/user-guide/workloads/create-deployment/"
```

Expected Result: When users on the platform deploy applications in the namespace, they can select images in the 
public registry space for deployment through the image selector.

![selecting images](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/admin01.png)

![images selected](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/admin02.png)

## Sharing private images

Assuming that you have created a Managed Harbor or integrated to an external harbor, follow the steps below 
to share a private image with the namespace under the specified workspace (tenant):

The prerequisites are:

```mermaid
graph TB

create[Workspace created] --> bind[Namespace and workspace binded]

classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class create,bind cluster;

click create "https://docs.daocloud.io/en/ghippo/user-guide/workspace/workspace/"
click bind "https://docs.daocloud.io/en/ghippo/user-guide/workspace/quota/"
```
Concrete steps are as follows:

```mermaid
graph TB

create[Create managed Harbor] --> setpublic[Create a registry space and set it to public]
--> push[Push image]
--> bind[Registry space binding workspace]
--> deploy[Deploy application]

classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class create,setpublic,push,bind,deploy cluster;

click create "https://docs.daocloud.io/en/kangaroo/hosted/"
click setpublic "https://docs.daocloud.io/en/kangaroo/integrate/create-space/"
click push "https://docs.daocloud.io/en/kangaroo/quickstart/push/"
click bind "https://docs.daocloud.io/en/kangaroo/integrate/integrate-admin/bind-to-ws/"
click deploy "https://docs.daocloud.io/en/kpanda/user-guide/workloads/create-deployment/"
```

Expected Result: Only when deploying applications in namespaces under this workspace, can you use the image selector 
to select private images under this registry space to deploy applications.

![selecting images](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/admin03.png)

![images selected](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/admin04.png)

!!! tip

    1. The connected Harbor can achieve the same effect as above.
    1. Docker Registry itself only has public images, so after accessing, the images will be open to all namespaces.
