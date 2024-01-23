# Image Reclamation

In a container registry, many images may no longer be needed after a certain period of time
or after being updated to a certain version. These redundant images consume a lot of storage space.
If you are a Workspace Admin, you can manage the images in all registry spaces under the workspace.
You can manage the images in the container registry by setting up image reclamation rules and
put some images into the recycle bin according to certain rules on a scheduled/manual basis.

Here, image reclamation refers to deleting an image and reclaiming the resources used to create it.
When you no longer need an image, you can delete it, which will free up disk space used by the image.
This process is called "image reclamation". With image reclamation, you can free up disk space and 
other resources on your system, while also keeping the system clean and optimized.

You can create image reclamation rules for the current registry space.
All image reclamation rules are calculated independently and apply to all images that meet the conditions.
Currently, DCE 5.0 supports up to 15 reclamation rules.

1. Log in to DCE 5.0 with a user who has the Workspace Admin role.
   Click the `Registry Space` on the left navigation bar, click a name in the list.

    ![Switch Instance](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/space01.png)

2. Click the `Reclaim` tab and click the `Create Reclaim Rule` button.

    ![Click Button](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/reclaim01.png)

    !!! Note

        Only Harbor repository supports image reclamation

3. Follow the prompts to select the image and configure the rule.

    ![Create Rule](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/reclaim02.png)

4. Return to the image reclamation list. Click the `⋮` on the right to disable, edit, or delete the reclamation rule.

    ![Click Button](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/reclaim03.png)
