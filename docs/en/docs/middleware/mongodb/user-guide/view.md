---
MTPE: ModetaNiu
DATE: 2024-09-19
---

# View MongoDB Instance

In the MongoDB instance list, select the instance you want to view and click the instance name to enter the detail page.

## Overview

The Overview page supports viewing Basic Information, Access Settings, Resource Quota, Synchronization delay, 
Alert, Pod List and Recent Events. Among them, 

- Synchronization delay: It refers to the time difference between the standby node receiving the packets sent by 
  the master node due to network latency or other factors during the replication or synchronization process.

- Alert: The overview page only supports viewing the latest 10 alerts. Click __View More__ to enter alert list.

![Overview](../images/view.png)

## Parameter Configuration

Click the __Update__ button in the upper right corner of the page to update the `Current` value.

![Parameter Configuration](../images/view01.png)

!!! warning

    Updating parameters requires a restart, which will make the instance unavailable. Proceed with caution!

## Instance Insight

- Select __Instance Insight__ from the navigation bar on the left, you can view various panels.

    ![Instance Insight](../images/view02.png)
