---
MTPE: windsonsea
Date: 2024-07-22
---

# Notebook Not Controlled by Queue Quota

In the Intelligent Engine module, when users create a Notebook,
they find that even if the selected queue lacks resources, the Notebook can still be created successfully.

## Issue 01: Unsupported Kubernetes Version

- Analysis:

    The queue management capability in intelligent computing is provided by [Kueue](https://kueue.sigs.k8s.io/),
    and the Notebook service is provided through [JupyterHub](https://jupyter.org/hub). JupyterHub has high
    requirements for the Kubernetes version. For versions below v1.27, even if queue quotas are set in DCE 5.0,
    and users select the quota when creating a Notebook, the Notebook will not actually be restricted by the queue quota.

    ![local-queue-initialization-failed](./images/kueue-k8s127.png)

- Solution: Plan in advance. It is recommended to use Kubernetes version `v1.27` or above in the production environment.

- Reference: [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/latest/)

## Issue 02: Configuration Not Enabled

- Analysis:

    When the Kubernetes cluster version is greater than v1.27, the Notebook still cannot be restricted by the queue quota.

    This is because Kueue needs to have support for `enablePlainPod` enabled to take effect for the Notebook service.

    ![local-queue-initialization-failed](./images/kueue-plainpod.png)

- Solution: When deploying `baize-agent` in the worker cluster, enable Kueue support for `enablePlainPod`.

- Reference: [Run Plain Pods as a Kueue-Managed Job](https://kueue.sigs.k8s.io/docs/tasks/run/plain_pods/)
