---
MTPE: FanLin
Date: 2024-01-08
---

# Manage Native Applications

After [creating a native application](native-app.md#create-a-native-application), you can view the application details or update the application configuration as needed.

## View Application Details

On the __Workbench__ -> __Overview__ page, click the __Native Applications__ tab, and then click the name of the native application.

![entry](../../images/native-app01.png)

- Here you can view basic information like the application name, alias, description, namespace, creation time, and more.

    ![basic](../../images/native-app02.png)

- Click the __App Resources__ tab to view the Kubernetes resources associated with the native application, such as workloads, services, and routes. You also have the ability to edit and delete various resources.

    ![resource](../../images/native-app03.png)

- Click the __APP Topology__ tab to visually see the resources including workloads, containers, storage, configurations, and secrets.

    ![topology](../../images/native-app04.png)

    - View basic resource information and navigate to the __Container Management__ module to see more resource details:

        ![basic](../../images/native-app05.png)

    - Nodes in the visual topology are color-coded, so that the health status of some resources that support a status can be judged by the node color:

        ![color](../../images/native-app06.png)

- Click the __Version Snapshot__ tab to view the version number, version name, description, creation time, and more.

    ![snapshot](../../images/native-app09.png)

## Edit basic information of a native application

1. Click the name of the native application, and then click the __ⵈ__ in the upper-right corner of the page, and select __Edit Basic Info__.
2. Set an alias or provide additional description as needed.

    ![color](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/native-app07.png)

## View YAML of a native application

1. Click the name of the native application, then click the __ⵈ__ in the upper-right corner of the page, and select __Check YAML__.
2. View the manifest file of the native application.

    ![color](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/native-app08.png)
