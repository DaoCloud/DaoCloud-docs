---
hide:
  - toc
---

# Delete Mesh

When users no longer need the mesh governance service, they can use the delete operation.
Deleting a mesh requires users to complete a series of prerequisite operations
before activating the __Delete__ button in the dialog box.

!!! danger

    After performing the delete operation, the mesh cannot be recovered. If you want to manage it again, you need to recreate the mesh.

1. On the right side of the Mesh List, click the __...__ button, and select __Delete__ from the pop-up menu.

    ![Delete Mesh](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/deletemesh01.png)

2. Depending on the mesh type, the system will automatically detect whether the deletion conditions are met.

    - Delete External Mesh. Only need to confirm the mesh name to complete the deletion operation.

        ![External Mesh](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/user-guide/images/deletemesh02.png)

    - Delete Dedicated Mesh. Follow the prompts to disable mesh deletion protection, uninstall injected sidecars, clean up gateways, and then confirm the deletion operation by entering the mesh name.

        ![Dedicated Mesh](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/deletemesh03.png)

    - Delete Managed Mesh. Follow the prompts to disable mesh deletion protection, uninstall injected sidecars, clean up gateways, remove clusters under the mesh, and then confirm the deletion operation by entering the mesh name.

        ![Hosted Mesh](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/deletemesh04.png)
