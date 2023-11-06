---
date: 2022-11-17
hide:
   - toc
---

# Install insight-agent

Please confirm that your cluster has successfully connected to the container management platform, and then perform the following steps to install insight-agent to collect data.

1. Enter `Container Management` from the left navigation bar, and enter `Cluster List`.

    

1. Click the name of the cluster where you want to install insight-agent.

    

1. In the left navigation bar, select `Helm Apps` -> `Helm chart`, find `insight-agent`, and click the tile card.

    

1. Select the appropriate version and click `Install`.

    

1. Fill in the name, select the namespace and version, and fill in the addresses of logging, metric, audit, and trace reporting data in the yaml file.

    The system has filled in the address of the component for data reporting by default, please check it before clicking `OK` to install.
    If you need to modify the data reporting address, please refer to [Get Data Reporting Address](./gethosturl.md).

    

1. The system will automatically return to `Helm Apps`. When the application status changes from `not ready` to `deployed`, it means that insight-agent is installed successfully.

    

    !!! note

        - Click `⋮` on the far right, and you can perform more operations such as `Update`, `View YAML` and `Delete` in the pop-up menu.
        - For a practical installation demo, watch [Video demo of installing insight-agent](../../../videos/insight.md#install-insight-agent)
