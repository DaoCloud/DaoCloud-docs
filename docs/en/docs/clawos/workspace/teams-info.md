# Integrate OpenClaw with Microsoft Teams

This document describes how to register a Microsoft Entra single-tenant application, create an Azure Bot, and integrate OpenClaw with Microsoft Teams.

## Prerequisites

Before getting started, make sure:

- You have a customer Microsoft Entra tenant and Azure subscription.
- You have permissions to create app registrations and Azure Bots.
- The Messaging endpoint is a publicly accessible HTTPS URL.

## Fields

| OpenClaw Field | Microsoft Name | Value to Enter | Notes |
| --- | --- | --- | --- |
| Client ID | Application (client) ID / Microsoft App ID | The GUID from the Entra app registration Overview page | Do not enter Object ID |
| Client Secret | Client secret -> Value | The Value displayed after creating a client secret | Do not enter Secret ID; Value is displayed only once |
| Tenant ID | Directory (tenant) ID / App Tenant ID | The Entra tenant GUID | Must match the tenant where the app registration was created |
| Messaging endpoint | Azure Bot -> Configuration -> Messaging endpoint | The complete URL provided by OpenClaw | Must use the full HTTPS URL |

## Obtain Client ID, Tenant ID, and Client Secret

### Register an Application

1. Visit [Microsoft Entra admin center](https://entra.microsoft.com/) and select **Entra ID** -> **App registrations** -> **New registration**.

    Configure the following:

    - **Name**: For example, `OpenClaw-Teams-Prod`
    - **Supported account types**: Select `Accounts in this organizational directory only`
    - **Redirect URI**: Usually not required for this workflow

2. After registration is complete, copy the following values from the **Overview** page:

    - **Application (client) ID**: Use as the OpenClaw Client ID
    - **Directory (tenant) ID**: Use as the OpenClaw Tenant ID

### Create a Client Secret

1. In the app registration, select **Certificates & secrets** -> **Client secrets** -> **New client secret**.

2. Enter a description and expiration period, then select **Add**.

3. Immediately copy the **Value** after creation. This value is the OpenClaw Client Secret.

!!! note

    Microsoft will not display the Secret Value again. If you forget to save it, you must create a new Client Secret.

## Create and Configure an Azure Bot

Open the [Azure portal](https://portal.azure.com/) and select **Create a resource** -> search for `bot` -> **Azure Bot** -> **Create**.

### Configure App ID

In the **Microsoft App ID** or identity configuration section:

1. Select **Single Tenant**.
2. Select **Use existing app registration**.
3. Enter the previously created **Application (client) ID**.
4. If the page requires a Tenant ID, enter the same **Directory (tenant) ID**.

After completing the configuration, select **Review + create** -> **Create**.

### Configure Messaging Endpoint

1. Open the Azure Bot resource and select **Settings** -> **Configuration**.

2. Enter the complete endpoint provided by OpenClaw into **Messaging endpoint**, then select **Apply**.

    The endpoint address must:

    - Use HTTPS.
    - Be publicly accessible.
    - Preserve the complete path provided by OpenClaw.

### Enable Microsoft Teams Channel

1. Go to **Channels** -> **Microsoft Teams**.

2. Accept the related terms. If the page displays **Cloud environment**, select the option that matches the customer's Teams environment, then select **Apply**.

## Enter Information in OpenClaw

| OpenClaw Field | Value to Enter |
| --- | --- |
| Client ID | The Application (client) ID of the Entra application |
| Client Secret | The Value of the Entra Client secret |
| Tenant ID | The Directory (tenant) ID of the Entra application |

After saving, verify that there are no extra spaces or line breaks in any field.

## Add the Bot to Teams

After enabling the Teams channel, you still need to add the Bot to Teams.

### Test Environment

1. In Azure Bot, select **Channels** -> **Microsoft Teams**.

2. Obtain the Teams test link on the page, open it, and select either the Teams client or Teams Web to add the Bot to Teams.

### Production Environment

For production environments, it is recommended to create a Teams App, set the Bot ID to the Entra application's **Application (client) ID**, and then upload or publish it to the customer's Teams tenant.

Adding the Bot only through the Bot GUID is suitable for testing and is not recommended for production environments.

## Verification Checklist

| Check Item | Success Criteria |
| --- | --- |
| App registration | Application type is Single Tenant |
| Client ID | Application ID is consistent across OpenClaw, Entra, and Azure Bot |
| Client Secret | Secret Value is used and has not expired |
| Tenant ID | Tenant ID in OpenClaw matches the Entra tenant ID |
| Messaging endpoint | Configured with the complete HTTPS URL provided by OpenClaw |
| Teams channel | Microsoft Teams channel is enabled |
| Teams installation | Bot has been added to Teams |
| Message test | Teams messages successfully trigger OpenClaw responses |

## Secret Rotation

Before the Client Secret expires:

1. Create a new Client Secret.
2. Update the new Value in OpenClaw.
3. Send a Teams test message to verify it works.
4. Delete the old Secret afterward.

## Troubleshooting

### Bot Cannot Be Found in Teams

Check whether the Teams channel is enabled and whether the Bot has been added to Teams through the test link or Teams App.

### No Response After Sending Messages

Check the following:

- Whether the Messaging endpoint is complete.
- Whether the endpoint is publicly accessible.
- Whether the Client ID, Client Secret, and Tenant ID are correct.
- Whether the Cloud environment is selected correctly.

### 401 or 403 Errors

Check the following:

- Whether the Secret ID was entered by mistake.
- Whether the Client Secret has expired.
- Whether the Tenant ID belongs to the tenant where the current app registration was created.

## References

- [Register a bot with Azure](https://learn.microsoft.com/en-us/azure/bot-service/bot-service-quickstart-registration?tabs=++userassigned&view=azure-bot-service-4.0)
- [Connect a Bot Framework bot to Microsoft Teams](https://learn.microsoft.com/en-us/azure/bot-service/channel-connect-teams?view=azure-bot-service-4.0)
