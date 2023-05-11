---
hide:
   - toc
---

# Install Harbor Operator

Managed Harbor uses Harbor Operator technology to manage the entire life cycle of Harbor creation, upgrade, and deletion.
Before creating a managed Harbor, you need to install Harbor Operator in the container management, the minimum version requirement is 1.4.0.

1. If the following exception prompt appears when creating a Harbor instance, please click `Go to Install`.

     

1. Go to `Helm Application` -> `Helm Template` of `Container Management`, find and click the Harbor Operator card.

     

1. Select the version and click `Install`.

     

1. After entering the name and namespace, click `OK`.

     

1. Wait for the installation to complete.

     

Next step: [Create a managed Harbor instance](./harbor.md)