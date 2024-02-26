# Other Issues

## Error Encountered when Creating Database with CR

The database is running normally, but an error occurs when creating a database using CR. This issue can be caused by the presence of special characters in the __mysql root__ password.

![image](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/mysql/images/faq-mysql-2.png)

1. Retrieve and view the original password:

    ```bash
    [root@master-01 ~]$ kubectl get secret -n mcamel-system mcamel-common-mysql-cluster-secret -o=jsonpath='{.data.ROOT_PASSWORD}' | base64 -d
    ```

2. If the password contains special characters such as __-__ , attempting to enter the original password in MySQL Shell will result in the following error:

    ```console
    bash-4.4# mysql -uroot -p
    Enter password:
    ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
    ```

3. To resolve this issue, perform the following steps:

    - Method 1: Clean up and rebuild:
        - Clear the data directory by deleting the Pod. Wait for the sidecar to be running, then delete the data directory again and finally delete the Pod:

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
