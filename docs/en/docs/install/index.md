---
MTPE: windsonsea
date: 2024-05-11
---

# Overview

DCE has two versions: DCE Community and DCE Enterprise.

- DCE Community includes Container Management, Global Management, and Insight modules,
  which can be used for free permanently.

- DCE Enterprise can be purchased on demand with advanced modules such as Service Mesh,
  Microservice Engine, Multicloud Management, Data Middleware, Container Registry,
  Cloud Edge Collaboration, and Containerized VM on the basis of DCE Community.
  It has more comprehensive features and applicable to a variety of production environments.

<table>
  <thead>
    <tr>
      <th>Releases</th>
      <th>Modules</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DCE Community</td>
      <td>
        <ul>
          <li><a href="../ghippo/intro/">Global Management</a></li>
          <li><a href="../kpanda/intro/">Container Management</a></li>
          <li><a href="../insight/intro/">Insight</a></li>
        </ul>
      </td>
      <td>
        <a href="../dce/license0/">Permanently free license</a>, the 3 modules will receive continuous updates, and you can <a href="https://docs.daocloud.io/en/download/#download-modules">download offline packages for sub-modules</a> anytime.
      </td>
    </tr>
    <tr>
      <td>DCE Enterprise</td>
      <td> <p>On top of DCE Community, more modules are added:</p>
        <ul>
          <li><a href="../amamba/intro/"><span style="white-space: nowrap;">Workbench</span></a></li>
          <li><a href="../kairship/intro/">Multicloud Management</a></li>
          <li><a href="../skoala/intro/"><span style="white-space: nowrap;">Microservice Engine</span></a></li>
          <li><a href="../mspider/intro/">Service Mesh</a></li>
          <li><a href="../middleware/"><span style="white-space: nowrap;">Middleware</span></a></li>
          <li><a href="../kangaroo/intro/">Container Registry</a></li>
          <li><a href="../kant/intro/">Cloud Edge Collaboration</a></li>
          <li><a href="../virtnest/intro/">Containerized VM</a></li>
          <li><a href="../topohub/intro/">Device Management</a></li>
          <li><a href="../network/intro/">Networking</a></li>
          <li><a href="../storage/hwameistor/intro/">HwameiStor</a></li>
        </ul>
      </td>
      <td>
        Contact us for licensing: email info@daocloud.io or call 400 002 6898. You can freely combine the modules as needed, and <a href="https://docs.daocloud.io/en/download/#download-modules">download offline packages for sub-modules</a> anytime.
      </td>
    </tr>
  </tbody>
</table>

## Install DCE Community

The installation process of DCE Community is as follows:

```mermaid
flowchart TB

subgraph second[Instructions]
    direction TB
    free[Apply for free trial] --- kpanda[Container Management]
    kpanda --- ghippo[Global Management]
    ghippo --- insight[Insight]
    insight -.- ask[ASK!!!]
end

subgraph first[Install DCE Community]
    direction TB
    plan[Resource Planning] --> k8s[Prepare K8s Cluster]
    k8s --> tools[Install Dependencies]
    tools -.-> kind[Online Install with kind]
    tools -.-> s1[Online Install with K8s]
    tools -.-> s2[Offline Install with K8s]
end

start([fa:fa-user DCE Community<br>Installation Process]) --> first
start --> second

click plan "community/resources/"
click k8s "community/kind/online/#install-kind-cluster"
click tools "install-tools/"
click kind "community/kind/online/"
click s1 "community/k8s/online/"
click s2 "community/k8s/offline/"
click kpanda "../kpanda/intro/"
click ghippo "../ghippo/intro/"
click insight "../insight/intro/"
click free "../dce/license0/"
click ask "#contact-us"
```

## Install DCE Enterprise

The installation process of DCE Enterprise is as follows:

```mermaid
flowchart TB

    start([fa:fa-user DCE Enterprise<br>Installation Process]) -.- arch[Learn Deployment Architecture]
    arch --> deploy[Check Deployment Requirements]
    deploy --> prepare[Prepare Environment]
    prepare --> download[Download Offline Package]
    download --> config[Edit<br>clusterConfig.yaml]
    
    config -.-> other-k8s[Install on<br>Different K8s]
    config -.-> install[Normal Installation]
    config -.-> other-os[Install on<br>Different Linux]

    other-k8s -.-> ocp[Install on<br>OpenShift OCP]
    other-k8s -.-> ali[Install on<br>Alibaba Cloud ECS]

    other-os -.-> uos[Install on UOS]
    other-os -.-> oracle[Install on<br>Oracle Linux]
    other-os -.-> tencent[Install on<br>TencentOS Server]
    other-os -.-> other[Install on<br>Other Linux]

click arch "commercial/deploy-arch/"
click deploy "commercial/deploy-requirements/"
click prepare "commercial/prepare/"
click download "commercial/start-install/#download-offline-package"
click config "commercial/start-install/#edit-clusterconfigyaml"
click install "commercial/start-install/#install"
click ocp "k8s-install/ocp-install-dce5.0/"
click ali "k8s-install/ecs-install-dce5.0/"
click uos "os-install/uos-v20-install-dce5.0/"
click oracle "os-install/oracleLinux-install-dce5.0/"
click tencent "os-install/TencentOS-install-dce5.0/"
click other "os-install/otherlinux/"
```

## Contact us

The installation guide may change. Please bookmark this page and follow the update information.

- If you have any installation or usage problems, please
  [give us a feedback](https://github.com/DaoCloud/DaoCloud-docs/issues).

- Scan the QR code and communicate with developers freely:

    ![DCE Community Exchange Group](https://docs.daocloud.io/daocloud-docs-images/docs/images/assist.png)

[Download Center](https://docs.daocloud.io/en/download/){ .md-button }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button }
