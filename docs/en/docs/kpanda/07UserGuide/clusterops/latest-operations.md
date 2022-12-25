---
hide:
  - toc
---

# recent operations

On this page, you can view the recent cluster operation records and Helm operation records, as well as the YAML files and logs of each operation, and you can also delete a certain record.

![Operation Record](../../images/operations01.png)

Set the number of reserved entries for Helm operations:

By default, the system keeps the last 100 Helm operation records. If you keep too many entries, it may cause data redundancy, and if you keep too few entries, you may lose the key operation records you need. A reasonable reserved quantity needs to be set according to the actual situation. Specific steps are as follows:

1. Click the name of the target cluster, and click `Recent Operations`->`Helm Operations`->`Set Number of Retained Items` in the left navigation bar.

    ![Number of reserved entries](../../images/operations02.png)

2. Set how many Helm operation records need to be kept, and click `OK`.

    ![Reserved number](../../images/operations03.png)