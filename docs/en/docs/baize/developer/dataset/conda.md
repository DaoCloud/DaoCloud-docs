---
MTPE: windsonsea
date: 2024-06-17
---

# Manage Python Environment Dependencies

This document aims to guide users on managing environment dependencies using DCE Intelligent Computing Power. Below are the specific steps and considerations.

1. [Overview of Environment Management](#overview)
2. [Create New Environment](#creat-new-environment)
3. [Configure Environment](#configure-environment)
4. [Troubleshooting](#troubleshooting)

## Overview

Traditionally, Python environment dependencies are built into an image, which includes the Python version
and dependency packages. This approach has high maintenance costs and is inconvenient to update, often requiring a complete rebuild of the image.

In DCE 5.0 Intelligent Computing Power, users can manage pure environment dependencies through the
**Environment Management** module, decoupling this part from the image. The advantages include:

- One environment can be used in multiple places, such as in Notebooks, distributed training tasks, and even inference services.
- Updating dependency packages is more convenient; you only need to update the environment dependencies without rebuilding the image.

The main components of the environment management are:

- **Cluster** : Select the cluster to operate on.
- **Namespace** : Select the namespace to limit the scope of operations.
- **Environment List** : Displays all environments and their statuses under the current cluster and namespace.

![Environment Management](../../images/conda01.png)

### Explanation of Environment List Fields

- **Name** : The name of the environment.
- **Status** : The current status of the environment (normal or failed). New environments undergo a warming-up process, after which they can be used in other tasks.
- **Creation Time** : The time the environment was created.

## Creat New Environment

On the **Environment Management** interface, click the **Create** button at the top right
to enter the environment creation process.

![Environment Management](../../images/conda02.png)

Fill in the following basic information:

- **Name** : Enter the environment name, with a length of 2-63 characters,
  starting and ending with lowercase letters or numbers.
- **Deployment Location**:
    - **Cluster** : Select the cluster to deploy, such as `gpu-cluster`.
    - **Namespace** : Select the namespace, such as `default`.
- **Remarks** (optional): Enter remarks.
- **Labels** (optional): Add labels to the environment.
- **Annotations** (optional): Add annotations to the environment. After completing the information,
  click **Next** to proceed to environment configuration.

## Configure Environment

In the environment configuration step, users need to configure the Python version and dependency management tool.

![Environment Management](../../images/conda03.png)

### Environment Settings

- **Python Version** : Select the required Python version, such as `3.12.3`.
- **Package Manager** : Choose the package management tool, either `PIP` or `CONDA`.
- **Environment Data** :
    - If `PIP` is selected: Enter the dependency package list in `requirements.txt` format in the editor below.
    - If `CONDA` is selected: Enter the dependency package list in `environment.yaml` format in the editor below.
- **Other Options** (optional):
    - **Additional pip Index URLs** : Configure additional pip index URLs; suitable for internal enterprise private repositories or PIP acceleration sites.
    - **GPU Configuration** : Enable or disable GPU configuration; some GPU-related dependency packages
      need GPU resources configured during preloading.
    - **Associated Storage** : Select the associated storage configuration; environment dependency packages
      will be stored in the associated storage. **Note: Storage must support `ReadWriteMany`.**

After configuration, click the **Create** button, and the system will automatically create and configure the new Python environment.

## Troubleshooting

- If environment creation fails:
    - Check if the network connection is normal.
    - Verify that the Python version and package manager configuration are correct.
    - Ensure the selected cluster and namespace are available.

- If dependency preloading fails:
    - Check if the `requirements.txt` or `environment.yaml` file format is correct.
    - Verify that the dependency package names and versions are correct. If other issues arise,
      contact the platform administrator or refer to the platform help documentation for more support.

---

These are the basic steps and considerations for managing Python dependencies in DCE 5.0 Intelligent Computing Power.
