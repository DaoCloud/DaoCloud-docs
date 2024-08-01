---
hide:
  - toc
---

# Image List

The image list is displayed based on the workspace, showing all available public and
private images under the tenant. There are two main sources of images:

1. The first part includes all public images in the integrated or hosted container registry
   of the DCE 5.0 Container Registry, as well as private images assigned to the workspace separately through the binding of 
   registry space and workspace.
2. The second part includes all public or private images obtained by the workspace actively associating with 
   a specific container registry.

![space](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/space02.png)

**The main features**

- Rapid application deployment: Both the image list and Workbench take the workspace
  as the dimension, so when you select the same workspace to deploy the application under Workbench, 
  you can click the __Choose Image__ button to obtain all visible images under the workspace.
- Fine-grained allocation: After integrating or creating a managed Harbor instance in the DCE 5.0 Container Registry, the administrator 
  can assign different registry spaces to different workspaces by binding the registry space to the workspace.
- Image scanning: Image list provides image scanning and analysis features. You can visually check the
  level and distribution of bugs. Log scanning is supported for tracking bugs.
- Image pushing: The image can be pushed to the authorized registry space through the
  commands provided by the DCE 5.0 Container Registry.
- View details such as levels: Provides a display of detailed information such as
  image versions, level information, creators, and create time for images within the visible range.

**Functional advantages**

- Safety and reliability: Fine-grained image allocation is realized by binding the registry space
  and workspace, ensuring that private images can only be pulled by the specified workspace.
- Convenience: After the administrator creates a managed Harbor or integrates
  other registries, if he wants to share it with all workspaces and namespaces, he only needs to
  make the container registry public.
- Flexible access: In addition to platform-level registry integration capabilities, it also
  provides integrated registry features under each workspace. After integration,
  the container registry can only be used by the workspace.
- Global linkage: Workbench and Container Management provide the image selector feature
  for the container registry. When deploying the application, you can click the __Choose Image__
  button to obtain all visible images with one click, and quickly complete the deployment.

## Push command

You can push an image to current registry space and set the command to push.

1. In the image list, click the __Push command__ button on the right.

    ![click button](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/push00.png)

1. You can add __Generate login command__ and view the command to push images.

    ![push command](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/push01.png)

Here is a sample command to push image:

```bash
docker tag [ImageID] 10.6.194.1:30010/kangaroo/REPOSITORY[:TAG]
docker push 10.6.194.1:30010/kangaroo/REPOSITORY[:TAG]
```

Next step: [Artifacts and Description](./desc.md)
