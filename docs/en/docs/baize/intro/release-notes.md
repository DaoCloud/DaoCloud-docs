---
MTPE: windsonsea
date: 2024-07-12
---

# AI Lab Release Notes

This page lists the Release Notes for AI Lab,
so that you can learn its evolution path and feature changes.

!!! note

    Features labeled as Beta may undergo changes; please use them with caution
    and provide prompt feedback if you encounter any issues.

## 2024-11-30

### v0.11.0

- **Added** status detail display for `Notebooks`, `Datasets`, `Training Jobs`,
  and `Inference Service` to improve exception handling efficiency.
- **Added** queue management in the operator console, allowing viewing of all
  resources that have used the queue on the queue details page.
- **Improved** interaction for dataset updates.

## 2024-10-31

### v0.10.0

#### Features

- **Added** the feature to specify the type of GPU to use when configuring vGPU resources in the `Training Job`.
- **Added** support for Huggingface data sources in the `Dataset`, allowing you to download a vast array of models and datasets.
- **Added** support for Modelscope data sources in the `Dataset`, allowing you to download a vast array of models and datasets.
- **Added** the feature for **cross-namespace** references in `Dataset`.
- **Added** support for specifying the type of card to use when configuring vGPU resources in the `Inference Service`.
- **Added** a GPU management module in the `Operations Console`, which supports viewing card-level monitoring and metrics information.
- **Added** compatibility for `Moxi` GPUs.

#### Improvements

- **Improved** the dataset update interface to provide more configuration options.
- **Improved** the entry position of the Notebook to enhance accessibility.

## 2024-09-30

### v0.9.0

!!! note

    The product module name was changed from `Intelligent Computing Engine` to `AI Lab` globally.

- **Added** a new data management sub-module, “Data Labeling,” for managing data labeling features across main data categories.
- **Added** a new model management sub-module, “Model List,” which supports to quickly import data.
- **Added** the feature to specify PVC storage size when creating a “Dataset.”
- **Added** support for one-click restarts of training jobs.
- **Added** the option to specify the GPU type when using vGPU resources.
- **Added** an upgrade of the base image for “baize-notebook” to v0.9.0.
- **Improved** global alerts support to ensure data availability during cluster exceptions.

## 2024-08-31

### v0.8.0

- **Added** [Beta] support for manually saving a `Notebook` as an image while it is running (depending on the Container Registry module).
- **Added** [Beta] support for automatically saving a `Notebook` as an image when it is closed (depending on the Container Registry module).
- **Added** an feature to select private images from the Container Registry via a form for `Notebook` images.
- **Added** support for configuring **data input** and **data output** for `Notebook`, directly associating them with datasets.
- **Added** support for configuring `Notebook` to start as `Root`.
- **Added** support for configuring **data input** and **data output** for `training jobs`, which can be directly linked to datasets.
- **Added** [Beta] support for configuring breakpoint continuation for `training jobs`, with automatic detection and repair of job failures.
- **Added** an feature to select private images from the Container Registry via a form for `training job` images.
- **Added** the display of job parameters in the detail page of `training jobs`.
- **Added** an feature in environment management to query preloading progress and provide a quick debugging entry.
- **Added** support for service invocation monitoring in the detail page of `inference jobs`.
- **Added** an upgrade of the base image for `baize-notebook` to v0.8.0.

## 2024-07-31

### v0.7.0

- **Added** support for `Datasets` to query preloading progress after dataset creation, along with a quick debug entry.
- **Added** support for `training jobs` to create both single-machine and distributed tasks with `MxNet`.
- **Added** support for `training jobs` to create `MPI` distributed tasks.
- **Added** support for `training jobs` to use a default image, standardizing the use of base images.
- **Added** support for `training jobs` to configure the startup command directly with a startup script.
- **Added** support for `training jobs` to specify the working directory location for run parameters.
- **Added** support for `Inference Tasks` to display example documentation for `API` calls in the details.
- **Improved** the `Env Management` list to show the package managers and `Python` versions available in the environment.

## 2024-07-10

### v0.6.1

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

#### Improvement

- **Improved** the default queue priority to `High` when creating a `Notebook`.

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
- **Added** Improvements for custom environment configuration updates and improvements to
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
- **Added** distributed training jobs can now configure `SHM size` through the UI.
- **Added** one-click restart function for training jobs.
- **Added** model training jobs support custom cluster scheduler specification.
- **Added** training job analysis tool `Tensorboard` support, can be launched with one click
  in `Notebook` and training jobs.
- **Added** when editing queue quotas, hints are provided for the shared resource configuration of
  the current workspace.
- **Added** upgrade and adapt Kueue to v0.6.2.

#### Fixes

- **Fixed** an occasional sync anomaly issue with `Notebook` `CRD`.
- **Fixed** an issue where the query interface for `Notebook` affinity configuration parameters did not return.

## 2024-04-01

### v0.3.0

- **Added** the Notebooks module, supporting development tools like `Jupyter Notebook`.
- **Added** the Job Center module, supporting the training of jobs with various mainstream
  development frameworks such as `Pytorch`, `Tensorflow`, and `Paddle`.
- **Added** the Model Inference module, supporting rapid deployment of `Model Serving`,
  compatible with any model algorithm and large language models.
- **Added** the Data Management module, supporting the integration of mainstream data sources
  such as `S3`, `NFS`, `HTTP`, and `Git`, with support for automatic data preloading.
