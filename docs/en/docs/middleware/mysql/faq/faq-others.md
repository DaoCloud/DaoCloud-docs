---
MTPE: ModetaNiu
DATE: 2024-08-15
---

# Other Issues

## Error Encountered when Creating Database with CR

The database is running normally, but an error occurs when creating a database using CR. 
This issue can be caused by the presence of special characters in the __mysql root__ password.

![image](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/mysql/images/faq-mysql-2.png)

1. Retrieve and view the original password:

    ```bash
    [root@master-01 ~]$ kubectl get secret -n mcamel-system mcamel-common-mysql-cluster-secret -o=jsonpath='{.data.ROOT_PASSWORD}' | base64 -d
    ```

2. If the password contains special characters such as __-__ , attempting to enter the original password 
   in MySQL Shell will result in the following error:

    ```console
    bash-4.4# mysql -uroot -p
    Enter password:
    ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
    ```

3. To resolve this issue, you are offered two methods to clean up and rebuild:

    - Method 1: Clear the data directory and delete the Pod. Wait for the sidecar to be running, 
      then delete the data directory again and repete deleting the Pod:

        ```bash
        [root@master-01 ~]# kubectl exec -it mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c sidecar -- /bin/sh
        sh-4.4# cd /var/lib/mysql
        sh-4.4# ls | xargs rm -rf
        ```

    - Method 2: Delete the PVC first, then delete the Pod to restore functionality:

        ```bash
        kubectl delete pvc data-mcamel-common-mysql-cluster-mysql-1 -n mcamel-system
        ```

        ```bash
        kubectl delete pod mcamel-common-mysql-cluster-mysql-1 -n mcamel-system
        ```

!!! note

    Using the above methods to clean and rebuild will result in the database being reset and data loss.

## The Following MySQL Message in the DCE 5.0 Platform

When the following message appears during operations in the management platform, it indicates that 
the master-replica relationship of the MySQL nodes has changed. 
However, other modules of the platform have not timely updated the connection objects, 
resulting in a write operation being executed on a read-only replica node.

```prompt
The MySQL server is running with the read-only option so it cannot execute this statement
```

Solution: Go to the __Container Management__ platform and restart all related __replica__ nodes.