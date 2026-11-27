---
hide:
  - toc
---

# Deployment Preparation

This document describes the environment, resources, and model files to prepare before deploying a model service. After completing the checks, choose a deployment method that matches the target model and hardware.

## Prepare the Environment

- **User permissions**: confirm you have access and deployment permissions for the target workspace, cluster, and namespace. See [Workspace Permission Description](../../ghippo/user-guide/workspace/ws-permission.md).
- **System components**: confirm that the system components required by Turbo Inference are installed in the target cluster.
- **Compute resources**: confirm that GPU model, GPU count, GPU memory, CPU, and memory resources and quotas meet the deployment plan.
- **Inference image**: choose an image that supports the target model and hardware. If you use a custom image, confirm that target nodes can pull it.
- **Model weights**: store model weights in a PVC available in the target cluster and namespace. See [Model Weight Download and Configuration](../best-practice/model-weights-setup.md).
- **Network resources**: before PD Disaggregated or multi-node deployment, confirm that the network between nodes is available. If the deployment plan requires RDMA, configure the corresponding network resources in advance.
- **Deployment template (optional)**: when using an optimized template, confirm that the template library has a template that fits the target model and GPU.

## Optional Deployment Methods

- [Optimized Template](optimized-template.md): choose a template that matches the model, GPU, and inference mode, and supplement deployment environment information.
- [Generic Template](generic-template.md): configure resources and inference parameters yourself based on the model, hardware, and inference engine.
- **Custom Deployment**: deploy with a `values.yaml` that matches the current platform Helm Chart.

Choosing a suitable optimized template enables quick deployment. A template marked **Production Ready** has been validated in real environments; a template marked **Early Access** is suitable for trial and evaluation.

When no template fully matches, you can copy the parameters of a similar template into the **Generic Template**, adjust them according to the actual model, hardware, and engine, and then verify compatibility and running results.
