---
MTPE: todo
date: 2022-12026
---

# Image scan

After the image is downloaded, it can be used directly, which provides users with a lot of convenience, but it is not necessarily safe, and may be maliciously implanted with a backdoor. Users need to scan the downloaded image to obtain the image security information.

In the (DevOps) CI/CD process, the image is directly pushed to the image registry, which cannot guarantee the security of the image, and there is a need for continuous security integration and automatic scanning.

Security scanning is an active preventive measure, which can effectively avoid hacker attacks and prevent problems before they happen. It is recommended to scan the image regularly/manually.

(Put into production) After the container enters the production environment, the production environment has high requirements on the security of the container, and the security of the container needs to be guaranteed. Therefore, before using the image to run the container, it is necessary to scan the image to improve security.

The final scan results should provide more guidance on corrective actions. When users receive the bad news that a container image is plagued by a vulnerability, they need to figure out how to fix it for themselves. Where did the vulnerability come from? What can be done to fix the problem?

## Image scan features

Currently, the image registry module of DCE 5.0 supports the following scanning  images:

- Hosted Harbor repositories support Trivy scanning.
- Native Harbor repositories support Clair and Trivy scanning, depending on what plugins the user has installed.

When the user scans the image index, all indexed images will be scanned synchronously, and the scan result is the sum of the scan results of the indexed  images.

## Manually scan images

For associated and integrated repositories, will appear in the list of images. You can manually scan some  images on demand.

1. Enter the image list in the image registry, select an instance and registry space, and click an image.

    

2. In the image details list, click `⋮` on the right side of the list, and select `Scan` from the pop-up menu.

    

3. The system starts to scan the image, usually the status is `queuing`, `scanning`, `scanning completed`.

    

    

    

    Scan status includes:

    - Not Scanned: The image has never been scanned.
    - Not Supported: This image does not support scanning.
    - Queued: The scan task is scheduled but not yet run.
    - Scanning: The scanning task is in progress and a progress bar is displayed.
    - View log: The scan task failed to complete. Click on `View Logs` to view the related logs.
    - Scan Complete: The scan task completed successfully.

4. After the scan is complete, hover the cursor over the scale bar of the scan to view the scan details.

    

## Scan native Harbor images

Integrated native Harbor repository with support for scanning by Clair or Trivy.

The specific operation steps are:

1. Log in to the image registry as a platform administrator, and click `registry Integration` at the bottom left.

    

2. In the list of integrated registries, hover the cursor over a certain registry, and click the `Native Harbor` icon.

    

3. Jump to the native Harbor, see [Scanning Harbor images](https://goharbor.io/docs/2.1.0/administration/vulnerability-scanning/scan-individual-artifact/).
