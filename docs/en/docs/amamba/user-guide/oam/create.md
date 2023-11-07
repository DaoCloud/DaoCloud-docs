# Creating an OAM Application

The OAM application feature is based on the open-source software KubeVela, which uses the Open Application Model (OAM) as the top-level abstraction for application delivery. It abstracts and integrates Kubernetes resources to achieve standardized and efficient application delivery in a hybrid environment.

For an introduction to OAM concepts, refer to [OAM Concept Introduction](concept.md) or the [KubeVela Official Documentation](http://kubevela.net/docs/v1.2/).

## Prerequisites

- [Create a Workspace](../../../ghippo/user-guide/workspace/workspace.md) and [Create a User](../../../ghippo/user-guide/access-control/user.md/).
- Add the user to the workspace and assign them the 'Workspace Editor' or higher permission.

## Procedure

1. In the `App Workbench` -> `Overview` page, go to the `OAM App` tab and click `Create App`.


2. Fill in the basic information according to the instructions below and click `Next`.

    - Name/Alias: Enter the name/alias of the OAM application.
    - Main Component Type: Different component types require different configurations. For detailed descriptions of various component types, refer to the [Built-in Component List](https://kubevela.io/en/docs/end-user/components/references).
        - CronTask: Defines a task that runs code or a script periodically.
        - Task: Defines a task that executes code or a script only once.
        - Daemon: Defines a service that runs on each node in Kubernetes.
        - K8s-Object: Each element in the list represents a complete Kubernetes resource structure.
        - Webservice: Defines a long-running, scalable containerized service and exposes an endpoint to accept external traffic from clients.
    - Deployment Location: Select which cluster and namespace to deploy the application to, supporting multiple cluster environments.


3. Configure parameters for the selected components based on the [Built-in Component List](https://kubevela.io/en/docs/end-user/components/references).


4. Configure traits for the selected components based on the [Built-in Trait List](https://kubevela.io/en/docs/end-user/traits/references).


5. Click `OK` to complete the creation. Once created successfully, you will be redirected to the OAM application list page.


6. Click the application name to view the OAM application details page. You can view the basic information of the OAM application, the list of included components, the status of deployed application resources, and perform operations such as adding components and traits.
