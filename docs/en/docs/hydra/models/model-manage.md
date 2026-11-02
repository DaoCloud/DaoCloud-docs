---
hide:
  - toc
---

# Manage Models

*[Hydra]: Internal codename for LLM Studio

This page describes how to view the model list in **Model Management** and perform operations such as deploy,
update, and delete.
To create new model metadata, or to manage deployment templates and model weight files, see [Create Model](./index.md).

## View the Model List

1. Enter LLM Studio, expand **Model Serving** in the left navigation bar, and click **Model Management**.

2. In the **┇** menu on the right side of the list, you can perform **Deploy**, **Update**, and **Delete** operations.

    ![model-manage](../images/model-manage-01.png)

## Deploy a Model

1. In the model management list, click the **┇** menu to the right of the target model and select **Deploy**.
2. The page jumps to the **Deploy New Model** page. Continue to complete the deployment form configuration.

For deployment parameter descriptions, see [Deploying a New Model](../deploy/deploy.md).

## Update a Model

1. In the model management list, click the **┇** menu to the right of the target model and select **Update**.
2. On the edit page, modify the model name, model tags, model icon, or model description, and then click
   **Confirm** to save the changes.

You can also select **Update** from the **┇** menu in the upper right corner of the model details page to enter
the same edit page.

## Delete a Model

1. In the model management list or on the model details page, click the **┇** menu and select **Delete**.
2. The system verifies whether the current model has an associated model service:

    - If an associated service exists, delete the corresponding model service first, and then delete the model;
    - After the verification passes, enter the model name and confirm the deletion.

!!! note

    Once deleted, it cannot be recovered. Please proceed with caution.
