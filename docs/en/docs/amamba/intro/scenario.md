---
hide:
  - toc
---

# Use Cases

- Pipeline for Continuous Delivery

    For complex business systems, each phase, from project creation, compilation, building, unit tests, integrated tests, pre-production verification, to production release, requires a lot of manpower and time, and is prone to human errors. Continuous Integration/Continuous Delivery (CI/CD) can solve this problem by standardizing and automating the process, using code changes as a flow unit, based on the release pipeline, connecting all features of development, testing, and operations, to continuously, quickly, and reliably deliver applications.

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/scenarios01.png)

- Cloud-native CD Based on GitOps and Pipelines

    Workbench incorporates the GitOps concept and Argo CD, an open-source software, to deploy applications in Kubernetes.
    Users only need to submit YAML files to the code repository. GitOps can automatically detect the changes in the YAML files and, with the help of merge requests in the code repository, automatically push these changes to the cluster, without the need to learn the deployment commands of Kubernetes or operate the cluster directly.

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/scenarios02.png)