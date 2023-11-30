---
hide:
   - toc
---

# Create Managed Harbor

Prerequisite: [Cert Manager](https://cert-manager.io/docs/installation/) and [Harbor Operator](./operator.md) have been installed.

!!! note

     For Harbor instances, in addition to using administrator accounts,
     it is also possible to achieve the same level of access by using robot accounts.

1. Log in to DCE 5.0 as a user with the Admin role, and click `container registry` -> `Managed Harbor` from the left navigation bar.

     ![nav](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/hosted01.png)

1. Click the `Create Instance` button in the upper right corner.

     ![button](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/hosted02.png)

1. Fill in the instance name, select the deployment location and click `Next`
   (if there is no deployment location to choose, you need to go to the container management to create a cluster and namespace).

     ![fill](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/hosted03.png)

1. Fill in the database, Redis instance and image/Charts storage information and click `Next` (currently only supports access to external databases and Redis instances).

     The system will automatically detect PostgreSQL and Redis. If there is no available database, you can click the link to create one.
     
     Tips for filling out the database:

     - Address: `postgres://{host}:{port}`, for example `postgres://acid-minimal-cluster.default.svc:5432`
     - Username: Fill in the username to connect to the database
     - Password: fill in the password to connect to the database

     Redis filling is divided into stand-alone and sentinel modes:

     - Fill in the address in stand-alone mode: `redis://{host}:{port}`, you need to replace the two parameters host and port.
     - Fill in the address in sentinel mode: `redis+sentinel://{host}:{port}?sentinelMasterId={master_id}`, you need to replace the three parameters host, port, and master_id.
     - Password: Fill in as required

     ![spec](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kangaroo/images/hosted04.png)

1. Fill in the domain name, select the ingress instance, enter the administrator password and click `OK` (username/password is used to log in to the native Harbor instance, please keep the password safe).

     Tips for filling in the domain name: `http://{host}`, `http://` in front of the host must be brought.

     

1. Return to the list of managed Harbor instances. The newly created instance is the first one by default. Wait for the status to change from 'Updating' to 'Healthy' before it can be used normally.

     

1. Click `...` on the right side of an instance, and you can choose to edit, delete, or enter the original Harbor.

     

Next step: [Create registry space](../integrate/registry-space.md)
