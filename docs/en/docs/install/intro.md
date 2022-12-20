---
hide:
  - toc
---

#Introduction to installation

There are two editions of DCE 5.0: Community Edition and Commercial Edition.

| Version | Included Modules | Description |
| ------ | ------------------------------------------ ------------------ | ------------------------------- ------------------- |
| Community Edition| [Global Management](../ghippo/01ProductBrief/WhatisGhippo.md)<br />[Container Management](../kpanda/03ProductBrief/WhatisKPanda.md)<br />[Observability]( ../insight/03ProductBrief/WhatisInsight.md) | [Permanent free license](../dce/license0.md), the 3 modules will be updated continuously, and you can [download offline packages of submodules](../ download/dce5.md) |
| Commercial | [Global Management](../ghippo/01ProductBrief/WhatisGhippo.md)<br />[Container Management](../kpanda/03ProductBrief/WhatisKPanda.md)<br />[Observability]( ../insight/03ProductBrief/WhatisInsight.md)<br />[Application Workbench](../amamba/01ProductBrief/WhatisAmamba.md)<br />[Multi-Cloud Orchestration](../kairship/01product/whatiskairship. md)<br />[Microservice Engine](../skoala/intro/features.md)<br />[Service Mesh](../mspider/01Intro/WhatismSpider.md)<br />[Fine Choose Middleware](../middleware/midware.md)<br />[Cloud Native Network](../network/intro/what-is-net.md)<br />[Cloud Native Storage](. ./hwameistor/intro/what.md)<br />[Mirror Warehouse](../kangaroo/intro.md) | [Genuine Authorization](https://qingflow.com/f/e3291647), each module can Free combination on demand, you can [download the offline package of the submodule](../download/dce5.md) at any time |

### Community Edition Installation Process

The installation process of DCE 5.0 Community Edition is as follows:

```mermaid
flowchart TB

subgraph second[instructions for use]
    direction TB
    U[ ] -.-
    free[apply for free experience] --- kpanda[container management]
    kpanda --- ghippo [global management]
    ghippo --- insight [observability]
    insight -.- ask[ASK!!!]
end

subgraph first [install community edition]
    direction TB
    S[ ] -.-
    plan[resource planning] --> k8s[prepare K8s cluster]
    k8s --> tools[install dependencies]
    tools -.-> kind [via kind cluster<br>online install]
    tools -.-> s1 [via standard k8s cluster<br>online installation]
    tools -.-> s2 [via standard k8s cluster<br>offline install]
end

start([fa:fa-user DCE 5.0 Community Edition<br>Installation and usage process]) --> first
start --> second

classDef gray fill:#dddddd,stroke:#ffffff,stroke-width:px,color:#000000, font-size:15px;
classDef white fill:#ffffff,stroke:#000,stroke-width:px,color:#000,font-weight:bold
classDef spacewhite fill:#ffffff,stroke:#fff,stroke-width:0px,color:#000
classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill: #326ce5, stroke: #fff, stroke-width: 1px, color: #fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class plan,k8s,tools,kind,s1,s2,kpanda,ghippo,insight,free,ask cluster;
class start plain
class S,U spacewhite

click plan "https://docs.daocloud.io/install/community/resources/"
click k8s "https://docs.daocloud.io/install/community/kind/online/#kind"
click tools "https://docs.daocloud.io/install/install-tools/"
click kind "https://docs.daocloud.io/install/community/kind/online/"
click s1 "https://docs.daocloud.io/install/community/k8s/online/"
click s2 "https://docs.daocloud.io/install/community/k8s/offline/"

click kpanda "https://docs.daocloud.io/kpanda/03ProductBrief/WhatisKPanda/"
click ghippo "https://docs.daocloud.io/ghippo/01ProductBrief/WhatisGhippo/"
click insight "https://docs.daocloud.io/insight/03ProductBrief/WhatisInsight/"
click free "https://docs.daocloud.io/dce/license0/"
click ask "https://docs.daocloud.io/install/intro/#_4"
```

!!! tip

    - The blue text in the picture above can be clicked to jump
    - Refer to [Nanny Install DCE 5.0](../blogs/dce5-install1209.md)

### Commercial Edition Installation Process

The installation process of DCE 5.0 Commercial Edition is as follows:

```mermaid
flowchart TB

    start([fa:fa-user DCE 5.0 Commercial Edition<br>Installation Process]) -.- deploy[deployment plan]
    deploy --> tools[install dependencies on tinder node]
    tools --> download[download offline package]
    download --> config[edit and configure <br>clusterConfig.yaml]

    config -.compactClusterMode: false.-> typical[classic mode<br>multiple data centers]
    typical --> mng2[automatically create K8s management cluster<br>install Kubean Operator]
    typical --> gsc2[automatically create<br>K8s global service cluster<br>install DCE general components]

    config -.compactClusterMode: true.-> simple[simple mode<br>single data center]
    simple --> k8s1[automatically create<br>a K8s management cluster]
    simple --> gsc1 [automatically install all DCE components on this cluster]

classDef gray fill:#dddddd,stroke:#ffffff,stroke-width:1px,color:#000000, font-size:15px;
classDef white fill:#ffffff,stroke:#000,stroke-width:1px,color:#000,font-weight:bold
classDef spacewhite fill:#ffffff,stroke:#fff,stroke-width:0px,color:#000
classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill: #326ce5, stroke: #fff, stroke-width: 1px, color: #fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class deploy,tools,download,config cluster
class typical, k8s, mng2, gsc2, k8s2 k8s
class simple, start plain
class gsc1,k8s1 gray

click deploy "https://docs.daocloud.io/install/commercial/deploy-plan/"
click tools "https://docs.daocloud.io/install/install-tools/"
click download "https://docs.daocloud.io/install/commercial/download-file/"
click config "https://docs.daocloud.io/install/commercial/clusterconfig/"
click typical, simple "https://docs.daocloud.io/install/commercial/start-install/"
```

### contact us

DaoCloud Enterprise 5.0 is still in the early stages of release, and the installation process may change. Please bookmark this page and pay attention to the update dynamics, and more operation documents are also being produced.

- If you have any installation or usage problems, please [give feedback](https://github.com/DaoCloud/DaoCloud-docs/issues).

- Welcome to scan the QR code and communicate with developers freely:

    ![Community Edition Exchange Group](../images/assist.png)

[Download DCE 5.0](../download/dce5.md){ .md-button .md-button--primary }
[Apply for community free experience](../dce/license0.md){ .md-button .md-button--primary }