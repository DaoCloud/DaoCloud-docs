# Services

The App Mesh provides service management capabilities, allowing you to create services that bind application instances and configure access ports, enabling mutual access between applications on nodes.

## Creating a Service

!!! note

    To ensure that the created service can be accessed, EdgeMesh application must be installed on the node from which the access is initiated.

Follow the steps below to create a service:

1. Select `Edge Computing` -> `Cloud Edge Collaboration` in the left navigation bar to enter the Edge Unit list page. Click the `Edge Unit Name` to enter the Edge Unit details page.

2. Select `App Mesh` -> `Services` in the left menu and click the `Create Service` button in the top right corner of the service list.

3. Fill in the relevant parameters.

    | Parameter        | Description                                                  | Example   |
    | ---------------- | ------------------------------------------------------------ | --------- |
    | Access Type      | **Type**: Not required<br />**Meaning**: Specifies the way Pod services are discovered. Default is cluster internal access (ClusterIP). | ClusterIP |
    | Service Name     | **Type**: Required<br />**Meaning**: Enter the name of the newly created service.<br />**Note**: Please enter a string of 4 to 63 characters, which can include lowercase letters, numbers, and hyphens (-), and must start with a lowercase letter and end with a lowercase letter or a number. | Svc-01    |
    | Namespace        | **Type**: Required<br />**Meaning**: Select the namespace where the new service is located. For more information about namespaces, please refer to the [Namespace Overview](../namespaces/createns.md).<br />**Note**: Please enter a string of 4 to 63 characters, which can include lowercase letters, numbers, and hyphens (-), and must start with a lowercase letter and end with a lowercase letter or a number. | default   |
    | Label Selector   | **Type**: Required<br />**Meaning**: Add labels. Service selects Pods based on labels. Fill in and click "Add". | app:job01 |
    | Port Configuration | **Type**: Required<br />**Meaning**: Add protocol ports to the service. You need to first select the protocol type, currently supporting TCP and UDP.<br />**Port Name**: Enter a custom name for the port.<br />**Service Port (port)**: The access port for the Pod to provide services to the outside world.<br />**Container Port (targetport)**: The actual container port that the workload listens on, used to expose services within the cluster. |           |
    | Session Affinity | **Type**: Optional<br />**Meaning**: When enabled, requests from the same client will be forwarded to the same Pod. | Enabled   |
    | Maximum Session Affinity Duration | **Type**: Optional<br />**Meaning**: When session affinity is enabled, the maximum duration of the affinity. Default is 30 seconds. | 30 seconds |
    | Labels           | **Type**: Optional<br />**Meaning**: Add labels to the service. |           |
    | Annotations      | **Type**: Optional<br />**Meaning**: Add annotations to the service. |           |

4. Click `OK` to create the service successfully. You will be returned to the service list page, where you can view the access ports corresponding to the service in the service list.

!!! tip

    You can also create a service through `YAML`.

## Updating a Service

Services support updating service aliases, label selectors, port configurations, and session affinity settings.

Follow the steps below to update a service:

1. Go to the Edge Unit details page and select `App Mesh` -> `Services` in the left navigation bar.

2. Click the service name to enter the service details page. Click the `⋮` button in the top right corner of the page, and select `Update` from the pop-up menu to modify the service alias, label selector, port configuration, and session affinity settings.

## Viewing Events

You can view service event information.

On the service details page, select the `Events` tab to view service event information.

## Deleting a Service

1. Go to the Edge Unit details page and select `App Mesh` -> `Services` in the left navigation bar.

2. Click the service name to enter the service details page. Click the `⋮` button in the top right corner of the page, and select `Delete` from the pop-up menu to modify the service alias, label selector, port configuration, and session affinity settings.
