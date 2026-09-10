# Five-Step Deployment of DeepSeek Multimodal Model

This article introduces how to directly use DeepSeek through container instances in the Compute Cloud module, and how to perform secondary algorithm development via Jupyter, VSCode, and SSH.

!!! note

    The DeepSeek-ai/Janus-Pro-7B-ComfyUI WebUI version of the text-to-image model launched on Compute Cloud
    supports both Multimodal Understanding and Text-to-Image Generation services.
    After deployment, it can be accessed and used directly through **port 10002**.

## Prerequisites

- Register and log in to d.run
- Account balance must be greater than or equal to the unit price of the selected resource type

## Create DeepSeek Instance

1. Log in to the d.run platform, select **Compute Cloud**, then enter the **Compute Market**. On the Compute Market page, select the compute specification, click **Buy Now**, and proceed to the container instance creation page.

    !!! tip

        Running the Janus-Pro-7B model requires about 20GB of GPU memory. Please ensure the selected compute specification meets this requirement.

    <!-- ![Compute Market](../zestu/images/zestu-market.png) -->

2. Fill in the instance name and select the DeepSeek image as DeepSeek-ai/Janus-Pro-7B-ComfyUI. (It is recommended to initialize and mount file storage on first use.) Click **OK** to complete the deployment.

    <!-- ![Compute Market 2](../zestu/images/zestu-market2.png) -->

3. Refresh the page. When the container instance status is running, click **Access Management**, open **port 10002**, and you can access the Janus-Pro-7B UI.

    <!-- ![Access Management 1](../zestu/images/interview.png) -->

4. Use the multimodal understanding and text-to-image services provided by DeepSeek Janus-Pro.

    <!-- ![Text-to-Image](../zestu/images/deepseek1.png) -->

## Secondary Algorithm Development via Jupyter and VSCode

Additionally, the DeepSeek Janus-Pro 7B deployed by this method usually stores model files in the container directory `/JANUS/deepseek-ai/Janus-Pro-7B/`.  
If needed, you can perform secondary development through Jupyter or VSCode. These tools can be opened directly on the page. SSH login supports both username/password and SSH public key passwordless login.

For SSH public key passwordless login, you can import your public key in the personal center. This allows passwordless login after restart or for newly created instances.

<!-- ![More Access](../zestu/images/moreintervoew.png)

![SSH Access](../zestu/images/ssh.png) -->
