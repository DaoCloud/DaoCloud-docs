# OAM Application Management

After [creating an OAM application](create.md), you can view the application details and update its components or traits.

## View Application Details

1. In the __App Workbench__ -> __Overview__ page, go to the __OAM App__ tab to view the list of OAM applications.
2. Click the application name to view the application details, including fields such as name, status, alias, description, and creation time.
3. On the application details page, click the __Components__ tab to view the number, types, and traits of the components defined in the current application.

4. On the application details page, click the __Application Status__ tab to view the component status and application resources.

    - Component Status: Displays the health status of each component in the current application. If there are unhealthy components, investigate and address the operational issues promptly.

    - Application Resources: Provides information about the Kubernetes resources deployed in the current application.


## Edit Basic Information of an OAM Application

1. Click the OAM application name, then click the __ⵈ__ icon in the top right corner of the page and select __Edit Basic Information__.
2. Set the alias as desired or provide additional description information.



## Edit YAML File of an OAM Application

1. Click the OAM application name, then click the __ⵈ__ icon in the top right corner of the page and select __Edit YAML__.
2. Edit the YAML file of the OAM application as necessary.


## Add Components

1. Click the OAM application name, go to the __Components__ tab, and click __Add Component__ on the right side.



2. Select the desired component type and fill in the corresponding component parameters based on the [Built-in Component List](https://kubevela.io/docs/end-user/components/references).



### Add/Update Traits

1. Click the OAM application name, go to the __Components__ tab, and click the __ⵗ__ icon on the right side of the component to select __Edit Traits__.



2. Update the trait properties based on the [Built-in Trait List](https://kubevela.io/en/docs/end-user/traits/references).

