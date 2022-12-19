# Warehouse integration

Warehouse integration is the entrance to the mirror warehouse of the centralized management platform, which supports the integration of external mirror warehouses, such as Harbor Registry and Docker Registry;
It can also automatically integrate the managed Harbor created by the platform. After the repository is integrated, the platform administrator can assign a private mirror space to one or more workspaces (namespaces under the workspace) by binding the mirror space to the workspace.
Or set the mirror space as public for use by all namespaces of the platform.

## The main function

- Supports the integration of mainstream mirror warehouses, such as Harbor Registry and Docker Registry, to help you centrally manage platform-level mirror warehouses.
- Support quick viewing of data such as warehouse address, number of mirrored spaces, and storage usage through the overview page.
- Support creating and setting mirror space status as public or private. If the status of the image space is public, the images under it can be used by all namespaces of the platform.
  If the status of the image space is private, after binding the image space to one or more workspaces, only the namespaces under the bound workspace can use the private image to ensure the security of the private image.
- Automatic integration of managed Harbor, after the platform creates a managed Harbor instance, it will be automatically integrated into the list of integrated warehouses for unified management.

## Functional advantages

- Unified management portal for unified management of integrated mirror warehouses and managed Harbor instances.
- High security, private images can only be pulled when deploying applications by binding the image space to the workspace.
- Convenient and fast, once the image space is set to public, all namespaces within the platform can pull the public images under it when deploying applications.
- Support mainstream mirror warehouse types: Harbor Registry, Docker Registry.

## Steps

1. Log in to the web console as a user with the Admin role, and click `Mirror Warehouse` from the left navigation bar.

    ![Mirror Warehouse](images/hosted01.png)

1. Click `Warehouse Integration` on the left navigation bar, and click the `Warehouse Integration` button in the upper right corner.

1. Select the warehouse type, fill in the integration name, warehouse address, user name and password to integrate the external mirror warehouse into the platform.