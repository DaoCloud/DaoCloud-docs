---
hide:
   - toc
---

# System Configuration

 __System Configuration__ displays the default storage time of metrics, logs, traces and the default Apdex threshold.

1. Click the right navigation bar and select __System Configuration__.

    ![System Configuration](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/systemconfig00.png)

2. Currently only supports modifying the storage duration of historical alerts, click __Edit__ to enter the target duration.

    When the storage duration is set to "0", the historical alerts will not be cleared.

    ![System Configuration](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/sysconfig02.png)

3. Modify the default configuration of the topology rendering, click __Edit__ to define the topology thresholds in the system as needed.

    The threshold must be greater than 0, the previously entered threshold must be less than the later entered one, and the entered thresholds must be within the maximum and minimum ranges.

    ![Topology Configuration](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/map-setting.png)

!!! note

    To modify other configurations, please click to view [How to modify the system configuration?](modify-config.md)
