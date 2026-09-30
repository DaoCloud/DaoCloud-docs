---
hide:
  - toc
---

# Workbench Features

The Workbench is a module included in DCE Enterprise Package, providing the following features.

| **Features** | **Description** |
|-------------|---------|
| Application Management | <ul><li>Supports "polyform" cloud native applications in various cloud native scenarios, including Kubernetes native applications, Helm applications, OAM applications, and more.</li><li>Provides full lifecycle management for cloud native applications, such as scaling applications, viewing logs and monitoring, and updating applications.</li><li>Supports microservice applications based on the SpringCloud, Dubbo, and ServiceMesh frameworks to achieve microservice governance, and seamlessly integrates with DCE's <a href="../../skoala/intro/index.md">Microservice Engine</a> and <a href="../../mspider/intro/index.md">Service Mesh</a>.</li></ul> |
| Pipeline Orchestration | <ul><li>Supports four modes of creating pipelines: custom creation, creation based on Jenkinsfile, creation based on templates, and creation of multi-branch pipelines.</li><li>Supports graphical pipeline editing.</li><li>Supports building applications from Git source code, Jar packages, Helm charts, and container images.</li></ul> |
| Credential Management | <ul><li>Provides credential management of different types for the code repositories and image repositories used in pipelines.</li></ul> |
| Continuous Deployment | <ul><li>Introduces the GitOps concept to achieve continuous deployment of applications, which is used to control the application release and deployment delivery process after code building.</li><li>Based on Argo CD, deploys enterprise applications to production environments frequently and continuously in an automated manner.</li><li>Provides creation, synchronization, and deletion management of Argo CD Applications.</li></ul> |
| Repository Management | <ul><li>Supports importing Git code repositories. After importing, you can use the repository in continuous deployment to continuously deploy applications.</li></ul> |
| Canary Release | <ul><li>Canary release can ensure the stability of the overall system, allowing problems to be discovered and adjusted during the initial canary phase, reducing the scope of impact of the problems.</li><li>Supports advanced release policies such as canary release, blue-green deployment, and A/B Testing.</li><li>Canary release supports an automated progressive release process.</li><li>Supports quick application rollback through monitoring metric analysis.</li></ul> |
