---
hide:
  - toc
---

# Batch Device Onboarding

When devices in the same data center or rack are initially deployed, dozens or even hundreds of devices may need to be imported at once. Onboarding them one by one is time-consuming and labor-intensive.  
The batch device onboarding feature allows users to quickly import multiple devices at once, improving onboarding efficiency.

This guide explains how to import multiple devices at once using an Excel template.

## Prerequisites (Optional)

- An Excel file prepared according to the system-provided template.

## Steps

1. In the left navigation bar, select **Devices** to enter the device management list page, then click the **Batch Onboard** button at the top right corner.

    <!-- ![Device Management List](../images/batch-access-device-01.png) -->

2. In the **Batch Device Onboarding** popup, click **Download Template** to get the Excel template, and fill in the device information row by row according to the template headers.  
   If you have already prepared the Excel file according to the template, skip this step.

    <!-- ![Batch Device Onboarding](../images/batch-access-device-02.png) -->

3. Click **Select File**, choose the prepared `.xlsx` file, and after confirming the selection, click **Onboard Devices**.

    !!! note

        Do not leave the popup page before all devices are onboarded. Leaving the page will interrupt the onboarding process and prevent viewing the results.

4. Once all devices are successfully onboarded, you will automatically return to the device list where the new devices can be viewed.  
   If some devices fail to onboard, check the device records and failure reasons in the popup page, make necessary corrections, and re-upload.

Next step: [Manage Devices](./manage-device.md)
