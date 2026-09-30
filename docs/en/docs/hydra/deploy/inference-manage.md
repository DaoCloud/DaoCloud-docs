---
hide:
  - toc
---

# Manage Model Services

*[Hydra]: Internal codename for LLM Studio

This page describes how to view and manage deployed model services, including service details, start/stop,
scaling, and deletion.

## View the Model Service List

1. Enter LLM Studio, and in the left navigation bar, click **Model Serving**.
2. In the model service list, you can view the service status, number of instances, deployment location, and other information.
3. Click the target service name (the service must be running) to enter the service details page.

![service](../images/service02.png)

## View Service Details

On the service details page, you can view:

- Basic service information (name, status, deployment location, access address, etc.).
- API call information and the authentication method.
- Deployment configurations (resource configuration, runtime configuration, and scheduling configuration).

## Start and Stop Services

1. In the model service list, click the **┇** menu to the right of the target service.
2. Select **Start Service** or **Stop Service**.
3. After the operation is complete, check the service status change in the list.

## Scale Model Services

If you find resource shortages or stuttering during model usage, you can scale the model service.

1. In the model service list, click the **┇** menu to the right of the target service and select **Scale**.

    ![Scaling](../images/service03.png)

2. Enter the target number of instances and click **Confirm**.

    ![Scaling](../images/service04.png)

## Delete Model Services

1. In the model service list, click the **┇** menu to the right of the target service and select **Delete**.
2. Enter the name of the model service to delete and confirm the deletion.

    ![Delete Service](../images/service05.png)

!!! note

    Once deleted, it cannot be recovered. Please proceed with caution.

## Service Invocation

- Access authentication: Service APIs use API Key authentication. Carry `Authorization: Bearer {API_KEY}` in the request header.
- Obtaining an API Key: See [API Key Management](../apikey.md).
- API call examples and response field descriptions: See [Model Service Details](./deploy-detail.md).
- More invocation methods: See [Model Invocation](../api-call.md).
