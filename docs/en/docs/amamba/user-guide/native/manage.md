# Native Application Management

After [creating a native application](native-app.md), you can view the application details or update the application configuration as needed.

## View Application Details

In the `App Workbench` - `Overview` page, click on the `Native App` tab and then click on the name of the native application.

- View basic information such as application name, alias, description, namespace, creation time, etc.


- Click on the `Application Resources` tab to view Kubernetes resources under the native application, such as workloads, services, routes, etc. It supports editing and deleting various resources.


- Click on the `Application Topology` tab to view a visual representation of resources including workloads, containers, storage, configurations, and secrets.


    - View basic information of resources and navigate to the `Container Management` module to see resource details:


    - Nodes in the visual topology are color-coded to indicate the health status of resources that support it:


## Edit Basic Information of a Native Application

1. Click on the name of the native application and then click on the `ⵈ` in the upper-right corner of the page and select `Edit Basic Information`.
2. Set an alias or provide additional description as needed.


## View YAML of a Native Application

1. Click on the name of the native application and then click on the `ⵈ` in the upper-right corner of the page and select `View YAML`.
2. View the manifest file of the native application.

