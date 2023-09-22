# 其他故障

## CR 创建数据库失败报错

数据库运行正常，使用 CR 创建数据库出现了报错，此类问题的原因有：`mysql root` 密码有特殊字符

![image](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/mysql/images/faq-mysql-2.png)

1. 获取查看原密码：

    ```bash
    [root@master-01 ~]$ kubectl get secret -n mcamel-system mcamel-common-mysql-cluster-secret -o=jsonpath='{.data.ROOT_PASSWORD}' | base64 -d
    ```

2. 如果密码含有特殊字符 ` -> ` ，进入 MySQL 的 shell 输入原密码出现以下错误

    ```bash
    bash-4.4# mysql -uroot -p
    Enter password:
    ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
    ```

3. 清理重建：

    - 方法一：清理数据目录，删除 Pod 等待 sidecar running 以后，再删除一次数据目录，再删除 Pod 即可恢复:

    ```bash
    [root@master-01 ~]# kubectl exec -it mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c sidecar -- /bin/sh
    sh-4.4# cd /var/lib/mysql
    sh-4.4# ls | xargs rm -rf
    ```

    - 方法二：删除 PVC 再删除 Pod，只需要处理一次,即可恢复：

    ```bash
    kubectl delete pvc data-mcamel-common-mysql-cluster-mysql-1 -n mcamel-system
    ```

    ```bash
    kubectl delete pod mcamel-common-mysql-cluster-mysql-1 -n mcamel-system
    ```
