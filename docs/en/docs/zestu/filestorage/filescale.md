# File Storage Scaling (Expansion and Reduction)

This document demonstrates how to scale (expand or reduce) file storage in **d.run**.

## Prerequisites

- The selected region must have file storage initialized.
- Your account balance must exceed the required cost for expansion.

## Steps

1. Log in to **d.run**, and go to **Compute Cloud** -> **File Storage**.
  
2. On the **File Storage** page, click **Scale** in the upper right corner.

    <!-- ![File Storage](../images/file1.png) -->

3. In the pop-up **Scale** window, enter the desired **storage quota**, and click **OK**.

    <!-- ![Scaling](../images/file2.png) -->

## Billing Rules

1. **Billing rule**: Storage exceeding the free 20 GB is billed daily. If usage is less than one day, charges are based on actual usage time, accurate to the second.
2. **Billing period**: Billing starts from the moment of expansion and continues until the next expansion or reduction. If storage is reduced to 20 GB, billing stops. If scaled to any other size, a new billing cycle begins.
3. **Overdue payments**: If your account balance falls below 0 and you have previously expanded storage beyond the free 20 GB, the system will retain your data for 15 days and continue billing during this period.
   You may manually reduce the storage during this time. If reduced to 20 GB, billing stops. If your balance remains negative for over 15 days, the system will automatically reduce storage to 20 GB. Any data lost due to automatic reduction cannot be recovered—please top up your account in time.
4. **Prolonged inactivity**: If there is no spending activity on the platform for 30 consecutive days (including but not limited to services like Compute Cloud or Large Model Services), the platform will automatically delete the file storage. You will need to reinitialize it upon the next use.
