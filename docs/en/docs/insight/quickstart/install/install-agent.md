---
date: 2022-11-17
hide:
   - toc
---

# Install insight-agent

insight-agent is a plugin for collecting insight data, supporting unified observation of metrics, links, and log data. This article describes how to install insight-agent in an online environment for the accessed cluster.

## Prerequisites

- The cluster has been successfully connected to the __container management__ module. For how to connect a cluster, refer to [Integrate Clusters](../../../kpanda/user-guide/clusters/integrate-cluster.md)

## Steps

1. Enter __Container Management__ from the left navigation bar, and enter __Clusters__ . Find the cluster where you want to install insight-agent.

    ![Find Cluster](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/insight-agent01.png)

1. Choose __Install now__ to jump, or click the cluster and click __Helm Applications__ -> __Helm Templates__ in the left navigation bar, search for __insight-agent__ in the search box, and click it for details.

    ![Search insight-agent](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/insight-agent02.png)

1. Select the appropriate version and click __Install__ .

    ![Install](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/insight-agent03.png)

1. Select the version to install and fill in the addresses of the corresponding data storage components in the global service cluster in the form below. After confirming that the information is correct, click __OK__ .

    - By default, insight-agent is deployed in the `insight-system` namespace of the cluster.
    - It is recommended to install the latest version of insight-agent.
      - The system has filled in the address of the component for data reporting by default. Please still check it before clicking __OK__  to install. If you need to modify the data reporting address, please refer to [Get Data Reporting Address](../install/gethosturl.md).

    ![Sheet Fill1](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/insight-agent04-1.png)

    ![Sheet Fill2](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/insight-agent04-2.png)

1. The system will automatically return to the __Helm Apps__ list. When the status of the insight-agent application changes from __Not Ready__ to __Deployed__ and all component statuses are __Running__ , the installation is successful. After a while, you can view the data of this cluster in the __Insight__ module.

    ![Finish Page](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/quickstart/images/insight-agent05.png)

    !!! note

        - Click __┇__ on the far right, and you can perform more operations such as __Update__ , __View YAML__ and __Delete__ in the pop-up menu.
        - For a practical installation demo, watch [Video demo of installing insight-agent](../../../videos/insight.md#install-insight-agent)
