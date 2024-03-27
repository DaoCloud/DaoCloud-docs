# Edge-Cloud Messages

Cloud Edge Collabration provides edge-cloud message routing functionality. You can configure message routes, and the platform will forward messages to the corresponding endpoints according to the message routing configuration. This allows flexible control over data routing and enhances data security.

- Message Endpoint: The sender or receiver of a message, which can be an edge application, cloud service, etc.
- Message Routing: The path through which messages are forwarded.

## Message Endpoints

The platform provides the following three types of message endpoints:

- Rest: Cloud-side endpoints that send message requests to the edge or receive messages from the edge.
- Event Bus: Edge-side endpoints that send data to the cloud or receive messages from the cloud.
- Service Bus: Edge-side endpoints that send message requests to the edge or receive messages from the edge.

## Message Routing

For different types of message endpoints, the platform provides the following message forwarding paths:

- Rest -> EventBus: User applications invoke REST APIs in the cloud to send messages, and the messages are ultimately sent to the MQTT broker in the edge.
- EventBus -> Rest: You publish messages to the MQTT broker in the edge, and the messages are ultimately sent to the REST API in the cloud.
- Rest -> ServiceBus: User applications invoke REST APIs in the cloud to send messages, and the messages are ultimately sent to edge applications.

Next Step: [Create Message Routes](./create-route.md)
