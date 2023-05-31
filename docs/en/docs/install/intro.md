# Introduction to installation

There are two editions of DCE 5.0: Community Release and Commercial Release.

| Version | Included Modules | Description |
| ------ | ------------------------------------------ ------------------ | ------------------------------- ------------------- |
| Community Release| [Global Management](../ghippo/intro/what.md)<br />[Container Management](../kpanda/intro/what.md)<br />[Observability](../insight/intro/what.md) | [Permanent free license](../dce/license0.md), the 3 modules will be updated continuously, and you can [download offline packages of submodules](../download/dce5.md) |
| Commercial | [Global Management](../ghippo/intro/what.md)<br />[Container Management](../kpanda/intro/what.md)<br />[Observability]( ../insight/intro/what.md)<br />[Workbench](../amamba/intro/what.md)<br />[Multicloud Management](../kairship/intro/what.md)<br />[Microservice Engine](../skoala/intro/what.md)<br />[Service Mesh](../mspider/intro/what.md)<br />[Refined Middleware](../middleware/what.md)<br />[container registry](../kangaroo/what.md) | Contact us for authorization: email info@daocloud.io or call 400 002 6898, each module can be freely combined as needed, and you can [download the offline package of submodules](../download/dce5.md) at any time |

## Community Release installation process

The installation process of DCE 5.0 Community Release is as follows:

```mermaid
flowchart TB

subgraph second[Instructions]
    direction TB
    U[ ] -.-
    free[Apply for free trial] --- kpanda[Container Management]
    kpanda --- ghippo[Global Management]
    ghippo --- insight[Insight]
    insight -.- ask[ASK!!!]
end

subgraph first[Install Community Release]
    direction TB
    S[ ] -.-
    plan[Resource planning] --> k8s[Prepare K8s cluster] 
    k8s --> tools[Install dependencies]
    tools -.-> kind[Online install with kind]
    tools -.-> s1[Online install with k8s]
    tools -.-> s2[Offline install with k8s]
end

start([fa:fa-user DCE 5.0 Community Release Installation]) --> first
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

click plan "https://docs.daocloud.io/install/community/resources/"
click k8s "https://docs.daocloud.io/install/community/kind/online/#kind"
click tools "https://docs.daocloud.io/install/install-tools/"
click kind "https://docs.daocloud.io/install/community/kind/online/"
click s1 "https://docs.daocloud.io/install/community/k8s/online/"
click s2 "https://docs.daocloud.io/install/community/k8s/offline/"

click kpanda "https://docs.daocloud.io/kpanda/intro/what/"
click ghippo "https://docs.daocloud.io/ghippo/intro/what/"
click insight "https://docs.daocloud.io/insight/intro/what/"
click free "https://docs.daocloud.io/dce/license0/"
click ask "https://docs.daocloud.io/install/intro/#contact-us"
```

!!! tip

     The blue text in the picture above can be clicked to jump

## Commercial version installation process

The installation process of DCE 5.0 Commercial Release is as follows:

```mermaid
flowchart TB

    start([fa:fa-user DCE 5.0 Commercial Release<br>Installation Procedure]) -.- arch[Deployment architecture]
    arch --> deploy[Deployment requirements]
    deploy --> prepare[Preparation]
    prepare --> download[Download offline package]
    download --> config[Edit and config<br>clusterConfig.yaml]
    config --> install[Install]

classDef grey fill:#dddddd,stroke:#ffffff,stroke-width:1px,color:#000000, font-size:15px;
classDef white fill:#ffffff,stroke:#000,stroke-width:1px,color:#000,font-weight:bold
classDef spacewhite fill:#ffffff,stroke:#fff,stroke-width:0px,color:#000
classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class arch,deploy,prepare,download,config,install cluster
class start plain

click arch "https://docs.daocloud.io/en/install/commercial/deploy-arch/"
click deploy "https://docs.daocloud.io/en/install/commercial/deploy-requirements/"
click prepare "https://docs.daocloud.io/en/install/commercial/prepare/"
click download "https://docs.daocloud.io/en/install/commercial/start-install/#step-1-download-offline-package"
click config "https://docs.daocloud.io/en/install/commercial/start-install/#step-2-configure-the-cluster-configuration-file"
click install "https://docs.daocloud.io/en/install/commercial/start-install/#step-3-start-the-installation"
```

## Contact us

DaoCloud Enterprise 5.0 is still in the early stages of release, and the installation process may change. Please bookmark this page and pay attention to the update dynamics, and more operation documents are also being produced.

- If you have any installation or usage problems, please [give feedback](https://github.com/DaoCloud/DaoCloud-docs/issues).

- Welcome to scan the QR code and communicate with developers freely:

     ![Community Release Exchange Group](https://docs.daocloud.io/daocloud-docs-images/docs/images/assist.png)

[Download DCE 5.0](../download/dce5.md){ .md-button .md-button--primary }
[Free Trial Now](../dce/license0.md){ .md-button .md-button--primary }
