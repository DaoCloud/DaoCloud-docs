# Image Scan

Downloading an image provides convenience to users. However, downloaded images may not be safe and may contain backdoors that can be maliciously implanted. Therefore, it is essential to scan downloaded images for obtaining security information.

In a DevOps CI/CD process, pushing an image directly to the container registry cannot guarantee its security. Thus, continuous security integration and automatic scanning are necessary.

Security scanning is an active preventive measure that can effectively avoid hacker attacks and prevent problems before they occur. It is recommended to regularly or manually scan images.

After entering the production environment, the container must meet high-security standards, and its security must be ensured. Therefore, it is necessary to scan the image for security improvement before running the container.

The final scan results should provide more guidance on corrective actions. When users receive news that a container image has a vulnerability, they need to identify the issue's source and fix it themselves.

## Image Scan Features

DCE 5.0's container registry module supports the following image scanning:

- Managed Harbor repositories support Trivy scanning.
- Native Harbor repositories support Clair and Trivy scanning, depending on what plugins the user has installed.

When the user scans the image index, all indexed images will be scanned synchronously, and the scan result is the sum of the indexed images' scan results.

## Manually Scan Images

For integrated repositories, images appear on the list. You can manually scan images on demand.

1. Go to the container registry, enter the image list, select an instance and registry space, and click an image.

2. In the image details list, click `⋮` on the right side of the list, and select `Scan` from the pop-up menu.

3. The system starts to scan the image, usually displaying the status `queuing`, `scanning`, or `scanning completed`.

    Scan status includes:

    - Not Scanned: The image has never been scanned.
    - Not Supported: This image does not support scanning.
    - Queued: The scan task is scheduled but not yet run.
    - Scanning: The scanning task is in progress, and a progress bar is displayed.
    - View log: The scan task failed to complete. Click on `View Logs` to view the related logs.
    - Scan Complete: The scan task completed successfully.

4. After the scan is complete, hover the cursor over the scale bar of the scan to view the scan details.

## Scan Native Harbor Images

Integrated native Harbor repositories support scanning by Clair or Trivy.

The specific steps are:

1. Log in to the container registry as a platform administrator and click `registry Integration` at the bottom left.

2. In the list of integrated registries, hover the cursor over a certain registry and click the `Native Harbor` icon.

3. Jump to the native Harbor; see [Scanning Harbor images](https://goharbor.io/docs/2.1.0/administration/vulnerability-scanning/scan-individual-artifact/).
