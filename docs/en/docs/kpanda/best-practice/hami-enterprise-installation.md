# HAMi Enterprise Installation and Configuration Guide

This article introduces how to install and configure HAMi (Heterogeneous AI Computing Virtualization Middleware) Enterprise Edition on the DCE 5.0 platform to enable GPU virtualization functionality.

!!! note

    This article applies to enterprise users who have deployed DCE 5.0 platform and need to enable GPU virtualization to support multi-container shared GPU resources.
    HAMi Enterprise Edition provides more powerful GPU resource management and virtualization capabilities. For more details, refer to [HAMi Project Website](https://project-hami.io).

## Prerequisites

Before installing HAMi Enterprise Edition, ensure the following conditions are met:

### System Requirements

- DCE 5.0 platform successfully deployed
- Kubernetes cluster version 1.20 or higher
- At least one node with GPU configured in the cluster (this article takes NVIDIA GPU cards as an example)
- Have cluster administrator permissions

### GPU Hardware Requirements

- Recommended NVIDIA GPU cards (CUDA supported), refer to [HAMi Enterprise Edition Supported GPU Types](https://project-hami.io/docs/userguide/Device-supported).
- GPU driver correctly installed
- Hardware architecture supporting GPU virtualization

!!! warning

    Before starting installation, ensure important data is backed up and the installation process is verified in a test environment.
