---
hide:
  - toc
---

# Introduction to installation

There are two releases of DCE 5.0: Community Release and Commercial Release.

| Version | Included Modules | Description |
| ------ | ------------------------------------------ ------------------ | ------------------------------- ------------------- |
| Community Release| [Global Management](../ghippo/intro/what.md)<br />[Container Management](../kpanda/intro/WhatisKPanda.md)<br />[Observability]( ../insight/03ProductBrief/WhatisInsight.md) | [Permanent free license](../dce/license0.md), the 3 modules will be updated continuously, and you can [download offline packages of submodules](../ download/dce5.md) |
| Commercial | [Global Management](../ghippo/intro/what.md)<br />[Container Management](../kpanda/intro/WhatisKPanda.md)<br />[Observability]( ../insight/03ProductBrief/WhatisInsight.md)<br />[Application Workbench](../amamba/intro/WhatisAmamba.md)<br />[Multicloud Orchestration](../kairship/01product/whatiskairship. md)<br />[Microservice Engine](../skoala/intro/features.md)<br />[Service Mesh](../mspide../mspider/intro/WhatismSpider.md)<br />[Choose Middleware](../middleware/midware.md)<br />[Cloud Native Network](../network/intro/what-is-net.md)<br />[Cloud Native Storage](../storage/intro.md)<br />[container registry](../kangaroo/intro.md) | [Genuine Authorization](https://qingflow.com/f/e3291647), each module can Free combination on demand, you can [download the offline package of the submodule](../download/dce5.md) at any time |

## Community Release Installation Process

The installation process of DCE 5.0 Community Release is as follows:

```mermaid
flowchart TB

subgraph second[Instructions for use]
    direction TB
    U[ ] -.-
    free[Free Trial] --- kpanda[Container Management]
    kpanda --- ghippo[Global Management]
    ghippo --- insight[Observability]
    insight -.- ask[ASK!!!]
end

subgraph first[Install community release]
    direction TB
    S[ ] -.-
    plan[resource planning] --> k8s[Prepare K8s cluster]
    k8s --> tools[Install dependencies]
    tools -.-> kind[Online install with kind]
    tools -.-> s1[Online install with k8s]
    tools -.-> s2[Offline install with k8s]
end

start([fa:fa-user DCE 5.0 Community Release Installation and Usage Process]) --> first
start --> second

classDef grey fill:#dddddd,stroke:#ffffff,stroke-width:px,color:#000000, font-size:15px;
classDef white fill:#ffffff,stroke:#000,stroke-width:px,color:#000,font-weight:bold
classDef spacewhite fill:#ffffff,stroke:#fff,stroke-width:0px,color:#000
classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class plan,k8s,tools,kind,s1,s2,kpanda,ghippo,insight,free,ask cluster;
class start plain
class S,U spacewhite

click plan "https://docs.daocloud.io/en/install/community/resources/"
click k8s "https://docs.daocloud.io/en/install/community/kind/online/#kind"
click tools "https://docs.daocloud.io/en/install/install-tools/"
click kind "https://docs.daocloud.io/en/install/community/kind/online/"
click s1 "https://docs.daocloud.io/en/install/community/k8s/online/"
click s2 "https://docs.daocloud.io/en/install/community/k8s/offline/"

click kpanda "https://docs.daocloud.io/en/kpanda/03ProductBrief/WhatisKPanda/"
click ghippo "https://docs.daocloud.io/en/ghippo/01ProductBrief/WhatisGhippo/"
click insight "https://docs.daocloud.io/en/insight/03ProductBrief/WhatisInsight/"
click free "https://docs.daocloud.io/en/dce/license0/"
click ask "https://docs.daocloud.io/en/install/intro/#_4"
```

!!! tip

    - The blue text in the picture above can be clicked to jump
    - Refer to [Nanny Install DCE 5.0](../blogs/dce5-install1209.md)

## Commercial Release Installation Process

The installation process of DCE 5.0 Commercial Release is as follows:

```mermaid
flowchart TB

    start([fa:fa-user DCE 5.0 Commercial Release Installation Process]) -.- deploy[Deployment requirement]
    deploy --> tools[Install dependencies on bootstrapping node]
    tools --> download[Download offline package]
    download --> config[Edit clusterConfig.yaml]

    config -.compactClusterMode: false.-> typical[Classic mode with multiple data centers]
    typical --> mng2[Create K8s management cluster<br>and install Kubean Operator]
    typical --> gsc2[Create K8s global service cluster<br>and install DCE components]

    config -.compactClusterMode: true.-> simple[Simple mode with<br>single data center]
    simple --> k8s1[Create a K8s<br>management cluster]
    simple --> gsc1[Install all DCE<br>components on this cluster]

classDef grey fill:#dddddd,stroke:#ffffff,stroke-width:1px,color:#000000, font-size:15px;
classDef white fill:#ffffff,stroke:#000,stroke-width:1px,color:#000,font-weight:bold
classDef spacewhite fill:#ffffff,stroke:#fff,stroke-width:0px,color:#000
classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class deploy,tools,download,config cluster
class typical,k8s,mng2,gsc2,k8s2 k8s
class simple,start plain
class gsc1,k8s1 grey

click deploy "https://docs.daocloud.io/en/install/commercial/deploy-plan/"
click tools "https://docs.daocloud.io/en/install/install-tools/"
click download "https://docs.daocloud.io/en/install/commercial/download-file/"
click config "https://docs.daocloud.io/en/install/commercial/clusterconfig/"
click typical,simple "https://docs.daocloud.io/en/install/commercial/start-install/"
```

### Contact us

DaoCloud Enterprise 5.0 is still in the early stages of release, and the installation process may change. Please bookmark this page and pay attention to the update dynamics, and more operation documents are also being produced.

- If you have any installation or usage problems, please [give feedback](https://github.com/DaoCloud/DaoCloud-docs/issues).

- Welcome to scan the QR code and communicate with developers freely:

    

[Download DCE 5.0](../download/dce5.md){ .md-button .md-button--primary }
[Free Trial](../dce/license0.md){ .md-button .md-button--primary }