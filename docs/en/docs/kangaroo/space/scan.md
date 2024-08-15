---
MTPE: ModetaNiu
DATE: 2024-08-09
---

# Scan Image

An image downloaded can be used directly, which provides convenience to users. 
However, downloaded images may not be safe and may contain backdoors that can be maliciously implanted. 
Therefore, it is essential to scan downloaded images for obtaining security information.

In a DevOps CI/CD process, pushing an image directly to the Container Registry cannot guarantee its security. 
Thus, continuous security integration and automatic scanning are necessary.

Security scanning is an active preventive measure that can effectively avoid hacker attacks and prevent problems 
before they occur. It is recommended to regularly or manually scan images.

After entering the production environment, the container must meet high-security standards, and security must be ensured. 
Therefore, it is necessary to scan the image for security improvement before running the container.

The final scan results should provide more guidance on corrective actions. When users receive news that 
a container image has a vulnerability, they need to identify the issue's source and fix it themselves.

## Image Scan Features

DCE 5.0 Container Registry module supports the following image scanning:

- Managed Harbor registries support Trivy scanning.
- Native Harbor registries support Clair and Trivy scanning, depending on what plugins the user has installed.

When the user scans the image index, all indexed images will be scanned synchronously, 
and the scan result is the sum of the indexed images' scan results.

## Manually Scan Images

For integrated registries, images appear on the list. You can manually scan images on demand.

1. Go to the registry space, enter the image list, select an instance and registry space, and click an image.

    ![Image List](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/scan01.png)

2. In the image details list, click __┇__ on the right side of the list, and select __Scan__ from the pop-up menu.

    ![Scan](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/scan02.png)

3. The system starts to scan the image, usually displaying the status `Queued`, `Scanning`, or `Complete`.

    ![Queued](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/scan03.png)

    ![Scanning](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/scan04.png)

    ![Complete](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/scan05.png)

    Scan status includes:

    - Not Scanned: The image has never been scanned.
    - Not Supported: This image does not support scanning.
    - Queued: The scan task is scheduled but not yet run.
    - Scanning: The scanning task is in progress, and a progress bar is displayed.
    - View log: The scan task failed to complete. Click __View Logs__ to view the related logs.
    - Complete: The scan task completed successfully.

4. After the scan is complete, hover the cursor over the scale bar of the scan to view the scan details.

    ![Details](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/scan06.png)

## Scan Native Harbor Images

Integrated native Harbor registries support scanning by Clair or Trivy.

The specific steps are:

1. Log in to the Container Registry as a platform administrator and click __Integrated Registry__ at the bottom left.

    ![Integrated Registry](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/scan07.png)

2. In the list of integrated registry, hover the cursor over a certain registry and click the __Go to Native Harbor Registry__ icon.

    ![Go to NHR](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/scan08.png)

3. Jump to the native Harbor; see [Scanning Harbor images](https://goharbor.io/docs/2.1.0/administration/vulnerability-scanning/scan-individual-artifact/).
