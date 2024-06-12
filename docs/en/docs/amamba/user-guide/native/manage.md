---
MTPE: FanLin
Date: 2024-01-08
---

# Manage Native Applications

After [creating a native application](native-app.md), you can view the application details or update the application configuration as needed.

1. Go to the __Workbench__ -> __Overview__ page, click the __Applications__ tab, and then click the name of the native application.

    ![Application Overview](../../images/native-app01.png)

- Here you can view basic information like the application name, alias, description, status, creation time, and more.

    ![Basic Info](../../images/native-app02.png)

- Click the __App Resources__ tab to view the Kubernetes resources associated with the native application, such as workloads, services, routes, etc. You also have the ability to edit and delete various resources.

    ![App Resources](../../images/native-app03.png)

- Click the __APP Topology__ tab to visually see the resources including workloads, containers, storage, configurations, and secrets.

    ![Application Topology](../../images/native-app04.png)

    - View basic resource information and navigate to the __Container Management__ module to see more resource details:

        ![Resource Details](../../images/native-app05.png)

    - Nodes in the visual topology are color-coded to indicate the health status of resources that support it:

        ![Node Color](../../images/native-app06.png)

- Click the __Version Snapshot__ tab to view version, version name, description, and creation time. 

    ![Snapshot](../../images/native-app09.png)    

## Editing basic information of a native application

1. Click the name of the native application, and then click the __ⵈ__ in the upper-right corner of the page, and select __Edit Basic Info__.

2. Set an alias or provide additional description as needed.

    ![Alias Info](../../images/native-app07.png)

## Viewing YAML of a native application

1. Click the name of the native application, then click the __ⵈ__ in the upper-right corner of the page, and select __Check YAML__.

2. View the manifest file of the native application.

    ![Check YAML](../../images/native-app08.png)
