---
MTPE: windsonsea
date: 2024-05-21
---

# Intelligent Engine Release Notes

This page lists the Release Notes for Intelligent Engine,
so that you can learn its evolution path and feature changes.

## 2024-04-30

### v0.4.0

#### Features

- **Added** **`Notebook` now supports local SSH access, compatible with various development tools such as `Pycharm`, `VS Code`, etc.** 🔥🔥🔥
- **Added** **Upgrade `Notebook` image to support the built-in `CLI` tool `baizectl`, for command-line task submission and management.** 🔥🔥🔥
- **Added** `Notebook` adds affinity scheduling strategy configuration.
- **Added** Distributed training tasks can now configure `SHM size` through the UI.
- **Added** One-click restart function for training tasks.
- **Added** **Model training tasks support custom cluster scheduler specification.** 🔥🔥🔥
- **Added** **Training task analysis tool `Tensorboard` support, can be launched with one click in `Notebook` and training tasks.** 🔥🔥🔥
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
