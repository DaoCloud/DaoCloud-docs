# 普通用户授权规划

普通用户是指能够使用 DCE 大部分产品模块及功能（管理功能除外），对权限范围内的资源有一定的操作权限，能够独立使用资源部署应用。

对这类用户的授权及资源规划流程如下图所示。

```mermaid
graph TB

    start([开始]) --> user[1. 创建用户]
    user --> ns[2. 准备 Kubernetes 命名空间]
    ns --> ws[3. 准备工作空间]
    ws --> ws-to-ns[4. 工作空间绑定命名空间]
    ws-to-ns --> authu[5. 给用户授权 Workspace Editor]
    authu --> complete([结束])
    
click user "https://docs.daocloud.io/ghippo/04UserGuide/01UserandAccess/User/"
click ns "https://docs.daocloud.io/kpanda/07UserGuide/Namespaces/createns/"
click ws "https://docs.daocloud.io/ghippo/04UserGuide/02Workspace/Workspaces/"
click ws-to-ns "https://docs.daocloud.io/ghippo/04UserGuide/02Workspace/ws-to-ns-across-clus/"
click authu "https://docs.daocloud.io/ghippo/04UserGuide/02Workspace/wspermission/"

 classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
 classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
 class user,ns,ws,ws-to-ns,authu k8s;
 class start,complete plain;
```

授权后普通用户在各模块的权限为：

- [应用工作台](../../permissions/amamba.md)
- [微服务引擎](../../permissions/skoala.md)
- [服务网格](../../permissions/mspider.md)（需要重复 2 - 4 准备网格/网格命名空间并绑定到工作空间）
- [可观测性](../../../insight/06UserGuide/permission.md)
