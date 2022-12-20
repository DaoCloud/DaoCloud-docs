---
hide:
  - toc
---

# delete registry

1. On the `Managed Registry List` page, select the registry to be deleted, click **`⋯`** on the right and select `Delete`.

    ![Enter the delete page](imgs/delete01.png)

2. Enter the name of the registry and click `Remove`.

    ![Confirm Name](imgs/delete02.png)

!!! note

    Access-type registries only support `remove` operations, while managed-type registries only support `delete` operations. The difference between the two is:

         - Removal: just remove the registration center from the microservice engine of DCE 5.0, and will not delete the original registration center and data, and you can access the registration center again later.
         - Delete: delete the registration center and all the data in it, the registration center cannot be used again later, and a new registration center needs to be recreated.