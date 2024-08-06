# Registry space

DCE 5.0 container registry provides a feature of isolating images based on registry spaces.
Registry spaces are divided into two types: public and private.

- Public registry: accessible by all users, usually storing public images. There is a default public registry space.
- Private registry: only authorized users can access, usually storing images of the registry space itself.

You can choose different instances to view all registry spaces underneath.

![Switch instances](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/space01.png)

Click a name of registry space to view the current image list and reclaim rules for that space.
You can create reclaim rules for the current registry space. All reclaim rules are calculated
independently and apply to all qualified images, with a maximum of 15 reclaim rules supported.

![What's in the registry space](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/space02.png)

After entering the registry space through the __Integrated Registry (Workspace)__ on the left navigation bar,
click the __Push command__ button located on the right side.

![Button](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/push-cmd01.png)

You can view the push command that can be used to push the image to the current registry space.

![Push Command](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/push-cmd02.png)

Click the __Upload image__ button to upload an image file in tar or tar.gz format.
Please note that the file size should not exceed 2 GB, and each file corresponds to one image.
Currently, only image compression packages made with container runtime v1.11.2 and above are supported to upload.

![Upload Image](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/push-cmd03.png)
