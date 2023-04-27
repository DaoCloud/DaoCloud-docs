---
hide:
  - toc
---

# Applicable scenarios

- Continuous delivery pipeline

    For complex business systems, each stage from project creation, compilation, construction, self-inspection, integration verification, class production verification, and launch requires a lot of manpower and time, and is prone to errors due to human factors.
    Due to the standardization and automation characteristics of continuous integration and continuous delivery, code changes are used as flow units, and based on the release pipeline, all functions of development, testing, and operation and maintenance are pulled through, and software is released continuously, quickly, and with high reliability, which can solve this problem very well. question.

    **Automated CI/CD pipeline**

    

- Based on pipeline + GitOps to achieve continuous delivery of applications under cloud native

    Thanks to the concept of GitOps, the open source software Argo CD is used to practice Kubernetes application release.
    Users only need to submit the Kubernetes YAML file to the codebase, and GitOps will automatically sense the changes in the YAML file, and cooperate with the merge request function of the codebase.
    Automatically push the changes of the YAML file to the cluster, the whole process does not need to learn Kubernetes release commands, and does not need to directly operate the cluster.

    