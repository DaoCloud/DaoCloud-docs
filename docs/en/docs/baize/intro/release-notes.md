---
MTPE: windsonsea
date: 2024-05-21
---

# Intelligent Engine Release Notes

This page lists the Release Notes for Intelligent Engine,
so that you can learn its evolution path and feature changes.

## 2024-06-30

### v0.6.0

#### Features

- **New**: Support for creating `Code` type `Notebook`, providing a native `VS Code` development experience.
- **New**: Support for quickly copying `Notebook`.
- **New**: When selecting a work cluster, display the cluster's status information, making it unselectable if it is disconnected or offline.
- **New**: When creating inference services, support using `vLLM` as the inference engine, exposing native `vLLM` capabilities.
- **New**: When creating inference services, `vLLM` supports configuring `Lora` inference parameters.
- **Optimization**: When creating a `Notebook`, the default queue priority is adjusted to `High`.

#### Fixes

- **Fixed**: Minimum resource limits for `Tensorboard` to prevent startup failures due to insufficient resources.
- **Fixed**: Optimized the Chinese descriptions of task statuses to avoid misunderstandings caused by unclear status descriptions.

## 2024-05-30

### v0.5.0

#### Features

- **Added** Support for adding `Tensorboard` analysis dashboard when creating tasks with `baizectl`.
- **Added** Support for binding `Job` to custom environments created in `Environment Management`.
- **Added** Optimizations for custom environment configuration updates and improvements to the `Python` version selector in `Environment Management`.
- **Added** Support for viewing resource monitoring dashboards in the details of `Inference Service`.
- **Added** Support for binding `Inference Service` to custom environments created in `Environment Management`.

#### Fixes

- **Fixed** the issue where `Python` version prompts permission problems in certain cases within environment management.
- **Fixed** the issue where the inference service does not support stopping during exceptions.

## 2024-04-30

### v0.4.0

#### Features

- **Added** `Notebook` now supports local SSH access, compatible with various development tools such as `Pycharm`, `VS Code`, etc.
- **Added** Upgrade `Notebook` image to support the built-in `CLI` tool `baizectl`, for command-line task submission and management.
- **Added** `Notebook` adds affinity scheduling strategy configuration.
- **Added** Distributed training tasks can now configure `SHM size` through the UI.
- **Added** One-click restart function for training tasks.
- **Added** Model training tasks support custom cluster scheduler specification.**
- **Added** Training task analysis tool `Tensorboard` support, can be launched with one click in `Notebook` and training tasks.
- **Added** When editing queue quotas, hints are provided for the shared resource configuration of the current workspace.
- **Added** Upgrade and adapt Kueue version `v0.6.2`.

#### Fixes

- **Fixed** Occasional sync anomaly issue with `Notebook` `CRD`.
- **Fixed** The query interface for `Notebook` affinity configuration parameters did not return.

## 2024-04-01

### v0.3.0

#### Features

- **Added** the Notebooks module, supporting development tools like `Jupyter Notebook`.
- **Added** the Job Center module, supporting the training of jobs with various
  mainstream development frameworks such as `Pytorch`, `Tensorflow`, and `Paddle`.
- **Added** the Model Inference module, supporting rapid deployment of `Model Serving`,
  compatible with any model algorithm and large language models.
- **Added** the Data Management module, supporting the integration of mainstream data sources
  such as `S3`, `NFS`, `HTTP`, and `Git`, with support for automatic data preheating.
