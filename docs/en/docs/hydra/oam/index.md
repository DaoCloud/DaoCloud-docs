# Model Gallery

Platform administrators can comprehensively manage large models in the Model Gallery through the **Operations Management** feature, including batch import, model creation, parameter editing, and model deployment or withdrawal. This feature helps administrators quickly build and maintain the model ecosystem, improving overall platform operation efficiency.

## Batch Import Models

Supports batch importing multiple models via remote URLs to simplify the model onboarding process.

1. On the **Model Gallery** page, click the **Batch Import** button at the top right corner.

    ![Click Button](./images/import01.png)

2. In the pop-up import window:

    - Paste the URL containing model file addresses;
    - The platform will automatically parse and display the list of importable models;
    - Check one or more models;
    - Click the **Import** button.

    ![Import Models](./images/import02.png)

    !!! note

        Models already existing in the system will be grayed out and cannot be imported again.

3. Return to the model list page, where newly imported models will appear at the top of the list by default for easier follow-up operations.

## Create Model

If you need to manually add a model, you can use the model creation feature.

1. On the **Model Gallery** page, click the **Create** button at the top right corner.

    ![Click Button](./images/import01.png)

2. In the pop-up create model window, fill in the following parameters in order:

    - Model name;
    - Model type (e.g., LLM, Embedding, Diffusion, etc.);
    - Model version;
    - Runtime environment (e.g., PyTorch, TensorFlow);
    - Required resources (CPU/GPU count, memory, VRAM, etc.);
    - Weight file URL or path;
    - Description (optional), etc.

    After filling out, click **Confirm** to complete creation.

    ![Create Model](./images/create-model.png)

3. Return to the model list page, the newly created model will be displayed at the top.

## Edit Model

Administrators can edit model parameter information anytime after model creation to meet actual operation or business changes.

1. In the model list, click the **┇** menu icon to the right of the target model and select **Edit**.

    ![Select Menu](./images/edit01.png)

2. In the pop-up edit window, modify the model parameters as needed and click **Confirm** to save changes.

    ![Modify Parameters](./images/edit02.png)

3. After returning to the model list, the model position remains unchanged and updated parameters take effect immediately.

    !!! tip

        Editing model parameters does not affect the model’s current online status, but it is recommended to perform edits during idle periods.

## Model Deployment / Withdrawal

Administrators can manually control the display status of models in the marketplace based on operational strategies or resource scheduling.

1. In the model list, click the **┇** menu next to the target model and select **Deploy to Marketplace** or **Withdraw from Marketplace**.

    ![Select Menu](./images/edit01.png)

2. Taking withdrawal as an example, after selecting **Withdraw from Marketplace**, the page will show a success message and the model will be hidden from the marketplace frontend.

    ![Withdraw](./images/offline.png)

    !!! note

        Withdrawing a model only affects its visibility on the marketplace frontend and does not delete the model itself or its configuration. To completely remove it, please use the “Delete” function.

---

By following the above operations, platform administrators can efficiently complete model import, configuration, and publication, ensuring the Model Gallery content is updated timely and configured accurately to meet diverse business needs.
