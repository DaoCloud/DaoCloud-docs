# Snapshot Management

This guide explains how to create snapshots for virtual machines and restore them.

Users can create snapshots for virtual machines to save the current state of the virtual machine. A snapshot can be restored multiple times, and each time the virtual machine will be reverted to the state when the snapshot was created. Snapshots are commonly used for backup, recovery, rollback, and other scenarios.

## Create a Snapshot

1. Click `Container Management` in the left navigation menu, then click `Virtual Machines` to access the list page. Click the `︙` on the right side of the list for a virtual machine to perform snapshot operations (only available for non-error state virtual machines).


2. In the pop-up dialog, provide a name and description for the snapshot. Creating a snapshot may take a few minutes, during which no operations can be performed on the virtual machine.


3. After the snapshot is created successfully, you can view the snapshot information in the virtual machine details. You can also edit the description, restore from the snapshot, delete the snapshot, and perform other operations.


## Restore from a Snapshot

1. Click `Restore from Snapshot` and provide a name for the virtual machine recovery record. The recovery operation may take some time to complete, depending on the size of the snapshot and other factors. After a successful recovery, the virtual machine will be restored to the state when the snapshot was created.


2. After some time, you can scroll down to the snapshot information to view all the recovery records for the current snapshot. It also provides a way to locate the position of the recovery.

