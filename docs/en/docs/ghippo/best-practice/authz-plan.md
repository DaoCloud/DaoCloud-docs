# Ordinary user authorization plan

Ordinary users refer to those who can use most of DCE's product modules and features (except management features), have certain operation rights to resources within the scope of authority, and can independently use resources to deploy applications.

The authorization and resource planning process for such users is shown in the following figure.

```mermaid
graph TB

    start([Start]) --> user[1. Create User]
    user --> ns[2. Prepare Kubernetes Namespace]
    ns --> ws[3. Prepare Workspace]
    ws --> ws-to-ns[4. Bind a workspace to namespace]
    ws-to-ns --> authu[5. Authorize a user with Workspace Editor]
    authu --> complete([End])
    
click user "https://docs.daocloud.io/en/ghippo/user-guide/access-control/user/"
click ns "https://docs.daocloud.io/en/kpanda/user-guide/namespaces/createns/"
click ws "https://docs.daocloud.io/en/ghippo/user-guide/workspace/workspace/"
click ws-to-ns "https://docs.daocloud.io/en/ghippo/user-guide/workspace/ws-to-ns-across-clus/"
click authu "https://docs.daocloud.io/en/ghippo/user-guide/workspace/wspermission/"

 classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
 classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
 classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;
 class user,ns,ws,ws-to-ns,authu cluster;
 class start,complete plain;
```

After authorization, the permissions of ordinary users in each module are:

- [Workbench](../permissions/amamba.md)
- [Microservice Engine](../permissions/skoala.md)
- [Service Mesh](../permissions/mspider.md) (need to repeat 2 - 4 to prepare mesh/mesh namespace and bind to workspace)
- [Observability](../../insight/intro/permission.md)
