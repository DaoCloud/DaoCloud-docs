---
date: 2022-11-17
hide:
   - toc
---

# Install insight-agent

Please confirm that your cluster has successfully connected to the container management platform, and then perform the following steps to install insight-agent to collect data.

1. Enter `Container Management` from the left navigation bar, and enter `Cluster List`.

    ![Enter cluster list](../../images/login01.png)

1. Click on the name of the cluster where you want to install insight-agent.

    ![Click on the cluster name](../../images/login02.png)

1. In the left navigation bar, select `Helm Application` -> `Helm Template`, find `insight-agent`, and click the tile card.

    ![found insight-agent](../../images/installagent01.png)

1. Select the appropriate version and click `Install`.

    ![install](../../images/installagent02.png)

1. Fill in the name, select the namespace and version, and fill in the addresses of logging, metric, audit, and trace reporting data in the yaml file.

    The system has filled in the address of the component for data reporting by default, please check it before clicking `OK` to install.
    If you need to modify the data reporting address, please refer to [Get Data Reporting Address](gethosturl.md).

    ![Fill out the form](../../images/installagent03.png)

1. The system will automatically return to `Helm application`. When the application status changes from `not ready` to `deployed`, it means that insight-agent is installed successfully.

    ![Success](../../images/login03.png)

    !!! note

        - Click `⋮` on the far right, and you can perform more operations such as `Update`, `View YAML` and `Delete` in the pop-up menu.
        - For a practical installation demo, watch [Video demo of installing insight-agent](../../../videos/insight.md#_6)