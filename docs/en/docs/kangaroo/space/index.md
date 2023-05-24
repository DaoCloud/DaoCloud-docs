# Registry space

DCE 5.0 container registry provides a feature of isolating images based on registry spaces.
Registry spaces are divided into two types: public and private.

- Public registry: accessible by all users, usually storing public images. There is a default public registry space.
- Private registry: only authorized users can access, usually storing images of the image space itself.

You can choose different instances to view all registry spaces underneath.

![Switch instances](../img/space01.png)

Click on the name of a registry space to view the current image list and reclaim rules for that space. You can create reclaim rules for the current registry space. All reclaim rules are calculated independently and apply to all qualified images, with a maximum of 15 reclaim rules supported.

![What's in the registry space](../img/space02.png)
