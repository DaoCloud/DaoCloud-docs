---
hide:
  - toc
---

# Create Model

*[Hydra]: Internal codename for LLM Studio

**Model Management** is used to add user-defined models or fine-tuning task results, and to maintain their
metadata, deployment templates, and weight mount information. It consolidates deployable assets in the platform,
reducing repeated configuration and making it easier for teams to reuse and quickly deploy models later. The
following sections describe the steps for creating metadata and managing templates and weight files.

## Create Model Metadata

1. Enter LLM Studio, expand **Model Serving** in the left navigation bar, and click **Model Management**.

2. On the model management page, click **Create Model**.

    ![create-model](../images/create-model-01.png)

3. After filling in the parameters on the creation page, click **Confirm**, and the model is created successfully.

    | Parameter | Constraints / Description | Remarks |
    | --- | --- | --- |
    | Model Name | Required<br>**Length**: Up to 63 characters<br>**Characters**: Only lowercase letters, numbers, hyphens (-), or dots (.) are allowed<br>**Rule**: Must start and end with a letter or number | |
    | Model Tags | Required. Multiple selections are supported | Used to identify the model capability type |
    | Model Icon | Optional | Supports local upload, or an image URL starting with `https://`; supports SVG, PNG, JPG, and JPEG formats, with a file size smaller than 40 KB. The recommended size is 100 x 100 pixels |
    | Model Description | Optional | Up to 800 characters each for Chinese and English |

    ![create-model](../images/create-model-02.png)

## Manage Deployment Templates

Deployment templates are used to preset resource configurations and runtime configurations for models.
When deploying a custom model, you can directly use a template to reduce repeated input.

### Create a Deployment Template

1. In the model management list, click the target model name to enter the model details page.

1. Select the **Deployment Templates** tab, and click **Create** in the upper right corner of the list.

    ![create-model](../images/create-model-03.png)

1. Fill in **Basic Information**, **Resource Configuration**, and **Runtime Configuration** in sequence, and then click **Confirm**.

    | Parameter | Constraints / Description | Remarks |
    | --- | --- | --- |
    | Template Name | Required<br>**Length**: Up to 63 characters<br>**Characters**: Only lowercase letters, numbers, hyphens (-), or dots (.) are allowed<br>**Rule**: Must start and end with a letter or number | |
    | Description | Optional | Up to 800 characters |
    | CPU / Memory | Resource configuration | |
    | GPU | Optional | Includes the GPU type, number of physical cards, computing power, and video memory |
    | Runtime Framework | Select the inference runtime | Switching the framework automatically brings up the default startup command |
    | Startup Command | Can be modified as needed | |
    | Environment Variables | Optional | Configured as key-value pairs |

    To use a custom inference runtime, complete the runtime configuration on the operations side first.
    For details, see [Custom LLM Inference Runtime](../user-guides/custom-runtime.md).

    ![create-model](../images/create-model-031.png)

### Edit and Delete a Deployment Template

1. In the **Deployment Templates** tab, click the **┇** menu to the right of the target template.

2. Select **Edit/Delete** to modify or delete the template.

## Manage Model Weight Files

Model weight files associate the weight directory on a cluster with the mount path inside the container for the
current model. When deploying a custom model, the corresponding weight files can be found through this mount path.

### Create a Model Weight File

**Prerequisites**

- The target cluster must have Hydra Agent installed and [file storage](../file-storage/storage.md) created.
- The weight files must already be uploaded to the corresponding directory of the file storage, or synchronized
  to the cluster through [remote file preheat](../file-storage/file-preheat.md).

**Steps**

1. On the model details page, select the **Model Weight Files** tab, and click **Create** in the upper right
   corner of the list.

    ![create-model](../images/create-model-04.png)

1. After filling in the parameter information, click **Confirm**.

    | Parameter | Constraints / Description | Remarks |
    | --- | --- | --- |
    | Cluster | Required | Only clusters with Agent installed and file storage created can be selected. If no file storage has been created for the current cluster, click **Create Now** to go to the file storage creation page |
    | Version Identifier | Required | Used to distinguish between different weight versions under the same cluster |
    | Storage Type | Required | Currently only **File Storage** is supported |
    | Storage Directory | Required | Can be entered manually, or selected from the file storage by clicking **Select Directory**; you can also click **Create Now** to manage files |
    | Mount Path | Required | The mount path of the weights inside the container. The default example is `/mnt/path` |

    ![create-model](../images/create-model-041.png)

### Update and Delete a Model Weight File

1. In the **Model Weight Files** tab, click the **┇** menu to the right of the target record.
2. Select **Edit/Delete** to modify or delete the record.

## Next Steps

- [Manage Models](./model-manage.md)
