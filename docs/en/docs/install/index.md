# Overview

DCE 5.0 has two versions: Community package and Enterprise package.

The Community package includes Container Management, Global Management, and Insight modules, which can be used for free permanently. 

The Enterprise package can be purchased on demand with advanced modules such as Service Mesh, Microservice Engine, MultiCloud Management, Data Middleware, Image Repository, etc. in addtion to those modules contained in the Community package. It has more comprehensive features and can better meet the needs of production environments.

<table>
  <thead>
    <tr>
      <th>Version</th>
      <th>Included Modules</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Community Package</td>
      <td>
        <ul>
          <li><a href="../ghippo/intro/index.md">Global Management</a></li>
          <li><a href="../kpanda/intro/index.md">Container Management</a></li>
          <li><a href="../insight/intro/index.md">Observability</a></li>
        </ul>
      </td>
      <td>
        <a href="../dce/license0.md">Perpetual Free License</a>, 3 modules will be continuously updated and can be downloaded as offline packages
        <a href="../download/index.md">here</a>
      </td>
    </tr>
    <tr>
      <td>Enterprise Package</td>
      <td>
        <ul>
          <li><a href="../ghippo/intro/index.md">Global Management</a></li>
          <li><a href="../kpanda/intro/index.md">Container Management</a></li>
          <li><a href="../insight/intro/index.md">Observability</a></li>
          <li><a href="../amamba/intro/index.md">Application Workbench</a></li>
          <li><a href="../kairship/intro/index.md">Multi-Cloud Orchestration</a></li>
          <li><a href="../skoala/intro/index.md">Microservice Engine</a></li>
          <li><a href="../mspider/intro/index.md">Service Mesh</a></li>
          <li><a href="../middleware/index.md">Selected Middleware</a></li>
          <li><a href="../kangaroo/index.md">Image Repository</a></li>
        </ul>
      </td>
      <td>
        Contact us for licensing: email info@daocloud.io or call 400 002 6898. Modular flexibility available for each module, and offline packages can be downloaded
        <a href="../download/index.md">here</a>
      </td>
    </tr>
  </tbody>
</table>

## Install Community Package

The installation process of DCE 5.0 Community package is as follows:

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

subgraph first[Install Community Package]
    direction TB
    S[ ] -.-
    plan[Resource Planning] --> k8s[Prepare K8s Cluster] 
    k8s --> tools[Install Dependencies]
    tools -.-> kind[Online Install with kind]
    tools -.-> s1[Online Install with K8s]
    tools -.-> s2[Offline Install with K8s]
end

start([fa:fa-user DCE 5.0 Community Package Installation]) --> first
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

click kpanda "https://docs.daocloud.io/en/kpanda/intro/"
click ghippo "https://docs.daocloud.io/en/ghippo/intro/"
click insight "https://docs.daocloud.io/en/insight/intro/"
click free "https://docs.daocloud.io/en/dce/license0/"
click ask "https://docs.daocloud.io/en/install/intro/#contact-us"
```

!!! tip

     Click the blue text in the diagram, you can go to the corresponding page for details.

## Install Enterprise Package

The installation process of DCE 5.0 Commercial package is as follows:

```mermaid
flowchart TB

    start([fa:fa-user DCE 5.0 Enterprise Package<br>Installation Procedure]) -.- arch[Deployment Architecture]
    arch --> deploy[Deployment Requirements]
    deploy --> prepare[Preparation]
    prepare --> download[Download Offline Package]
    download --> config[Edit and Config<br>clusterConfig.yaml]
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

DaoCloud Enterprise 5.0 is still in the early stage of release, and the installation guide may change. Please bookmark this page and pay attention to the update dynamics.

- If you have any installation or usage problems, please [give us a feedback](https://github.com/DaoCloud/DaoCloud-docs/issues).

- Scan the QR code and communicate with developers freely:

     ![Community Package Exchange Group](https://docs.daocloud.io/daocloud-docs-images/docs/images/assist.png)

[Download DCE 5.0](../download/index.md){ .md-button .md-button--primary }
[Free Try](../dce/license0.md){ .md-button .md-button--primary }
