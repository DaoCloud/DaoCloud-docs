# API Key Management

The API Key is a core credential for invoking model services, used to authenticate users and protect data security.

![api keys](./images/apikey01.png)

## Feature Overview

- **Purpose of API Key**:
    - It is required for invoking model services and performing identity verification.
    - With an API Key, you can securely access deployed model services.

- **Security Tips**:
    - Keep your API Key safe. Avoid exposing it in client-side code or public environments.
    - If your API Key is compromised, delete it immediately and generate a new one.

## Creating an API Key

1. On the **API Key Management** page, click the **Create** button in the top-right corner.
2. In the popup window, enter a name for the API Key (e.g., `test-key`) to indicate its purpose or associated project.
3. Click **Confirm**, and the system will generate a new API Key.

!!! note

    Please save the API Key immediately after creation, as it will not be displayed in full again.

## Viewing API Keys

- The API Key list displays all the keys you’ve created:
    - **Name**: Identifier for the API Key, helping to distinguish between different use cases.
    - **API Key**: Partially masked key content for reference.
    - **Created At**: Timestamp when the API Key was generated.
- Click the refresh icon :material-refresh: in the top-right to update the key list.

## Deleting an API Key

1. Locate the API Key you wish to delete in the list.
2. Click the row to initiate the deletion.
3. Confirm the deletion in the popup dialog.
4. Once deleted, the API Key becomes immediately invalid, and any dependent service calls will be rejected.

## Using API Key to Call Services

When invoking a model service, include the following field in your HTTP request header:

```http
Authorization: Bearer {API_KEY}
```

**Example**:

```shell
curl 'https://sh-02.d.run/v1/chat/completions' \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-x1VDTAFB7Ra1hldATbncOa_dddVttDvRHQibTA-Oi7ucU" \
  -d '{
    "model": "u-8105f7322477/test",
    "messages": [{"role": "user", "content": "Hello, model!"}],
    "temperature": 0.7
  }'
```

## Notes

* **API Key Limit**: Each account has a limit on the number of API Keys that can be created. Allocate them wisely.
* **Key Leakage Handling**: If a key is compromised, delete it immediately and generate a new one.
* **Key Access Control**: Different API Keys can be assigned to different projects or services to isolate permissions.
* **Key Rotation**: For security, it's recommended to periodically delete old keys and generate new ones.
