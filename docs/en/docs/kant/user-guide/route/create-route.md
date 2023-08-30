# Create Message Routes

This document describes the steps to create message endpoints, message routes, and delete message routes.

## Create Message Endpoints

Follow these steps:

1. Go to the `Edge Unit` details page and select the left-side menu `Edge-Cloud Messaging` -> `Message Endpoints`.

2. Click the `Create Message Endpoint` button in the upper right corner of the message endpoint list.


3. Fill in the relevant parameters.

    - Message Endpoint Type: Select the type, which can be Rest (Cloud-side endpoint), Event Bus (Edge-side endpoint), or Service Bus (Edge-side endpoint).
    - Namespace: The namespace where the message endpoint is located.
    - Message Endpoint Name: Enter a name for the message endpoint.
    - Service Port: Only applicable to Service Bus type edge endpoints. Range: 1-65535.

4. Click `OK` to create the message endpoint successfully and return to the message endpoint list page.



## Create Message Routes

Follow these steps:

1. Go to the `Edge Unit` details page and select the left-side menu `Edge-Cloud Messaging` -> `Message Routes`.

2. Click the `Create Message Route` button in the upper right corner of the message route list.


3. Fill in the relevant parameters.

    - Message Route Name: Enter a name for the message route.
    - Namespace: The namespace where the message route is located.
    - Source Endpoint: Select the source endpoint, which comes from the created message endpoints.
    - Source Endpoint Resource:
        - For Cloud Rest type source endpoint, enter the REST path, such as /abc/bc.
        - For Edge Event Bus type source endpoint, enter the topic, which consists of letters, numbers, underscores (_), hyphens (-), and slashes (/).
    - Destination Endpoint: Select the destination endpoint, which comes from the created message endpoints.
    - Destination Endpoint Resource:
        - For Cloud Rest type destination endpoint, enter the URL, such as http://127.0.0.1:8080/hello.
        - For Edge Service Bus type destination endpoint, enter the Service Bus path, such as /abc/bc.


4. Click `OK` to create the route rule successfully and return to the message route list page.

After creating the route rule, the system will forward messages sent to the specified resource of the source endpoint according to the corresponding rule to the specified resource of the destination endpoint.

## Delete Message Routes

Follow these steps:

1. Go to the `Edge Unit` details page and select the left-side menu `Edge-Cloud Messaging` -> `Message Routes`.

2. Click the `Delete` button on the right side of the specific message route.

3. In the delete confirmation dialog box, enter the `Message Route Name`.

4. Click `Delete` to delete it successfully and return to the message route list page.

