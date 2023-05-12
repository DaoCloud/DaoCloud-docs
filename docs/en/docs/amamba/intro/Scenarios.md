---
hide:
  - toc
---

# Application scenario

- Continuous delivery pipeline

    For complex business systems, the various stages from project creation, compilation, construction, self-verification, integration verification, class production verification, and online require a lot of manpower and time, and are prone to human factors and errors. Continuous integration and continuous delivery with the characteristics of standardization and automation, code change as a fluid unit, based on the release pipeline, pull all functions of development, testing, operation and maintenance, continuous, fast, high reliable release of software, can be a good solution to this problem.

    ** Automatic CI/CD pipeline **

    <!--![]()screenshots-->

- Implementation of continuous application delivery under cloud native based on pipeline + GitOps

    Thanks to the concept of GitOps, we use open source software Argo CD to practice Kubernetes application release. Users only need to submit Kubernetes YAML files to the code warehouse, and GitOps will automatically perceive the changes of YAML files and push the changes to the cluster automatically with the combination request function of the code warehouse. There is no need to learn the Kubernetes publishing command or manipulate the cluster directly.

    <!--![]()screenshots-->
