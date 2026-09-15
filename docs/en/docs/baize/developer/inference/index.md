# Model List

The AI Lab model list is used to display and manage various machine learning or deep learning models, making it convenient for users to quickly carry out data science and machine learning experiments. You can create models and download public models in different clusters and namespaces to manage your models.

## Create a Model

1. In the left navigation bar, click **Model Service** -> **Model List**, and then click the **Create** button on the right.


2. Select the cluster and namespace where the model is deployed, as well as the architecture, model format, model label, model description, model version, and so on, and then click **OK**.


Currently supported model architectures include CNN, RNN, LSTM, TRANSFORMER, MLP, BERT, GAN, RESNET, and so on. Model formats include PYTORCH, TENSORFLOW, and ONNX.

## Download a Public Model

AI Lab supports downloading models from ModelScope and HuggingFace. You can view more models in the [ModelScope Model Library](https://www.modelscope.cn/models) and the [HuggingFace Model Hub](https://huggingface.co/models).

Click the **Public Model Download** button on the right side of the model list, select the **Public Model Source**, configure the cluster and namespace where the model is deployed, the associated storage pool, the data storage size, the Endpoint, and so on, and then enter the Token for authorized access. Then click **OK**.


## Deploy a Model

1. In the model list, click the **┇** on the right side of a model, then choose **Deploy** from the dropdown menu.


2. You will be redirected to the Inference Service page to deploy the model.
 

## Create a New Version

Click **┇** -> **Create New Version** on the right side of the model list, and then set the version number, dataset, path, and other information of the new model version in the pop-up window.


## Update a Model

Click **┇** -> **Update** on the right side of the model list to update the target model.


## Delete a Model

Click **┇** -> **Delete** on the right side of the model list. In the pop-up window, confirm the model you want to delete, enter the model name, and then click **Delete**.


!!! caution

    Once a model is deleted, it cannot be recovered, so please proceed with caution.
