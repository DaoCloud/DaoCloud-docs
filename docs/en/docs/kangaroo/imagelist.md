---
hide:
  - toc
---

# Image list

The image list takes the workspace as the dimension and displays all available public images and private images under the tenant.
There are two main sources of images. The first part is all public images in the container registry integrated or hosted by the platform, as well as private images that are individually assigned to the workspace through the binding of registry space and workspace.
The second part is all the public or private images obtained by actively associating the workspace with a container registry.

[](images/list01.png)

**The main function**

- Rapid application deployment: Both the image list and the application workbench take the workspace as the dimension, so when you select the same workspace to deploy the application under the application workbench, you can click the `Select Image` button to obtain the image list under the workspace with one click All visible images in , quickly complete the deployment.
- Fine-grained allocation: After integrating the platform or creating a managed Harbor instance, the administrator can assign different registry spaces to different workspaces by binding the registry space to the workspace to achieve fine-grained allocation.
- image scanning: Provides image scanning and analysis functions, visually checks the level and distribution of vulnerabilities, and provides scanning logs to facilitate tracking of vulnerabilities.
- Push image: The image can be pushed to the authorized registry space through the commands provided by the platform.
- View details such as levels: Provides a display of detailed information such as image versions, level information, creators, and creation times for images within the visible range.

**Functional advantages**

- Safe and reliable: Fine-grained image allocation is realized by binding the registry space and workspace, ensuring that private images can only be pulled by the specified workspace.
- Simple and convenient: After the platform administrator creates a managed Harbor or integrates other registrys, if he wants to share it with all workspaces and namespaces, he only needs to make the container registry public.
- Flexible access: In addition to platform-level registry integration capabilities, it also provides associated registry functions under each workspace. After association, the container registry can only be used by the workspace.
- Global linkage: The application workbench and container management provide the "image selector" function for the image registry. When deploying the application, you can click the "select image" button to obtain all visible images with one click, and quickly complete the deployment.
