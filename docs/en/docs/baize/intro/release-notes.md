---
MTPE: windsonsea
date: 2024-07-12
---

# AI Lab Release Notes

This page lists the Release Notes for AI Lab,
so that you can learn its evolution path and feature changes.

## 2024-09-30

### v0.9.0

#### Features

- **Added** Added a new data management sub-module “Data Annotation” which can manage data annotation capabilities for
  mainstream data types.
- **Added** Added a new model management sub-module “Model List” which supports quick data import.
- **Added** When creating a “Data Set”, the PVC storage space size can be specified.
- **Added** Supports one-click restart of “Training jobs”.
- **Added** When using vGPU resources, the GPU card type can be specified.
- **Added** The base image of “baize-notebook” has been upgraded to v0.9.0.
- **Improved** Supports global alerts while ensuring data availability when there is a cluster exception.

## 2024-08-31

### v0.8.0

#### Features

- **Added** [Beta] support manually saving as an image while a `Notebook` is running (depends on the image repository
  module).
- **Added** [Beta] support automatically saving as an image when a `Notebook` is closed (depends on the image repository
  module).
- **Added** Support selecting private images in the image repository through a form for `Notebook` images.
- **Added** Support configuring **data input** and **data output** for `Notebook`, which can be directly associated with
  datasets.
- **Added** Support configuring `Notebook` to start as `Root`.
- **Added** Support configuring **data input** and **data output** for `training tasks`, which can be directly
  associated with datasets.
- [Beta] **Added** Support configuring breakpoint continuation for `training tasks` and automatically detecting and
  repairing task failures.
- **Added** Support selecting private images in the image repository through a form for `training task` images.
- **Added** Support adding display of task parameter information in the details of `training tasks`.
- **Added** The `environment management` can query the preheating progress and support a quick debugging entry.
- **Added** Support adding service invocation monitoring in the details of `inference tasks`.
- **Added** The base image of `baize-notebook` is upgraded to v0.8.0.

## 2024-07-31

### v0.7.0

#### Features

- **Added** support for `Datasets` to query preheating progress after dataset creation, along with a quick debug entry.
- **Added** support for `Training Tasks` to create both single-machine and distributed tasks with `MxNet`.
- **Added** support for `Training Tasks` to create `MPI` distributed tasks.
- **Added** support for `Training Tasks` to use a default image, standardizing the use of base images.
- **Added** support for `Training Tasks` to configure the startup command directly with a startup script.
- **Added** support for `Training Tasks` to specify the working directory location for run parameters.
- **Added** support for `Inference Tasks` to display example documentation for `API` calls in the details.
- **Improved** the `Env Management` list to show the package managers and `Python` versions available in the environment.

## 2024-07-10

### v0.6.1

#### Fixes

- **Fixed** an issue where `Inference` create services using the `Triton` framework lacked the `vLLM` option.

## 2024-06-30

### v0.6.0

#### Features

- **Added** support for creating `Code` type `Notebook`, providing a native `VS Code` development experience.
- **Added** support for quickly copying `Notebook`.
- **Added** when selecting a worker cluster, display the cluster's status information,
  making it unselectable if it is disconnected or offline.
- **Added** support for using `vLLM` as the inference engine, exposing native `vLLM` capabilities
  when creating inference services.
- **Added** `vLLM` supports configuring `Lora` inference parameters when creating inference services.

#### Optimization

- **Optimized** the default queue priority to `High` when creating a `Notebook`.

#### Fixes

- **Fixed** an issue with minimum resource limits for `Tensorboard` to prevent startup failures
  due to insufficient resources.
- **Fixed** an issue with the Chinese descriptions of task statuses to avoid misunderstandings
  caused by unclear status descriptions.

## 2024-05-30

### v0.5.0

#### Features

- **Added** support for adding `Tensorboard` analysis dashboard when creating tasks with `baizectl`.
- **Added** support for binding `Job` to custom environments created in `Environment Management`.
- **Added** optimizations for custom environment configuration updates and improvements to
  the `Python` version selector in `Environment Management`.
- **Added** support for viewing resource monitoring dashboards in the details of `Inference Service`.
- **Added** support for binding `Inference Service` to custom environments created in `Environment Management`.

#### Fixes

- **Fixed** an issue where `Python` version prompts permission problems in certain cases
  within environment management.
- **Fixed** an issue where the inference service does not support stopping during exceptions.

## 2024-04-30

### v0.4.0

#### Features

- **Added** `Notebook` now supports local SSH access, compatible with various development tools such as Pycharm, and VS Code.
- **Added** upgrade `Notebook` image to support the built-in `CLI` tool `baizectl`,
  for command-line task submission and management.
- **Added** `Notebook` adds affinity scheduling policy configuration.
- **Added** distributed training tasks can now configure `SHM size` through the UI.
- **Added** one-click restart function for training tasks.
- **Added** model training tasks support custom cluster scheduler specification.
- **Added** training task analysis tool `Tensorboard` support, can be launched with one click
  in `Notebook` and training tasks.
- **Added** when editing queue quotas, hints are provided for the shared resource configuration of
  the current workspace.
- **Added** upgrade and adapt Kueue version to `v0.6.2`.

#### Fixes

- **Fixed** an occasional sync anomaly issue with `Notebook` `CRD`.
- **Fixed** an issue where the query interface for `Notebook` affinity configuration parameters did not return.

## 2024-04-01

### v0.3.0

#### Features

- **Added** the Notebooks module, supporting development tools like `Jupyter Notebook`.
- **Added** the Job Center module, supporting the training of jobs with various mainstream
  development frameworks such as `Pytorch`, `Tensorflow`, and `Paddle`.
- **Added** the Model Inference module, supporting rapid deployment of `Model Serving`,
  compatible with any model algorithm and large language models.
- **Added** the Data Management module, supporting the integration of mainstream data sources
  such as `S3`, `NFS`, `HTTP`, and `Git`, with support for automatic data preheating.
